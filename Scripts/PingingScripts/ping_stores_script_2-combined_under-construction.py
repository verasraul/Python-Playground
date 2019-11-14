import subprocess



ips = {'Corporate' : '10.10.1.1', 'Madison': '10.10.21.1',
           'Costa Mesa': '10.10.23.1', 'Melrose': '10.10.24.1',
           'Bal Harbor': '10.10.27.1', 'Elmhurst': '10.10.28.1'}

def ping_stores():
    for name, value in ips.items():
        #process = subprocess.call(['ping', '-n', '5', values])
        process = subprocess.call(['ping', '-n', '5', value], stdout=subprocess.PIPE)
        if process == 0:
            print ("ping to", name, "OK")
        elif process == 2:
            print ("no response from", name)
        else:
            print ("ping to", name, "failed!")


ping_stores()

        
