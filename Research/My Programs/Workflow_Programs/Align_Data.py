import numpy as np
import pandas as pd

from Configuration_Variables import *


def find_percentile_index(force_data):
    """
    Find the index of the first occurrence of a value equal to or greater than the specified percentile.

    :param force_data: Array-like, data in which to find the percentile index.
    :return: Tuple, (index, percentile_value).
    """
    percentile_value = np.percentile(force_data, PERCENTILE)
    index = np.argmax(force_data >= percentile_value)
    return index


def align_and_save_arduino_data(sensor_num, parsed_instron_data, parsed_arduino_data, aligned_data_dir):
    """
    Align and save Arduino data to the specified directory.

    :param sensor_num: Integer, the sensor number.
    :param parsed_instron_data: DataFrame, the data from the Instron device.
    :param parsed_arduino_data: DataFrame, the data from the Arduino device.
    :param aligned_data_dir: Path, directory to save the aligned data.
    """
    # Find the index of the percentile value in both datasets
    instron_index = find_percentile_index(parsed_instron_data["Force [N]"])
    arduino_index = find_percentile_index(parsed_arduino_data[f"ADC{'' if SIMPLIFY else sensor_num}"])

    # Align the datasets based on the percentile index
    aligned_arduino_data = parsed_arduino_data.iloc[arduino_index:]
    aligned_instron_data = parsed_instron_data.iloc[instron_index:]

    # Truncate both datasets to the shortest length
    min_length = min(len(aligned_arduino_data), len(aligned_instron_data))
    aligned_arduino_data = aligned_arduino_data.head(min_length)

    # Combine and save the aligned data
    column_names = ["Time [s]"] + ["ADC"] if SIMPLIFY else [f"ADC{sensor_num}", f"Force [N]"]
    aligned_arduino_data = aligned_arduino_data[column_names]
    aligned_arduino_data.to_csv(aligned_data_dir, index=False)  # parsed_arduino_data

    print(f"Aligned data saved to {aligned_data_dir}")


def align_data():
    """
    Align data for all sensors.
    """
    for sensor_num in range(1, NUM_SENSORS + 1):
        parsed_instron_data = pd.read_csv(get_data_filepath(PARSED_INSTRON_DIR, sensor_num))
        parsed_arduino_data = pd.read_csv(get_data_filepath(PARSED_ARDUINO_DIR, sensor_num))

        aligned_data_filename = get_data_filepath(ALIGNED_ARDUINO_DIR, sensor_num)
        align_and_save_arduino_data(sensor_num, parsed_instron_data, parsed_arduino_data, aligned_data_filename)
