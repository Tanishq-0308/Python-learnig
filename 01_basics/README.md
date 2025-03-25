# Basics of python

1- def is a function.
2- __pycache__ folder is always created when you run any file, but only visible when you import any module in other module. 

3- first.cpython-312.pyc is generated in the __pycache__ folder 

        here cpython is the python we are using,
        312 is the version of the python.

        This is the byte code generated from the python file which send to the PVM ( python virtual machine ).
        byte code is platform independent.


# mutable and immutable

# Mutable Objects

Mutable objects can be modified in place. This means you can change their content without creating a new object. Common mutable types include:

Lists: You can add, remove, or change elements.
Dictionaries: You can change values, add new key-value pairs, or remove them.
Sets: You can add or remove elements.

```python
my_list = [1, 2, 3]
my_list.append(4)  # Modifies the original list
print(my_list)  # Output: [1, 2, 3, 4]
```


# Immutable Objects

Immutable objects cannot be modified after they are created. If you try to change their content, a new object is created instead. Common immutable types include:

Tuples: Once created, you cannot change the elements.
Strings: Any modification creates a new string.
Frozensets: Similar to sets but immutable.


```python
my_string = "hello"
new_string = my_string.replace("h", "j")  # Creates a new string
print(my_string)  # Output: "hello"
print(new_string)  # Output: "jello"
```




# Object Types / Data Types

- Number : 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List : [1, [2, 'three'], 4.5], list(range(10))
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

- Set : set('abc'), {'a', 'b', 'c'}

- File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')

- Boolean : True, False
- None : None
- Funtions, modules, classes

- Advance: Decorators, Generators, Iterators, MetaProgramming



# Numeric
a = 10          # int
b = 3.14        # float
c = 2 + 3j      # complex

# Sequences
s = "Hello"     # str
l = [1, 2, 3]   # list
t = (4, 5, 6)   # tuple

# Mapping
d = {"key": "value"}  # dict

# Sets
s1 = {1, 2, 2}  # set (becomes {1, 2})
fs = frozenset([1, 2])  # frozenset

# Boolean and None
flag = True     # bool
n = None        # NoneType