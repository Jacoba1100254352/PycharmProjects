import numpy as np
import pandas as pd
from File_Paths import *

def find_percentile_index(force_data, percentile):
    percentile_value = np.percentile(force_data, percentile)
    for i, value in enumerate(force_data):
        if value >= percentile_value:
            return i, percentile_value
    return None, percentile_value

def find_deviation_point(data, column, baseline, deviation_threshold):
    """
    Find the point in the dataset where the values start to consistently deviate
    from the baseline by more than the specified threshold.
    """
    deviation_count = 0
    for i, value in enumerate(data[column]):
        if abs(value - baseline) > deviation_threshold:
            deviation_count += 1
        else:
            deviation_count = 0

        # Assuming "consistently" means 10 consecutive points
        if deviation_count >= 10:
            return i
    return None


def align_and_save_arduino_data(sensor_num, instron_data, arduino_data, aligned_data_dir, percentile=1):
    # Find the index of the percentile value in both datasets
    instron_index, instron_percentile = find_percentile_index(instron_data["Force [N]"], percentile)
    arduino_index, arduino_percentile = find_percentile_index(arduino_data[f"ADC{"" if SIMPLIFY else sensor_num}"], percentile)

    # Align the datasets based on the percentile index
    aligned_arduino_data = arduino_data.iloc[arduino_index:]
    aligned_instron_data = instron_data.iloc[instron_index:]

    # Ensure both datasets have the same length after alignment
    min_length = min(len(aligned_arduino_data), len(aligned_instron_data))
    aligned_arduino_data = aligned_arduino_data.head(min_length)
    aligned_instron_data = aligned_instron_data.head(min_length)

    # Truncating to the shortest length
    min_length = min(len(aligned_arduino_data), len(aligned_instron_data))
    aligned_arduino_data = aligned_arduino_data.head(min_length)

    # Combine and save the aligned data
    if SIMPLIFY:
        aligned_data = aligned_arduino_data[
            ["Time [s]", f"ADC", f"Force [N]"]
        ]
    else:
        aligned_data = aligned_arduino_data[
            ["Time [s]"]
            + [f"ADC{i}" for i in range(1, NUM_SENSORS + 1)]
            + [f"Force{i} [N]" for i in range(1, NUM_SENSORS + 1)]
            + ["TotalForce1 [N]", "TotalForce2 [N]"]
            ]
    aligned_data.to_csv(aligned_data_dir, index=False)

    print(f"Aligned data saved to {aligned_data_dir}")


# Load and align data
def align_data():
    for sensor_num in range(1, NUM_SENSORS + 1):
        parsed_instron_data_filename = f"{WORKING_DIR}{INSTRON_DIR}Parsed Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv"
        parsed_instron_data = pd.read_csv(parsed_instron_data_filename)
        parsed_arduino_data_filename = f"{WORKING_DIR}{ARDUINO_DIR}Parsed Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv"
        parsed_arduino_data = pd.read_csv(parsed_arduino_data_filename)

        aligned_data_filename = f"{WORKING_DIR}{ALIGNED_DATA_DIR}Aligned Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv"
        align_and_save_arduino_data(sensor_num, parsed_instron_data, parsed_arduino_data, aligned_data_filename, PERCENTILE)
