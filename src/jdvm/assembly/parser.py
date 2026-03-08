from . import commands, opcodes

class Parser:
	def __init__(self, raw: str):
		self.commands = raw.split('\n')
		self.arg_cast = {
			'#': int,
			'%': float,
			'&': self.decode_label,
			'$': str,
			'!': self._donothing
		}
		self.lbl_map = {}
	
	def _donothing(self, arg):
		return arg

	def map_labels(self) -> None:
		cp = 0
		for command in self.commands:
			opcode, _, arg = command.partition(' ')
			if opcode == "LBL":
				self.lbl_map[arg[1:]] = cp + 1
			cp += 1

	def decode_label(self, label_id) -> int:
		return self.lbl_map[label_id]

	def parse(self) -> tuple[commands.Command]:
		code = []

		self.map_labels()

		for command in self.commands:
			opcode, _, arg = command.partition(' ')
			arg = self.arg_cast[arg[0]](arg[1:]) if arg else None
			code.append(getattr(commands, opcode)(arg))
		return tuple(code)

