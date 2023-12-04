import serial.tools.list_ports
import time
from datetime import datetime
import struct

# Set up the serial line
port = '/dev/ttyACM0'
ser = serial.Serial(port, 115200)
ser.flushInput()

# Function to create a new file with a timestamp in the name
def create_new_file():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_")
    filename = f'serial_data_{timestamp}.txt'
    return open(filename, 'wb')  # Open in binary write mode

# Initialize variables
file = create_new_file()
line_count = 0
byte_count = 0
while True:
    try:
        ser_bytes = ser.read(4)

        if len(ser_bytes) == 4:
            value = struct.unpack('<I', ser_bytes)[0]
            print(f"{value},", end='')

        byte_count += 1
        if byte_count == 4:
            print()  
            byte_count = 0  


            file.write(ser_bytes)
            file.flush()
            line_count += 1

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
