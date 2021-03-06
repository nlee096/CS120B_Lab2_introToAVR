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
#0000 4 
    {'description': 'PINA: 0x00 => PORTC: 0x04',
    'steps': [ {'inputs': [('PINA',0x00)], 'iterations': 5 } ],
    'expected': [('PORTC',0x04)],
    },
#0001 3
    {'description': 'PINA: 0x01 => PORTC: 0x03',
    'steps': [ {'inputs': [('PINA',0x01)], 'iterations': 5 } ],
    'expected': [('PORTC',0x03)],
    },
#0010 3
    {'description': 'PINA: 0x02 => PORTC: 0x03',
    'steps': [ {'inputs': [('PINA',0x02)], 'iterations': 5 } ],
    'expected': [('PORTC',0x03)],
    },
#0011 2
    {'description': 'PINA: 0x03 => PORTC: 0x02',
    'steps': [ {'inputs': [('PINA',0x03)], 'iterations': 5 } ],
    'expected': [('PORTC',0x02)],
    },
#0100 3
    {'description': 'PINA: 0x04 => PORTC: 0x03',
    'steps': [ {'inputs': [('PINA',0x04)], 'iterations': 5 } ],
    'expected': [('PORTC',0x03)],
    },
#0101 2
    {'description': 'PINA: 0x05 => PORTC: 0x02',
    'steps': [ {'inputs': [('PINA',0x05)], 'iterations': 5 } ],
    'expected': [('PORTC',0x02)],
    },
#0110 2
    {'description': 'PINA: 0x06 => PORTC: 0x02',
    'steps': [ {'inputs': [('PINA',0x06)], 'iterations': 5 } ],
    'expected': [('PORTC',0x02)],
    },
#0111 1
    {'description': 'PINA: 0x07 => PORTC: 0x01',
    'steps': [ {'inputs': [('PINA',0x07)], 'iterations': 5 } ],
    'expected': [('PORTC',0x01)],
    },
#1000 3
    {'description': 'PINA: 0x08 => PORTC: 0x03',
    'steps': [ {'inputs': [('PINA',0x08)], 'iterations': 5 } ],
    'expected': [('PORTC',0x03)],
    },
#1001 2
    {'description': 'PINA: 0x09 => PORTC: 0x02',
    'steps': [ {'inputs': [('PINA',0x09)], 'iterations': 5 } ],
    'expected': [('PORTC',0x02)],
    },
#1010 2
    {'description': 'PINA: 0x0A => PORTC: 0x02',
    'steps': [ {'inputs': [('PINA',0x0A)], 'iterations': 5 } ],
    'expected': [('PORTC',0x02)],
    },
#1011 1
    {'description': 'PINA: 0x0B => PORTC: 0x01',
    'steps': [ {'inputs': [('PINA',0x0B)], 'iterations': 5 } ],
    'expected': [('PORTC',0x01)],
    },
#1100 2
    {'description': 'PINA: 0x0C => PORTC: 0x02',
    'steps': [ {'inputs': [('PINA',0x0C)], 'iterations': 5 } ],
    'expected': [('PORTC',0x02)],
    },
#1101 1
    {'description': 'PINA: 0x0D => PORTC: 0x01',
    'steps': [ {'inputs': [('PINA',0x0D)], 'iterations': 5 } ],
    'expected': [('PORTC',0x01)],
    },
#1110 1
    {'description': 'PINA: 0x0E => PORTC: 0x01',
    'steps': [ {'inputs': [('PINA',0x0E)], 'iterations': 5 } ],
    'expected': [('PORTC',0x01)],
    },
#1111 0
    {'description': 'PINA: 0x0F => PORTC: 0x80',
    'steps': [ {'inputs': [('PINA',0x0F)], 'iterations': 5 } ],
    'expected': [('PORTC',0x80)],
    },
    ]
#watch = ['PORTC']


# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
#watch = ['<function>::<static-var>','PORTC']

