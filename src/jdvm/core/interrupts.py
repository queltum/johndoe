from . import context

class Interrupt:
	QUIT = 0
	PRINT = 1
	INPUT = 2

class InterruptController:
	def __init__(self, ctx: context.Context):
		self.ctx = ctx
		self.table = (
			self.int_quit, self.int_print, self.int_input
		)

	def call(self, int_id: int) -> None:
		self.table[int_id]()

	def int_quit(self) -> None:
		self.ctx.running = False
		self.ctx.trapped = True

	def int_print(self) -> None:
		print(self.ctx.stack.peek())
		self.ctx.pc += 1

	def int_input(self) -> None:
		self.ctx.stack.push(input())
		self.ctx.pc += 1
