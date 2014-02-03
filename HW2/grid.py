# Exercise 3.5: Drawing of grid with three rows and three columns.

def row():
    return "+ - - - - + - - - - +"

def column():
    return "|         |         |"

print row()
for i in range(1,4):
    print column()
print row()
for i in range(1,4):
    print column()
print row()

# Exercise 3.5: Drawing of grid with four rows and four columns.

def row1():
    return "+ - - - - + - - - - + - - - - + - - - - +"

def column1():
    return "|         |         |         |         |"

print row1()
for i in range(1,5):
    print column1()
print row1()
for i in range(1,5):
    print column1()
print row1()
for i in range(1,5):
    print column1()
print row1()
for i in range(1,5):
    print column1()
print row1()