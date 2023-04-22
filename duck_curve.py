import csv
from HouseClass import House
#accesses the csv file data (meaning the power grids data and from that we are going to calc total load and generation)
with open('mock_data.csv', newline = '') as csvfile:
    csvreader = csv.reader(csvfile)
##power managing functions##
def can_discharge(): # during the times before 8:30am and after 6pm gigawatt can be discharged from the house to the grid
    with open('mock_data.csv', newline = '') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) > 0:
                min = row[0]
                #print(min)
            if (int(min) < 510):
                print
            if(int(min) >= 1080):
                return True
            else:
                return False
   
def can_charge(): # From 9am to 5:30pm power can be charged from the grid to the house
    with open('mock_data.csv', newline = '') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) > 0:
                min = row[0]
                if ((540) <= int(min) <= (1050)):
                    return True
                else:
                    return False

def can_sell_power(): #During the hr 6pm to early morning power can be sold to the grid reads from the csv file
    end_flag = False
    with open('mock_data.csv', newline = '') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) >= 1:
                megawatt = row[1] #this will get the power grids megawattage the 22000 is when we want a house to sell to the grid
                if((float(megawatt)) >= 22000):
                    end_flag = True
    return end_flag

def idle():# this is during times 8:30am to 9am and 5:30pm to 6pm
    with open('mock_data.csv', newline = '') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            time = row[0]
            if ((510) <= time <= (540)):
                return True
            if((1050) <= time <= (1080)):
                return True
            else:
                return False

#exHouse = House()
#if(exHouse.HomeOwnersLimit <= exHouse.CurrentChargeStatusPercentage):
    #if(can_discharge()):
        #print(can_sell_power())
randHouse = House()
randHouse.HouseDataShuffle()
print(randHouse.HomeOwnersLimit)
print(randHouse.CurrentChargeStatusPercentage)
can_discharge()
can_charge()
if(randHouse.HomeOwnersLimit <= randHouse.CurrentChargeStatusPercentage):
    if((can_discharge())):
        print(can_sell_power())
