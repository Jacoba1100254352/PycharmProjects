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
PERCENTILE = 5

# Determines whether to only list the sensor specific values
SIMPLIFY = True


def get_data_filepath(directory, sensor_num=None):
    """
    Generate the correct file path based on the given directory and sensor number.

    :param directory: The directory in which the file resides.
    :param sensor_num: The sensor number, if applicable.
    :return: The file path for the specified directory and sensor.
    """
    # Determine file extension and prefix
    if directory in [ORIGINAL_ARDUINO_DIR, CALIBRATED_ARDUINO_DIR, ALIGNED_ARDUINO_DIR, PARSED_ARDUINO_DIR]:
        ext = 'txt' if directory == ORIGINAL_ARDUINO_DIR else 'csv'
        prefix = 'Parsed' if directory == PARSED_ARDUINO_DIR else \
            'Updated' if directory == CALIBRATED_ARDUINO_DIR else \
            'Aligned' if directory == ALIGNED_ARDUINO_DIR else \
            'Original'
    elif directory in [ORIGINAL_INSTRON_DIR, PARSED_INSTRON_DIR]:
        ext = 'csv' if directory == PARSED_INSTRON_DIR else 'xlsx'
        prefix = 'Parsed' if directory == PARSED_INSTRON_DIR else 'Original'
    elif directory == PLOTS_DIR:
        return directory / f"Calibration Test {TEST_NUM} Sensor {sensor_num} plot.png"
    else:
        raise ValueError("Invalid directory")

    # Construct file name
    sensor_str = f" Sensor {sensor_num}" if sensor_num and directory != ORIGINAL_INSTRON_DIR else ""
    return directory / f"{prefix} Calibration Test {TEST_NUM}{sensor_str} Data.{ext}"
