# HOMAcalc v1.0
# HOMA calculator, powered by Python 3.9
# Last Update: 2021-05-25
# Author: Zhe Wang
# Homepage: https://www.wangzhe95.net/program-homacalc

print("*******************************************************************************")
print("*                                                                             *")
print("*                                                                             *")
print("*                               H O M A c a l c                               *")
print("*                                                                             *")
print("*                                                                             *")
#print("*     ====================== Version 1.0 for macOS ======================     *")
#print("*     ====================== Version 1.0 for Linux ======================     *")
#print("*     ================ Version 1.0 for Microsoft Windows ================     *")
print("*     =================== Version 1.0 for Source Code ===================     *")
print("*                           Last update: 2021-05-25                           *")
print("*                                                                             *")
print("*         A HOMA calculator, developed by Zhe Wang. Online document is        *")
print("*        available from https://www.wangzhe95.net/program-homacalc .          *")
print("*                                                                             *")
print("*                             -- Catch me with --                             *")
print("*                         E-mail  wongzit@yahoo.co.jp                         *")
print("*                       Homepage  https://www.wangzhe95.net                   *")
print("*                         GitHub  https://github.com/wongzit                  *")
print("*                                                                             *")
print("*******************************************************************************")
print("\nPRESS Ctrl+c to exit the program.\n")

def calcHOMA (userInputted, alpha, Ropt):
	calcAtom = userInputted[:]
	calcAtom.append(userInputted[0])
	disMatrix = []
	for i in range(len(userInputted)):
		disABx = float(xCoors[int(calcAtom[i]) - 1]) - float(xCoors[int(calcAtom[i + 1]) - 1])
		disABy = float(yCoors[int(calcAtom[i]) - 1]) - float(yCoors[int(calcAtom[i + 1]) - 1])
		disABz = float(zCoors[int(calcAtom[i]) - 1]) - float(zCoors[int(calcAtom[i + 1]) - 1])
		disAB = pow(disABx * disABx + disABy * disABy + disABz * disABz, 0.5)
		disMatrix.append(disAB)
	sumDiff = 0.0000
	for j in range(len(disMatrix)):
		diffRoptRi = (float(disMatrix[j]) - Ropt) * (float(disMatrix[j]) - Ropt)
		sumDiff += diffRoptRi
	valueHOMA = 1 - alpha * sumDiff / float(len(disMatrix))
	return valueHOMA

print("Please specify the Gaussian output file path:")

# For Unix/Linux OS
fileName = input("(e.g.: /HOMAcalc/example/4cpp.log)\n")
if fileName.strip()[0] == '\'' and fileName.strip()[-1] == '\'':
    fileName = fileName.strip()[1:-1]

# For Microsoft Windows
#fileName = input("(e.g.: C:\\HOMAcalc\\example\\4cpp.log\n")
with open(fileName.strip(), 'r') as logFile:
	logFileLines = logFile.readlines()

endOutput = []

print("\n------ Parameters used in HOMAcalc ------")
print("")
print("      alpha = 98.89,  R_opt = 1.397      ")
print("    ref.: Chem. Rev., 2014, 114, 6383    ")
print("")
print("-----------------------------------------\n")

alpha = 98.89
Ropt = 1.397

for lineNo in range(len(logFileLines) - 1, 0, -1):
	#print(lineNo)
	endOutput.append(logFileLines[lineNo])
	if logFileLines[lineNo][:5] == ' 1\\1\\':
		break

endOutput.reverse()
endOutput2 = []

for endLineNo in range(len(endOutput)):
	endOutput2.append(endOutput[endLineNo].strip())

endOutStr = "".join(endOutput2)
endOutput3 = endOutStr.split('\\')
endOutput4 = []

for endLineNo3 in range(len(endOutput3)):
	if endOutput3[endLineNo3].count('.') == 3 and endOutput3[endLineNo3].count(',') == 3:
		if endOutput3[endLineNo3][0].isalpha():
			endOutput4.append(endOutput3[endLineNo3])

xCoors = []
yCoors = []
zCoors = []
element = []

for endLineNo4 in range(len(endOutput4)):
	element.append(endOutput4[endLineNo4].split(',')[0])
	xCoors.append(endOutput4[endLineNo4].split(',')[1])
	yCoors.append(endOutput4[endLineNo4].split(',')[2])
	zCoors.append(endOutput4[endLineNo4].split(',')[3])

print("Please input the atom numbers, seperated by space:")
print("(for changing parameters, please input \'para\'.)")
userInput = input("(e.g.: 1 2 3 4 5 6)\n")

if userInput == 'para':
	print("-----------------------------------")
	print("      Aplha (default: 98.89)")
	print("      R_opt (default: 1.397")
	print("-----------------------------------")

	while True:
		try:
			alpha = float(input("Specify the alpha value:\n"))
			break
		except ValueError:
			print("\nInput error, please input a number!")
			continue
	print(f"Alpha = {alpha}")

	while True:
		try:
			Ropt = float(input("Specify the Ropt value:\n"))
			break
		except ValueError:
			print("\nInput error, please input a number!")
			continue
	print(f"Ropt = {Ropt}")

	print("Please input the atom numbers, seperated by space:")
	userInput = input("(e.g.: 1 2 3 4 5 6)\n")

while userInput != 'q':
	while True:
		try:
			userInputList = userInput.split()
			break
		except ValueError:
			print("\nInput error, HOMAcalc termination.")
	print(f"\nHOMA value of ring [{userInput}] is {format(calcHOMA(userInputList, alpha, Ropt), '.4f')}.")
	print("\nInput atom numbers to calculate for other ring,")
	userInput = input("or input \'q\' to quit HOMAcalc.\n")

print("\n*******************************************************************************")
print("")
print("                       Normal termination of HOMAcalc.")
print("")
print("*******************************************************************************\n")
