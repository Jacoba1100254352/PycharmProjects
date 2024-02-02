import numpy as np
import pandas as pd

from Configuration_Variables import *


def find_percentile_index(force_data, percentile):
    """
    Find the index of the first occurrence of a value equal to or greater than the specified percentile.

    :param force_data: Array-like, data in which to find the percentile index.
    :param percentile: Integer, the desired percentile.
    :return: Tuple, (index, percentile_value).
    """
    percentile_value = np.percentile(force_data, percentile)
    index = np.argmax(force_data >= percentile_value)
    return index


def align_and_save_data(sensor_num, parsed_instron_data, parsed_arduino_data):
    """
    Align and save Arduino data to the specified directory.

    :param sensor_num: Integer, the sensor number.
    :param parsed_instron_data: DataFrame, the data from the Instron device.
    :param parsed_arduino_data: DataFrame, the data from the Arduino device.
    """
    percentiles = range(1, 100, 1)  # Percentiles from 10% to 90% at 10% intervals
    time_offsets = []

    for percentile in percentiles:
        # Find the index of the current percentile in both datasets
        # Negate the instron data to invert it positively to align with the arduino data for analysis purposes
        instron_index = find_percentile_index(-parsed_instron_data["Force [N]"], percentile)
        arduino_index = find_percentile_index(parsed_arduino_data[f"ADC{'' if SIMPLIFY else sensor_num}"], percentile)

        # Calculate and store the time offset for the current percentile
        time_offset = parsed_instron_data["Time [s]"][instron_index] - parsed_arduino_data["Time [s]"][arduino_index]
        time_offsets.append(time_offset)

    # Calculate the average of the time offsets
    avg_time_offset = sum(time_offsets) / len(time_offsets)

    # Adjust Arduino time
    parsed_arduino_data["Time [s]"] = parsed_arduino_data["Time [s]"] + avg_time_offset

    # Truncate both datasets to the shortest length
    min_length = min(len(parsed_instron_data), len(parsed_arduino_data))
    aligned_instron_data = parsed_instron_data.head(min_length)
    aligned_arduino_data = parsed_arduino_data.head(min_length)

    # Get the aligned data directory names
    aligned_arduino_data_dir = get_data_filepath(ALIGNED_ARDUINO_DIR, sensor_num)
    aligned_instron_data_dir = get_data_filepath(ALIGNED_INSTRON_DIR, sensor_num)

    # Save the aligned data
    aligned_arduino_data.to_csv(aligned_arduino_data_dir, index=False)
    aligned_instron_data.to_csv(aligned_instron_data_dir, index=False)  # This step and file set is likely unnecessary
    print(f"Aligned arduino data saved to {aligned_arduino_data_dir}")
    print(f"Aligned instron data saved to {aligned_instron_data_dir}")


def align_data():
    """
    Align data for all sensors.
    """
    for sensor_num in range(1, NUM_SENSORS + 1):
        parsed_instron_data = pd.read_csv(get_data_filepath(PARSED_INSTRON_DIR, sensor_num))
        parsed_arduino_data = pd.read_csv(get_data_filepath(PARSED_ARDUINO_DIR, sensor_num))

        align_and_save_data(sensor_num, parsed_instron_data, parsed_arduino_data)
