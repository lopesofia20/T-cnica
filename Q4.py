def a (n):
    return 2*n - 1
print(a(5))

def b(n):
  return 2**n
print(b(7))

def c(n):
   return n**2
print(c(8))

def d(n):
   return (n*2)**2
print(d(5))

def e(n):
   if n <= 1:
      return n
   else:
      return e (n-1) + e(n-2)
print(e(7))