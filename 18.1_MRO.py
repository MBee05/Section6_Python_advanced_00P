class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass


# print(M.mro())
print(M.__mro__)

# MRO exist but no good to use it