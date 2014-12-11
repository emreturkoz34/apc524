import matrix3d
import deltaPDF
import test
import vector
import numpy as np

print "test"

nPoints = 11
a = test.Line()
a = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
test.print_line(a)
b = np.linspace(0, 1, nPoints)
print b[nPoints-1]
print b[nPoints/2]

v = vector.Vector(nPoints)
d = deltaPDF.DeltaPDF(a, nPoints)
