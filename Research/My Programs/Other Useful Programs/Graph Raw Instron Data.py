import pandas as pd
import matplotlib.pyplot as plt

# Define Global constants
SENSOR_SET = 1
NUM_SENSORS = 4
TEST_NUM = 1
BASE_DIR = "/Users/jacobanderson/Library/CloudStorage/Box-Box/Nanogroup/Projects/Bioimpedance/Pressure Controller/Jacob's Tests/"

UNCALIBRATED_DIR = f"Calibration Tests/Arduino Data/Sensor Set {SENSOR_SET}/"
EXCEL_DIR = "Calibration Tests/Raw Test Data (Excel)/"
CALIBRATION_PREFIX = "Calibration "

# Running the analysis with interpolation and plotting the results
for sensorNum in range(1, NUM_SENSORS + 1):
    # Load and interpolate Arduino data
    uncalibrated_filename = f"{BASE_DIR}{UNCALIBRATED_DIR}{CALIBRATION_PREFIX}Test {TEST_NUM} Sensor {sensorNum}.txt"
    # Define indexing constant aid
    INDEX_DIFFERENCE = 3

    # Open and read file data
    excel_filename = (
        f"{EXCEL_DIR}Sensor Set {SENSOR_SET}/{CALIBRATION_PREFIX}Test {TEST_NUM}.xlsx"
    )
    excel_data = pd.read_excel(
        BASE_DIR + excel_filename, sheet_name=f"Sensor {sensorNum}"
    )
    excel_time = excel_data["Time [s]"].values
    excel_force = [abs(value) for value in excel_data["Force [N]"].values]

    # Plotting
    plt.figure(figsize=(10, 6))

    plt.plot(
        excel_time,
        excel_force,
        label="Interpolated Uncalibrated Arduino Data",
        color="orange",
    )

    # Finalize plot
    plt.xlabel("Time [s]")
    plt.ylabel("Force [N]")
    plt.legend()
    plt.title(
        f"Comparison of Force Data for Sensor Set {SENSOR_SET}, Sensor {sensorNum}, Test {TEST_NUM}"
    )
    plt.grid(True)
    plt.show()
