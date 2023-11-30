import serial
import time
from datetime import datetime

# Set up the serial line
port = 'COM5'
ser = serial.Serial(port, 115200)
ser.flushInput()

# Function to create a new file with a timestamp in the name
def create_new_file():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_")
    filename = f'serial_data_{timestamp}.txt'
    return open(filename, 'w')

# Initialize variables
line_count = 0
file = create_new_file()

while True:
    try:
        # Read a line from the serial port
        ser_bytes = ser.readline()

        # Decode bytes to string
        decoded_bytes = ser_bytes.decode('utf-8').rstrip()

        # Write to the file
        file.write(decoded_bytes + '\n')
        file.flush()  # Ensure data is written to the file
        line_count += 1

        # Optional: print to console
        # print(decoded_bytes)
        
        # Check if line count has reached a million
        if line_count >= 1000000:
            file.close()  # Close the current file
            file = create_new_file()  # Open a new file with a new timestamp
            line_count = 0  # Reset line count

    except KeyboardInterrupt:
        print("Keyboard Interrupt: Exiting...")
        break
    except Exception as e:
        print("Error:", e)
        break

# Close the current file and the serial connection
file.close()
ser.close()
