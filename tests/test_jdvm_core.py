import unittest

import jdvm

class TestJDVMCore(unittest.TestCase):
	def setUp(self):
		self.vm = jdvm.core.Executor(
			jdvm.core.Context(3, False),
			0,
			None
		)
	def test_add(self):
		self.vm.reset()
		self.vm.load_commands((
			Command(jdvm.assembly.Opcode.PUSH, 2),
			Command(jdvm.assembly.Opcode.PUSH, 24),
			Command(jdvm.assembly.Opcode.ADD),
			Command(jdvm.assembly.Opcode.END)
		))
		self.assertEqual(vm.ctx.stack.peek(), 26)


