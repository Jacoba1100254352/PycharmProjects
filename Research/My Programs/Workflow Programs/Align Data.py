import numpy as np
import pandas as pd

# Define Global constants
SENSOR_SET = 1
NUM_SENSORS = 4
TEST_NUM = 2
WORKING_DIR = "/Users/jacobanderson/Library/CloudStorage/Box-Box/Nanogroup/Projects/Bioimpedance/Pressure Controller/Jacob's Tests/"

PERCENTILE = 3

# Calibration and graphing flags
calibration = True

# Adjusting directory paths based on calibration flag
PLOT_DIR = "Calibration Tests/Data Plots/" if calibration else "Data Plots/"
EXCEL_DIR = (
    "Calibration Tests/Raw Test Data (Excel)/"
    if calibration
    else "Raw Test Data (Excel)/"
)
SENSOR_SET_DIR = f"Sensor Set {SENSOR_SET}/"
ALIGNED_DATA_DIR = (
    "Calibration Tests/Aligned Arduino Data/"
    if calibration
    else "Aligned Arduino Data/"
)

# Directory adjustments
ARDUINO_DIR = f"Calibration Tests/Arduino Data/" if calibration else "Arduino Data/"
CALIBRATION_PREFIX = "Calibration "

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
    arduino_index, arduino_percentile = find_percentile_index(arduino_data[f"ADC{sensor_num}"], percentile)

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
    aligned_data = aligned_arduino_data[
        ["Timestamp"]
        + [f"ADC{i}" for i in range(1, NUM_SENSORS + 1)]
        + [f"Force{i}" for i in range(1, NUM_SENSORS + 1)]
        + ["TotalForce1", "TotalForce2"]
        ]
    aligned_data.to_csv(aligned_data_dir, index=False)

    print(f"Aligned data saved to {aligned_data_dir}")


# Load and align data
for sensor_num in range(1, NUM_SENSORS + 1):
    instron_filename = f"{WORKING_DIR}{EXCEL_DIR}{SENSOR_SET_DIR}Interpolated Calibration Test {TEST_NUM} Sensor {sensor_num}.csv"
    instron_data = pd.read_csv(instron_filename)
    original_arduino_data_filename = f"{WORKING_DIR}{ARDUINO_DIR}{SENSOR_SET_DIR}{CALIBRATION_PREFIX}Test {TEST_NUM} Sensor {sensor_num}.csv"
    original_arduino_data = pd.read_csv(original_arduino_data_filename)

    aligned_data_filename = f"{WORKING_DIR}{ALIGNED_DATA_DIR}{SENSOR_SET_DIR}Aligned Test {TEST_NUM} Sensor {sensor_num}.csv"
    align_and_save_arduino_data(sensor_num, instron_data, original_arduino_data, aligned_data_filename, PERCENTILE)
