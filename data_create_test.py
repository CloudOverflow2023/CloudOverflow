"""
From chat gpt OpenFMB CSV example:

    Time,Grid_Voltage,Grid_Freq uency,Grid_Active_Power,Grid_Reactive_Pow er,Grid_Apparent_Power
    0,240.1,60.0,100.0,50.0,150.0
    1,240.2,60.2,110.0,60.0,170.0
    2,240.3,60.4,120.0,70.0,190.0
    3,240.4,60.6,130.0,80.0,210.0
    4,240.5,60.8,140.0,90.0,230.0
    5,240.6,61.0,150.0,100.0,250.0
    
        Time: 
            This is the timestamp of the data point.
        Grid_Voltage: 
            This is the voltage of the grid at the given time.
"""
      #           .----.
      #.---------. | == |
      #|.-"""""-.| |----|
      #||       || | == |
      #||       || |----|
      #|'-.....-'| |::::|
      #`"")---(""` |___.|
     #/:::::::::::\" _  "
    #/:::=======:::\`\`\
 #`"""""""""""""`  '-'
"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣤⣤⣤⣀⣀⠈⠋⠉⣁⣠⣤⣤⣤⣀⡀⠀⠀
⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀
⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀
⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀
⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀
⠀⠀⠀⠈⠙⢿⣿⣿⣿⠿⠟⠛⠻⠿⣿⣿⣿⡿⠋⠀⠀⠀
        Grid_Frequency: 
            This is the frequency of the grid at the given time.
        Grid_Active_Power: 
            This is the amount of active power flowing through the grid at the given time.
        Grid_Reactive_Power: 
            This is the amount of reactive power flowing through the grid at the given time.
        Grid_Apparent_Power: 
            This is the amount of apparent power flowing through the grid at the given time.


"""
import random
import time

clock = 0

def new_datapoint(time_stamp):
    Time = time_stamp
    """Grid_Voltage = None
    Grid_Frequency = None
    Grid_Active_Power = None
    Grid_Reactive_Power = None
    Grid_Apparent_Power = None"""
    
    Grid_Voltage = round(random.uniform(239, 241), 1)
    Grid_Frequency = round(random.uniform(59, 62), 1)
    Grid_Active_Power = round(random.uniform(90, 200), 1)
    Grid_Reactive_Power = round(random.uniform(40, 101), 1)
    Grid_Apparent_Power = round(random.uniform(100, 300), 1)
    
    return [Time,Grid_Voltage,Grid_Frequency,Grid_Active_Power,Grid_Reactive_Power,Grid_Apparent_Power]

while(True):
    data = new_datapoint(clock)
    clock += 1
    print(data)
    time.sleep(1)
    