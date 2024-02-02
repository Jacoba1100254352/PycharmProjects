import os
import serial

# Modify the port and baud rate as per your setup
PORT = "/dev/cu.usbserial-1420"  # On Windows, this is usually "COMX" where X is a number. On Mac/Linux, it might be "/dev/ttyUSB0" or similar.
BAUD_RATE = 38400
SENSOR_NUM = 2
TEST_NUM = 2
WORKING_DIR = "/Users/jacobanderson/Library/CloudStorage/Box-Box/Nanogroup/Projects/Bioimpedance/Pressure Controller/Jacob's Tests/Arduino Data/"
OUTPUT_FILE = WORKING_DIR + f"Sensor{SENSOR_NUM} Test {TEST_NUM}.txt"


def main():
    # Open the serial port
    with serial.Serial(PORT, BAUD_RATE, timeout=1) as ser:
        print(f"Connected to {PORT} at {BAUD_RATE} baud rate.")

        # Ensure the directory exists
        directory = os.path.dirname(OUTPUT_FILE)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Wait for the user to press the 'r' key
        while True:
            key = input("Press 'r' to start reading data...")
            if key.lower() == 'r':
                break

        # Open the output file in append mode
        with open(OUTPUT_FILE, 'a') as file:
            try:
                while True:
                    # Read a line from the serial port
                    line = ser.readline().decode("utf-8").strip()

                    # If the line is not empty, print and save it
                    if line:
                        print(line)
                        file.write(line + "\n")

            except KeyboardInterrupt:
                print("Exiting...")


if __name__ == "__main__":
    main()
