import jdvm

vm = jdvm.core.Executor(
	ctx=jdvm.core.Context(
		32,
		False
	),
	entry=0,
	code=jdvm.parser.Parser(
		"REM !hello world program\nPUSH $hello world\nINT #1\nEND"
	).parse()
)

vm.execute()
