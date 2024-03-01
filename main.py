import pickle as pkl
import dill, json, os
# import hashlib
import pickletools as pklt
from hashlib import *
import cryptography as cry
def encode(*input_data):
    output=b""
    # code
    output += sha3_512(output.encode()) + sha3_512(input_data.encode())
    return output
def decode(input_data_serialized_vfid):
    output=encode(b" ")
    input_data_serialized=input_data_serialized_vfid[:-128]
    hashes=[input_data_serialized_vfid[-128:-64],input_data_serialized_vfid[-64:]]
    if hashes[0] != sha3_512(input_data_serialized):
        raise ValueError("Incorrect first hash")
    # code
    if hashes[1] != sha3_512(output):
        raise ValueError("Incorrect second hash")
    return(output)
print(decode(b" "))