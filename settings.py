#
#   #   
#   #   # ECE350 Processor Autograder
#   #   # Code adapted from ECE250 Homework 4 Assignment  (nc)
#   #
#

# ======= GENERAL SETTINGS: Adapt these per assignment =============
ASSIGNMENT = "Duke ECE/CS 350 Processor"
SEMESTER = "Spring 2020"
TEST_DIR = 'tests' # where test files are located
IS_GRADER = False # if true, we'll expect to see a 'points' parameter in test setup

SPIM_BINARY = 'spim' # location of spim executable (or just 'spim' if in path); only needed if mode is SPIM
LOGISIM_JAR = 'logisim_cli.jar' # location of logisim_cli.jar; only needed if mode is LOGISIM

# modes: 
#   EXECUTABLE - for C programs, etc.
#   SPIM       - run with command line spim
#   LOGISIM    - run with logisim command-line front-end
MODE = 'LOGISIM'

NON_ZERO_EXIT_STATUS_PENALTY = 0.75 # multiply score by this if exit status is non-zero
VALGRIND_PENALTY = 0.5 # multiply score by this if a valgrind test showed a leak

# ============= TEST SETUP ========================
force_suite_filename = 'processor.circ'
suite_names = ['math', 'memory', 'compare', 'misc'] # 'arithmetic_1', 'arithmetic_2', 'control_1', 'control_2']
suites = {
    "math": [
        { "desc": "math instructions",                                    "args": ['-c 20   -lo tests/math.imem.lgsim -la tests/math.dmem.lgsim'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
    "memory": [
        { "desc": "memory instructions",                                  "args": ['-c 20   -lo tests/memory.imem.lgsim -la tests/memory.dmem.lgsim'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
    "compare": [
        { "desc": "memory instructions",                                  "args": ['-c 20   -lo tests/compare.imem.lgsim -la tests/compare.dmem.lgsim'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
    "misc": [
        { "desc": "misc instructions",                                    "args": ['-c 20   -lo tests/misc.imem.lgsim -la tests/misc.dmem.lgsim'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
}

'''
"arithmetic_1": [
        { "desc": "arithmetic instructions, full bypass",                 "args": ['-c 50   -lo tests/arithmetic_1.imem.lgsim -la tests/arithmetic_1.dmem.lgsim'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
    "arithmetic_2": [   
        { "desc": "arithmetic instructions, no bypass",                   "args": ['-c 100  -lo tests/arithmetic_2.imem.lgsim -la tests/arithmetic_2.dmem.lgsim'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
    "control_1": [
        { "desc": "control, full bypass",                                 "args": ['-c 500 -lo tests/control_1.imem.lgsim -la tests/control_1.dmem.lgsim'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
    "control_2": [
        { "desc": "control, no bypass",                                   "args": ['-c 500   -lo tests/control_2.imem.lgsim -la tests/control_2.dmem.lgsim'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
'''

'''
suite_names = ['simple', 'boolean', 'arithmetic', 'shift', 'memory', 'control', 'io' ]
suites = {
    "simple": [
        { "desc": "addi basics",                       "args": ['-c 1000 -ic 1,reset=1:2,reset=0 -lo tests/simple.imem.lgsim -la tests/simple.dmem.lgsim'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
    "boolean": [
        { "desc": "not, xor instrctions",              "args": ['-c 10 -ic 1,reset=1:2,reset=0 -lo tests/boolean.imem.lgsim -la tests/boolean.dmem.lgsim'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
    "arithmetic": [
        { "desc": "addi, add, sub instructions",       "args": ['-c 10 -ic 1,reset=1:2,reset=0 -lo tests/arithmetic.imem.lgsim -la tests/arithmetic.dmem.lgsim'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
    "shift": [
        { "desc": "sll, srl instructions",             "args": ['-c 10 -ic 1,reset=1:2,reset=0 -lo tests/shift.imem.lgsim -la tests/shift.dmem.lgsim'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
    "memory": [
        { "desc": "lw, sw instructions",               "args": ['-c 20 -ic 1,reset=1:2,reset=0 -lo tests/memory.imem.lgsim -la tests/memory.dmem.lgsim'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
    "control": [
        { "desc": "blt, bne, jal, j, jr instructions", "args": ['-c 12 -ic 1,reset=1:2,reset=0 -lo tests/control.imem.lgsim -la tests/control.dmem.lgsim'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
    "io": [
        { "desc": "input, output instructions",        "args": ['-lo tests/io.imem.lgsim -la tests/io.dmem.lgsim -lk tests/io.buffer -c 20 -tty full'], 'command_append': "| grep -E -v '(probe         |/ )'" },
    ],
}
'''
