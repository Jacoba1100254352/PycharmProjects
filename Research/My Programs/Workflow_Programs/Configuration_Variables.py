from pathlib import Path

# Define Global constants
SENSOR_SET = 1
NUM_SENSORS = 4
TEST_NUM = 2
WORKING_DIR = Path(
    "/Users/jacobanderson/Library/CloudStorage/Box-Box/Nanogroup/Projects/Bioimpedance/Pressure Controller/Jacob's Tests/Calibration Tests"
)

# Relative directory paths using pathlib
# Supplemental
SENSOR_SET_DIR = f"Sensor Set {SENSOR_SET}"
COEFFICIENTS_DIR = WORKING_DIR / "Coefficients" / SENSOR_SET_DIR
PLOTS_DIR = WORKING_DIR / "Data Plots" / SENSOR_SET_DIR

# Arduino
ARDUINO_DIR = "Arduino Data"
ALIGNED_ARDUINO_DIR = WORKING_DIR / ARDUINO_DIR / "Aligned Arduino Data" / SENSOR_SET_DIR
CALIBRATED_ARDUINO_DIR = WORKING_DIR / ARDUINO_DIR / "Calibrated Arduino Data" / SENSOR_SET_DIR
ORIGINAL_ARDUINO_DIR = WORKING_DIR / ARDUINO_DIR / "Original Arduino Data" / SENSOR_SET_DIR
PARSED_ARDUINO_DIR = WORKING_DIR / ARDUINO_DIR / "Parsed Arduino Data" / SENSOR_SET_DIR

# Instron
INSTRON_DIR = "Instron Data"
ORIGINAL_INSTRON_DIR = WORKING_DIR / INSTRON_DIR / "Original Instron Data" / SENSOR_SET_DIR
PARSED_INSTRON_DIR = WORKING_DIR / INSTRON_DIR / "Parsed Instron Data" / SENSOR_SET_DIR

# For Align Data program
PERCENTILE = 3

# Determines whether to only list the sensor specific values
SIMPLIFY = True
