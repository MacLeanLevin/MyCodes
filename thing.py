import pygame
pygame.init()
print("Hello, I am Shin your personal nurse")
name = input("What is your name pacient?")
print("Hello", name, " nice to meet you, I will be taking care of you.")
feel = input("How are you feeling on a 1-5 scale?")

if feel == "1":
    print("Thats horrible I will bring you to surgery")
if feel == "2":
    print("Thats not good I will find more nurses")
if feel == "3":
    print("Your going to be okay I will scan you for injuries")
if feel == "4":
    print("Take a lollipop relax your more than fine")
an = input("Are you feeling hot, cold, or perfect?")
if an == "hot":
    print("Okay I will turn the heat down to furfill your needs")
if an == "cold":
    print("I will turn the heat up so you can stay tostey")
if an == "perfect":
    print("That is fantastic, Im glad to hear it")
print("Once you say you are satisfied with your care I will leave.")
pygame.time.wait(3000)
answer = input("Are you satisfied with your care? ")
if answer == "I am safisfied":
    print("Goodbye", name ,"nice meeting you, feel better")
if answer == "I am not satisfied":
    print("This is not good, I will not leave till you feel better")
