import sys
import asm
import core

VERSION = "0x0001"

debug = None
stack_sz = None

# EXECUTORS = {
# 	(False, False): local_exec,
# 	(False, True): local_static_exec,
# 	(True, False): local_tracing_exec,
# 	(True, True): local_trancing_static_exec
# }
core.local_exec(
	asm.parse(
		asm.preprocess(
			open("../test_programs/hello_world.jda", "r").read()
		)
	), 128
)

# for arg in sys.argv[1]:
# 	if arg.startswith("-debug"):
# 		debug = True
# 	elif arg.startswith("-sz="):
# 		stack_sz = int(arg.split('=')[1])
# 	elif arg.startswith("-version") or arg.startswith("-v"):
# 		print(f"harpie virtual machine version {VERSION}")
# 		break
