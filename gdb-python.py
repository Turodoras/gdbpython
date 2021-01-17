#!/usr/bin/env python3

import gdb
from subprocess import Popen, PIPE

"""
print `msg` if `debug` is True
"""
def log(debug=False, msg):
    if debug:
        print(f'[*] {msg}')

"""
continue
"""
def cont(debug=False):
    log(debug, 'continue')
    output = gdb.execute('c', to_string)
    return output

"""
break on `symbol` and continue if `c` is True
if `c` is True then return output
"""
def bs(symbol, c=False, debug=False):
    log(debug, f'breaking on symbol {symbol}')
    gdb.execute(f'b {symbol}')
    if c:
        return cont(debug)

"""
break at `addr` and continue if `c` is True
if `c` is True then return output
"""
def ba(addr, c=False, debug=False):
    log(debug, f'breaking at address {addr}')
    gdb.execute(f'b *{addr}')
    if c:
        return cont(debug)

"""
file `filename`
"""
def f(filename, debug=False):
    log(debug, f'file on {filename}')
    gdb.execute(f'file {filename}')


