import numpy as np
import pandas as pd
from File_Paths import *


def find_rising_edge(data_series, threshold_ratio=0.0001):
    series = pd.Series(data_series)
    derivative = series.diff().fillna(0)
    threshold = threshold_ratio * derivative.abs().max()
    rising_edge_index = derivative[derivative.abs() > threshold].index.min()
    return rising_edge_index


def calculate_linear_fit(excel_force, arduino_raw_force):
    A = np.vstack([arduino_raw_force, np.ones(len(arduino_raw_force))]).T
    m, c = np.linalg.lstsq(A, excel_force, rcond=None)[0]
    return m, c


# Write the new coefficients for all sensors to a file
def write_output_to_file(filename, coefficients):
    with open(filename, "w") as f:
        formatted_data = f"{{ {', '.join([f"{{ {m}, {c} }}" for m, c in coefficients])} }}"
        f.write(formatted_data)
        print(f"New coefficients: {formatted_data}")


def calculate_coefficients():
    # Modified loop over sensors and tests to process the data
    new_coefficients_corrected = []

    for sensor_num in range(1, NUM_SENSORS + 1):
        # Load the Excel data
        instron_data = pd.read_csv(
            f"{WORKING_DIR}{INSTRON_DIR}Parsed Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv",
        )
        instron_time = instron_data["Time [s]"].values
        instron_force = [abs(value) for value in instron_data["Force [N]"].values]

        # Load the Arduino data
        parsed_arduino_data = pd.read_csv(
            f"{WORKING_DIR}{ARDUINO_DIR}Parsed Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv"
        )
        arduino_time = parsed_arduino_data["Time [s]"]
        arduino_raw_force = parsed_arduino_data[f"ADC{"" if SIMPLIFY else sensor_num}"]

        # Adjust timestamps
        excel_start_idx = find_rising_edge(instron_force)
        arduino_start_idx = find_rising_edge(arduino_raw_force)
        time_shift = instron_time[excel_start_idx] - arduino_time[arduino_start_idx]
        adjusted_arduino_time = [time + time_shift for time in arduino_time]

        # Interpolate Arduino data to have common time points with Excel data
        interpolated_arduino_force = np.interp(
            instron_time, adjusted_arduino_time, arduino_raw_force
        )

        # Calculate new m and c values using Excel data and interpolated Arduino data
        m_new, c_new = calculate_linear_fit(instron_force, interpolated_arduino_force)

        new_coefficients_corrected.append((m_new, c_new))

    # Write the corrected new coefficients for all sensors to a file
    write_output_to_file(
        f"{WORKING_DIR}{COEFFICIENTS_DIR}New Coefficients.txt",
        new_coefficients_corrected,
    )
