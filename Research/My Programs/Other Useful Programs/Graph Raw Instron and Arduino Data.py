import matplotlib.pyplot as plt
import pandas as pd

# Define Global constants
SENSOR_SET = 1
NUM_SENSORS = 4
TEST_NUM = 2
BASE_DIR = "/Users/jacobanderson/Library/CloudStorage/Box-Box/Nanogroup/Projects/Bioimpedance/Pressure Controller/Jacob's Tests/"

# Running the analysis and plotting the results
for sensorNum in range(1, NUM_SENSORS + 1):
    # Arduino Data
    arduino_filename = f"{BASE_DIR}Calibration Tests/Arduino Data/Sensor Set {SENSOR_SET}/Calibration Test {TEST_NUM} Sensor {sensorNum}.txt"

    # Read Arduino data
    with open(arduino_filename, "r") as file:
        lines = file.readlines()
    arduino_time = [
        (i + 1) * 20 for i, line in enumerate(lines)
    ]  # Assuming 20s is the correct interval
    arduino_force = [
        float(line.split(",")[sensorNum].strip()) for line in lines
    ]  # Adjust index as needed

    # Instron Data
    excel_filename = f"{BASE_DIR}Calibration Tests/Raw Test Data (Excel)/Sensor Set {SENSOR_SET}/Calibration Test {TEST_NUM}.xlsx"
    excel_data = pd.read_excel(excel_filename, sheet_name=f"Sensor {sensorNum}")
    excel_time = (
            excel_data["Time [s]"].values * 1000
    )  # Scaling time by 1000 as per your code
    excel_force = [abs(value) for value in excel_data["Force [N]"].values]

    # Plotting
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot Arduino data with ax1 as the primary axis
    ax1.plot(
        arduino_time, arduino_force, label=f"Arduino Sensor {sensorNum}", color="orange"
    )
    ax1.set_xlabel(
        "Time [ms]" if excel_time[-1] > arduino_time[-1] else "Time [s]"
    )  # Choose appropriate label
    ax1.set_ylabel("Arduino Force [N]", color="orange")
    ax1.tick_params(axis="y", labelcolor="orange")

    # Create a second y-axis for the Instron data
    ax2 = ax1.twinx()
    ax2.plot(excel_time, excel_force, label=f"Instron Sensor {sensorNum}", color="blue")
    ax2.set_ylabel("Instron Force [N]", color="blue")
    ax2.tick_params(axis="y", labelcolor="blue")

    # Finalize plot
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc=0)

    plt.title(
        f"Overlay of Force Data for Sensor Set {SENSOR_SET}, Sensor {sensorNum}, Test {TEST_NUM}"
    )
    plt.grid(True)
    plt.show()
