from math_operations import Math_operations
import sys

"""
    Method used to read a file, with is chosen because have the close method integrated,
    to avoid code errors or mistakes and for a better read of it.
    PATH_SOURCE is the folder where the file is located.
    The FILE_NAME is given in the 1 arguments from the use.
"""
def read_file():
    with open(f'{PATH_SOURCE}/{FILE_NAME}', 'r') as fr:
        data = fr.readlines()
    return data

"""
    Method used to write a file, with is chosen because have the close method integrated,
    to avoid code errors or mistakes and for a better read of it.
    PATH_TMP is the temporary folder where the file is created.
    The ENCRIPTED_FILE_NAME is given in the 1 arguments from the use.
"""
def write_file(data):
    with open(f'{PATH_TMP}/{ENCRIPTED_FILE_NAME}', 'w') as fw:
        fw.writelines(data)

"""
    Take a value and return a bool.
"""               
def isfloat(num):
    try:
        float(num)
        return True
    except:
        return False

"""
    Used to find all the float value in a column or else if the values are not float it use the len of the field.
    Data is a list of dictionaries. 
    Column is the name of the column to use.
""" 
def find_num(data, column) -> list:
    list_of_values = [] # init list
    try:
        for dicto in data: 
            for key, value in dicto.items():
                if isfloat(value) and key.lower() == column.lower():
                    list_of_values.append(float(value)) # add to the list all the float vaues found
                elif not isfloat(value) and key.lower() == column.lower() and value != ' ':
                    list_of_values.append(len(value)) # add to the list all the lenghts of the value found if it is not a float
        return list_of_values
    except KeyError as e:
        print("Invalid Key ", e)
    finally:
        #if there are an error return an empty list
        return list_of_values

"""
    Encriptor method.
    data is a list of dictionaries to encript. -> required
    encripter_alpha is the encriptor used. -> required
    encripter_num is not required and set to 0, so if no argument is pass for this one the ecripter for numeric values will be 0.
    matchers is not required and set to None, if no matcher is pass to the method it will encript all the columns not numeric.
""" 
def encript(data, encripter_alpha, encripter_num=0, matchers=None) -> list:
    encripted_list = [] # init list
    try:
        for dicto in data:
            for key, value in dicto.items():
                if matchers: # if matchers are pass as argument
                    for v in value:
                        if v.isalpha() and key.lower() in matchers:
                            value = value.replace(v, encripter_alpha) # replacing all the characters alpha of the value
                    dicto[key] = value # save the new value
                    if isfloat(value) and key.lower() in matchers:
                        value = encripter_num # replacing all the characters numeric of the value
                        dicto[key] = value # save the new value
                else: #same conditions without matchers
                    for v in value:
                        if v.isalpha():
                            value.replace(v, encripter_alpha)
                    dicto[key] = value
                    if isfloat(value):
                        value = encripter_num
                        dicto[key] = value
            encripted_list.append(dicto) # saving the encripted dictionaries in a new list
        return encripted_list
    except KeyError as e:
        print("Invalid Key ", e)
    finally:
        #if there are an error return an empty list
        return encripted_list
    
"""
    Method to convert the string rows reads in a list of dictionaries. 
    Return a list of dictionaries
    data is a list of strings
""" 
def dict_converter(data):
    try:
        list_of_dict = [] # init list
        keys = data[0].replace('\n', '').split(',') # assuming that we use a csv structure with the first line as name of columns, trasform it to dict keys
        for item in data[1:]:
            values = item.replace('\n', '').split(',') # all the other lines will be the values split by column
            list_of_dict.append({keys[i]: values[i] for i in range(len(keys))})
        return list_of_dict
    except IndexError as e:
        print(e)

"""
    Method to convert list of dictionaries to string. 
    Return a list of string.
    dicts is a list of dictionaries.
""" 
def list_converter(dicts):
    try:
        list_of_string = [] # init list
        list_of_string.append(','.join(dicts[0].keys()) + '\n') #add a '\n' caracter to jump line in the new file
        for dicto in dicts:
            list_of_string.append(','.join(str(value) for key, value in dicto.items()) + '\n')
        return list_of_string
    except IndexError as e:
        print(e)

"""
    Make the report using the object Math_operations
    The argument can be multiple and make a report for each one of them
""" 
def report(*math_ops):
    sys.stdout.write("Report:")
    sys.stdout.write('\n'*2)
    for ops in math_ops:
        sys.stdout.write(str(ops))
        sys.stdout.write('\n')

"""
    Main method
"""                   
def main():
    # 1. read the file
    data = read_file()
    # 2. convert the string rows in a list of dict to map the data
    data_dict_list = dict_converter(data)
    # 3. initiate the math_ops objects and set matchers for encripting
    math_ops_avg = Math_operations(find_num(data_dict_list, COLUMN_AVG), COLUMN_AVG) # COLUMN_AVG is the 'Billing' column
    math_ops_len = Math_operations(find_num(data_dict_list, COLUMN_LEN), COLUMN_LEN) # COLUMN_AVG is the 'Name' column
    matchers = [x.lower() for x in FIELDS_TO_ENCRIPT.split(',')] # set the matchers
    # 4. with math_ops_bill calculete the average of the column take in count -> COLUMN_AVG
    avg = math_ops_avg.avg()
    # 5. encript the data
    data_encripted = encript(data_dict_list, ALPHA_ENCRIPTER, avg, matchers)
    # 6. convert the thata tu list of string to be write in a file
    list_to_write = list_converter(data_encripted)
    # 7. write a new encripted file
    write_file(list_to_write)
    # 8. make a report with the math_ops using the given columns of interest
    report(math_ops_avg, math_ops_len)
    
if __name__ == '__main__':
    # the user can itroduce all the arguments
    if len(sys.argv) == 9: #if introduce all arguments
        FILE_NAME = sys.argv[1]
        ENCRIPTED_FILE_NAME = sys.argv[2]
        ALPHA_ENCRIPTER = sys.argv[3]
        FIELDS_TO_ENCRIPT = sys.argv[4]
        COLUMN_AVG = sys.argv[5]
        COLUMN_LEN = sys.argv[6]
        PATH_SOURCE = sys.argv[7]
        PATH_TMP = sys.argv[8]
        main()
    elif len(sys.argv) == 1: #if none of them
        FILE_NAME = "customers.csv"
        ENCRIPTED_FILE_NAME = "masked_client.csv"
        ALPHA_ENCRIPTER = 'X'
        FIELDS_TO_ENCRIPT = "Name,Email,Billing"
        COLUMN_AVG = "Billing"
        COLUMN_LEN = "Name"
        PATH_SOURCE = "./source"
        PATH_TMP = "./tmp"
        main()
    else: # if the user do not pass enough arguments
        sys.stdout.write("Introduce the correct number of paramiters or none of them to execute the script")
        sys.stdout.write('\n')        
        