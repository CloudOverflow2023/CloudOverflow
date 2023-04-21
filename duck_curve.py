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

##RTU stuff
def net_load(): # works with RTU files potentional generation to help balance the total load
    return net_load 
def net_generation():# works with RTU files potentional load to help balance the total generation
    return net_generation
def idle():# if total generation adn load and equal then nothing will happen with the RTUs
    if(net_load == net_generation):
        return 0
def generation_of_power():
    return generation_of_power
    