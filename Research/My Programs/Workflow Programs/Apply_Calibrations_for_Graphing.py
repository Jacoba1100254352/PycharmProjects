import re
import pandas as pd
from File_Paths import *
from Raw_to_CSV import write_updated_data_to_csv

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


def apply_calibration_coefficients():
    # Read both initial and new coefficients
    new_coefficients = read_coefficients(
        f"{WORKING_DIR}{COEFFICIENTS_DIR}New Coefficients.txt"
    )

    # Calculate the new coefficients for each sensor
    for sensor_num in range(1, NUM_SENSORS + 1):
        # Parse the Arduino data
        aligned_data_filename = f"{WORKING_DIR}{ALIGNED_DATA_DIR}Aligned Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv"
        aligned_arduino_data = pd.read_csv(aligned_data_filename)

        # Get initial and new coefficients for the current sensor
        # m_new, c_new = new_coefficients[i - 1]

        if SIMPLIFY:
            # Apply the new calibration coefficients to the force readings
            aligned_arduino_data["Force [N]"] = round(
                new_coefficients[0][0] * aligned_arduino_data["ADC"]
                + new_coefficients[0][1],
                2,
            )
        else:
            # Apply the new calibration coefficients to the force readings
            for j in range(4):
                aligned_arduino_data[f"Force{j + 1} [N]"] = round(
                    new_coefficients[j][0] * aligned_arduino_data[f"ADC{j + 1}"]
                    + new_coefficients[j][1],
                    2,
                )

            # Update Total Force value (N)
            aligned_arduino_data["TotalForce1 [N]"] = sum(
                [aligned_arduino_data[f"Force{j + 1} [N]"] for j in range(4)]
            )

            # Set Total Force (kPa) to 0 for now
            aligned_arduino_data["TotalForce2 [N]"] = 0

        # Write the updated Arduino data to a new CSV file
        updated_csv_filename = f"{WORKING_DIR}{CALIBRATED_DIR}Updated Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv"
        write_updated_data_to_csv(updated_csv_filename, aligned_arduino_data)
