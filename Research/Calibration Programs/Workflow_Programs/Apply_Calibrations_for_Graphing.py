import re

import pandas as pd

from Configuration_Variables import *


def read_coefficients(filename):
    """
    Read coefficients from a file.

    :param filename: Path, the file from which to read coefficients.
    :return: List of tuples, containing the coefficients.
    """
    try:
        with open(filename, "r") as f:
            content = f.read()
            pairs = re.findall(r"\{\s*([-\d.]+(?:e[-+]?\d+)?)\s*,\s*([-\d.]+(?:e[-+]?\d+)?)\s*}", content)
            return [(float(m), float(b)) for m, b in pairs]
    except FileNotFoundError:
        print(f"Warning: The file {filename} does not exist!")
        raise
    except ValueError as e:
        print(e)
        raise


def write_updated_data_to_csv(filename, data):
    """
    Write sensor data to a CSV file.

    :param filename: Path, the file to which the data will be written.
    :param data: DataFrame, the sensor data to be written.
    """
    columns = ["Time [s]", "Force [N]"] if SIMPLIFY else ["Time [s]", "ADC1", "ADC2", "ADC3", "ADC4",
                                                          "Force1 [N]", "Force2 [N]", "Force3 [N]", "Force4 [N]",
                                                          "TotalForce1 [N]", "TotalForce2 [N]"]
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(filename, index=False)
    print(f"Data successfully saved to {filename}")


def apply_calibration_coefficients():
    """
    Apply calibration coefficients to each sensor's data and center the data around zero.
    """
    new_coefficients = read_coefficients(COEFFICIENTS_DIR / "New Coefficients.txt")

    # Apply the calibration to each sensor's data
    for sensor_num in range(1, NUM_SENSORS + 1):
        # Read the aligned data
        aligned_data_filename = get_data_filepath(ALIGNED_ARDUINO_DIR, sensor_num)
        aligned_arduino_data = pd.read_csv(aligned_data_filename)
        calibrated_arduino_data = aligned_arduino_data.copy()

        # Apply calibration and center the data
        if SIMPLIFY:
            # Apply the calibration to the force data
            m, b = new_coefficients[sensor_num - 1][:]
            calibrated_arduino_data["Force [N]"] = m * calibrated_arduino_data["ADC"] + b
        else:
            # Apply the calibration to each force sensor and calculate the total force
            for _sensor_num in range(1, NUM_SENSORS + 1):
                m, b = new_coefficients[_sensor_num - 1][:]
                calibrated_arduino_data[f"Force{_sensor_num} [N]"] = m * calibrated_arduino_data[
                    f"ADC{_sensor_num}"] + b
            calibrated_arduino_data["TotalForce1 [N]"] = sum(
                [calibrated_arduino_data[f"Force{_sensor_num} [N]"] for _sensor_num in range(1, NUM_SENSORS + 1)])
            calibrated_arduino_data["TotalForce2 [N]"] = 0

        # Write the updated data to a CSV file
        updated_csv_filename = get_data_filepath(CALIBRATED_ARDUINO_DIR, sensor_num)
        write_updated_data_to_csv(updated_csv_filename, calibrated_arduino_data)
