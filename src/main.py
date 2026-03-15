import sys
from preprocessor import *
from parser import *
from executor import *

debug = None
stack_sz = 128
_exec = fast_exec

for arg in sys.argv[1:]:
	if arg.startswith("-debug"):
		_exec = debug_exec
	elif arg.startswith("-sz="):
		stack_sz = int(arg.split('=')[1])
	else:
		pass

file = open(sys.argv[-1], "r")

_exec(
	parse(
		preprocess(
			file.read()
		)
	), stack_sz
)

file.close()
