import numpy as np
import pandas as pd

from Configuration_Variables import *


def calculate_linear_fit(excel_force, arduino_raw_force):
    """
    Calculate the linear regression coefficients for force data.

    This function computes the linear regression coefficients (slope 'm' and intercept 'c')
    that best fit the relationship between force data from an Excel file (typically Instron data)
    and raw force data from an Arduino device.

    :param excel_force: Array-like, force data from Excel (Instron data).
    :param arduino_raw_force: Array-like, raw force data from Arduino.
    :return: Tuple, (m, b) coefficients from the linear fit.
    """
    A = np.vstack([arduino_raw_force, np.ones(len(arduino_raw_force))]).T
    m, b = np.linalg.lstsq(A, excel_force, rcond=None)[0]
    return m, b


def write_coefficients_to_file(filename, coefficients):
    """
    Write the calculated linear regression coefficients to a file.

    This function takes the calculated coefficients and writes them into the specified file.
    The coefficients are formatted as a series of tuples, each representing the slope 'm'
    and intercept 'b' for a sensor.

    The formatting is meant to then be paste-able into the arduino code.

    :param filename: String, path of the file where coefficients are to be saved.
    :param coefficients: Iterable of tuples, each tuple containing the 'm' and 'c' coefficients.
    """
    with open(filename, "w") as f:
        formatted_data = f"{{ {', '.join([f'{{ {m}, {b} }}' for m, b in coefficients])} }}"
        f.write(formatted_data)
        print(f"New coefficients: {formatted_data}")


def calculate_coefficients():
    """
    Calculate new calibration coefficients for all sensors and write them to a file.
    """
    new_coefficients_corrected = []

    for sensor_num in range(1, NUM_SENSORS + 1):
        # Read data from CSV files
        instron_data = pd.read_csv(get_data_filepath(ALIGNED_INSTRON_DIR, sensor_num))
        aligned_arduino_data = pd.read_csv(get_data_filepath(ALIGNED_ARDUINO_DIR, sensor_num))

        # Get force data from both datasets
        instron_force = instron_data["Force [N]"].values
        arduino_raw_force = aligned_arduino_data[f"ADC{'' if SIMPLIFY else sensor_num}"].values

        # Calculate linear fit and append to list of new coefficients
        new_coefficients_corrected.append(calculate_linear_fit(instron_force, arduino_raw_force))

    write_coefficients_to_file(COEFFICIENTS_DIR / "New Coefficients.txt", new_coefficients_corrected)
