import os
import sys
import hashlib
lib_path = os.path.abspath('..')
sys.path.append(lib_path)
sys.path.append('~/cloud_convert')


import CloudConvert

apikey = open("apikey.txt", "r").read().strip()

print apikey
process = CloudConvert.ConversionProcess(apikey)

print("possible?", CloudConvert.CloudConvert.is_possible("jpg", "png"))

process.init("i1.jpg", "o1.png")

print("from", process.fromformat)
print("to", process.toformat)

print("start")
process.start()

print("waiting")
process.wait_for_completion()

print("Saving")
process.save()

with open(process.fromfile, "rb") as f:
    a = hashlib.md5(f.read()).hexdigest()

with open(process.tofile, "rb") as f:
    b = hashlib.md5(f.read()).hexdigest()

print("Same file?", a == b)
