from pathlib import Path 
from integrity import checksum #Hashing and checking Module

#Temp Test Code - Hashing
usr_inp = Path(input("File/Folder >>> "))
print(checksum.calculate_hash(usr_inp))

# Temp Test Code - Check Hash
# print(checksum.check_hash(usr_inp,"")) # here input the hash of the file in quotes to check it