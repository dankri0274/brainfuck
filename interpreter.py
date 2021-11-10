import sys

#*	'>'	=	Increment the pointer
#*	'<'	=	Decrement the pointer
#*	'+'	=	Increment the value at the pointer
#*	'-'	=	Decrement the value at the pointer
#*	'.'	=	Output the value at the pointer as UTF-8 character
#*	','	=	Accept one byte of input, storing its value in the mem at the pointer
#*	'['	=	If the byte at the pointer is zero, then jump to the matching ]
#*	']'	=	If the byte at the pointer is not zero, then jump it back to the matching [

MEMORY_SIZE = 30000
MEMORY = [0 for i in range(MEMORY_SIZE)]
POINTER = 0

if __name__ == "__main__":
	ARGS = sys.argv
	PATH = ARGS[1]
	with open(PATH) as f:
		code = f.read()
	codeList = list(code)
	HEAD = 0
	while HEAD < len(codeList):
		if codeList[HEAD] == "+":
			MEMORY[POINTER] += 1
		elif codeList[HEAD] == "-":
			MEMORY[POINTER] -= 1
		elif codeList[HEAD] == "[":
			if MEMORY[POINTER] == 0:
				COUNT = 1
				while COUNT != 0:
					HEAD += 1
					if HEAD == len(codeList):
						print("']' is missing!")
						sys.exit(1)
					if codeList[HEAD] == "[":
						COUNT += 1
					elif codeList[HEAD] == "]":
						COUNT -= 1
		elif codeList[HEAD] == "]":
			if MEMORY[POINTER] != 0:
				COUNT = 1
				while COUNT != 0:
					HEAD -= 1
					if HEAD < 0:
						print("'[' is missing!")
					if codeList[HEAD] == "]":
						COUNT += 1
					elif codeList[HEAD] == "[":
						COUNT -= 1
		elif codeList[HEAD] == ".":
			print(chr(MEMORY[POINTER]), end = "")
		elif codeList[HEAD] == ",":
			MEMORY[POINTER] = ord(input()[0])
		elif codeList[HEAD] == ">":
			POINTER += 1
			if POINTER > MEMORY_SIZE:
				print("OVERFLOW")
				sys.exit(1)
		elif codeList[HEAD] == "<":
			if POINTER == 0:
				print("Can't decrement anymore")
			POINTER -= 1
		else:
			pass
		HEAD += 1
