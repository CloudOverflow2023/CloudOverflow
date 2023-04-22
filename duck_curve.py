import csv
#accesses the csv file data (meaning the power grids data and from that we are going to calc total load and generation)
with open('mock_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
        
## PUT IN WILLS PROGRAM ##
def total_grid_power():
    return total_grid_power
###########################

def can_sell_power():# during the hr 6pm to early morning power can be sold to the grid
    end_flag = False
    for row in csvreader:
        megawatt = row[1]
        if(megawatt >= 22000):
            end_flag = True
    return can_sell_power

def idle():# this is during times 8:30am to 9am and 5:30pm to 6pm
    return idle