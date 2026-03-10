class Command:

	def __init__(self, opcode: int, arg):
		self.opcode = opcode
		self.arg = arg

	def __repr__(self):
		return f"opcode: {self.opcode}, arg: {self.arg}"

def ADD(arg) -> Command:
	return Command(0, None)

def SUB(arg) -> Command:
	return Command(1, None)

def MUL(arg) -> Command:
	return Command(2, None)

def DIV(arg) -> Command:
	return Command(3, None)

def INC(arg) -> Command:
	return Command(4, None)

def DEC(arg) -> Command:
	return Command(5, None)

def MOD(arg) -> Command:
	return Command(6, None)

def POW(arg) -> Command:
	return Command(7, None)

def AND(arg) -> Command:
	return Command(8, None)

def OR(arg) -> Command:
	return Command(9, None)

def XOR(arg) -> Command:
	return Command(10, None)

def NOT(arg) -> Command:
	return Command(11, None)

def LSH(arg) -> Command:
	return Command(12, None)

def RSH(arg) -> Command:
	return Command(13, None)

def SET(arg) -> Command:
	return Command(14, None)

def POKE(arg) -> Command:
	return Command(15, None)

def PUSH(arg) -> Command:
	return Command(16, arg)

def POP(arg) -> Command:
	return Command(17, None)

def DUP(arg) -> Command:
	return Command(18, arg)

def SWAP(arg) -> Command:
	return Command(19, arg)

def REM(arg) -> Command:
	return Command(20, arg)

def LBL(arg) -> Command:
	return Command(21, arg)

def BPT(arg) -> Command:
	return Command(22, None)

def END(arg) -> Command:
	return Command(23, None)

def JE(arg) -> Command:
	return Command(24, arg)

def JNE(arg) -> Command:
	return Command(25, arg)

def JG(arg) -> Command:
	return Command(26, arg)

def JGE(arg) -> Command:
	return Command(27, arg)

def JL(arg) -> Command:
	return Command(28, arg)

def JLE(arg) -> Command:
	return Command(29, arg)

def JMP(arg) -> Command:
	return Command(30, arg)

def CALL(arg) -> Command:
	return Command(31, arg)

def RET(arg) -> Command:
	return Command(32, None)

def THROW(arg) -> Command:
	return Command(33, None)

def YIELD(arg) -> Command:
	return Command(34, None)

def AWAIT(arg) -> Command:
	return Command(35, None)

def IN(arg) -> Command:
	return Command(36, arg)

def OUT(arg) -> Command:
	return Command(37, arg)

def INT(arg) -> Command:
	return Command(38, arg)

def ASYNC_CALL(arg) -> Command:
	return Command(39, arg)