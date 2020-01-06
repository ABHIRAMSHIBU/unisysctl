def get_mem_data():
    f = open("/proc/meminfo")
    data = f.read().strip()
    data = data.split("\n")
    return capture_meminfo_list(data)   
class meminfo:
    def __init__(self,info):
        self.mem_data={}
        for line in info:
            self.attribute,self.value=line.strip().split(':')
            self.mem_data[self.attribute]=self.value.strip(" ")
    def __repr__(self):
        return str(self.mem_data)
def capture_meminfo_list(memlist):
    list=meminfo(memlist)
    return list
print(get_mem_data())