import jdvm

file = open(r"./test_programs/stack_test.jda", "r")

vm = jdvm.core.Executor(
	ctx=jdvm.core.Context(
		32,
		False
	),
	entry=0,
	code=jdvm.parser.Parser(
		file.read()
	).parse()
)

vm.execute()
