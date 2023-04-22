import csv
#accesses the csv file data (meaning the power grids data and from that we are going to calc total load and generation)
with open('mock_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
        
## PUT IN WILLS PROGRAM ##
def total_grid_power():
    return total_grid_power
###########################

##power managing functions##
def can_discharge(): # during the times before 8:30am and after 6pm gigawatt can be discharged from the house to the grid
    for row in csvreader:
        time = row[0]
        if (time >= 64800) or (time < 30600):
            return True
        else:
            return False
        
def can_charge(): # From 9am to 5:30pm power can be charged from the grid to the house
    for row in csvreader:
        time = row[0]
        if (32400 <= time <= 63000):
            return True
        else:
            return False

def can_sell_power(): #During the hr 6pm to early morning power can be sold to the grid reads from the csv file
    end_flag = False
    for row in csvreader:
        megawatt = row[1] #this will get the power grids megawattage the 22000 is when we want a house to sell to the grid
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