from dataclasses import replace
from fileinput import close
import json
from enckey import create_key,decreypt_key
import random
import string

alphabet_string = string.ascii_uppercase

alphabet_list = list(alphabet_string)

curr_loaded_key=''
file_data={}

def write_json(filename='keys.json'):
    with open(filename,'r+') as file:
        json.dump(file_data, file)


def commands_operator():
    commands={'info':enc_info,'load':enc_load,'save':enc_save,'newkey':enc_key,'enc':enc_txt,'dec':dec_txt}
    return commands


def cli_main():
    commands=commands_operator()
    switch=False
    while not switch:
        cmd=input('sub>')
        cmd_input=cmd.split()
        if cmd_input and cmd_input[0] == 'done':
            switch=True
        if cmd_input and cmd_input[0]=='enc':
                enc_txt(cmd_input[1],cmd_input[2])
                continue 
        if cmd_input and cmd_input[0]=='dec':
                dec_txt(cmd_input[1],cmd_input[2])
                continue       
        if cmd_input:
            commands[cmd_input[0]](cmd_input[1:])



def enc_info(nothing):
    print(curr_loaded_key)

def enc_save(filename):
    global file_data  
    temp=str(filename)
    temp2=repair_key_name(temp)
    temp2+='.json'
    change_key_state(repair_key_name(temp2))

    with open("keys.json", 'r+') as f:
        json_object=json.load(f) 

    with open(temp2,'a+') as file:
        json.dump(json_object, file)
    print(f'Enc/Dec keys saved in {temp2} file')                
                

def enc_key(keyname):
    keyname_repaired=repair_key_name(keyname)
    random.shuffle(alphabet_list)  
    new_random_key=''.join(alphabet_list)
   
    key_list=[x for x in new_random_key]

    print(f"A new key called {keyname_repaired} was created!")
    
    temp_key=create_key(new_random_key)
    

    enc_key_list=[x for x in temp_key]
    

    key_enckey= {key_list[i]:enc_key_list[i] for i in range(len(key_list))}
    key_deckey={enc_key_list[i]:key_list[i] for i in range(len(enc_key_list))}

    decrey=decreypt_key(new_random_key,key_deckey)

    data = {
    keyname_repaired: [
        {
            "current key": keyname_repaired,
            "key-id": new_random_key,
            "state": "not saved",
            "encrytpion": temp_key,
            "decryption": decrey
        }
    ]
}
    y=json.dumps(data)
    file_data[keyname_repaired]=y
    write_json('keys.json')
    

    

def enc_load(keyname):
    global file_data
    for i in file_data.items():
        if repair_key_name(keyname) not in str(file_data[i[0]]):
         print('no such key!')
         return

    global curr_loaded_key 
    with open("keys.json", 'r') as f:
        json_object=json.load(f) 
        for i in json_object.keys():
            if i==repair_key_name(keyname):
                temp=json_object[i]
                curr_loaded_key=temp

    print(f'{keyname} loaded succefully')


def enc_txt(file1,file2):
    with open(file1) as f:
        file1_contents = f.read()
        enc_file1=create_key(file1_contents)
    with open(file2,'w') as f2:
        f2.write(enc_file1)
    print(f'File {file1} was encrypted into {file2}')
    pass


def dec_txt(file1,file2):
    with open(file1) as f:
        file1_contents = f.read()
        enc_file1=create_key(file1_contents)
    with open(file2,'w') as f2:
        f2.write(enc_file1)
    print(f'File {file1} was decrypted into {file2}')    
    pass

def change_key_state(file_key_saved_in):
    global file_data
    global curr_loaded_key
    for i in file_data.items():
        if curr_loaded_key in str(file_data[i[0]]):
         curr_loaded_key=str(file_data[i[0]]).replace("not saved",f'"key saved in {file_key_saved_in} "')


def repair_key_name(keyname):
    keyname1=str(keyname).replace('[','')
    keyname2=str(keyname1).replace(']','')
    return keyname2

cli_main()
