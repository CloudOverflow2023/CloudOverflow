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
import csv
import datetime

filename = 'mock_data.csv'
fields = ['Time','MW_MegaWatts']
 
def create_list_from_csv(filename):
    chat_context_list = []
    # read csv file and save to a list that can readily be used by python
    with open(filename) as fh:
        rd = csv.DictReader(fh, delimiter=',')
        for row in rd:
            chat_context_list.append(row)
    return chat_context_list

def write_to_csv(a_list, filename):
    chat_context_list = create_list_from_csv(filename)
    # writing changed list of dictionaries to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        # writing headers (field names)
        writer.writeheader()
        # writing data rows
        writer.writerows(a_list)
    #return true false depending if was able to write to file or not, could also just not return anything if feeling like being lazy



while True:
    now = datetime.datetime.now()
    Time = str(now.strftime('%X')) 
    chat_context_list = create_list_from_csv(filename)
    MW_MegaWatts = round(random.uniform(239, 241), 1)
    chat_context_list.append({'Time':Time, 'MW_MegaWatts':MW_MegaWatts})
    write_to_csv(chat_context_list, filename)
    time.sleep(1)
    