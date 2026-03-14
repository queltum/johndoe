from . import context as ctx

def op_add(x):
	sp = ctx.sp - 1
	stack = ctx.stack
	stack[sp] += stack[sp + 1]
	ctx.sp = sp
	ctx.pc += 1

def op_sub(x):
	sp = ctx.sp - 1
	stack = ctx.stack
	stack[sp] -= stack[sp + 1]
	ctx.sp = sp
	ctx.pc += 1

def op_mul(x):
	sp = ctx.sp - 1
	stack = ctx.stack
	stack[sp] *= stack[sp + 1]
	ctx.sp = sp
	ctx.pc += 1

def op_div(x):
	sp = ctx.sp - 1
	stack = ctx.stack
	stack[sp] /= stack[sp + 1]
	ctx.sp = sp
	ctx.pc += 1

def op_inc(x):
	ctx.stack[ctx.sp] += 1
	ctx.pc += 1

def op_dec(x):
	ctx.stack[ctx.sp] -= 1
	ctx.pc += 1

def op_mod(x):
	sp = ctx.sp - 1
	stack = ctx.stack
	stack[sp] %= stack[sp + 1]
	ctx.sp = sp
	ctx.pc += 1

def op_pow(x):
	sp = ctx.sp - 1
	stack = ctx.stack
	stack[sp] **= stack[sp + 1]
	ctx.sp = sp
	ctx.pc += 1

def op_and(x):
	sp = ctx.sp - 1
	stack = ctx.stack
	stack[sp] &= stack[sp + 1]
	ctx.sp = sp
	ctx.pc += 1

def op_or(x):
	sp = ctx.sp - 1
	stack = ctx.stack
	stack[sp] |= stack[sp + 1]
	ctx.sp = sp
	ctx.pc += 1

def op_xor(x):
	sp = ctx.sp - 1
	stack = ctx.stack
	stack[sp] ^= stack[sp + 1]
	ctx.sp = sp
	ctx.pc += 1

def op_not(x):
	sp = ctx.sp
	stack = ctx.stack
	stack[sp] = ~stack[sp]
	ctx.pc += 1

def op_lsh(x):
	sp = ctx.sp - 1
	stack = ctx.stack
	stack[sp] <<= stack[sp + 1]
	ctx.sp = sp
	ctx.pc += 1

def op_rsh(x):
	sp = ctx.sp - 1
	stack = ctx.stack
	stack[sp] >>= stack[sp + 1]
	ctx.sp = sp
	ctx.pc += 1

def op_s2i(x):
	sp = ctx.sp
	stack = ctx.stack
	stack[sp] = int(stack[sp])
	ctx.pc += 1

def op_s2f(x):
	sp = ctx.sp
	stack = ctx.stack
	stack[sp] = float(stack[sp])
	ctx.pc += 1

def op_pushi(obj):
	sp = ctx.sp + 1
	ctx.stack[sp] = int(obj)
	ctx.sp = sp
	ctx.pc += 1

def op_pushf(obj):
	sp = ctx.sp + 1
	ctx.stack[sp] = float(obj)
	ctx.sp = sp
	ctx.pc += 1

def op_pushs(obj):
	sp = ctx.sp + 1
	ctx.stack[sp] = obj
	ctx.sp = sp
	ctx.pc += 1

def op_pop(n):
	ctx.sp -= n
	ctx.pc += 1

def op_dup(offset):
	sp = ctx.sp + 1
	stack = ctx.stack
	stack[sp] = stack[ctx.bp + int(offset)]
	ctx.pc += 1
	ctx.sp = sp

def op_poke(offset):
	stack = ctx.stack
	stack[ctx.bp + int(offset)] = stack[ctx.sp]
	ctx.pc += 1

def op_swap(offset):
	sp = ctx.sp
	bp_off = ctx.bp + int(offset)
	stack = ctx.stack
	temp = stack[sp]
	stack[sp] = stack[bp_off]
	stack[bp_off] = temp
	ctx.pc += 1

def op_ret(x):
	sp = ctx.sp
	bp = ctx.bp
	stack = ctx.stack
	ctx.bp, ctx.pc = stack[bp]
	stack[bp] = stack[sp]
	ctx.sp -= 1

def op_noret(x):
	ctx.bp, ctx.pc = ctx.stack[ctx.sp]
	ctx.sp -= 1

def op_call(addr):
	sp = ctx.sp + 1
	stack = ctx.stack
	stack[sp] = (ctx.bp, ctx.pc + 1)
	ctx.bp = sp
	ctx.pc = int(addr)
	ctx.sp = sp

def op_je(addr):
	sp = ctx.sp
	stack = ctx.stack
	
	if stack[sp - 1] == stack[sp]:
		ctx.pc = int(addr)
	else:
		ctx.pc += 1

def op_jne(addr):
	sp = ctx.sp
	stack = ctx.stack
	
	if stack[sp - 1] != stack[sp]:
		ctx.pc = int(addr)
	else:
		ctx.pc += 1

def op_jg(addr):
	sp = ctx.sp
	stack = ctx.stack
	
	if stack[sp - 1] > stack[sp]:
		ctx.pc = int(addr)
	else:
		ctx.pc += 1

def op_jge(addr):
	sp = ctx.sp
	stack = ctx.stack
	
	if stack[sp - 1] >= stack[sp]:
		ctx.pc = int(addr)
	else:
		ctx.pc += 1

def op_jl(addr):
	sp = ctx.sp
	stack = ctx.stack
	
	if stack[sp - 1] < stack[sp]:
		ctx.pc = int(addr)
	else:
		ctx.pc += 1

def op_jle(addr):
	sp = ctx.sp
	stack = ctx.stack
	
	if stack[sp - 1] <= stack[sp]:
		ctx.pc = int(addr)
	else:
		ctx.pc += 1

def op_jmp(addr):
	ctx.pc = int(addr)

def op_in(port_id):
	ctx.pc += 1

def op_out(port_id):
	ctx.pc += 1

def op_int(func_id):
	ctx.pc += 1

_running = False

def op_end(x):
	global _running
	_running = False 

dispatch = {
	"add": op_add, "sub": op_sub, "mul": op_mul, "div": op_div,
	"inc": op_inc, "dec": op_dec, "mod": op_mod, "pow": op_pow,
	"and": op_and,  "or": op_or,  "xor": op_xor, "not": op_not,
	"lsh": op_lsh, "rsh": op_rsh, "s2i": op_s2i, "s2f": op_s2f,
	"pushi": op_pushi, "pushf": op_pushf, "pushs": op_pushs, "pop": op_pop,
	"dup": op_dup, "poke": op_poke, "swap": op_swap, "ret": op_ret, 
	"noret": op_noret, "call": op_call, "je": op_je, "jne": op_jne,
	"jg": op_jg, "jge": op_jge, "jl": op_jl, "jle": op_jle, "jmp": op_jmp,
	"end": op_end, "in": op_in, "out": op_out, "int": op_int
}

def execute(code):
	global _running

	ctx.pc = 0
	ctx.sp = -1
	ctx.bp = 0
	ctx.clock = 0

	_running = True
	while _running:
		cmd = code[ctx.pc]
		dispatch[cmd[0]](cmd[1])