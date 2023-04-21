import csv
#accesses the csv file data (meaning the power grids data and from that we are going to calc total load and generation)
with open('mock_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print (row)
        
def total_grid_load():
    return total
def total_grid_gen():
    return total

##RTU stuff
def load_offsetting(): # works with RTU files potentional generation to help balance the total load
    return total_load 
def generation_offsetting():# works with RTU files potentional load to help balance the total generation
    return total_generation
def idle():# if total generation adn load and equal then nothing will happen with the RTUs
    if(total_load == total_generation):
        return 0

def generation_of_power():
    return generation_of_power
    