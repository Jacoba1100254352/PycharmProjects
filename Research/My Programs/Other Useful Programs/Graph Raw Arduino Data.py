import matplotlib.pyplot as plt

# Define Global constants
SENSOR_SET = 1
NUM_SENSORS = 4
TEST_NUM = 1
BASE_DIR = "/Users/jacobanderson/Library/CloudStorage/Box-Box/Nanogroup/Projects/Bioimpedance/Pressure Controller/Jacob's Tests/"

# Running the analysis with interpolation and plotting the results
for sensorNum in range(1, NUM_SENSORS + 1):
    # Load and interpolate Arduino data
    uncalibrated_filename = f"{BASE_DIR}Calibration Tests/Arduino Data/Sensor Set {SENSOR_SET}/Calibration Test {TEST_NUM} Sensor {sensorNum}.txt"
    # Define indexing constant aid
    INDEX_DIFFERENCE = 3

    # Open and read file data
    with open(uncalibrated_filename, "r") as file:
        lines = file.readlines()
    arduino_time = [(i + 1) * 20 for i, line in enumerate(lines)]
    arduino_force = [float(line.split(",")[sensorNum].strip()) for line in lines]

    # Plotting
    plt.figure(figsize=(10, 6))

    plt.plot(
        arduino_time,
        arduino_force,
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
