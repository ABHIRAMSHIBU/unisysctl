#!/usr/bin/env pypy3
import os
class battery:
    battery_data={}
    path=""
    def read_data(self):
        standard_files=["type", "power_now", "capacity", "cycle_count", "voltage_now",
                        "energy_now", "energy_full_design","energy_full"]
        for i in standard_files:
            current_file=self.path+"/"+i
            if(os.path.exists(current_file)):
                f=open(current_file,"r")
                data=f.read().strip()
                f.close()
                self.battery_data[i]=data
            else:
                print("Error no such file ",current_file)

    def __init__(self,path):
        self.path=path
        self.read_data()
    def __repr__(self):
        return str(self.battery_data)


power_supplies=os.listdir("/sys/class/power_supply")
def get_batteries():
    batteries=[]
    mains=[]
    others=[]
    for i in power_supplies:
        type_path="/sys/class/power_supply"+"/"+i+"/type"
        actual_path="/sys/class/power_supply"+"/"+i
        if(os.path.exists(type_path)):
            f = open(type_path)
            contents=f.read().strip()
            f.close()
            if(contents=="Battery"):
                batteries.append(actual_path)
            elif(contents=="Mains"):
                mains.append(actual_path)
            else:
                others.append(actual_path)
    return batteries,mains,others
batteries,mains,others=get_batteries()
def get_battery_objects():
    battery_objects=[]
    for i in batteries:
        batt=battery(i)
        battery_objects.append(batt)
    return battery_objects
print(get_battery_objects())