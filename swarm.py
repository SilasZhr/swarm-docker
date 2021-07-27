import os
import json
import codecs

from eth_utils import encode_hex

from eth_keyfile.keyfile  import decode_keyfile_json

path = "/root/bee"
files= os.listdir(path)

s = []
for file in files: 
     if not os.path.isdir(file):
          if file.startswith("16"):
              file_list = os.listdir(path+"/"+file)
              for i in file_list:
                  keystore = os.listdir(path+"/"+file+"/"+i+"/keystore")[0]
                  password = open((path+"/"+file+"/"+i+"/password")).readlines()[0]
                  password = codecs.encode(password, 'utf8')
                  keyfile_json = json.load(open(path+"/"+file+"/"+i+"/keystore/"+keystore))
                  derived_private_key = decode_keyfile_json(keyfile_json, password)
                  derived_private_key = encode_hex(derived_private_key)
                  print(derived_private_key)
          if file.startswith("66"):
              file_list = os.listdir(path+"/"+file)
              for i in file_list:
                  print(i)
                  keystore = os.listdir(path+"/"+file+"/"+i+"/_data/keystore")[0]
                  password = open((path+"/"+file+"/"+i+"/_data/password")).readlines()[0]
                  password = codecs.encode(password, 'utf8')
                  keyfile_json = json.load(open(path+"/"+file+"/"+i+"/_data/keystore/"+keystore))
                  derived_private_key = decode_keyfile_json(keyfile_json, password)
                  derived_private_key = encode_hex(derived_private_key)
                  print(i,derived_private_key)
