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
    # Find the index of the 20% and 80% percentile values in both datasets
    # Negate the instron data to invert it positively to align with the arduino data for analysis purposes
    instron_20_index = find_percentile_index(-parsed_instron_data["Force [N]"], 20)
    instron_80_index = find_percentile_index(-parsed_instron_data["Force [N]"], 80)
    arduino_20_index = find_percentile_index(parsed_arduino_data[f"ADC{'' if SIMPLIFY else sensor_num}"], 20)
    arduino_80_index = find_percentile_index(parsed_arduino_data[f"ADC{'' if SIMPLIFY else sensor_num}"], 80)

    # Calculate time offsets
    time_offset_20 = parsed_instron_data["Time [s]"][instron_20_index] - parsed_arduino_data["Time [s]"][
        arduino_20_index]
    time_offset_80 = parsed_instron_data["Time [s]"][instron_80_index] - parsed_arduino_data["Time [s]"][
        arduino_80_index]
    avg_time_offset = (time_offset_20 + time_offset_80) / 2

    # Adjust Arduino time # FIXME: should find a way to use avg_time_offset or combine both offsets
    parsed_arduino_data["Time [s]"] = parsed_arduino_data["Time [s]"] + time_offset_20

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
