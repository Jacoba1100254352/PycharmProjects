import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define Global constants
SENSOR_SET = 1
NUM_SENSORS = 4
TEST_NUM = 2
BASE_DIR = "/Users/jacobanderson/Library/CloudStorage/Box-Box/Nanogroup/Projects/Bioimpedance/Pressure Controller/Jacob's Tests/"

# Calibration and graphing flags
calibration = True
graph_uncalibrated = False

# Adjusting directory paths based on calibration flag
PLOT_DIR = "Calibration Tests/Data Plots/" if calibration else "Data Plots/"
EXCEL_DIR = (
    "Calibration Tests/Raw Test Data (Excel)/"
    if calibration
    else "Raw Test Data (Excel)/"
)
CALIBRATION_PREFIX = "Calibration " if calibration else ""
UNCALIBRATED_DIR = (
    f"Calibration Tests/Arduino Data/Sensor Set {SENSOR_SET}/"
    if calibration
    else f"Arduino Data/Sensor Set {SENSOR_SET}/"
)
CALIBRATED_DIR = (
    f"Calibration Tests/Updated Arduino Data/Sensor Set {SENSOR_SET}/"
    if calibration
    else f"Updated Arduino Data/Sensor Set {SENSOR_SET}/"
)


# Running the plotting for each sensor
for sensor_num in range(1, NUM_SENSORS + 1):
    # Load the Excel data
    excel_filename = f"{BASE_DIR}{EXCEL_DIR}Sensor Set {SENSOR_SET}/{CALIBRATION_PREFIX}Test {TEST_NUM}.xlsx"
    instron_data = pd.read_excel(excel_filename, sheet_name=f"Sensor {sensor_num}")
    instron_time = instron_data["Time [s]"].values
    instron_force = abs(instron_data["Force [N]"].values)

    # Load updated Arduino data
    updated_data_filename = f"{BASE_DIR}{CALIBRATED_DIR}Updated Calibration Test {TEST_NUM} Sensor {sensor_num}.csv"
    updated_data = pd.read_csv(updated_data_filename)

    # Ensure the column names match those in your CSV
    updated_arduino_time, updated_arduino_force = (
        updated_data["Timestamp"],
        updated_data[f"Force{sensor_num}"],
    )

    # Setup Plot
    plt.figure(figsize=(10, 6))

    # Plotting updated Arduino data
    plt.plot(
        updated_arduino_time,
        updated_arduino_force,
        label="Updated Arduino Data",
        color="red",
    )

    # Plotting the Instron Data
    plt.plot(instron_time, instron_force, label="Instron Data", color="blue")

    # Ensure the lengths of the arrays are the same for difference calculation
    min_length = min(len(instron_force), len(updated_arduino_force))
    difference = np.array(instron_force[:min_length]) - np.array(
        updated_arduino_force[:min_length]
    )
    plt.plot(
        instron_time[:min_length],
        difference,
        label="Difference (Instron - Updated Arduino)",
        color="green",
        linestyle="--",
    )

    """
        difference = np.array(excel_force) - np.array(updated_arduino_force)
    plt.plot(excel_time, difference, label="Difference (Instron - Updated Arduino)", color="green",
             linestyle="--")
    """

    plt.xlabel("Time [s]")
    plt.ylabel("Force [N]")
    plt.legend()
    plt.title(
        f"Comparison of Force Data for Sensor Set {SENSOR_SET}, Sensor {sensor_num}, Test {TEST_NUM}"
    )
    plt.grid(True)

    plot_filename = f"{BASE_DIR}{PLOT_DIR}Sensor Set {SENSOR_SET}/{CALIBRATION_PREFIX}Test {TEST_NUM} Sensor {sensor_num} plot.png"
    plt.savefig(plot_filename, dpi=300)
    plt.show()
