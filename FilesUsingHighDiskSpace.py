import os

getcurrworking  = os.getcwd()

print(getcurrworking)

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

for root , dirs , files in os.walk("."):
        for filename in files:
            status = os.stat(filename)
            print(filename , convert_bytes(status.st_size))
            #print(status)
