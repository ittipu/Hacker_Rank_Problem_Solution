import cmath
eq = input()

print("{:.3f}".format(abs(complex(eq))))
print("{:.3f}".format(cmath.phase(complex(eq))))

