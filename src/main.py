import jdvm.preprocessor
import jdvm.executor

file = open(r"./test_programs/add_func.jda", "r")

program = jdvm.preprocessor.preprocess(file.read())
print(program)

jdvm.executor.execute(program)

