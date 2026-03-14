class Context:

	class Clock:

		def __init__(self):
			self._clock = 0

		def tick(self) -> None:
			self._clock += 1

		def now(self) -> int:
			return self._clock

	def __init__(self, stack_size: int, tracing: bool):
		self.clock = Context.Clock()
		self.stack_size = stack_size
		self.stack = [0] * stack_size
		self.pc = 0
		self.sp = -1
		self.bp = 0
		self.running = False
		self.waiting = False
		self.tracing = tracing
		self.trapped = False
