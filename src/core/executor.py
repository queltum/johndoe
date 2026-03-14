def local_exec(il, stack_sz):
	stack = [0] * stack_sz
	sp = -1
	bp = 0
	pc = 0
	
	while True:
		opcode, arg = il[pc]

		match opcode:
			# .add TESTED
			case 0o00:
				sp -= 1
				stack[sp] += stack[sp + 1]
				pc += 1
			# .sub TESTED
			case 0o01:
				sp -= 1
				stack[sp] -= stack[sp + 1]
				pc += 1
			# .mul TESTED
			case 0o02:	
				sp -= 1
				stack[sp] *= stack[sp + 1]
				pc += 1
			# .div TESTED
			case 0o03:
				sp -= 1
				stack[sp] /= stack[sp + 1]
				pc += 1
			# .mod TESTED
			case 0o04:
				sp -= 1
				stack[sp] %= stack[sp + 1]
				pc += 1
			# .pow TESTED
			case 0o05:
				sp -= 1
				stack[sp] **= stack[sp + 1]
				pc += 1
			# .inc TESTED
			case 0o06:
				stack[sp] += 1
				pc += 1
			# .dec TESTED
			case 0o07:
				stack[sp] -= 1
				pc += 1
			# .and TESTED
			case 0o10:
				sp -= 1
				stack[sp] &= stack[sp + 1]
				pc += 1
			# .or TESTED
			case 0o11:
				sp -= 1
				stack[sp] |= stack[sp + 1]
				pc += 1
			# .xor TESTED
			case 0o12:
				sp -= 1
				stack[sp] ^= stack[sp + 1]
				pc += 1
			# .not TESTED
			case 0o13:
				stack[sp] = ~stack[sp]
				pc += 1
			# .lsh TESTED
			case 0o14:
				sp -= 1
				stack[sp] <<= stack[sp + 1]
				pc += 1
			# .rsh TESTED
			case 0o15:
				sp -= 1
				stack[sp] >>= stack[sp + 1]
				pc += 1
			# !bic TESTED
			case 0o16:
				stack[sp] &= ~arg
				pc += 1
			# .neg TESTED
			case 0o17:
				stack[sp] = -stack[sp]
				pc += 1
			# !push TESTED
			case 0o20:
				sp += 1
				stack[sp] = arg
				pc += 1
			# !pop TESTED
			case 0o21:
				sp -= arg
				pc += 1
			# !dup TESTED
			case 0o22:
				sp += 1
				stack[sp] = stack[bp + arg]
				pc += 1
			# !poke TESTED
			case 0o23:
				sp -= 1
				stack[bp + arg] = stack[sp + 1]
				pc += 1
			# !swap TESTED
			case 0o24:
				top = stack[sp]
				stack[sp] = stack[bp + arg]
				stack[bp + arg] = top
				pc += 1
			# !over TESTED
			case 0o25:
				stack[sp + 1 : sp + 1 + arg] = stack[bp - arg : bp]
				sp += arg
				pc += 1
			# .dump TESTED
			case 0o26:
				pc += 1
			# .breakpoint TESTED
			case 0o27:
				pc += 1
			# !je
			case 0o30:
				if stack[sp - 1] == stack[sp]:
					pc = arg
				else:
					pc += 1
			# !jne
			case 0o31:
				if stack[sp - 1] != stack[sp]:
					pc = arg
				else:
					pc += 1
			# !jg
			case 0o32:
				if stack[sp - 1] > stack[sp]:
					pc = arg
				else:
					pc += 1
			# !jge
			case 0o33:
				if stack[sp - 1] >= stack[sp]:
					pc = arg
				else:
					pc += 1
			# !jl
			case 0o34:
				if stack[sp - 1] < stack[sp]:
					pc = arg
				else:
					pc += 1
			# !jle
			case 0o35:
				if stack[sp - 1] <= stack[sp]:
					pc = arg
				else:
					pc += 1
			# !jmp TESTED
			case 0o36:
				pc = arg
			# .goto
			case 0o37:
				pc = stack[sp]
			# !jez
			case 0o40:
				if not stack[sp - 1]:
					pc = arg
				else:
					pc += 1
			# !jnez
			case 0o41:
				if stack[sp - 1]:
					pc = arg
				else:
					pc += 1
			# !jgz
			case 0o42:
				if stack[sp - 1] > 0:
					pc = arg
				else:
					pc += 1
			# !jgez
			case 0o43:
				if stack[sp - 1] >= 0:
					pc = arg
				else:
					pc += 1
			# !jlz
			case 0o44:
				if stack[sp - 1] < 0:
					pc = arg
				else:
					pc += 1
			# !jlez
			case 0o45:
				if stack[sp - 1] <= 0:
					pc = arg
				else:
					pc += 1
			# !repeat
			case 0o46:
				prev_opcode, prev_arg = il[pc - 1]
				
				match prev_opcode:
					# !repeat .add
					case 0o00:
						tmp = sp - arg
						stack[tmp] = sum(stack[tmp : sp])
						sp = tmp
					# .sub
					case 0o01:
						while arg:
							sp -= 1
							stack[sp] *= stack[sp + 1]
							arg -= 1

					# !repeat .mul
					case 0o02:
						while arg:
							sp -= 1
							stack[sp] *= stack[sp + 1]
							arg -= 1 
					# !repeat .div
					case 0o03:
						while arg:
							sp -= 1
							stack[sp] /= stack[sp + 1]
							arg -= 1
					# !repeat .mod
					case 0o04:
						while arg:
							sp -= 1
							stack[sp] %= stack[sp + 1]
							arg -= 1 
					# !repeat .pow
					case 0o05:
						while arg:
							sp -= 1
							stack[sp] **= stack[sp + 1]
							arg -= 1
					# !repeat .inc
					case 0o06:
						stack[sp] += arg
					# !repeat .dec
					case 0o07:
						stack[sp] -= arg
					# !repeat .and
					case 0o10:
						while arg:
							sp -= 1
							stack[sp] &= stack[sp + 1]
							arg -= 1
					# !repeat .or
					case 0o11:
						while arg:
							sp -= 1
							stack[sp] |= stack[sp + 1]
							arg -= 1
					# !repeat .xor
					case 0o12:
						while arg:
							sp -= 1
							stack[sp] ^= stack[sp + 1]
							arg -= 1
					# !repeat .not
					case 0o13:
						if arg % 2:
							stack[sp] = ~stack[sp]
					# !repeat .lsh
					case 0o14:
						while arg:
							sp -= 1
							stack[sp] <<= stack[sp + 1]
							arg -= 1
					# !repeat .rsh
					case 0o15:
						while arg:
							sp -= 1
							stack[sp] >>= stack[sp + 1]
							arg -= 1
					# !repeat !bic
					case 0o16:
						stack[sp] &= ~prev_arg
					# !repeat .neg
					case 0o17:
						if arg % 2:
							stack[sp] = ~stack[sp] + 1
					# !repeat !push
					case 0o20:
						stack[sp + 1 : sp + 1 + arg] = [prev_arg] * arg
						sp += arg
					# !repeat !pop
					case 0o21:
						sp -= (prev_arg * arg)
					# !repeat !dup
					case 0o22:
						stack[sp + 1 : sp + 1 + arg] = [stack[bp + prev_arg]] * arg
						sp += arg
					# !repeat !poke
					case 0o23:
						sp -= arg
						stack[bp + prev_arg] = stack[sp + 1]
					# !repeat !swap
					case 0o24:
						if arg % 2:
							top = stack[sp]
							stack[sp] = stack[bp + prev_arg]
							stack[bp + prev_arg] = top
					# !repeat !over
					case 0o25:
						_vars = [*stack[bp - prev_arg : bp]] * arg
						stack[sp + 1 : sp + 1 + prev_arg * arg] = _vars
						sp += prev_arg * arg
				pc += 1
			# .end TESTED
			case 0o47:
				return
			# !call TESTED
			case 0o50:
				sp += 1
				stack[sp] = pc + 1, bp
				pc, bp = arg, sp
			# .invoke
			case 0o51:
				pc += 1
			# !acall
			case 0o52:
				pc += 1
			# !await
			case 0o53:
				pc += 1
			# .ret0 TESTED
			case 0o54:
				pc, bp = stack[sp]
				sp -= 1
			# .ret1 TESTED
			case 0o55:
				pc, bp = stack[bp]
				sp -= 1
				stack[sp] = stack[sp + 1]
			# .ret2
			case 0o56:
				pc, bp = stack[bp]
				stack[bp] = stack[sp - 1]
				stack[sp - 1] = stack[sp]
				sp -= 1
			# .retn
			case 0o57:
				tmp = stack[bp]
				ret_val = stack[bp + 1 : sp + 1]
				sp -= 1
				stack[bp : sp] = ret_val
				pc, bp = tmp
			# !int TESTED
			case 0o60:
				print(stack[sp])
				pc += 1
			case _:
				print(f"jdvm_warn: unknown opcode {opcode}")
				pc += 1

def local_tracing_exec(il, stack_sz):
	stack = [0] * stack_sz
	tracing = False
	sp = -1
	bp = 0
	pc = 0
	
	while True:
		opcode, arg = il[pc]

		match opcode:
			# .add
			case 0o00:
				sp -= 1
				stack[sp] += stack[sp + 1]
				pc += 1
			# .sub
			case 0o01:
				sp -= 1
				stack[sp] -= stack[sp + 1]
				pc += 1
			# .mul
			case 0o02:	
				sp -= 1
				stack[sp] *= stack[sp + 1]
				pc += 1
			# .div
			case 0o03:
				sp -= 1
				stack[sp] /= stack[sp + 1]
				pc += 1
			# .mod
			case 0o04:
				sp -= 1
				stack[sp] %= stack[sp + 1]
				pc += 1
			# .pow
			case 0o05:
				sp -= 1
				stack[sp] **= stack[sp + 1]
				pc += 1
			# .inc
			case 0o06:
				stack[sp] += 1
				pc += 1
			# .dec
			case 0o07:
				stack[sp] -= 1
				pc += 1
			# .and
			case 0o10:
				sp -= 1
				stack[sp] &= stack[sp + 1]
				pc += 1
			# .or
			case 0o11:
				sp -= 1
				stack[sp] |= stack[sp + 1]
				pc += 1
			# .xor
			case 0o12:
				sp -= 1
				stack[sp] ^= stack[sp + 1]
				pc += 1
			# .not
			case 0o13:
				stack[sp] = ~stack[sp]
				pc += 1
			# .lsh
			case 0o14:
				sp -= 1
				stack[sp] <<= stack[sp + 1]
				pc += 1
			# .rsh
			case 0o15:
				sp -= 1
				stack[sp] >>= stack[sp + 1]
				pc += 1
			# !bic
			case 0o16:
				stack[sp] &= ~arg
				pc += 1
			# .neg
			case 0o17:
				stack[sp] = -stack[sp + 1]
				pc += 1
			# !push
			case 0o20:
				sp += 1
				stack[sp] = arg
				pc += 1
			# !pop
			case 0o21:
				sp -= arg
				pc += 1
			# !dup
			case 0o22:
				sp += 1
				stack[sp] = stack[bp + arg]
				pc += 1
			# !poke
			case 0o23:
				sp -= 1
				stack[bp + arg] = stack[sp + 1]
				pc += 1
			# !swap
			case 0o24:
				top = stack[sp]
				stack[sp] = stack[bp + arg]
				stack[bp + arg] = top
				pc += 1
			# !over
			case 0o25:
				stack[sp + 1 : sp + 1 + arg] = stack[bp - arg : bp]
				sp += arg
				pc += 1
			# .dump
			case 0o26:
				print(f"jdmv_dump: sp={sp}, bp={bp}, pc={pc}, [sp]={stack[sp]}")
				pc += 1
			# .breakpoint
			case 0o27:
				tracing = True
				pc += 1
			# !je
			case 0o30:
				if stack[sp - 1] == stack[sp]:
					pc = arg
				else:
					pc += 1
			# !jne
			case 0o31:
				if stack[sp - 1] != stack[sp]:
					pc = arg
				else:
					pc += 1
			# !jg
			case 0o32:
				if stack[sp - 1] > stack[sp]:
					pc = arg
				else:
					pc += 1
			# !jge
			case 0o33:
				if stack[sp - 1] >= stack[sp]:
					pc = arg
				else:
					pc += 1
			# !jl
			case 0o34:
				if stack[sp - 1] < stack[sp]:
					pc = arg
				else:
					pc += 1
			# !jle
			case 0o35:
				if stack[sp - 1] <= stack[sp]:
					pc = arg
				else:
					pc += 1
			# !jmp
			case 0o36:
				pc = arg
			# .goto
			case 0o37:
				pc = stack[sp]
			# !jez
			case 0o40:
				if not stack[sp - 1]:
					pc = arg
				else:
					pc += 1
			# !jnez
			case 0o41:
				if stack[sp - 1]:
					pc = arg
				else:
					pc += 1
			# !jgz
			case 0o42:
				if stack[sp - 1] > 0:
					pc = arg
				else:
					pc += 1
			# !jgez
			case 0o43:
				if stack[sp - 1] >= 0:
					pc = arg
				else:
					pc += 1
			# !jlz
			case 0o44:
				if stack[sp - 1] < 0:
					pc = arg
				else:
					pc += 1
			# !jlez
			case 0o45:
				if stack[sp - 1] <= 0:
					pc = arg
				else:
					pc += 1
			# !repeat
			case 0o46:
				prev_opcode, prev_arg = il[pc - 1]
				
				match prev_opcode:
					# !repeat .add
					case 0o00:
						tmp = sp - arg
						stack[tmp] = sum(stack[tmp : sp])
						sp = tmp
					# .sub
					case 0o01:
						while arg:
							sp -= 1
							stack[sp] *= stack[sp + 1]
							arg -= 1

					# !repeat .mul
					case 0o02:
						while arg:
							sp -= 1
							stack[sp] *= stack[sp + 1]
							arg -= 1 
					# !repeat .div
					case 0o03:
						while arg:
							sp -= 1
							stack[sp] /= stack[sp + 1]
							arg -= 1
					# !repeat .mod
					case 0o04:
						while arg:
							sp -= 1
							stack[sp] %= stack[sp + 1]
							arg -= 1 
					# !repeat .pow
					case 0o05:
						while arg:
							sp -= 1
							stack[sp] **= stack[sp + 1]
							arg -= 1
					# !repeat .inc
					case 0o06:
						stack[sp] += arg
					# !repeat .dec
					case 0o07:
						stack[sp] -= arg
					# !repeat .and
					case 0o10:
						while arg:
							sp -= 1
							stack[sp] &= stack[sp + 1]
							arg -= 1
					# !repeat .or
					case 0o11:
						while arg:
							sp -= 1
							stack[sp] |= stack[sp + 1]
							arg -= 1
					# !repeat .xor
					case 0o12:
						while arg:
							sp -= 1
							stack[sp] ^= stack[sp + 1]
							arg -= 1
					# !repeat .not
					case 0o13:
						if arg % 2:
							stack[sp] = ~stack[sp]
					# !repeat .lsh
					case 0o14:
						while arg:
							sp -= 1
							stack[sp] <<= stack[sp + 1]
							arg -= 1
					# !repeat .rsh
					case 0o15:
						while arg:
							sp -= 1
							stack[sp] >>= stack[sp + 1]
							arg -= 1
					# !repeat !bic
					case 0o16:
						stack[sp] &= ~prev_arg
					# !repeat .neg
					case 0o17:
						if arg % 2:
							stack[sp] = ~stack[sp] + 1
					# !repeat !push
					case 0o20:
						stack[sp + 1 : sp + 1 + arg] = [prev_arg] * arg
						sp += arg
					# !repeat !pop
					case 0o21:
						sp -= (prev_arg * arg)
					# !repeat !dup
					case 0o22:
						stack[sp + 1 : sp + 1 + arg] = [stack[bp + prev_arg]] * arg
						sp += arg
					# !repeat !poke
					case 0o23:
						sp -= arg
						stack[bp + prev_arg] = stack[sp + 1]
					# !repeat !swap
					case 0o24:
						if arg % 2:
							top = stack[sp]
							stack[sp] = stack[bp + prev_arg]
							stack[bp + prev_arg] = top
					# !repeat !over
					case 0o25:
						_vars = [*stack[bp - prev_arg : bp]] * arg
						stack[sp + 1 : sp + 1 + prev_arg * arg] = _vars
						sp += prev_arg * arg
				pc += 1
			# .end
			case 0o47:
				return
			# !call
			case 0o50:
				sp += 1
				stack[sp] = pc + 1, bp
				pc, bp = arg, sp
			# .invoke
			case 0o51:
				pc += 1
			# !acall
			case 0o52:
				pc += 1
			# !await
			case 0o53:
				pc += 1
			# .ret0
			case 0o54:
				pc, bp = stack[sp]
				sp -= 1
			# .ret1
			case 0o55:
				pc, bp = stack[bp]
				sp -= 1
				stack[sp] = stack[sp + 1]
			# .ret2
			case 0o56:
				pc, bp = stack[bp]
				stack[bp] = stack[sp - 1]
				stack[sp - 1] = stack[sp]
				sp -= 1
			# .retn
			case 0o57:
				tmp = stack[bp]
				ret_val = stack[bp + 1 : sp + 1]
				sp -= 1
				stack[bp : sp] = ret_val
				pc, bp = tmp
			# !int
			case 0o60:
				print(stack[sp])
				pc += 1
			case _:
				print(f"jdvm_warn: unknown opcode {opcode}")
				pc += 1
		if tracing:
			input(f"jdvm_dump: sp={sp}, bp={bp}, pc={pc}, [sp]={stack[sp]}")
