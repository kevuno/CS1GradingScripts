import sys

import subprocess
args = []
for arg in sys.argv:
	args += [arg]


input_tests = ["1"]




for i in range(len(input_tests)):	
	#Execure the python file passed in the args and redirect the input
	input_str = 'input'+input_tests[i]
	print(input_str)
	input_file = 'input1'
	file_output = subprocess.Popen(['python', args[1]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


	#Save ouput in a .txt file
	fouts = open('out.txt', 'wb')


	fouts.write(file_output.communicate(input=open("input1.txt", "rb").read())[0])
	fouts.close()
