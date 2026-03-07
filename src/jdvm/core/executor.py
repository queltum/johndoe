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
			self.op_lsh, self.op_rsh, self.op_set, self.op_reset,
			self.op_push, self.op_pop, self.op_dup, self.op_swap,
			self.op_rem, self.op_lbl, self.op_bpt, self.op_end,
			self.op_je, self.op_jne, self.op_jg, self.op_jge,
			self.op_jl, self.op_jle, self.op_jmp, self.op_call,
			self.op_ret, self.op_throw, self.op_yield, self.op_await,
			self.op_in, self.op_out, self.op_int, self.op_async_call
		)

	def reset(self) -> None:
		self.ctx.stack.sp = -1
		self.ctx.stack.bp = -1
		self.ctx.pc = self.entry
		self.ctx.running = False

	def load_commands(self, code: tuple) -> None:
		self.code = code

	def execute(self) -> None:
		self.ctx.running = True
		
		while self.ctx.running == True:
			self.dispatch[self.code[self.ctx.pc].opcode]()

	def op_add(self) -> None:
		self.ctx.stack.push(self.ctx.stack.pop() + self.ctx.stack.pop())
		self.ctx.pc += 1
	def op_sub(self) -> None:
		self.ctx.stack.push(self.ctx.stack.pop() - self.ctx.stack.pop())
		self.ctx.pc += 1
	
	def op_mul(self) -> None:
		self.ctx.stack.push(self.ctx.stack.pop() * self.ctx.stack.pop())
		self.ctx.pc += 1

	def op_div(self) -> None:
		self.ctx.stack.push(self.ctx.stack.pop() / self.ctx.stack.pop())
		self.ctx.pc += 1

	def op_inc(self) -> None:
		self.ctx.stack._stack[self.ctx.stack.sp] += 1
		self.ctx.pc += 1

	def op_dec(self) -> None:
		self.ctx.stack._stack[self.ctx.stack.sp] -= 1
		self.ctx.pc += 1

	def op_mod(self) -> None:
		self.ctx.pc += 1

	def op_pow(self) -> None:
		self.ctx.pc += 1

	def op_and(self) -> None:
		self.ctx.stack.push(self.ctx.stack.pop() & self.ctx.stack.pop())
		self.ctx.pc += 1

	def op_or(self) -> None:
		self.ctx.stack.push(self.ctx.stack.pop() | self.ctx.stack.pop())
		self.ctx.pc += 1

	def op_xor(self) -> None:
		self.ctx.stack.push(self.ctx.stack.pop() ^ self.ctx.stack.pop())
		self.ctx.pc += 1

	def op_not(self) -> None:
		self.ctx.stack._stack[self.ctx.stack.sp] = ~self.ctx.stack._stack[self.ctx.stack.sp]
		self.ctx.pc += 1

	def op_lsh(self) -> None:
		self.ctx.pc += 1

	def op_rsh(self) -> None:
		self.ctx.pc += 1

	def op_set(self) -> None:
		self.ctx.pc += 1

	def op_reset(self) -> None:
		self.ctx.pc += 1

	def op_push(self) -> None:
		self.ctx.stack.push(self.code[self.ctx.pc].arg)
		self.ctx.pc += 1

	def op_pop(self) -> None:
		self.ctx.stack.pop()
		self.ctx.pc += 1

	def op_dup(self) -> None:
		self.ctx.stack.push(
			self.ctx.stack._stack[
				self.ctx.stack.bp + self.code[self.ctx.pc].arg
			]
		)
		self.ctx.pc += 1

	def op_swap(self) -> None:
		offset = self.ctx.stack.bp - self.code[self.ctx.pc].arg
		tmp = self.ctx.stack._stack[offset]
		self.ctx.stack._stack[offset] = self.ctx.stack._stack[self.ctx.stack.sp]
		self.ctx.stack._stack[self.ctx.stack.sp] = tmp
		self.ctx.pc += 1

	def op_rem(self) -> None:
		self.ctx.pc += 1

	def op_lbl(self) -> None:
		self.ctx.pc += 1

	def op_bpt(self) -> None:
		self.ctx.pc += 1

	def op_end(self) -> None:
		self.ctx.running = False
		self.ctx.pc += 1

	def op_je(self) -> None:
		if self.ctx.stack._stack[self.ctx.stack.sp] == self.ctx.stack._stack[self.ctx.stack.sp - 1]:
			self.ctx.pc = self.code[self.ctx.pc].arg
		else:
			self.ctx.pc += 1

	def op_jne(self) -> None:
		if self.ctx.stack._stack[self.ctx.stack.sp] != self.ctx.stack._stack[self.ctx.stack.sp - 1]:
			self.ctx.pc = self.code[self.ctx.pc].arg
		else:
			self.ctx.pc += 1

	def op_jg(self) -> None:
		if self.ctx.stack._stack[self.ctx.stack.sp] > self.ctx.stack._stack[self.ctx.stack.sp - 1]:
			self.ctx.pc = self.code[self.ctx.pc].arg
		else:
			self.ctx.pc += 1

	def op_jge(self) -> None:
		if self.ctx.stack._stack[self.ctx.stack.sp] >= self.ctx.stack._stack[self.ctx.stack.sp - 1]:
			self.ctx.pc = self.code[self.ctx.pc].arg
		else:
			self.ctx.pc += 1

	def op_jl(self) -> None:
		if self.ctx.stack._stack[self.ctx.stack.sp] < self.ctx.stack._stack[self.ctx.stack.sp - 1]:
			self.ctx.pc = self.code[self.ctx.pc].arg
		else:
			self.ctx.pc += 1

	def op_jle(self) -> None:
		if self.ctx.stack._stack[self.ctx.stack.sp] <= self.ctx.stack._stack[self.ctx.stack.sp - 1]:
			self.ctx.pc = self.code[self.ctx.pc].arg
		else:
			self.ctx.pc += 1

	def op_jmp(self) -> None:
		self.ctx.pc = self.code[self.ctx.pc].arg

	def op_call(self) -> None:
		self.ctx.stack.push((self.ctx.pc + 1, self.ctx.stack.bp))
		self.ctx.stack.bp = self.ctx.stack.sp
		self.ctx.pc = self.code[self.ctx.pc].arg

	def op_ret(self) -> None:
		if self.ctx.stack.sp > self.ctx.stack.bp:
			ret_val = self.ctx.stack._stack[self.ctx.stack.sp]
			self.ctx.stack._stack[self.ctx.stack.sp] = self.ctx.stack._stack[self.ctx.stack.sp - 1]
			self.ctx.stack._stack[self.ctx.stack.sp - 1] = ret_val
		self.ctx.pc, self.ctx.stack.bp = self.ctx.stack.pop()

	def op_throw(self) -> None:
		pass
	def op_yield(self) -> None:
		pass
	def op_await(self) -> None:
		pass
	def op_in(self) -> None:
		pass
	def op_out(self) -> None:
		pass
	def op_int(self) -> None:
		self.interrupt_controller.call(self.code[self.ctx.pc].arg)
	def op_async_call(self) -> None:
		pass