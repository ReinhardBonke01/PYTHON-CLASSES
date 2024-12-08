import random
def guess_number():
  number=random.randint(1,100)
guess=None

while guess!=number:
    guess=int("Guess the number between 1 to 100")
if guess<number:
    print("Too Low")
elif guess>number:

   print("Too High")
else:
  print("congratulations")