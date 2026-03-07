import jdvm

vm = jdvm.core.Executor(
	jdvm.core.Context(
		32,
		False
	),
	0,
	(
		jdvm.commands.PUSH(128),
		jdvm.commands.PUSH(128),
		jdvm.commands.CALL(5),
		jdvm.commands.INT(jdvm.Interrupt.PRINT),
		jdvm.commands.END(),
		jdvm.commands.DUP(-1),
		jdvm.commands.DUP(-2),
		jdvm.commands.ADD(),
		jdvm.commands.RET(),
	)
)

vm.execute()