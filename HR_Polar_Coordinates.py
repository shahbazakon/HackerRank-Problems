# ============================================================= #
"""
Polar coordinates are an alternative way of representing
 Cartesian coordinates or Complex Numbers Z.
                        Z=x+yj
is completely determined by its real part  and imaginary part y.
Here,  is the imaginary unit.
"""
# ============================================================= #
from cmath import phase

complx = complex(input())
print(abs(complex(complx.real, complx.imag)))
print(phase(complex(complx.real, complx.imag)))

# ============================================================= #
