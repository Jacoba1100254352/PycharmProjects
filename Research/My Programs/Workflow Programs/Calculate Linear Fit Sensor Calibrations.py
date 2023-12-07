import numpy as np
import pandas as pd

# Define Global constants
SENSOR_SET = 1
NUM_SENSORS = 4
NUM_TESTS = 1
WORKING_DIR = "/Users/jacobanderson/Library/CloudStorage/Box-Box/Nanogroup/Projects/Bioimpedance/Pressure Controller/Jacob's Tests/"

# Calibration constants
WORKING_DIR += f"Calibration Tests/"
ARDUINO_DIR = f"Arduino Data/Sensor Set {SENSOR_SET}/"
CALIBRATION_PREFIX = "Calibration "


def find_rising_edge(data, threshold=0.5):
    """Find the start of the rising edge in the data."""
    for i in range(1, len(data)):
        if data[i] > threshold >= data[i - 1]:
            return i
    return -1


def calculate_linear_fit(excel_force, arduino_raw_force):
    A = np.vstack([arduino_raw_force, np.ones(len(arduino_raw_force))]).T
    m, c = np.linalg.lstsq(A, excel_force, rcond=None)[0]
    return m, c


def parse_arduino_data(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    time = []
    raw_force = []
    force_N = []

    j = 0
    calibration_values = []
    non_zero_index = None
    while non_zero_index is None:
        calibration_values = [
            float(lines[j].split(",")[i].strip()) for i in range(5, 9)
        ]
        non_zero_index = next(
            (i for i, value in enumerate(calibration_values) if value != 0.0), None
        )
        j += 1

    if non_zero_index is None:
        print("Error: No test value found")
        exit(1)
    elif calibration_values[non_zero_index] > 30:
        print(
            f"Error on line {j} of the file, incorrect sensor reading.\nFile Path: {file_path}"
        )
        exit(1)
    # else: print(non_zero_index, calibration_values, j)

    for line in lines:
        parts = line.split(",")
        timestamp = float(parts[0].strip()) / 1000
        sensor_values = [int(parts[i].strip("\t")) for i in range(1, 5)]

        # Find the index of the non-zero calibration value
        force_value = sensor_values[non_zero_index]

        time.append(timestamp)
        raw_force.append(force_value)
        force_N.append(float(parts[5:9][non_zero_index]))

    return time, raw_force, force_N


# Write the new coefficients for all sensors to a file
def write_output_to_file(filename, coefficients):
    with open(filename, "w") as f:
        formatted_data = f"{{ {', '.join([f"{{ {m}, {c} }}" for m, c in coefficients])} }}"
        f.write(formatted_data)
        print(f"New coefficients: {formatted_data}")


# Modified loop over sensors and tests to process the data
new_coefficients_corrected = []

for testNum in range(1, NUM_TESTS + 1):
    for sensorNum in range(1, NUM_SENSORS + 1):
        # Load the Excel data
        excel_data = pd.read_excel(
            f"{WORKING_DIR}Raw Test Data (Excel)/Sensor Set {SENSOR_SET}/{CALIBRATION_PREFIX}Test {testNum}.xlsx",
            sheet_name=f"Sensor {sensorNum}",
        )
        excel_time = excel_data["Time [s]"].values
        excel_force = [abs(value) for value in excel_data["Force [N]"].values]

        # Parse the Arduino data
        arduino_time, arduino_raw_force, arduino_force_N = parse_arduino_data(
            f"{WORKING_DIR}{ARDUINO_DIR}{CALIBRATION_PREFIX}Test {testNum} Sensor {sensorNum}.txt"
        )

        # Adjust timestamps
        excel_start_idx = find_rising_edge(excel_force)
        arduino_start_idx = find_rising_edge(arduino_force_N)
        time_shift = excel_time[excel_start_idx] - arduino_time[arduino_start_idx]
        adjusted_arduino_time = [time + time_shift for time in arduino_time]

        # Interpolate Arduino data to have common time points with Excel data
        interpolated_arduino_force = np.interp(
            excel_time, adjusted_arduino_time, arduino_raw_force
        )

        # Calculate new m and c values using Excel data and interpolated Arduino data
        m_new, c_new = calculate_linear_fit(excel_force, interpolated_arduino_force)

        new_coefficients_corrected.append((m_new, c_new))

# Write the corrected new coefficients for all sensors to a file
write_output_to_file(
    f"{WORKING_DIR}Coefficients/Sensor Set {SENSOR_SET}/New Coefficients.txt",
    new_coefficients_corrected,
)
