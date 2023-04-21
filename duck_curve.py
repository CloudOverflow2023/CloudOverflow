import csv
#accesses the csv file data (meaning the power grids data and from that we are going to calc total load and generation)
with open('mock_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print (row)
## PUT IN WILLS PROGRAM ##
def total_grid_load():
    return total
def total_grid_gen():
    return total
###########################

##power managing functions##
def can_discharge(): # if the total load is greater than the total generation then the RTU can discharge to the grid
    return can_discharge
def can_charge(): # if the total generation is greater than the total load then the RTU can charge from the grid
    return can_charge

def can_sell_power():# during the hr 6pm to early morning power can be sold to the grid
    return can_sell_power


def idle():# if total generation adn load and equal then nothing will happen with the RTUs
    if(total_grid_load() == total_grid_gen()):
        return 0
def generation_of_power():
    return generation_of_power
    