import numpy as np
import pandas as pd

# Define Global constants
SENSOR_SET = 1
TEST_NUM = 2
NUM_SENSORS = 4
WORKING_DIR = "/Users/jacobanderson/Library/CloudStorage/Box-Box/Nanogroup/Projects/Bioimpedance/Pressure Controller/Jacob's Tests/Calibration Tests/"

# Define file directory and naming conventions
EXCEL_DIR = "Raw Test Data (Excel)/"
SENSOR_SET_DIR = f"Sensor Set {SENSOR_SET}/"
ARDUINO_DIR = f"Arduino Data/{SENSOR_SET_DIR}"
CALIBRATION_PREFIX = "Calibration "


def parse_arduino_line(line):
    """Parse a line of Arduino data."""
    values = line.replace(",\t\t", ",").strip().split(",")

    # TODO: Make sure to bridge the gap with 20ms increment, verify this completes the gap
    if len(values) < 11:
        print(f"Ignoring invalid values -> {values}")
        return []

    timestamp = round(float(values[0]) / 1000, 2)
    adc_readings = list(map(int, values[1:5]))
    force_values = list(map(float, values[5:9]))
    total_values = list(map(float, values[9:11]))

    return [timestamp] + adc_readings + force_values + total_values


def interpolate_instron_data(instron_data):
    """Interpolate Instron data to match a regular time series with increments of 0.02 seconds, rounding 'Time [s]' to two decimal places and the other columns to four decimal places."""
    max_time = instron_data["Time [s]"].iloc[-1]
    new_times = np.arange(0, max_time + 0.02, 0.02)  # Include max_time in the range

    # Interpolate the values for 'Displacement [mm]' and 'Force [N]' at the new time points
    instron_data.set_index("Time [s]", inplace=True)
    interpolated_df = instron_data.reindex(new_times).interpolate().reset_index()

    # Round the 'Time [s]' column to two decimal places
    interpolated_df["Time [s]"] = interpolated_df["Time [s]"].round(2)

    # Round the 'Displacement [mm]' and 'Force [N]' columns to four decimal places
    interpolated_df["Displacement [mm]"] = interpolated_df["Displacement [mm]"].round(4)
    interpolated_df["Force [N]"] = -interpolated_df["Force [N]"].round(4)

    return interpolated_df[["Time [s]", "Displacement [mm]", "Force [N]"]]


def write_to_csv(filename, df):
    """Write DataFrame to a CSV file."""
    df.to_csv(filename, index=False)
    print(f"Instron data saved to {filename}")


def read_and_process_instron_data(sensor_num):
    """Read Instron data from an Excel file and process it."""
    excel_filename = f"{WORKING_DIR}{EXCEL_DIR}{SENSOR_SET_DIR.format(SENSOR_SET)}Calibration Test {TEST_NUM}.xlsx"
    instron_data = pd.read_excel(excel_filename, sheet_name=f"Sensor {sensor_num}")
    interpolated_instron_data = interpolate_instron_data(instron_data)
    instron_csv_filename = f"{WORKING_DIR}{EXCEL_DIR}{SENSOR_SET_DIR}Interpolated Calibration Test {TEST_NUM} Sensor {sensor_num}.csv"
    write_to_csv(instron_csv_filename, interpolated_instron_data)


def write_updated_data_to_csv(filename, data):
    """Write sensor data to a CSV file."""
    df = pd.DataFrame(
        data,
        columns=[
            "Timestamp",
            "ADC1",
            "ADC2",
            "ADC3",
            "ADC4",
            "Force1",
            "Force2",
            "Force3",
            "Force4",
            "TotalForce1",
            "TotalForce2",
        ],
    )
    df.to_csv(filename, index=False)
    print(f"Arduino data saved to {filename}")


def read_and_process_arduino_data(sensor_num):
    """Read Arduino data from a text file and process it."""
    arduino_filename = f"{WORKING_DIR}{ARDUINO_DIR.format(SENSOR_SET)}{CALIBRATION_PREFIX}Test {TEST_NUM} Sensor {sensor_num}.txt"
    with open(arduino_filename, "r") as file:
        arduino_data = [
            parse_arduino_line(line) for line in file if parse_arduino_line(line)
        ]
    arduino_csv_filename = f"{WORKING_DIR}{ARDUINO_DIR.format(SENSOR_SET)}{CALIBRATION_PREFIX}Test {TEST_NUM} Sensor {sensor_num}.csv"
    write_updated_data_to_csv(arduino_csv_filename, arduino_data)


# Process data for each sensor
for sensor_num in range(1, NUM_SENSORS + 1):
    read_and_process_instron_data(sensor_num)
    read_and_process_arduino_data(sensor_num)
