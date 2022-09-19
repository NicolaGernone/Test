# Test_Nicola_Gernone

## Problem Description

The problem is based on encripting sensitive informations in a CSV file, the sensitive informations are given in the [statement.2.0.md](statement.2.0.md) as how to encript the data.
No dependencies on the standard `csv` module or any 3rd-party modules are allowed.
- Encription rules:
  The columns containing sensitive data are "Name", "Email" and "Billing". 
  The output file should be named "masked_clients.csv" and will contain the same 
  columns as "customers.csv". 
  For example:
   * john@mail.com should be transformed to XXXX@XXXX.XXX, keeping the same length and format
   * If there are 2 rows in the billing column with values 10 and 5, both of them should be converted to 7.5
- Report rules:
  * Print a report (to standard output) containing:
    * Maximum, minimum and average length of the "Name" field value
    * Maximum, minimum and average of the "Billing" field value

## Approach
To approche the problem i choose to pass the file datas to a list of dictionaries to map better the datas based on their columns.
With this mapping i can easly obtain the data needed.
To read and write the file i choose the 'with' statemen to agilize the code as it has embedded a close funtion and a Exception Handler.
The implementation of Math_operation class allow me to easly use the mathematicals methods implemented in it to calculate the average for the encriptor and make the report with the min, max and avg of the given columns names.
To make user friendly the use of application i implement a way to introduce the names of the files in input and output if needed, if the names are not itroduced at the running the default ones, given in the statement, will be used (input: "customers.csv", output: "masked_clients.csv").

## Usage

Make sure to ave installed python3 on your computer [python](https://www.python.org/downloads/).
Create the output directory that you want to use or check if the tmp directory is in the Test directory to use the default output path.

To run the script cd to the cloned folder Test and open the terminal.
Run:
````bash
file_encriptor.py "name_of_the_file" "name_of_the_encripted_file" "encriptor" "col1,col2,col3,..." "column_avg" "column_len" "path_input" "path_output"
````
- Arguments:
    * "name_of_the_file": is the name of the input file.
    * "name_of_the_encripted_file": is the name of the output file.
    * "encriptor": is the character to use to encript the string.
    * "col1,col2,col3,...": is the list of columns to encript.
    * "column_avg": is the column to use to calculate the avg.
    * "column_len": is the column to use to calculate the avg dor the no numeric fields.
    * "path_input": is the path of the input file.
    * "path_output": is the path of the output file.

* Order is important*

- Example:
````bash
file_encriptor.py "customers.csv" "masked_client.csv" "&" "Name,Email,Billing" "Billing" "Name" "./source" "./tmp"
````

If you want to use the default names run:
````bash
file_encriptor.py
````

## Considerations

The list of dictionarie could be a dict with the keys as the column names and the values as a list of all the column data as well.
