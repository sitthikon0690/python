import numpy as np
a=np.array([1,2,3])
print(a)
b=np.array([[1,2,3],[4,5,6]])
print(b)

print(b.ndim)

li=[[1,2,3],[4,5,6],[7,8,9]]
c=np.array(li)
print(c)

li=((1,2,3),(4,5,6),(7,8,9))
d=np.array(li)
print(d)
print(d.ndim)