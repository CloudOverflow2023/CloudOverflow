class RTU:
    def __init__(self):
        #Can equal "idle", "power", Or "charge"
        self.status = "idle"
        self.macaddress = "00-00-00-00-00-00"
        #We are using "Power" as a umbrella term for currency
        self.power = 0




def main():

    TeslaModel3 = RTU()

    print(TeslaModel3.status)
    print(TeslaModel3.macaddress)

    print(TeslaModel3.power)

if __name__ == "__main__":
    main()