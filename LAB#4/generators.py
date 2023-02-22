#Create a generator that generates the squares of numbers up to some number N.
def sqrtn(n):
    s = (i**2 for i in range(n))
    for i in s:
      if i == 0:
        continue
      else:
        print(i)

n = int(input())
sqrtn(n+1)

#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def evenn(n):
   for i in range(n):
     if i % 2 ==0: 
       yield i

n = int(input())
even = evenn(n)
print(", ".join(str(x) for x in even))


#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divs(n):
  for i in range (n):
    if i % 3 == 0 and i % 4 == 0:
      yield i

n = int(input())
div = divs(n)
print(" ".join(str(x) for x in div))


#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a, b = int(input()), int(input())

for square in squares(a, b):
    print(square)


#Implement a generator that returns all numbers from (n) down to 0.
def revnum(n):
  s = (i for i in range (n))
  for i in range (n, 0, -1):
    yield i

n = int(input())
rev = revnum(n)
print(", ".join(str(i) for i in rev))

