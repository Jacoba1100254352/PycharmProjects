import matplotlib.pyplot as plt
import pandas as pd

from Configuration_Variables import *


def read_excel_sensor_data(filename, sheet_name):
    """
    Read sensor data from an Excel file.

    :param filename: Path, the file from which to read sensor data.
    :param sheet_name: String, the name of the sheet to read.
    :return: Tuple, (excel_time, excel_force).
    """
    excel_data = pd.read_excel(filename, sheet_name=sheet_name)
    excel_time = excel_data["Time [s]"].values
    excel_force = [abs(value) for value in excel_data["Force [N]"].values]
    return excel_time, excel_force


def plot_sensor_data(time_data, force_data, sensor_num):
    """
    Plot sensor data.

    :param time_data: Array-like, time data for the sensor.
    :param force_data: Array-like, force data for the sensor.
    :param sensor_num: Integer, the sensor number.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(time_data, force_data, label="Interpolated Uncalibrated Arduino Data", color="orange")

    plt.xlabel("Time [s]")
    plt.ylabel("Force [N]")
    plt.legend()
    plt.title(f"Comparison of Force Data for Sensor Set {SENSOR_SET}, Sensor {sensor_num}, Test {TEST_NUM}")
    plt.grid(True)
    plt.show()


# Running the analysis with interpolation and plotting the results
for sensorNum in range(1, NUM_SENSORS + 1):
    excel_filename = ORIGINAL_INSTRON_DIR / f"Original Calibration Test {TEST_NUM} Data.xlsx"
    excel_time, excel_force = read_excel_sensor_data(excel_filename, f"Sensor {sensorNum}")

    plot_sensor_data(excel_time, excel_force, sensorNum)
