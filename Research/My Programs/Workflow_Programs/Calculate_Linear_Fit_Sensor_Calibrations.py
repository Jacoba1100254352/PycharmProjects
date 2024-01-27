import numpy as np
import pandas as pd

from Configuration_Variables import *


def find_rising_edge(data_series, threshold_ratio=0.0001):
    """
    Find the index of the rising edge in a data series based on a specified threshold ratio.

    :param data_series: Iterable, the data series to analyze.
    :param threshold_ratio: Float, the ratio to determine the threshold for a rising edge.
    :return: Integer, the index of the rising edge.
    """
    series = pd.Series(data_series)
    derivative = series.diff().fillna(0)
    threshold = threshold_ratio * derivative.abs().max()
    return derivative[derivative.abs() > threshold].index.min()


def calculate_linear_fit(excel_force, arduino_raw_force):
    """
    Calculate linear fit (m and c) for given force data.

    :param excel_force: Array-like, force data from Excel.
    :param arduino_raw_force: Array-like, raw force data from Arduino.
    :return: Tuple, (m, c) coefficients from linear fit.
    """
    A = np.vstack([arduino_raw_force, np.ones(len(arduino_raw_force))]).T
    m, c = np.linalg.lstsq(A, excel_force, rcond=None)[0]
    return m, c


def write_output_to_file(filename, coefficients):
    """
    Write the calculated coefficients to a file.

    :param filename: Path, the file to write the coefficients to.
    :param coefficients: Iterable, the coefficients to write.
    """
    with open(filename, "w") as f:
        formatted_data = f"{{ {', '.join([f'{{ {m}, {c} }}' for m, c in coefficients])} }}"
        f.write(formatted_data)
        print(f"New coefficients: {formatted_data}")


def calculate_coefficients():
    """
    Calculate new calibration coefficients for all sensors and write them to a file.
    """
    new_coefficients_corrected = []

    for sensor_num in range(1, NUM_SENSORS + 1):
        # Load data from CSV files
        instron_data = pd.read_csv(get_data_filepath(PARSED_INSTRON_DIR, sensor_num))
        parsed_arduino_data = pd.read_csv(get_data_filepath(PARSED_ARDUINO_DIR, sensor_num))

        # Extract necessary data
        instron_time = instron_data["Time [s]"].values
        instron_force = [abs(value) for value in instron_data["Force [N]"].values]
        arduino_raw_force = parsed_arduino_data[f"ADC{'' if SIMPLIFY else sensor_num}"]

        # Find start index and adjust timestamps
        excel_start_idx = find_rising_edge(instron_force)
        arduino_start_idx = find_rising_edge(arduino_raw_force)
        time_shift = instron_time[excel_start_idx] - arduino_raw_force[arduino_start_idx]
        adjusted_arduino_time = [time + time_shift for time in arduino_raw_force]

        # Interpolate and calculate new coefficients
        interpolated_arduino_force = np.interp(instron_time, adjusted_arduino_time, arduino_raw_force)
        m_new, c_new = calculate_linear_fit(instron_force, interpolated_arduino_force)
        new_coefficients_corrected.append((m_new, c_new))

    # Write coefficients to file
    write_output_to_file(COEFFICIENTS_DIR / "New Coefficients.txt", new_coefficients_corrected)
