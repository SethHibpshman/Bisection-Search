x = 16 # Input what you want to take the sqrt of.
epsilon = 0.000001 # How accurate you want to be.

# Can handle any postive number; most explicitely handling numbers 0-1 and beyond 1.
if x >= 1:
    low = 1.0
    high = x
else:
    low = x
    high = 1.0

guess = (high + low) / 2 # The first guess.

while abs(guess**2 - x) >= epsilon: # Keep going until desired accuracy.
    print(f'low = {low} high = {high}') # Uncomment to debug or view itterations.
    if guess**2 < x: # If the guess squared is smaller than x, the guess is too low and becomes the new lowerbound.
        low = guess
    else: # If the guess is larger than x, the guess it too high and becomes the new upperbound.
        high = guess
    guess = (high + low) / 2

print(f'{guess} is close to the square root of {x}') # Print final answer.