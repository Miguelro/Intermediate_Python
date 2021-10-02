#Map and filter compute elements only when asked and they are faster than list comprehensions

############# Map #############
languages = ["python","perl","java","c++"]
print([len(s) for s in languages])
#The map function doesn't actual produce a list, though. 
#It returns an object which we can consume to get the transformed values 
print(map(len,languages)) 
print(tuple(map(len,languages)))

map(float, ['1.0','2.5','-4.1'])
tuple(map(float, ['1.0','2.5','-4.1']))
list(map(float, [1.0,2.5,-4.1]))

############# Filter #############
def is_member(a: str):
    members = ["suraj","aida"]
    if a in members:
        member = True
    else:
        member = False
    return member

rolodex = ["suraj", "sophia", "aida", "mark"]
[client for client in rolodex if is_member(client)]
filter(is_member, rolodex)
tuple(filter(is_member, rolodex))

############# Lambda #############
(lambda x: x>3)(4)
(lambda x: x>3)(2)
list(map(lambda x: x>3, [4,2]))

list(map(lambda val: val ** 2, range(10)))
list(filter(lambda pair: pair[1] >0, [(4,1),(3,-2),(4,5),(8,0)]))
sorted([(4,1),(3,-2),(4,5),(8,0)], key=lambda x: x[1])
sorted([('abc', 121),('abc', 231),('abc', 148), ('abc',221)], key=lambda x: x[1])

x = [(4,1),(3,-2),(4,5),(8,0)]
x.sort(key=lambda pair: pair[1])
x

############## Exercises ##############
##Map
# (a) ["apple", "orange", "pear"] => (5, 6, 4)  (length)
tuple(map(len,["apple", "orange", "pear"]))
# (b) ["apple", "orange", "pear"] => ("APPLE", "ORANGE", "PEAR")  (uppercase)
tuple(map(lambda x: x.upper(),["apple", "orange", "pear"]))
# (c) ["apple", "orange", "pear"] => ("elppa", "egnaro", "raep")  (reversed)
tuple(map(lambda x: x[::-1],["apple", "orange", "pear"]))
# (d) ["apple", "orange", "pear"] => ("ap", "or", "pe")  (first two letters)
tuple(map(lambda x: x[:2],["apple", "orange", "pear"]))

##Filter
# (a) range(100) => (0, 3, 6, 9, ...)  (div by 3)
tuple(filter(lambda x: x%3==0,range(100)))
# (b) range(100) => (0, 5, 10, 15, ...)  (div by 5)
tuple(filter(lambda x: x%5==0,range(100)))
# (c) range(100) => (0, 15, 30, 45, ...)  (div by 15)
tuple(filter(lambda x: x%15==0,range(100)))
# (d) range(100) => (1, 2, 4, 7, 8, 11, 13, 14, 16, 17, ...)  (not div by 3 and not div by 5)
tuple(filter(lambda x: x%3!=0 and x%5!=0,range(100)))



##########################################################
# Iterators
##########################################################

it = iter([1,2,3])
max(it)
min(it)
next(it)  # => 1
next(it)  # => 2
next(it)  # => 3
next(it)  # raises StopIteration error
list(it)

it = iter(range(100))
66 in it
next(it)
list(it)


##########################################################
# Generators
##########################################################
import time

ts = time.time()
4 in (x**2 for x in range(10000000))
print(time.time()-ts)

ts = time.time()
4 in [x**2 for x in range(10000000)] #List comprehension se recorre toda la lista
print(time.time()-ts)
##########################################################
# Generator functions
##########################################################
def generate_ints(n):
    for i in range(n):
        yield i

g = generate_ints(3)  # Doesn't start the function! Just sets up the iterator
type(g)  # => <class 'generator'>

next(g)  # => 0. Run until the next yield statement.
next(g)  # => 1. Run until the next yield statement.
next(g)  # => 2. Run until the next yield statement.
next(g)  # raises StopIteration. Finished the function before finding another yield statement.


##########################################################
# Infinite Stream
##########################################################
def generate_tribonacci_numbers():
    a, b, c = 0, 0, 1
    while True:
        yield a
        a, b, c = b, a + b + c, a
    
def is_tribonacci(num):
    """Return whether `num` is a Tribonacci number."""
    # Be careful to not loop infinitely!
    for t in generate_tribonacci_numbers():
        if num <= t:  
            if num == t:
                 return True
            else:
                break