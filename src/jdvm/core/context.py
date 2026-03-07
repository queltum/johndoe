class StackOverflowError(Exception):
	def __init__(self, limit: int):
		super().__init__(f"stack size exceeds limit {limit}")

class _Clock:
	def __init__(self):
		self._clock = 0

	def tick(self) -> None:
		self._clock += 1

	def now(self) -> int:
		return self._clock
		
class _Stack:
	def __init__(self, size: int):
		self.size = size
		self._stack = [0] * self.size
		self.sp = -1
		self.bp = 0

	def isempty(self) -> bool:
		return self.sp < 0

	def isfull(self) -> bool:
		return self.sp >= self.size

	def push(self, obj) -> None:
		if self.isfull():
			raise StackOverflowError(self.size)
		self.sp += 1
		self._stack[self.sp] = obj

	def pop(self) -> any:
		if self.isempty():
			return None
		self.sp -= 1
		return self._stack[self.sp + 1]

	def peek(self) -> any:
		return self._stack[self.sp]

class Context:
	def __init__(
		self, 
		stack_size: int, 
		tracing: bool, 
	):
		self.clock = _Clock()
		self.stack = _Stack(stack_size)
		self.pc = -1
		self.running = False
		self.waiting = False
		self.tracing = False
		self.trapped = False

	def get_state(self) -> str:
		return '\n'.join([
			"jdvm_state:",
			f">\tsp={self.stack.sp}",
			f">\tbp={self.stack.bp}",
			f">\tpc={self.pc}",
			f">\trunning={self.running}",
			f">\ttrapped={self.trapped}",
			"\n"
		])
