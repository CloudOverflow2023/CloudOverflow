#Mannaged by Calvin Schmeichel
"""
                 ⣀⣀⠀⠀⠀⠀⠀⠀
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


        Time:
            This is the timestamp of the data point.
        Grid_Voltage: 
            This is the voltage of the grid at the given time.
        Grid_Frequency:
            This is the frequency of the grid at the given time.
        Grid_Active_Power:
            This is the amount of active power flowing through the grid at the given time.
        Grid_Reactive_Power:
            This is the amount of reactive power flowing through the grid at the given time.
        Grid_Apparent_Power:
            This is the amount of apparent power flowing through the grid at the given time.

            
            
            Measure load in megawatts y axis
            time x axis

            Cash incentive to increase RTU's per house for more data

            custom smart house outlets to handle reachargables (Rechargables Plug)

            virtual houses (aka batterys == "idle", "power", Or "charge" )


class RTU:
    def __init__(self):
        #Can equal "idle", "power", Or "charge"
        self.status = "idle"
        self.macaddress = "00-00-00-00-00-00"
        #We are using "Power" as a umbrella term for currency
        self.power = 0


    def CalculatePotentialPowerOutput(self):

        #Insert Generation formula here
        
        return



def main():
    import csv

    with open('calvinstestdata.csv', 'r') as read_obj:

        csv_reader = csv.reader(read_obj)
        list_of_csv = list(csv_reader)

    print(list_of_csv)

    print(list_of_csv[15][1])

    TeslaModel3 = RTU()

    print(TeslaModel3.status)
    print(TeslaModel3.macaddress)

    print(TeslaModel3.power)


"""

import random
class House:
    def __init__(self):
        #0.58677
        self.TotalChargePotential = 0.58677
        self.CurrentChargeStatus = 0.3293
        self.CurrentChargeStatusPercentage = int(round(((self.CurrentChargeStatus)/(self.TotalChargePotential))*100, 0))

        #from ~20 - ~80
        self.HomeOwnersLimit = 20

    def HouseDataShuffle(self):
        print("This is from the class")
        self.TotalChargePotential = round((random.uniform(0.5, 0.58677)),5)
        self.CurrentChargeStatus = round((random.uniform(0, self.TotalChargePotential)),5)
        self.CurrentChargeStatusPercentage = int(round(((self.CurrentChargeStatus)/(self.TotalChargePotential))*100, 0))

    

def main():

    print(round((random.uniform(0.5, 0.58677)),5))

    

    print("Hello")
    WhiteHouse = House()

    print(WhiteHouse.TotalChargePotential)
    print(WhiteHouse.CurrentChargeStatus)
    print(WhiteHouse.CurrentChargeStatusPercentage)

    WhiteHouse.HouseDataShuffle()

    print(WhiteHouse.TotalChargePotential)
    print(WhiteHouse.CurrentChargeStatus)
    print(WhiteHouse.CurrentChargeStatusPercentage)



#This is so we can import the functions in this program in other code without having to run the main function
if __name__ == "__main__":
    main()





