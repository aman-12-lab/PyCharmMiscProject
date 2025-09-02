
"""
import numpy as np
a= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b = a.reshape(4,3)
n,m =np.shape(b)

 for i in range(n):
     for j in range(m):
         print("the element",i,j,"is",b[i][j])

         for a in np.nditer(a):
             print(a)


"""







"""
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arp = a.reshape(3,4)
print(arp)

a = np.delete(arp,[2],0)
print(a)

b= np.delete(arp,[2],1)
print(b)

"""

"""
z = np.zeros(10)
print(z)
z=np.ones((10,10))
print(z)
z=np.full((10,10),11)
print(z)
z1=np.linspace(0,5,10)
print(z1)
z1= np.arange(0,5,0.2)
print(z1)
z2 = np.random.random(100)
print(z2)
z2 = np.random.randint(1,10,100)
print(z2)
z3 = np.random.randn(100)
print(z3)

z4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(z4)

z4rp =z4.reshape(3,4)
print(z4rp)

z4rp = z4.reshape(3,2,2)
print(z4rp)

A = np.repeat([[1,1,1]],4,axis=0)
print(A)

B= np.repeat([[1,1,1]],4,axis=1)
print(B)
"""



"""
a = np.array([1,2,3,4,5])
print(a.ndim)

a = np.array([[1,2],[3,4]])
print(a)
print(a.ndim)

a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a)
print(a.ndim)
print(np.size(a))
print(np.shape(a))
print(a)

print("printing",a[1][1][0])

a= np.array([[[[1,2,3],[4,5,6]],
              [[1,2,3],[3,4,6]],
              [[11,12,13],[14,15,16]]]])

print("printing",a[0,2,1,1])
print("shape",np.shape(a))
"""
















