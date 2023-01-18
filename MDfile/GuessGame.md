# What is Guess Game?
Guess Game is a game in which we have to guess a random number is generated in a given range.
This game can be made in python too, by using the **random module**.

# Random Module
Random module is a library in python which is used to get random values.
This library has a function called **randint** to generate random integers within a given range.
For intstance this is how we can generate a random integer between 1 to 10:
```python
import random #imports the random module in your python file so that you can use all of its functions
random_integer = random.randint(1, 11) #generates a random integer between 1 and 11. It means that the integer is greater than 1 and lesser than 11.
print(random_integer)
```
**Output:**
```
3
```
The output could be different every time we run the code. Let's run a for loop to see its different outputs:
```python
import random
for i in range(3):
    random_integer = random.randint(1, 11) 
    print(random_integer)
```
**Output:**
```
2
5
10
```
We will be using only the randint function in the making of this function.
For more information about random module you can visit its offical documentation at https://docs.python.org/3/library/random.html

# Making of the game 
To make our very own guess game we first have to import the random module in our program.
**Like this:**
```python
import random
```
After importing random module we now have to generate a random integer between 1 to 100.
```python
random_integer = random.randint(1, 101)
```
Get the user's input as an integer.
```python
user_input = int(input("Enter the number: "))
```
Now, if the user's input is equals to the random integer generated, the user will win, else if, the user's input is greater than or less than the random number, it should display that the input is greater/lesser (depends on the user's input).

**Like this:**
```python
if user_input == random_integer:
    print("Congratulations you have gussed the number!")
elif user_input > random_integer:
    print("Your input is greater than the number")
elif:
    print("Your input is lesser than the number")
```
Now let's add turns!
```python
def game():
    turn = 1
    maxturn = 9
    random_integer = random.randint(1, 101
    while (turn<=maxturn):
        print(f"Turn: {turn} --- Turn(s) left: {maxturn-turn} ")
        user_input = int(input("Enter the number: "))
        if user_input == random_integer:
            print(f"Congratulations you have gussed the number!\nYou took {turn} turns!")
            break
        elif user_input > random_integer:
            print("Your input is greater than the number")
        elif:
            print("Your input is lesser than the number")
        turn+=1
    if turn>maxturn:
        print(f"You have lost the game!\nThe number was {random_integer}")
```
You just need to call this function to play the game!

You should make an infinite while loop and get the user's input to play the game or not.

Here's an example of how you can do this:
```python
while True: #or while 1
    choice = input("Press Enter to play the game: ")
    if choice == "":
        game()
    else:
        break
```
**Use os module to clear the screen:**
```python
import os
while True: #or while 1
    os.system("cls") # use os.system("clear") if you are using MacOS, Linux, Android, etc.
    choice = input("Press Enter to play the game: ")
    if choice == "":
        game()
    else:
        break
```
**That's it!**

**Hope that this tutorial will be clear for you!**