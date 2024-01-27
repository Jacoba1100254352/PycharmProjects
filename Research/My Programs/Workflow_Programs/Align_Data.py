import numpy as np
import pandas as pd

from Configuration_Variables import *


def find_percentile_index(force_data, percentile):
    """
    Find the index of the first occurrence of a value equal to or greater than the specified percentile.

    :param force_data: Array-like, data in which to find the percentile index.
    :param percentile: Numeric, the percentile to find.
    :return: Tuple, (index, percentile_value).
    """
    percentile_value = np.percentile(force_data, percentile)
    index = np.argmax(force_data >= percentile_value)
    return index, percentile_value


def find_deviation_point(data, column, baseline, deviation_threshold):
    """
    Find the point in the dataset where the values start to consistently deviate
    from the baseline by more than the specified threshold.

    :param data: DataFrame, the dataset to analyze.
    :param column: String, the column in the dataset to consider.
    :param baseline: Numeric, the baseline value for comparison.
    :param deviation_threshold: Numeric, the threshold for deviation.
    :return: Integer or None, the index of the deviation point or None if not found.
    """
    deviations = abs(data[column] - baseline) > deviation_threshold
    deviation_count = deviations.cumsum() - deviations.cumsum().where(~deviations).ffill().fillna(0)
    return deviation_count[deviation_count >= 10].idxmin() if any(deviation_count >= 10) else None


def align_and_save_arduino_data(sensor_num, instron_data, arduino_data, aligned_data_dir, percentile=1):
    """
    Align and save Arduino data to the specified directory.

    :param sensor_num: Integer, the sensor number.
    :param instron_data: DataFrame, the data from the Instron device.
    :param arduino_data: DataFrame, the data from the Arduino device.
    :param aligned_data_dir: Path, directory to save the aligned data.
    :param percentile: Numeric, the percentile used for alignment.
    """
    # Find the index of the percentile value in both datasets
    instron_index, _ = find_percentile_index(instron_data["Force [N]"], percentile)
    arduino_index, _ = find_percentile_index(arduino_data[f"ADC{'' if SIMPLIFY else sensor_num}"], percentile)

    # Align the datasets based on the percentile index
    aligned_arduino_data = arduino_data.iloc[arduino_index:]
    aligned_instron_data = instron_data.iloc[instron_index:]

    # Truncate both datasets to the shortest length
    min_length = min(len(aligned_arduino_data), len(aligned_instron_data))
    aligned_arduino_data = aligned_arduino_data.head(min_length)

    # Combine and save the aligned data
    column_names = ["Time [s]", f"ADC{'' if SIMPLIFY else sensor_num}", f"Force [N]"]
    aligned_data = aligned_arduino_data[column_names]
    aligned_data.to_csv(aligned_data_dir, index=False)

    print(f"Aligned data saved to {aligned_data_dir}")


def align_data():
    """
    Align data for all sensors.
    """
    for sensor_num in range(1, NUM_SENSORS + 1):
        parsed_instron_data_filename = PARSED_INSTRON_DIR / f"Parsed Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv"
        parsed_instron_data = pd.read_csv(parsed_instron_data_filename)
        parsed_arduino_data_filename = PARSED_ARDUINO_DIR / f"Parsed Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv"
        parsed_arduino_data = pd.read_csv(parsed_arduino_data_filename)

        aligned_data_filename = ALIGNED_ARDUINO_DIR / f"Aligned Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv"
        align_and_save_arduino_data(sensor_num, parsed_instron_data, parsed_arduino_data, aligned_data_filename,
                                    PERCENTILE)
