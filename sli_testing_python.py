"""
file: sli_testing_python.py

Authors: Kevin Bastian, Andrew Berson

"""

import sys
import subprocess
import os

args = sys.argv

"""
Modify the input test accordingly
"""
input_tests = ["1","2","3"]



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

"""
Config vars:
"""
require_input = True
student_sol_dir = "student"
input_dir = "input"

actual_output_prefix = "ex"
actual_output_subfix = "_sol"
input_test_prefix = "ex"
input_test_subfix = ""

import os
for filename in os.listdir(student_sol_dir):
	#In myCourses the fileformat is numbers-morenums - Lastname,Firstname - filename
	student_fullname = filename.strip().split("-")[2]
	#Print some header with the student's name
	print("=========================================")
	print("=========================================")
	print("Solution for "+ student_fullname +": " )

	filename_complete = student_sol_dir+"/"+filename
	#Run student's submission and check with the actual solution
	for i in input_tests:	
		#Execure the python files found in the student's directory redirect the input
		file_output = subprocess.Popen(['python3', filename_complete], universal_newlines=True,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

		#Save ouput in a .txt file
		output_filename = "out"+i+".txt"
		input_filename = "input"+i+".txt"
		fout = open(output_filename, "w")

		#Save the output of the run of the program with the correct redirected input.
		if (require_input):
			#Check if there are actual input files in the directory given, otherwise use the generic input test prefix and subfix filenames as input
			input_filename_complete = input_dir+"/"+input_filename+".txt"
			if(os.path.isfile(input_filename_complete)):
				fout.write(file_output.communicate(input=open(input_filename_complete, "r").read())[0])
			else:
				input_test = input_test_prefix + i + input_test_subfix +".txt\n"
				fout.write(file_output.communicate(input=input_test)[0])
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
		for line in open(actual_output_prefix+i+actual_output_subfix+".txt"):
			line = line.strip()
			actual_output.append(line)

		#Now read the program's run output and compare each line to the actual output
		line_index = 0
		for line in open("out"+i+".txt"):
			#if there is no more to read in the actual output but the program's run output is still going we just print multiple "_"
			if(line_index < len(actual_output)):
				if( len(actual_output[line_index]) > difference_column_index and len(line) > difference_column_index ):

					print('{:50}{}{:50}'.format(actual_output[line_index][:50],"|| ",line[:50]))
					print('{:50}{}{:50}'.format(actual_output[line_index][50:],"|| ",line[50:]))

				elif( len(actual_output[line_index]) > difference_column_index and len(line) <= difference_column_index ):
					
					print('{:50}{}{:50}'.format(actual_output[line_index][:50],"|| ",line))
					print('{:50}{}{:_<50}'.format(actual_output[line_index][50:],"|| ",""))

				elif( len(actual_output[line_index]) <= difference_column_index and len(line) > difference_column_index ):
					
					print('{:50}{}{:50}'.format(actual_output[line_index],"|| ",line[:50]))
					print('{:_<50}{}{:50}'.format("","|| ",line[50:]))	

				else:	
					print('{:50}{}{:50}'.format(actual_output[line_index],"|| ",line))
			else:
				print('{:_<50}'.format(''))
				
			line_index +=1





