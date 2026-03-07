jhondoe - is an experimental stack-based platform for learning and experimenting with programming concepts. The ultimate goal is to provide a visual programming interface, where users can drag and drop blocks to create programs.


Project Structure

src/ 
├── gui/
│   ├── todo
├── jdvm/
│   ├── __init__.py          # Main package
│   ├── core/
│   │   ├── __init__.py      # Shortened imports for Executor, Context and Interrupt
│   │   ├── context.py       # VM context definition
│   │   ├── executor.py      # executor
│   │   └── interrupts.py    # InterruptController
│   ├── assembly/
│   │   ├── __init__.py
│   │   ├── opcodes.py       # Opcode
│   │   ├── parser.py        # Parser
│   │   └── commands.py		 # DSL for building commands
└── README.md