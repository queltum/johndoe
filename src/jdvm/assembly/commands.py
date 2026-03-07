from .opcodes import Opcode

class Command:
	def __init__(self, opcode: int, arg):
		self.opcode = opcode
		self.arg = arg

	def __repr__(self):
		return f"opcode: {self.opcode}, arg: {self.arg}"

def ADD(arg) -> Command:
	return Command(Opcode.ADD, None)
def SUB(arg) -> Command:
	return Command(Opcode.SUB, None)
def MUL(arg) -> Command:
	return Command(Opcode.MUL, None)
def DIV(arg) -> Command:
	return Command(Opcode.DIV, None)
def INC(arg) -> Command:
	return Command(Opcode.INC, None)
def DEC(arg) -> Command:
	return Command(Opcode.DEC, None)
def MOD(arg) -> Command:
	return Command(Opcode.MOD, None)
def POW(arg) -> Command:
	return Command(Opcode.POW, None)
def AND(arg) -> Command:
	return Command(Opcode.AND, None)
def OR(arg) -> Command:
	return Command(Opcode.OR, None)
def XOR(arg) -> Command:
	return Command(Opcode.XOR, None)
def NOT(arg) -> Command:
	return Command(Opcode.NOT, None)
def LSH(arg) -> Command:
	return Command(Opcode.LSH, None)
def RSH(arg) -> Command:
	return Command(Opcode.RSH, None)
def SET(arg) -> Command:
	return Command(Opcode.SET, None)
def RESET(arg) -> Command:
	return Command(Opcode.RESET, None)
def PUSH(arg) -> Command:
	return Command(Opcode.PUSH, arg)
def POP(arg) -> Command:
	return Command(Opcode.POP, None)
def DUP(arg) -> Command:
	return Command(Opcode.DUP, arg)
def SWAP(arg) -> Command:
	return Command(Opcode.SWAP, arg)
def RET(arg) -> Command:
	return Command(Opcode.RET, None)
def THROW(arg) -> Command:
	return Command(Opcode.THROW, None)
def YIELD(arg) -> Command:
	return Command(Opcode.YIELD, None)
def AWAIT(arg) -> Command:
	return Command(Opcode.AWAIT, None)
def JE(arg) -> Command:
	return Command(Opcode.JE, arg)
def JNE(arg) -> Command:
	return Command(Opcode.JNE, arg)
def JG(arg) -> Command:
	return Command(Opcode.JG, arg)
def JGE(arg) -> Command:
	return Command(Opcode.JGE, arg)
def JL(arg) -> Command:
	return Command(Opcode.JL, arg)
def JLE(arg) -> Command:
	return Command(Opcode.JLE, arg)
def JMP(arg) -> Command:
	return Command(Opcode.JMP, arg)
def CALL(arg) -> Command:
	return Command(Opcode.CALL, arg)
def REM(arg) -> Command:
	return Command(Opcode.REM, arg)
def LBL(arg) -> Command:
	return Command(Opcode.LBL, arg)
def BPT(arg) -> Command:
	return Command(Opcode.BPT, None)
def END(arg) -> Command:
	return Command(Opcode.END, None)
def INT(arg) -> Command:
	return Command(Opcode.INT, arg)