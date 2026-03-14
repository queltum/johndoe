from .. import assembly
from . import context
from . import interrupts

class Executor:

	def __init__(self, ctx: context.Context, entry: int, code):
		self.ctx = ctx
		self.entry = entry
		self.ctx.pc = self.entry
		self.code = code
		self.interrupt_controller = interrupts.InterruptController(ctx)
		self.dispatch = (
			self.op_add, self.op_sub, self.op_mul, self.op_div,
			self.op_inc, self.op_dec, self.op_mod, self.op_pow,
			self.op_and, self.op_or, self.op_xor, self.op_not,
			self.op_lsh, self.op_rsh, self.op_set, self.op_poke,
			self.op_push, self.op_pop, self.op_dup, self.op_swap,
			self.op_rem, self.op_lbl, self.op_bpt, self.op_end,
			self.op_je, self.op_jne, self.op_jg, self.op_jge,
			self.op_jl, self.op_jle, self.op_jmp, self.op_call,
			self.op_ret, self.op_throw, self.op_yield, self.op_await,
			self.op_in, self.op_out, self.op_int, self.op_async_call
		)

	def load_commands(self, code: tuple):
		self.code = code

	def execute(self):
		self.ctx.running = True
		self.ctx.sp = -1
		self.ctx.bp = 0
		self.ctx.pc = self.entry

		while self.ctx.running:
			self.dispatch[self.code[self.ctx.pc].opcode]()

	def op_add(self):
		op_a = self.ctx.stack[self.ctx.sp]
		op_b = self.ctx.stack[self.ctx.sp - 1]
		self.ctx.sp -= 1
		self.ctx.stack[self.ctx.sp] = op_a + op_b
		self.ctx.pc += 1

	def op_sub(self):
		op_a = self.ctx.stack[self.ctx.sp]
		op_b = self.ctx.stack[self.ctx.sp - 1]
		self.ctx.sp -= 1
		self.ctx.stack[self.ctx.sp] = op_a - op_b
		self.ctx.pc += 1
	
	def op_mul(self):
		op_a = self.ctx.stack[self.ctx.sp]
		op_b = self.ctx.stack[self.ctx.sp - 1]
		self.ctx.sp -= 1
		self.ctx.stack[self.ctx.sp] = op_a * op_b
		self.ctx.pc += 1

	def op_div(self):
		op_a = self.ctx.stack[self.ctx.sp]
		op_b = self.ctx.stack[self.ctx.sp - 1]
		self.ctx.sp -= 1
		self.ctx.stack[self.ctx.sp] = op_a / op_b
		self.ctx.pc += 1

	def op_inc(self):
		self.ctx.stack[self.ctx.sp] += 1
		self.ctx.pc += 1

	def op_dec(self):
		self.ctx.stack[self.ctx.sp] -= 1
		self.ctx.pc += 1

	def op_mod(self):
		op_a = self.ctx.stack[self.ctx.sp]
		op_b = self.ctx.stack[self.ctx.sp - 1]
		self.ctx.sp -= 1
		self.ctx.stack[self.ctx.sp] = op_a % op_b
		self.ctx.pc += 1

	def op_pow(self):
		op_a = self.ctx.stack[self.ctx.sp]
		op_b = self.ctx.stack[self.ctx.sp - 1]
		self.ctx.sp -= 1
		self.ctx.stack[self.ctx.sp] = op_a ** op_b
		self.ctx.pc += 1

	def op_and(self):
		op_a = self.ctx.stack[self.ctx.sp]
		op_b = self.ctx.stack[self.ctx.sp - 1]
		self.ctx.sp -= 1
		self.ctx.stack[self.ctx.sp] = op_a & op_b
		self.ctx.pc += 1

	def op_or(self):
		op_a = self.ctx.stack[self.ctx.sp]
		op_b = self.ctx.stack[self.ctx.sp - 1]
		self.ctx.sp -= 1
		self.ctx.stack[self.ctx.sp] = op_a | op_b
		self.ctx.pc += 1

	def op_xor(self):
		op_a = self.ctx.stack[self.ctx.sp]
		op_b = self.ctx.stack[self.ctx.sp - 1]
		self.ctx.sp -= 1
		self.ctx.stack[self.ctx.sp] = op_a ^ op_b
		self.ctx.pc += 1

	def op_not(self):
		self.ctx.stack[self.ctx.sp] = ~self.ctx.stack[self.ctx.sp]
		self.ctx.pc += 1

	def op_lsh(self):
		op_a = self.ctx.stack[self.ctx.sp]
		op_b = self.ctx.stack[self.ctx.sp - 1]
		self.ctx.sp -= 1
		self.ctx.stack[self.ctx.sp] = op_a << op_b
		self.ctx.pc += 1

	def op_rsh(self):
		op_a = self.ctx.stack[self.ctx.sp]
		op_b = self.ctx.stack[self.ctx.sp - 1]
		self.ctx.sp -= 1
		self.ctx.stack[self.ctx.sp] = op_a >> op_b
		self.ctx.pc += 1

	def op_set(self):
		self.ctx.stack[self.ctx.sp] = self.code[self.ctx.pc].arg
		self.ctx.pc += 1

	def op_poke(self):
		self.ctx.stack[
			self.ctx.bp + self.code[self.ctx.pc].arg
		] = self.ctx.stack[self.ctx.sp]
		self.ctx.pc += 1

	def op_push(self):
		self.ctx.sp += 1
		self.ctx.stack[self.ctx.sp] = self.code[self.ctx.pc].arg
		self.ctx.pc += 1

	def op_pop(self):
		self.ctx.sp -= 1
		self.ctx.pc += 1

	def op_dup(self):
		self.ctx.sp += 1
		self.ctx.stack[self.ctx.sp] = self.ctx.stack[
			self.ctx.bp + self.code[self.ctx.pc].arg
		]
		self.ctx.pc += 1

	def op_swap(self):
		offset = self.ctx.bp + self.code[self.ctx.pc].arg
		tmp = self.ctx.stack[offset]
		self.ctx.stack[offset] = self.ctx.stack[self.ctx.sp]
		self.ctx.stack[self.ctx.sp] = tmp
		self.ctx.pc += 1

	def op_rem(self):
		self.ctx.pc += 1

	def op_lbl(self):
		self.ctx.pc += 1

	def op_bpt(self):
		self.ctx.pc += 1

	def op_end(self):
		self.ctx.running = False

	def op_je(self):
		if self.ctx.stack[self.ctx.sp] == self.ctx.stack[self.ctx.sp - 1]:
			self.ctx.pc = self.code[self.ctx.pc].arg
		else:
			self.ctx.pc += 1

	def op_jne(self):
		if self.ctx.stack[self.ctx.sp] != self.ctx.stack[self.ctx.sp - 1]:
			self.ctx.pc = self.code[self.ctx.pc].arg
		else:
			self.ctx.pc += 1

	def op_jg(self):
		if self.ctx.stack[self.ctx.sp] > self.ctx.stack[self.ctx.sp - 1]:
			self.ctx.pc = self.code[self.ctx.pc].arg
		else:
			self.ctx.pc += 1

	def op_jge(self):
		if self.ctx.stack[self.ctx.sp] >= self.ctx.stack[self.ctx.sp - 1]:
			self.ctx.pc = self.code[self.ctx.pc].arg
		else:
			self.ctx.pc += 1

	def op_jl(self):
		if self.ctx.stack[self.ctx.sp] < self.ctx.stack[self.ctx.sp - 1]:
			self.ctx.pc = self.code[self.ctx.pc].arg
		else:
			self.ctx.pc += 1

	def op_jle(self):
		if self.ctx.stack[self.ctx.sp] <= self.ctx.stack[self.ctx.sp - 1]:
			self.ctx.pc = self.code[self.ctx.pc].arg
		else:
			self.ctx.pc += 1

	def op_jmp(self):
		self.ctx.pc = self.code[self.ctx.pc].arg

	def op_call(self):
		self.ctx.sp += 1
		self.ctx.stack[self.ctx.sp] = (self.ctx.pc + 1, self.ctx.bp)
		self.ctx.bp = self.ctx.sp
		self.ctx.pc = self.code[self.ctx.pc].arg

	def op_ret(self):
		if self.ctx.sp > self.ctx.bp:
			ret_val = self.ctx.stack[self.ctx.sp]
			self.ctx.stack[self.ctx.sp] = self.ctx.stack[self.ctx.sp - 1]
			self.ctx.stack[self.ctx.sp - 1] = ret_val
		self.ctx.pc, self.ctx.bp = self.ctx.stack[self.ctx.sp]
		self.ctx.sp -= 1
		pass

	def op_throw(self):
		pass
	def op_yield(self):
		pass
	def op_await(self):
		pass
	def op_in(self):
		pass
	def op_out(self):
		pass
	def op_int(self):
		self.interrupt_controller.call(self.code[self.ctx.pc].arg)
		self.ctx.pc += 1
	def op_async_call(self):
		pass