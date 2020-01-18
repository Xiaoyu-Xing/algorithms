a = [0, 0, 0, 1, 1, 1, 3, 3, 6, 6, 9, 9]
print(len(a))


def root(x):
  while x != a[x]:
    a[x] = a[a[x]]
    print(x, a[x])
    x = a[x]
  return x


def root2(x):
  if x != a[x]:
    a[x] = root2(a[x])
  return a[x]


root2(9)
print(a)
