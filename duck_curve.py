import csv
#accesses the csv file data (meaning the power grids data and from that we are going to calc total load and generation)
with open('mock_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
        
## PUT IN WILLS PROGRAM ##
def total_grid_power():
    return total_grid_power
###########################

##power managing functions##
def can_discharge(): # if the total load is greater than the total generation then the RTU can discharge to the grid
    for row in csvreader:
        time = row[0]
        if (time >= 64800) or (time < 30600):
            return True
        else:
            return False
        
def can_charge(): # if the total generation is greater than the total load then the RTU can charge from the grid
    for row in csvreader:
        time = row[0]
        if (32400 <= time <= 63000):
            return True
        else:
            return False

def can_sell_power():# during the hr 6pm to early morning power can be sold to the grid reads from the csv file
    end_flag = False
    for row in csvreader:
        megawatt = row[1]
        if(megawatt >= 22000):
            end_flag = True
    return end_flag

def idle():# this is during times 8:30am to 9am and 5:30pm to 6pm
    for row in csvreader:
        time = row[0]
        if (30600 <= time <= 32400) or (63000 <= time <= 64800):
            return True
        else:
            return False