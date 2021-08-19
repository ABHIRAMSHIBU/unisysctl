import os
class memory:
    def __init__(self):
        data=os.popen("whoami").read()
        if(data!="root"):
            self.root_error=True
        else:
            self.root_error=False
        self.memory_list=self.get_memory_info()
    def __repr__(self):   
        return str(self.memory_list)
    def get_memory_list(self,buffer_data):
        data=buffer_data.split("\n")[::-1]
        pure=[]
        purgeFlag=True
        while(len(data)!=0):
            line=data.pop()
            if("*-bank" in line and purgeFlag==False):
                pass
            elif("*-memory" in line):
                purgeFlag=False
            elif("*-" in line):
                purgeFlag=True
            if(purgeFlag==False):
                if(line.strip()!=""):
                    pure.append(line.strip())
        #print(pure)
        memories=[i.split(", ")[1:-1] for i in ", ".join(pure).strip().split("*-memory")[1:]]
        sm=[]
        for pure in memories:
            splitslot=[i.split(", ")[:-1] for i in ", ".join(pure).split("*-bank:")]
            if("description: System Memory" in splitslot[0]):
                sm.append(splitslot)
        return sm
    def get_memory_info(self):
        from subprocess import Popen,PIPE
        run_shell=Popen(["lshw","-c","memory"],stdout=PIPE,stderr=PIPE) # sudo needs user to input password
        out=run_shell.stdout.read()
        err=run_shell.stderr.read()
        del(run_shell)
        if out != b'':
            return self.get_memory_list(out.decode())
        elif err != b'':
            return self.get_memory_list(err.decode())
def get_objects():
    l=[]
    l.append(memory())
    return l
print(get_objects())