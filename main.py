import pickle as pkl
import dill, json, os
# import hashlib
import pickletools as pklt
from hashlib import *
import cryptography as cry
def encode(*input_data):
    output=b""
    output+=(input_data)[0]
    # code
    output += str(sha3_512(output)) + str(sha3_512(output))
    print(output)
    return output
def decode(input_data_serialized_vfid):
    output=b''
    input_data_serialized=input_data_serialized_vfid[:-128]
    hashes=[input_data_serialized_vfid[-128:-64],input_data_serialized_vfid[-64:]]
    if hashes[0] != str(sha3_512(input_data_serialized)) and 0:
        raise ValueError("Incorrect first hash")
    output+=input_data_serialized
    # code
    if hashes[1] != str(sha3_512(output)) and 0:
        raise ValueError("Incorrect second hash")
    return(output)
print(decode(encode(b'hi')))