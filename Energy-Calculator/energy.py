import os
import sys
import datetime
DEBUG=True
warning_numbers=0
version=0.1
logo='''
   __                            __       _
  /  `                          /  )     //
 /--  ____  _  __  _,  __  ,   /   __.  // _.
(___,/ / <_</_/ (_(_)_/ (_/_  (__/(_/|_</_(__
                   /|    /
                  |/    '
    '''
def print_sign():
    '''
    This function print logo and version
    :return: None
    '''
    print(logo)
    print(line(70, "-"))
    print("Version :"+str(version))
    print("By Sepand Haghighi")
    print(line(70,"-"))
def line(number,char="*"):
    '''
    This function return line sign
    :param number: number of char
    :type number:int
    :param char: char item
    :type char:str
    :return: response line as str
    '''
    index=0
    response=""
    while(index<number):
        index+=1
        response+=char
    return response
def convert(num):
    '''
    This function convert number
    :param num: input numger
    :type num:int
    :return: output string
    '''
    for x in ['wh', 'kwh', 'mwh', 'gwh']:
        if num < 1000:
            return "%3.1f %s" % (num, x)
        num /= 1000

def check_constraint(input_num,mode=1):
    '''
    This function check for days and hours constraints
    :param input_num: input number
    :type input_num:int
    :param mode: mode flag for year and days
    :type mode:int
    :return: input_number after constraints
    '''
    if mode==1:
        if input_num>24:
            return 24
    else:
        if input_num>365:
            return 365
    return input_num

def handle_input(input_string):
    '''
    This function convert string input to integer and return 0 in error
    :param input_string: input sring
    :type input_string:str
    :return: integer number
    '''
    try:
        return int(input_string)
    except Exception as e:
        return 0
def seperator(input_string,char=","):
    '''
    This function seperate input string to key,wattage,number,hours_per_day,days_per_year
    :param input_string: input string before seperation
    :type input_string:str
    :return:  list of parameters
    '''
    try:
        seperated_data = input_string.split(char)
        key = seperated_data[0]
        wattage = int(seperated_data[1])
        number = int(seperated_data[2])
        hours_per_day = check_constraint(int(seperated_data[3]), mode=1)
        days_per_year = check_constraint(int(seperated_data[4]), mode=2)
        return [key,wattage,number,hours_per_day,days_per_year]
    except:
        global warning_numbers
        warning_numbers+=1
        print(str(warning_numbers)+"-Warning : Some issue In this line -->",input_string)
        print(line(70))
        return [0,0,0,0,0]
def find_ref():
    '''
    This function search for available ref file
    :return: ref file name
    '''
    for item in os.listdir():
        if item.find(".ref")!=-1:
            return item
    return "NOFILE"
def get_input():
    try:
        total_amount=0
        file_name=find_ref()
        if file_name=="NOFILE":
            print("There is no ref file")
            sys.exit()
        file=open(file_name,"r")
        output_file=open("energy.out","w")
        output_file.write(str(datetime.datetime.now())+"\n")
        output_file.write(line(70)+"\n")
        for item in file:
            coefficients=seperator(item)
            item_usage=coefficients[1]*coefficients[2]*coefficients[3]*coefficients[4]
            if item_usage!=0:
                output_file.write(coefficients[0]+" --> "+convert(item_usage)+"\n")
            total_amount+=item_usage
        output_response=convert(total_amount)
        output_file.write(line(70)+"\n"+"Total :"+output_response)
        file.close()
        output_file.close()
        return output_response
    except Exception as e:
        print("Error")
        if output_file.closed==False:
            output_file.close()
        if DEBUG==True:
            print(str(e))

if __name__=="__main__":
    print_sign()
    print("Total :"+get_input())