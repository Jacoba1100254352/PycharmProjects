import numpy as np
import pandas as pd

from Configuration_Variables import *

NUM_SENSORS_OFFSET = 4


def parse_arduino_line(line, sensor_num=None):
    """
    Parse a line of Arduino data.

    :param line: String, a line from Arduino data file.
    :param sensor_num: Integer, the number of the sensor to be processed.
    :return: List, parsed values including timestamp, sensor readings, and total values.
    """
    values = line.replace(",\t\t", ",").strip().split(",")

    if len(values) < 11:
        print(f"Ignoring invalid values -> {values}")
        return []

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
    """
    Interpolate Instron data to match a regular time series.

    :param instron_data: DataFrame, Instron data to be interpolated.
    :return: DataFrame, interpolated Instron data.
    """
    instron_data['Time [s]'] = pd.to_numeric(instron_data['Time [s]'])
    instron_data.set_index('Time [s]', inplace=True)

    max_time = instron_data.index.max()
    new_time_index = pd.Index(np.arange(0, max_time + 0.02, 0.02), name='Time [s]')

    interpolated_df = instron_data.reindex(new_time_index).interpolate(method='linear')
    interpolated_df = interpolated_df.reset_index()
    interpolated_df = interpolated_df.round({'Time [s]': 2, 'Displacement [mm]': 4, 'Force [N]': 4})

    return interpolated_df


def write_to_csv(filename, df):
    """
    Write DataFrame to a CSV file.

    :param filename: Path, the name of the file where the DataFrame will be saved.
    :param df: DataFrame, data to be written to CSV.
    """
    df.to_csv(filename, index=False)
    print(f"Instron data saved to {filename}")


def process_instron_data(sensor_num):
    """
    Process Instron data for a given sensor number.

    :param sensor_num: Integer, the number of the sensor to be processed.
    :return: DataFrame, processed Instron data.
    """
    instron_data_filename = INSTRON_DIR / f"Calibration Test {TEST_NUM}.xlsx"
    instron_data = pd.read_excel(instron_data_filename, sheet_name=f"Sensor {sensor_num}")
    return interpolate_instron_data(instron_data)


def process_arduino_data(sensor_num):
    """
    Process Arduino data for a given sensor number and convert it to a DataFrame.

    :param sensor_num: Integer, the number of the sensor to be processed.
    :return: DataFrame, processed Arduino data.
    """
    arduino_filename = ARDUINO_DIR / f"Calibration Test {TEST_NUM} Sensor {sensor_num}.txt"
    with open(arduino_filename, "r") as file:
        data = [parse_arduino_line(line, sensor_num) for line in file if parse_arduino_line(line, sensor_num)]

    # Check if data is empty
    if not data or not data[0]:
        print(f"No valid data found in {arduino_filename}")
        return pd.DataFrame()

    # Determine the number of columns based on the length of the first data entry
    num_columns = len(data[0])

    # Define column names based on the number of columns
    column_names = ["Time [s]"]
    if SIMPLIFY:
        column_names += [f"ADC", f"Force [N]"]
    else:
        column_names += [f"ADC{i}" for i in range(1, 5)] + [f"Force{i} [N]" for i in range(1, 5)]
        if num_columns > 9:
            column_names += ["TotalForce1 [N]", "TotalForce2 [N]"]

    return pd.DataFrame(data, columns=column_names)


def process_and_save_csv(read_filename, write_filename, process_function, **kwargs):
    """
    Read data from a CSV file, process it, and save it back to another CSV file.
    If read_filename is None, it directly processes the data using the process_function.

    :param read_filename: Path or None, the file from which to read data.
    :param write_filename: Path, the file to which processed data will be written.
    :param process_function: Function, the function to process the data.
    :param kwargs: Additional arguments passed to the process function.
    """
    if read_filename is not None:
        # Read the CSV file
        data = pd.read_csv(read_filename)
        # Process the data using the provided function
        processed_data = process_function(data, **kwargs)
    else:
        # Directly process the data
        processed_data = process_function(**kwargs)

    # Write the processed data to a CSV file
    processed_data.to_csv(write_filename, index=False)
    print(f"Data saved to {write_filename}")


def write_raw_data_to_csv():
    """
    Process raw data for each sensor and write it to CSV files.
    """
    for sensor_num in range(1, NUM_SENSORS + 1):
        instron_csv_filename = INSTRON_DIR / f"Parsed Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv"
        process_and_save_csv(None, instron_csv_filename, process_instron_data, sensor_num=sensor_num)

        arduino_csv_filename = ARDUINO_DIR / f"Parsed Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv"
        process_and_save_csv(None, arduino_csv_filename, process_arduino_data, sensor_num=sensor_num)
