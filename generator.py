from config import *

def generate(var1):
    if var1 == "FLI":
        f = open(f"{var1}.txt", "w+")
        supplierIDTemp = supplierID[0]
        recordTypeTemp = str(recordType[0]).zfill(10)

        f.write(f"{supplierIDTemp}{recordTypeTemp}{var1}")


    f.close()
