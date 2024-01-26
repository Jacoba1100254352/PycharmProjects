import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from File_Paths import *


# Running the plotting for each sensor
def graph_sensor_data():
    for sensor_num in range(1, NUM_SENSORS + 1):
        # Load the Excel data
        instron_data = pd.read_csv(
            f"{WORKING_DIR}{INSTRON_DIR}Parsed Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv",
        )
        instron_time = instron_data["Time [s]"].values
        instron_force = abs(instron_data["Force [N]"].values)

        # Load updated Arduino data
        updated_arduino_data_filename = f"{WORKING_DIR}{CALIBRATED_DIR}Updated Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv"
        updated_arduino_data = pd.read_csv(updated_arduino_data_filename)

        # Ensure the column names match those in your CSV
        updated_arduino_time, updated_arduino_force = (
            updated_arduino_data["Time [s]"],
            updated_arduino_data["Force [N]" if SIMPLIFY else f"Force{sensor_num} [N]"],
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

        plot_filename = f"{WORKING_DIR}{PLOT_DIR}Calibration Test {TEST_NUM} Sensor {sensor_num} plot.png"
        plt.savefig(plot_filename, dpi=300)
        plt.show()
