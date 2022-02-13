# https://stackify.com/python-garbage-collection/#:~:text=The%20Python%20garbage%20collector%20has,a%20threshold%20number%20of%20objects.
# The main garbage collection mechanism in CPython is through reference counts.
# can't handle cyclic references
# >>> import sys
# >>> a = 'my-string'
# >>> sys.getrefcount(a)
# 2
# additionally works Generational garbage collection
