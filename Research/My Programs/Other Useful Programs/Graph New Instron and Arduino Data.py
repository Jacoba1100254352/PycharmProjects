import matplotlib.pyplot as plt
import pandas as pd

# Define Global constants
SENSOR_SET = 1
NUM_SENSORS = 4
TEST_NUM = 2
BASE_DIR = "/Users/jacobanderson/Library/CloudStorage/Box-Box/Nanogroup/Projects/Bioimpedance/Pressure Controller/Jacob's Tests/"
PLOT_DIR = "Calibration Tests/Data Plots/"

# Running the analysis and plotting the results
for sensorNum in range(1, NUM_SENSORS + 1):
    # Arduino Data
    arduino_filename = f"{BASE_DIR}Calibration Tests/Updated Arduino Data/Sensor Set {SENSOR_SET}/Updated Calibration Test {TEST_NUM} Sensor {sensorNum}.txt"

    # Read Arduino data
    with open(arduino_filename, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if i >= 1:
            time = float(line.split(",")[0].strip())
            if time - float(lines[i - 1].split(",")[0].strip()) > 20:
                print("Times jump")
                print(lines[i - 1])
                print(lines[i])
                if i != len(lines) - 1:
                    print(lines[i + 1])
                exit(1)

    arduino_time = [(i + 1) * 20 for i, line in enumerate(lines)]
    arduino_force = [float(line.split(",")[sensorNum + 4].strip()) for line in lines]

    # Instron Data
    excel_filename = f"{BASE_DIR}Calibration Tests/Raw Test Data (Excel)/Sensor Set {SENSOR_SET}/Calibration Test {TEST_NUM}.xlsx"
    excel_data = pd.read_excel(excel_filename, sheet_name=f"Sensor {sensorNum}")
    excel_time = excel_data["Time [s]"].values * 1000
    excel_force = [abs(value) for value in excel_data["Force [N]"].values]

    # Plotting
    plt.figure(figsize=(10, 6))

    # Plot Arduino data
    plt.plot(
        arduino_time, arduino_force, label=f"Arduino Sensor {sensorNum}", color="orange"
    )

    # Plot Instron data
    plt.plot(excel_time, excel_force, label=f"Instron Sensor {sensorNum}", color="blue")

    # Finalize plot
    plt.xlabel("Time [s]")
    plt.ylabel("Force [N]")
    plt.legend()
    plt.title(
        f"Overlay of Force Data for Sensor Set {SENSOR_SET}, Sensor {sensorNum}, Test {TEST_NUM}"
    )
    plt.grid(True)

    plt.savefig(
        BASE_DIR
        + f"{PLOT_DIR}Sensor Set {SENSOR_SET}/Calibration Test {TEST_NUM} Sensor {sensorNum} plot.png",
        dpi=300,
    )
    plt.show()
