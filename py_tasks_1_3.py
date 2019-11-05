from itertools import zip_longest as zipped

list1 = [i for i in range(1, 10, 1)]
# with list2=list1 link 'list2' to array named 'list1' will be created
list2 = list1.copy()
# list2 = list(list1)
list2.append(10)
# list2.pop(0) # specific way to remove element from array using list syntax cause there is no simple arrays in Python
del list2[0]
list3 = list1[:]
list3.append('full copy magic')
# first (dirty) way to print
for i in range(9):
    print(list1[i], list2[i], list3[i], sep="\t")
print("\t", list3[-1], sep="\t")

# or second way with importing zip_longest function

for i in zipped(list1, list2, list3, fillvalue=""):
    print(i[0], i[1], i[2], sep="\t")

# preparing names for checking how functions works
names = ["uNMATCHED", "Matched", "lower", "UPPER", "a", "", 1, {1, 2}]


def hello_user(username):
    # seems legit to task, but will fail on hello_user("")
    print("Hello, " + username.upper()[0] + username.lower()[1:]+"!")


for name in names[:4]:
    hello_user(name)


def hello_user_opt(username):
    # will work without crush if only string value is given
    if len(username) > 0:
        print("Hello, " + username.upper()[0] + username.lower()[1:]+"!")
    else:
        print("Hello, The Faceless Man!")


for name in names[:5]:
    hello_user_opt(name)


def hello_opt(username):
    # will work without crush in any case except for hello_opt() without param
    # which is not a constructive way to destroy an app
    if type(username) is str:
        if len(username) > 0:
            print("Hello, " + username.upper()[0] + username.lower()[1:]+"!")
        else:
            print("No name - no greetings!")
    else:
        print("I used to greet you but then I took a "+str(type(username))+" in the knee...")


for name in names:
    hello_opt(name)


# If we need to greet user whose name consist of two words or more there are two ways: using string.split() or regex.
# Split() is the easiest way to solve more-than-one-word case but lack on flexibility.
# Regex is optimal due to it's ability to deal with difficult cases like "Obi van Kenobi"
# where only two words should be with upper case letters.

class Dog:
    # I can use standard constructor cause there is no memory-hungry data in class
    # and there is no task to create one class object from another
    # so no __init__ here is defined
    def bark(self, times=1):
        x = 'BARK!!! ' * times
        print(x[:-1])


class SmartDog(Dog):
    # class constructor inherits from Dog class
    def givepaw(self):
        print("Paw pat")


class NoizyDog(Dog):
    # class constructor from Dog class, bark method is an override method
    def bark(self, times=1):
        for i in range(times):
            print('BARK!!!')


class SmartNoizyDog(SmartDog, NoizyDog):
    # just child class that inherits all from parent classes SmartDog and NoizyDog
    # I use this disgusting way of inheritance for lines 108 and 110 of script
    pass


# there is no information in tasks if I should create variables with 'dog'-classes,
# so I decided to create anonymous objects

Dog().bark(3)
NoizyDog().bark(3)
SmartDog().bark(3)
SmartDog().givepaw()

# NoizyDog().givepaw() is impossible cause no such method in that class
# but smart and noisy dog can paw like SmartDog:
SmartNoizyDog().givepaw()
# and bark like NoizyDog:
NoizyDog.bark(SmartNoizyDog(),3)
# or SmartDog:
SmartDog.bark(SmartNoizyDog(),3)
