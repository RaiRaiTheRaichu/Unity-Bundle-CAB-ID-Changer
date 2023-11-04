import os
import sys
import hashlib
import argparse

for arg in sys.argv:
    
    #Skip first arg - it's always the script itself.
    if arg == sys.argv[0]:
        continue

    if not arg.endswith(".bundle"):
        raise argparse.ArgumentTypeError(f"File {arg} must be a valid Unity bundle.")
    
    #The whole file needs to be parsed first to generate an MD5 hash.
    with open(arg, "rb") as file:
        file_hash = hashlib.md5()
        chunk = file.read(8196)
        while chunk := file.read(8196):
            file_hash.update(chunk)
        newHash = file_hash.hexdigest()
        file.close()                    
    
    #Create a backup.
    os.rename(arg, arg + ".old")
        
    #Print out a modified bundle, with the swapped CAB-IDs.
    with open(arg + ".old", "rb") as file:
        print(f"Changing CAB-ID of {arg}")
        
        output = open(arg, "ab")
        
        chunk = file.read(8196)
        indexOfHash = chunk.find(b"CAB")
        if indexOfHash == -1:
            file.close()
            output.close()
            os.remove(arg)
            os.rename(arg + ".old", arg)
            raise Exception("Unable to find CAB-ID in bundle header. Bundle may be invalid or corrupt.")
        
        oldHash = chunk[indexOfHash+4:indexOfHash+36]
        print(f"Old CAB-ID is {str(oldHash.decode())}\nReplacing with: {newHash}")
        
        chunk = chunk.replace(oldHash, bytes(newHash, 'utf-8'))
        
        output.write(chunk)
        while chunk := file.read(8196):
            chunk = chunk.replace(oldHash, bytes(newHash, 'utf-8'))
            output.write(chunk)
        
        file.close()
        output.close()

print("Operation complete, press \"ENTER\" to close.")
input()