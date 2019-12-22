#!/usr/bin/env pypy3
import os
import math
class power:
    def read_data(self):
        standard_files=["type", "power_now", "capacity", "capacity_level" , "cycle_count",  
                        "voltage_now","energy_now", "energy_full_design","energy_full",
                        "model_name"]
        for i in standard_files:
            current_file=self.path+"/"+i
            if(os.path.exists(current_file)):
                f=open(current_file,"r")
                data=f.read().strip()
                f.close()
                self.battery_data[i]=data
            else:
                print("Warning no such file ",current_file)

    def __init__(self,path):
        self.battery_data={}
        self.path=""
        self.path=path
        self.read_data()
    def __repr__(self):
        returnData=""
        for i in self.battery_data:
            length=len(i)
            if(length<15):
                spacing="\t"*2
            if(length<10):
                spacing="\t"*2
            if(length<5):
                spacing="\t"*3
            returnData+=i+spacing+self.battery_data[i]+"\n"
        return returnData

power_supplies=os.listdir("/sys/class/power_supply")
def get_powersupplies():
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
                print("Detected Battery in ",actual_path)
                batteries.append(actual_path)
            elif(contents=="Mains"):
                mains.append(actual_path)
            else:
                others.append(actual_path)
    return batteries,mains,others
def get_objects():
    return_var={}
    return_var["batteries"]=get_battery_objects()
    return return_var
batteries,mains,others=get_powersupplies()
def get_battery_objects():
    battery_objects=[]
    for i in batteries:
        batt=power(i)
        battery_objects.append(batt)
    return battery_objects
print(get_objects())
