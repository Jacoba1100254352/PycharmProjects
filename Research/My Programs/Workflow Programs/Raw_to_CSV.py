import numpy as np
import pandas as pd
from File_Paths import *

NUM_SENSORS_OFFSET = 4

def parse_arduino_line(line, sensor_num=None):
    """Parse a line of Arduino data."""
    values = line.replace(",\t\t", ",").strip().split(",")

    # TODO: Make sure to bridge the gap with 20ms increment, verify this completes the gap
    if len(values) < 11:
        print(f"Ignoring invalid values -> {values}")
        return []

    #
    timestamp = [round(float(values[0]) / 1000, 2)]

    if SIMPLIFY:
        if sensor_num is not None and 0 <= sensor_num < len(values):
            adc_readings = [int(values[sensor_num])]
            force_values = [float(values[sensor_num + NUM_SENSORS_OFFSET])]
        else:
            print("Invalid sensor number")
            return []
    else:
        adc_readings = list(map(int, values[1:5]))
        force_values = list(map(float, values[5:9]))

    total_values = [] if SIMPLIFY else list(map(float, values[9:11]))

    return timestamp + adc_readings + force_values + total_values


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
    excel_filename = f"{WORKING_DIR}{INSTRON_DIR}Calibration Test {TEST_NUM}.xlsx"
    instron_data = pd.read_excel(excel_filename, sheet_name=f"Sensor {sensor_num}")
    interpolated_instron_data = interpolate_instron_data(instron_data)
    instron_csv_filename = f"{WORKING_DIR}{INSTRON_DIR}Parsed Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv"
    write_to_csv(instron_csv_filename, interpolated_instron_data)


def write_updated_data_to_csv(filename, data):
    """Write sensor data to a CSV file."""
    if SIMPLIFY:
        df = pd.DataFrame(
            data,
            columns=[
                "Time [s]",
                "ADC",
                "Force [N]",
            ],
        )
    else:
        df = pd.DataFrame(
            data,
            columns=[
                "Time [s]",
                "ADC1",
                "ADC2",
                "ADC3",
                "ADC4",
                "Force1 [N]",
                "Force2 [N]",
                "Force3 [N]",
                "Force4 [N]",
                "TotalForce1 [N]",
                "TotalForce2 [N]",
            ],
        )
    df.to_csv(filename, index=False)
    print(f"Data successfully saved to {filename}")


def read_and_process_arduino_data(sensor_num):
    """Read Arduino data from a text file and process it."""
    arduino_filename = f"{WORKING_DIR}{ARDUINO_DIR}Calibration Test {TEST_NUM} Sensor {sensor_num}.txt"
    with open(arduino_filename, "r") as file:
        arduino_data = [
            parse_arduino_line(line, sensor_num) for line in file if parse_arduino_line(line, sensor_num)
        ]
    arduino_csv_filename = f"{WORKING_DIR}{ARDUINO_DIR}Parsed Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv"
    write_updated_data_to_csv(arduino_csv_filename, arduino_data)


# Process data for each sensor
def write_raw_data_to_csv():
    for sensor_num in range(1, NUM_SENSORS + 1):
        read_and_process_instron_data(sensor_num)
        read_and_process_arduino_data(sensor_num)
