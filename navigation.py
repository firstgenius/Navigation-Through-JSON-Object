from typing import Any, List, Dict
import json


def read_file(path: str) -> list:
    '''
    This function reads information from a file and returns a dictionary.

    >>> type(read_file("kved.json"))
    <class 'dict'>
    '''

    fil = open(path, "r")
    all_info = json.load(fil)
    fil.close()
    return all_info


def list_data(info):
    end_range = len(info)
    print(f'Here are possible keys: 1 - {end_range + 1}. Choose one')
    user_input = int(input())
    return info[user_input - 1]
    

def dict_data(info):
    opportunities = list(info.keys())
    print('Here are possible keys. Choose one and write it')
    print(opportunities)
    user_input = input()
    return info[user_input]


def search(info):
    if type(info) == list:
        search(list_data(info))
    elif type(info) == dict:
        search(dict_data(info))
    else:
        print('Now you are at the bottom of the file')
        print(f"Here is searched data: {info}")


if __name__ == '__main__':
    user_input = input('Welome! This function navigates through the json object. Enter your file name: ')
    try:
        info = read_file(user_input)
        search(info)
    except FileNotFoundError:
        print('OOPS! No file with such name is found')