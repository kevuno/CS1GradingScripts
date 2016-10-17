"""
file: sli_testing_python.py

Authors: Kevin Bastian, Andrew Berson

"""

import sys
import subprocess


args = sys.argv

"""
Modify the input test accordingly
"""
input_tests = ["1","2","7"]

input_files = True

"""
Run for each test:
1. Run the program file to be tested in a subprocess.
2. Store the output the file_output instance in bytes.
3. Create a file instance output to write the bytes.
4. Redirect the input if needed using a text file in the same call where it writes the output of the process.
5. Close the output file stream.
TODOS

1. Compare both the output file and the actual output file by just printing the differences.
2. Qualify the tests by a passing or not passing.
3. Personalize the lines and/or a range of characters to be ignored.

"""




for i in input_tests:	
	#Execure the python file passed in the args and redirect the input
	file_output = subprocess.Popen(['python', args[1]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	#Save ouput in a .txt file
	output_filename = "out"+i+".txt"
	input_filename = "input"+i+".txt"
	fout = open(output_filename, "wb")

	#Save the output of the run of the program with the correct redirected input.
	if (input_files):
		fout.write(file_output.communicate(input=open(input_filename, "rb").read())[0])
	else:
		fout.write(file_output.communicate()[0])
	fout.close()


	
"""
Temporary implementation of difference checking
TODOS: Format output difference
"""

difference_column_index = 50

for i in input_tests:
	#Save each line of the actual output in a list
	actual_output = []
	for line in open("actual_out"+i+".txt"):
		line = line.strip()
		actual_output.append(line)

	#Now read the program's run output and compare each line to the actual output
	line_index = 0
	for line in open("out"+i+".txt"):
		#if there is no more to read in the actual output but the program's run output is still going we just print multiple "_"
		if(line_index < len(actual_output)):
			print('{:50}{}{:50}'.format(actual_output[line_index],"|| ",line))
		else:
			print('{:_<50}'.format(''))
			
		line_index +=1





