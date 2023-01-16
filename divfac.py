#! /usr/bin/env python3
import math as m
import sys

WANT=(float)(sys.argv[1])
NAME=sys.argv[2]

first=round(m.log(WANT,2))
error=1./WANT - 1./(2**first)
terms=[first]

print("template <typename T>")
print("static inline T %s(const T& val) {" % NAME)
if first == 0:
  print("  return val", end='')
else:
  print("  return (val >> %s)" % first, end='')

while m.fabs(error) > 1./(1<<32):
  sign = m.copysign(1, error)
  term = -round(m.log(m.fabs(error), 2.))
  print(" %s (val >> %s)" % ("-" if sign == -1.0 else "+", (int)(term)), end='')
  error -= sign*(2**(-term))

print(";\n}")
