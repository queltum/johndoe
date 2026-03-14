_opcodes = {
	"add": 0o00, "sub": 0o01, "mul": 0o02, "div": 0o03, 
	"mod": 0o04, "pow": 0o05, "inc": 0o06, "dec": 0o07,

	"and": 0o10, "or": 0o11, "xor": 0o12, "not": 0o13, 
	"lsh": 0o14, "rsh": 0o15, "bic": 0o16, "neg": 0o17,

	"push": 0o20, "pop": 0o21, "dup": 0o22, "poke": 0o23, 
	"swap": 0o24, "over": 0o25, "dump": 0o26, "breakpoint": 0o27,

	"je": 0o30, "jne": 0o31, "jg": 0o32, "jge": 0o33, 
	"jl": 0o34, "jle": 0o35, "jmp": 0o36, "goto": 0o37,

	"jez": 0o40, "jnez": 0o41, "jgz": 0o42, "jgez": 0o43, 
	"jlz": 0o44, "jlez": 0o45, "repeat": 0o46, "end": 0o47,

	"call": 0o50, "invoke": 0o51, "acall": 0o52, "await": 0o53, 
	"ret0": 0o54, "ret1": 0o55, "ret2": 0o56, "retn": 0o57,

	"int": 0o60, "trap": 0o61, "in": 0o62, "out": 0o63,
}

def resolve_labels(raw):
	pc = 0
	lbl_cnt = 0
	labels = {}

	for line in raw.splitlines():
		label, _, _ = line.partition(' ')
		if label[-1] == ':':
			labels[label[:-1]] = pc - lbl_cnt
			lbl_cnt += 1
		pc += 1
	return labels

def parse(raw):
	il = []
	opcodes = _opcodes
	labels = resolve_labels(raw)
	is_main = False

	for line in raw.splitlines():
		opcode, _, arg = line.partition(' ')
		
		if opcode.endswith(':'): 
			if opcode.startswith("main"): is_main = True
			continue

		match arg:
			case '': arg = 0
			case a if arg in labels: arg = labels[a]
			case a if a.startswith("0x"): arg = int(arg, 16)
			case a if a.startswith("0o"): arg = int(arg, 8)
			case a if a.startswith("0b"): arg = int(arg, 2)
			case a if a.startswith("\""): arg = a[1:-1]
			case _: 
				try: arg = int(a)
				except ValueError: arg = float(a)

		match opcode:
			case "ret" if is_main:
				opcode = "end"
				is_main = False
			case "ret":
				match arg:
					case 0: opcode = "ret0"
					case 1: opcode = "ret1"
					case 2: opcode = "ret2"
					case _: opcode = "retn"

		il.append((opcodes[opcode], arg))
	return il
