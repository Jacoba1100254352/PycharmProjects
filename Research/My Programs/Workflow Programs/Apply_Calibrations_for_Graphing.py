import re
import pandas as pd

# Define Global constants
SENSOR_SET = 1
NUM_SENSORS = 4
TEST_NUM = 2
WORKING_DIR = "/Users/jacobanderson/Library/CloudStorage/Box-Box/Nanogroup/Projects/Bioimpedance/Pressure Controller/Jacob's Tests/Calibration Tests/"


# Read m_initial and c_initial from a file
def read_coefficients(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            # Adjust the regular expression to match numbers in scientific notation as well
            pairs = re.findall(
                r"\{\s*([-\d.]+(?:e[-+]?\d+)?)\s*,\s*([-\d.]+(?:e[-+]?\d+)?)\s*}",
                content,
            )
            # Convert each pair of strings to a tuple of floats
            data = [(float(m), float(c)) for m, c in pairs]
            return data
    except FileNotFoundError:
        print(f"Warning: The file {filename} does not exist!")
        raise
    except ValueError as e:
        print(e)
        raise


# Write the updated Arduino data to a new file
def write_updated_data_to_csv(filename, data):
    # Convert data into a DataFrame
    df = pd.DataFrame(
        data,
        columns=[
            "Timestamp",
            "ADC1",
            "ADC2",
            "ADC3",
            "ADC4",
            "Force1",
            "Force2",
            "Force3",
            "Force4",
            "TotalForce1",
            "TotalForce2",
        ],
    )
    df.to_csv(filename, index=False)
    print(f"Updated data saved to {filename}")


def apply_calibration_coefficients():
    # Read both initial and new coefficients
    new_coefficients = read_coefficients(
        f"{WORKING_DIR}Coefficients/Sensor Set {SENSOR_SET}/New Coefficients.txt"
    )

    for sensor_num in range(1, NUM_SENSORS + 1):
        # Parse the Arduino data
        aligned_data_filename = f"{WORKING_DIR}Aligned Arduino Data/Sensor Set {SENSOR_SET}/Aligned Test {TEST_NUM} Sensor {sensor_num}.csv"
        aligned_arduino_data = pd.read_csv(aligned_data_filename)

        # Get initial and new coefficients for the current sensor
        # m_new, c_new = new_coefficients[i - 1]

        # Apply the new calibration coefficients to the force readings
        for j in range(4):
            aligned_arduino_data[f"Force{j + 1}"] = round(
                new_coefficients[j][0] * aligned_arduino_data[f"ADC{j + 1}"]
                + new_coefficients[j][1],
                2,
            )

        # Update Total Force value (N)
        aligned_arduino_data["TotalForce1"] = sum(
            [aligned_arduino_data[f"Force{j + 1}"] for j in range(4)]
        )

        # Set Total Force (kPa) to 0 for now
        aligned_arduino_data["TotalForce2"] = 0

        # Write the updated Arduino data to a new CSV file
        updated_csv_filename = f"{WORKING_DIR}Updated Arduino Data/Sensor Set {SENSOR_SET}/Updated Calibration Test {TEST_NUM} Sensor {sensor_num}.csv"
        write_updated_data_to_csv(updated_csv_filename, aligned_arduino_data)
