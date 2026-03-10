def preprocess(raw):
	cmdp = 0
	cmds = raw.split('\n')
	macro_cnt = 0
	map_lbl = {}
	set_jmp = {
		"jmp", "call", "je", "jne", 
		"jg", "jge", "jl", "jle"
	}

	for cmd in cmds:
		if cmd[0] == '.':
			if cmd.startswith(".noprep"):
				break
			if cmd.startswith(".lbl"):
				lbl_id = cmd[5:]
				map_lbl[lbl_id] = cmdp - macro_cnt
			macro_cnt += 1
		cmdp += 1

	prog = [None] * (cmdp - macro_cnt)
	cmdp = 0

	for cmd in cmds:
		if cmd[0] == '.':
			continue
		op, _, arg = cmd.partition(' ')
		if op in set_jmp:
			arg = map_lbl[arg]
		prog[cmdp] = (op, arg)
		cmdp += 1
	return tuple(prog)
