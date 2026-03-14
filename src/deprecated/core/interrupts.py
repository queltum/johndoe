from . import context

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
		pass

	def int_input(self) -> None:
		self.ctx.sp += 1
		self.ctx.stack[self.ctx.sp] = input()
