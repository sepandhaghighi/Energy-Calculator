DEBUG=True

def convert(num):
    for x in ['wh', 'kwh', 'mwh', 'gwh']:
        if num < 1000:
            return "%3.1f %s" % (num, x)
        num /= 1000

def check_constraint(input_num,mode=1):
    if mode==1:
        if input_num>24:
            return 24
    else:
        if input_num>365:
            return 365
    return input_num

def handle_input(input_string):
    try:
        return int(input_string)
    except Exception as e:
        return 0
def seperator(input_string):
    try:
        seperated_data = input_string.split(",")
        key = seperated_data[0]
        wattage = int(seperated_data[1])
        number = int(seperated_data[2])
        hours_per_day = check_constraint(int(seperated_data[3]), mode=1)
        days_per_year = check_constraint(int(seperated_data[4]), mode=2)
        return [key,wattage,number,hours_per_day,days_per_year]
    except:
        return [0,0,0,0,0]

def get_input():
    try:
        total_amount=0
        file=open("input.csv","r")
        for line in file:
            coefficients=seperator(line)
            total_amount+=coefficients[1]*coefficients[2]*coefficients[3]*coefficients[4]
        file.close()
        return convert(total_amount)
    except Exception as e:
        print("Error")
        if DEBUG==True:
            print(str(e))

if __name__=="__main__":
    print(get_input())