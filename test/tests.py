# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).

# tests = [ {'description': 'This test will run first.',
#    'steps': [ {'inputs': [('PINA',<val>)], 'iterations': 1 } ],
#    'expected': [('PORT',<val>)],
#    },
#    {'description': 'This test will run second.',
#    'steps': [ {'inputs': [('PIN', <val>)],'iterations': 1}, # Set PIN to val then run one iteration
#        {'inputs': [('PIN',<val>)], 'time': 300 }, # Set PIN to val then run 300 ms
#        {'inputs': [('PIN',<val>)], 'iterations': 1, 'expected': [('PORT',<val>)]}, 
#        {'inputs': [('PIN',<val>)], 'time': 600}, ],
#    'expected': [('PORT',<val>)],
#    },
#    ]

tests = [

# #0 0 0 
#     {'description': 'PINA: 0x00 PINB: 0x00 PINC: 0x00 => PORTD: 0x00',
#     'steps': [ {'inputs': [('PINA',0x00),('PINB',0x00),('PINC',0x00)], 'iterations': 5 } ],
#     'expected': [('PORTD',0x00)],
#     },
# #0 0 255
#     {'description': 'PINA: 0x00 PINB: 0x00 PINC: 0xFF => PORTD: 0xFF',
#     'steps': [ {'inputs': [('PINA',0x00),('PINB',0x00),('PINC',0xFF)], 'iterations': 5 } ],
#     'expected': [('PORTD',0xFF)],
#     },
# #0 255 0
#     {'description': 'PINA: 0x00 PINB: 0xFF PINC: 0x00 => PORTD: 0xFD',
#     'steps': [ {'inputs': [('PINA',0x00),('PINB',0xFF),('PINC',0x00)], 'iterations': 5 } ],
#     'expected': [('PORTD',0xFD)],
#     },
# #0 255 255
#     {'description': 'PINA: 0x00 PINB: 0xFF PINC: 0xFF => PORTD: 0xFF',
#     'steps': [ {'inputs': [('PINA',0x00),('PINB',0xFF),('PINC',0xFF)], 'iterations': 5 } ],
#     'expected': [('PORTD',0xFF)],
#     },
# #255 0 0
#     {'description': 'PINA: 0xFF PINB: 0x00 PINC: 0x00 => PORTD: 0xFF',
#     'steps': [ {'inputs': [('PINA',0xFF),('PINB',0x00),('PINC',0x00)], 'iterations': 5 } ],
#     'expected': [('PORTD',0xFF)],
#     },
# #255 255 0
#     {'description': 'PINA: 0xFF PINB: 0xFF PINC: 0x00 => PORTD: 0xFF',
#     'steps': [ {'inputs': [('PINA',0xFF),('PINB',0xFF),('PINC',0x00)], 'iterations': 5 } ],
#     'expected': [('PORTD',0xFF)],
#     },
# #255 255 255
#     {'description': 'PINA: 0xFF PINB: 0xFF PINC: 0xFF => PORTD: 0xBD',
#     'steps': [ {'inputs': [('PINA',0xFF),('PINB',0xFF),('PINC',0xFF)], 'iterations': 5 } ],
#     'expected': [('PORTD',0xBD)],
#     },

# #sum in more than 6 bits (m = max test, b = balance test)
# #m b 150 100 50 
#     {'description': 'PINA: 0x96 (150) PINB: 0x64 (100) PINC: 0x32 (50) => PORTD: 0x97',
#     'steps': [ {'inputs': [('PINA',0x96),('PINB',0x64),('PINC',0x32)], 'iterations': 5 } ],
#     'expected': [('PORTD',0x97)],
#     },

# #m !b 100 50 150
#     {'description': 'PINA: 0x64 (100) PINB: 0x32 (50) PINC: 0x96 (150) => PORTD: 0x95',
#     'steps': [ {'inputs': [('PINA',0x64),('PINB',0x32),('PINC',0x96)], 'iterations': 5 } ],
#     'expected': [('PORTD',0x95)],
#     },
# #!m b 110 10 10 
#     {'description': 'PINA: 0x6E (110) PINB: 0x0A (10) PINC: 0x0A (10) => PORTD: 0x82',
#     'steps': [ {'inputs': [('PINA',0x6E),('PINB',0x0A),('PINC',0x0A)], 'iterations': 5 } ],
#     'expected': [('PORTD',0x82)],
#     },

# #!m !b 50 30 50
#     {'description': 'PINA: 0x32 (50) PINB: 0x1E (30) PINC: 0x32 (50) => PORTD: 0x80',
#     'steps': [ {'inputs': [('PINA',0x32),('PINB',0x1E),('PINC',0x32)], 'iterations': 5 } ],
#     'expected': [('PORTD',0x80)],
#     },

# #sum in 6 bits (kg <= 63) (m = max bit, b = balance bit)
# #!m !b : 6 7 8 
#     {'description': 'PINA: 0x06 PINB: 0x07 PINC: 0x08 => PORTD: 0x54',
#     'steps': [ {'inputs': [('PINA',0x06),('PINB',0x07),('PINC',0x08)], 'iterations': 5 } ],
#     'expected': [('PORTD',0x54)],
#     },
# #140 exactly 46 48 46 
#     {'description': 'PINA: 0x2E (46) PINB: 0x30 (48) PINC: 0x2E (46) => PORTD: 0x8C',
#     'steps': [ {'inputs': [('PINA',0x2E),('PINB',0x30),('PINC',0x2E)], 'iterations': 5 } ],
#     'expected': [('PORTD',0x8C)],
#     },

# #80 exactly 8 80 88
#     {'description': 'PINA: 0x08 PINB: 0x50 (80) PINC: 0x58 (88) => PORTD: 0xB1',
#     'steps': [ {'inputs': [('PINA',0x08),('PINB',0x50),('PINC',0x58)], 'iterations': 5 } ],
#     'expected': [('PORTD',0xB1)],
#     },

#assuming sum weight can be represented in 8 bits
#000
    {'description': 'PINA: 0x00 PINB: 0x00 PINC: 0x00 => PORTD: 0x00',
     'steps': [ {'inputs': [('PINA',0x00),('PINB',0x00),('PINC',0x00)], 'iterations': 5 } ],
     'expected': [('PORTD',0x00)],
    },
#007
    {'description': 'PINA: 0x00 PINB: 0x00 PINC: 0x07 => PORTD: 0x00',
     'steps': [ {'inputs': [('PINA',0x00),('PINB',0x00),('PINC',0x07)], 'iterations': 5 } ],
     'expected': [('PORTD',0x00)],
    },
#070
    {'description': 'PINA: 0x00 PINB: 0x07 PINC: 0x00 => PORTD: 0x00',
     'steps': [ {'inputs': [('PINA',0x00),('PINB',0x07),('PINC',0x00)], 'iterations': 5 } ],
     'expected': [('PORTD',0x00)],
    },
#077
    {'description': 'PINA: 0x00 PINB: 0x07 PINC: 0x07 => PORTD: 0x00',
     'steps': [ {'inputs': [('PINA',0x00),('PINB',0x07),('PINC',0x07)], 'iterations': 5 } ],
     'expected': [('PORTD',0x00)],
    },
#700
    {'description': 'PINA: 0x07 PINB: 0x00 PINC: 0x00 => PORTD: 0x00',
     'steps': [ {'inputs': [('PINA',0x07),('PINB',0x00),('PINC',0x00)], 'iterations': 5 } ],
     'expected': [('PORTD',0x00)],
    },
#707
    {'description': 'PINA: 0x07 PINB: 0x00 PINC: 0x07 => PORTD: 0x00',
     'steps': [ {'inputs': [('PINA',0x07),('PINB',0x00),('PINC',0x07)], 'iterations': 5 } ],
     'expected': [('PORTD',0x00)],
    },
#770
    {'description': 'PINA: 0x07 PINB: 0x07 PINC: 0x00 => PORTD: 0x00',
     'steps': [ {'inputs': [('PINA',0x07),('PINB',0x07),('PINC',0x00)], 'iterations': 5 } ],
     'expected': [('PORTD',0x00)],
    },
#777
    {'description': 'PINA: 0x07 PINB: 0x07 PINC: 0x07 => PORTD: 0x04',
     'steps': [ {'inputs': [('PINA',0x07),('PINB',0x07),('PINC',0x07)], 'iterations': 5 } ],
     'expected': [('PORTD',0x04)],
    },

#sum in more than 6 bits (m = max test, b = balance test)
#m b  255 0 0
    {'description': 'PINA: 0xFF PINB: 0x00 PINC: 0x00 => PORTD: 0x3F',
     'steps': [ {'inputs': [('PINA',0xFF),('PINB',0x00),('PINC',0x00)], 'iterations': 5 } ],
     'expected': [('PORTD',0x3F)],
    },
#m !b 7 241 7
    {'description': 'PINA: 0x07 PINB: 0xF1 PINC: 0x07 => PORTD: 0x3D',
     'steps': [ {'inputs': [('PINA',0x07),('PINB',0xF1),('PINC',0x07)], 'iterations': 5 } ],
     'expected': [('PORTD',0x3D)],
    },
#!m b  6 7 88
    {'description': 'PINA: 0x06 PINB: 0x07 PINC: 0x58 => PORTD: 0x1A',
     'steps': [ {'inputs': [('PINA',0x06),('PINB',0x07),('PINC',0x58)], 'iterations': 5 } ],
     'expected': [('PORTD',0x1A)],
    },
#!m !b : 6 7 8 
    {'description': 'PINA: 0x06 PINB: 0x07 PINC: 0x08 => PORTD: 0x04',
     'steps': [ {'inputs': [('PINA',0x06),('PINB',0x07),('PINC',0x08)], 'iterations': 5 } ],
     'expected': [('PORTD',0x04)],
    },
#140 exactly 46 48 46 
    {'description': 'PINA: 0x2E (46) PINB: 0x30 (48) PINC: 0x2E (46) => PORTD: 0x20',
     'steps': [ {'inputs': [('PINA',0x2E),('PINB',0x30),('PINC',0x2E)], 'iterations': 5 } ],
     'expected': [('PORTD',0x20)],
    },
# #80 exactly 8 80 88
    {'description': 'PINA: 0x08 PINB: 0x50 (80) PINC: 0x58 (88) => PORTD: 0x2D',
     'steps': [ {'inputs': [('PINA',0x08),('PINB',0x50),('PINC',0x58)], 'iterations': 5 } ],
     'expected': [('PORTD',0x2D)],
    },
    ]
#watch = ['PORTC']


# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
#watch = ['<function>::<static-var>','PORTC']

