#! /usr/bin/env python3
import math as m
import sys

WANT=(int)(sys.argv[1])

first=round(m.log(WANT,2))
error=1./WANT - 1./(2**first)
terms=[first]

print("template <typename T>")
print("static inline T div_%s(const T& val) {" % WANT)
print("  return (val >> %s)" % first, end='')

while m.fabs(error) > 1./(1<<32):
  sign = m.copysign(1, error)
  term = -round(m.log(m.fabs(error), 2.))
  print(" %s (val >> %s)" % ("-" if sign == -1.0 else "+", (int)(term)), end='')
  error -= sign*(2**(-term))

print(";\n}")
