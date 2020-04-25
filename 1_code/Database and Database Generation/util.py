# Created on 20200216 by Kimberly Chang


import os
import sys


#####################
#     FUNCTIONS     #
#####################
# function to parse a CSV file into a nested linked list
# Input Parameters:
#       file: the file (and its path) to be parsed
#       skip: number of lines to skip from the beginning of the file
# Return Value:
#       csv_list: a nested linked list containing the data from the CSV
def parse_csv(file, skip):
    # check to see if the path is valid
    if not os.path.exists(file):
        print("ERROR: File does not exist!")
        sys.exit(-1)

    # parsing the file into the list
    csv_list = []
    with open(file, "r") as fd:
        for i in range(skip):
            fd.readline()  # skips lines
        for line in fd:
            line_list = line.rstrip("\n").split(',')
            csv_list.append(line_list)
    fd.close()

    # returning the created list
    return csv_list


# function to print the elements of a nested list
def print_nested_list(nested_list):
    for line in nested_list:
        for element in line:
            print(f'{element}\t', end="|")
        print('')


# function to print the elements of a list (object) stored in a hash table
def print_hash_table_obj(ht):
    for line in ht:
        if line is not None:
           for element in line:
                for item in element:
                    print(f'{item}\t', end="|")
                print(',')
        print('---')


# function to convert a string into an integer
# by converting each character of the string into its ASCII integer value and summing them
def str2int(s):
    s_sum = 0
    for letter in s:
        s_sum += ord(letter)
    return s_sum


# function to determine an integer hash value based on three inputs
# by adding their converted integer values from str2int() together
def d_hash(input0, input1, input2):
    return (str2int(input0) + str2int(input1) + str2int(input2)) % 20


# function to round a floating point number to the nearest integer
def int_round(num):
    int_num = int(num)
    if (num - float(int_num)) >= 0.5:
        return int_num+1
    else:
        return int_num


# function to write the contents of a nested list into a CSV file
# Input Parameters:
#       file: the file (and its path) to which to be written
#       o_list: the list whose contents are to be inserted in the CSV
def write_csv(file, o_list):
    fd = open(file, "w")
    for line in o_list:
        line_str = ""
        for element in line:
            line_str += f'{element},'
        line_str = line_str[:-1] + "\n"
        fd.write(line_str)
    fd.close()
