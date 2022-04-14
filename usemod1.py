import sys
# from pkg.pkg import module
# look for john/math/geometry.py in sys.path
from john.math import geometry

geometry.hello()

print(geometry.circle_area(77))
a = geometry.rectangle_area(8, 4.3)

# 1. current folder
# 2. folders in PYTHONPATH
# 3. builtin folders

for path in sys.path:
    print(path)

