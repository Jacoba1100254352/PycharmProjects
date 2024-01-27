from pathlib import Path

# Define Global constants
SENSOR_SET = 1
NUM_SENSORS = 4
TEST_NUM = 2
WORKING_DIR = Path(
    "/Users/jacobanderson/Library/CloudStorage/Box-Box/Nanogroup/Projects/Bioimpedance/Pressure Controller/Jacob's Tests/Calibration Tests")

# Relative directory paths using pathlib
SENSOR_SET_DIR = f"Sensor Set {SENSOR_SET}"
ALIGNED_DATA_DIR = WORKING_DIR / "Aligned Arduino Data" / SENSOR_SET_DIR
CALIBRATED_DIR = WORKING_DIR / "Updated Arduino Data" / SENSOR_SET_DIR
COEFFICIENTS_DIR = WORKING_DIR / "Coefficients" / SENSOR_SET_DIR
ARDUINO_DIR = WORKING_DIR / "Arduino Data" / SENSOR_SET_DIR
INSTRON_DIR = WORKING_DIR / "Instron Data" / SENSOR_SET_DIR
PLOT_DIR = WORKING_DIR / "Data Plots" / SENSOR_SET_DIR

# For Align Data program
PERCENTILE = 3

# Determines whether to only list the sensor specific values
SIMPLIFY = True
