# Numerical Stability
# Adding small values to a big value introduces lots of errors

value = 1000000000

for i in range(0, 1000000):
    value += 0.000001

value -= 1000000000

print(round(value,3))