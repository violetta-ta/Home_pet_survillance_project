#!/usr/bin/env python3
import serial
import time
if __name__ == '__main__':
    ser = serial.Serial('/dev/serial0', 115200, timeout=1)
    ser.flush()
    wheel_register = [0]
    speeds = [0]
    counts = 0
    time_t = 0
    f_wheel  = open("log_wheel_rotations.txt", "a")
    f_speeds = open("log_speeds.txt", "a")
    f_ammonia = open("ammonia.txt", "a")
    f_water = open("water.txt", "a")

    while True:
        
        if ser.in_waiting > 0:
            cur_time = time.time()
            print("have data")
            line = ser.readline().decode('latin-1').rstrip()
            print(line)
            if line.startswith("Sensor_1"):
                wheel_register.append(cur_time)
                f_wheel.write(str(cur_time) + "\n")
                print("1", wheel_register[-1])
                print("2", wheel_register[-2])
                if wheel_register[-1] - wheel_register[-2] < 1:
                    counts = counts + 1
                    time_t = time_t + wheel_register[-1] - wheel_register[-2]
                    print("no")
                else:
                    if time_t>0:
                        print("speed")
                        speed = counts * 53.38 / time_t
                        speeds.append(speed)
                        f_speeds.write(str(cur_time) + " " + str(speed) + "\n")
                        counts = 0
                        time_t = 0
                        
            #print(wheel_register)
            #print(speeds)
            elif (line.startswith("Sensor_2")):
                print(line)
                values = line.split()
                f_water.write(str(cur_time) + " " + str(values[-1]) + "\n")
            elif (line.startswith("Sensor_3")):
                print(line)
                values = line.split()
                f_ammonia.write(str(cur_time) + " " + str(values[-1]) + "\n")
            print(wheel_register)
            print(speeds)
#         counts = 0
#         time_t = 0
        #speeds = []
#         for i in range(len(wheel_register) - 1):
#             #current = wheel_register(i)
#             if wheel_register[i+1] - wheel_register[i] > 1.5:
#                 counts = counts + 1
#                 time_t = time_t + wheel_register[i+1] - wheel_register[i]
#             elif time_t == 0:
#                 continue
#             else:
#                 speed = counts * 10 / time_t
#                 speeds.append(speed)
#                 count = 0
#                 time_t = 0
#                 speed = 0
#             print(speeds)

    f_wheel.close()
    f_speeds.close()
    f_ammonia.close()
    f_water.close()