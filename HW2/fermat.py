# Exercise 5.3: Fermat's Theorem.

def check_fermat(a,b,c,n):
    if n>2 and (a**n)+(b**n)==c**n:
        return "Holy smokes, Fermat was wrong!"
    else:
        return "No, that doesn't work."

print check_fermat(3,4,5,2)

# Exercise 5.3: The user sets the input variables and test Fermat's theorem.

number1 = int(raw_input("Enter a number: "))
number2 = int(raw_input("Enter a number: "))
number3 = int(raw_input("Enter a number: "))
number4 = int(raw_input("Enter a number: "))
print check_fermat(number1, number2, number3, number4)
