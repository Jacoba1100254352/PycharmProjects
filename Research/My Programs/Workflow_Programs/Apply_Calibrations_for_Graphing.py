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
            return [(float(m), float(c)) for m, c in pairs]
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

    for sensor_num in range(1, NUM_SENSORS + 1):
        #
        aligned_data_filename = get_data_filepath(ALIGNED_ARDUINO_DIR, sensor_num)
        aligned_arduino_data = pd.read_csv(aligned_data_filename)
        calibrated_arduino_data = aligned_arduino_data.copy()

        # Apply calibration and center the data
        if SIMPLIFY:
            calibrated_arduino_data["Force [N]"] = new_coefficients[sensor_num - 1][0] * calibrated_arduino_data[
                "ADC"] + new_coefficients[sensor_num - 1][1]
        else:
            for j in range(4):
                calibrated_arduino_data[f"Force{j + 1} [N]"] = new_coefficients[j][0] * calibrated_arduino_data[
                    f"ADC{j + 1}"] + new_coefficients[j][1]
            calibrated_arduino_data["TotalForce1 [N]"] = sum(
                [calibrated_arduino_data[f"Force{j + 1} [N]"] for j in range(4)])
            calibrated_arduino_data["TotalForce2 [N]"] = 0

        # Subtract the baseline average or center at zero
        instron_data = pd.read_csv(
            get_data_filepath(ALIGNED_INSTRON_DIR, sensor_num))  # specify the correct path to the Instron data file
        baseline_average = instron_data["Force [N]"][:10].mean()  # FIXME: Make more robust (find the time frame)
        calibrated_arduino_data["Force [N]" if SIMPLIFY else f"Force{sensor_num} [N]"] -= baseline_average

        # Write the updated data to a CSV file
        updated_csv_filename = get_data_filepath(CALIBRATED_ARDUINO_DIR, sensor_num)
        write_updated_data_to_csv(updated_csv_filename, calibrated_arduino_data)
