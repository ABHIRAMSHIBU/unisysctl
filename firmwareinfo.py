def abstrct(buffer_data):
    for line in buffer_data:
        if line.startswith("*-cache:0"):
            break
        elif line.startswith("*-firmware:0"):
            continue
        else:
            print(line)
            index,value=line.strip().split(":")
            data[index]=value.strip(" ")
def throwbck(info):
    information=abstrct(str(info))
    return information
def get_hw_info():
    from subprocess import Popen,PIPE
    run_shell=Popen(["sudo","lshw","-c","memory"],stdout=PIPE,stderr=PIPE)
    out=str(run_shell.stdout.read())
    err=str(run_shell.stderr.read())
    if out is not None:
        return throwbck(out)
    elif err is not None:
        return throwbck(err)
get_hw_info()
data={}
index=""
value=""
data=get_hw_info()
#print(data)