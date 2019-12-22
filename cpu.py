#!/usr/bin/env pypy3
import os
import math
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
class cpu:
    def __init__(self,cpuattrlist):
        self.cpu_data={}
        self.process_cpuattrlist(cpuattrlist)
        self.processor=int(self.cpu_data["processor"])
        self.model_name=self.cpu_data["model name"]
        self.cores=int(self.cpu_data["cpu cores"])
        self.threads=int(self.cpu_data["siblings"])
        self.ht=False
        if(self.threads==2*self.cores):
            self.ht=True
    def process_cpuattrlist(self,cpuattrlist):
        for i in cpuattrlist:
            z=[i.strip() for i in i.split(":")]
            self.cpu_data[z[0]]=z[1]
            
    def __repr__(self):
        return_string="ID\t\t"+str(self.processor)+"\n"
        return_string+="MODEL\t\t"+self.model_name+"\n"
        return_string+="CORES\t\t"+str(self.cores)+"\n"
        return_string+="THREADS\t\t"+str(self.threads)+"\n"
        return_string+="HYPERTHREADED\t"+str(self.ht)+"\n"
        return return_string
        
def process_cpustringlist(cpulist):
    cpu_objects=[];
    for i in cpulist:
        currentcpu=i.split("\n")
        c=cpu(currentcpu)
        cpu_objects.append(c)
    return cpu_objects;
def get_objects():
    return cpu_identify()
def cpu_identify():
    cpuinfo="/proc/cpuinfo"
    f = open(cpuinfo,"r")
    data=f.read().strip()
    data=data.split("\n\n")
    return process_cpustringlist(data)
print(get_objects())
