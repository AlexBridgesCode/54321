## Dependencies

# Closing terminal time delay
import time

## Variables

# Sense Counts
see = 5
feel = 4
hear = 3
smell = 2
taste = 1

## Arrays

# Array of sense counts
senses = [see, feel, hear, smell, taste]

# Array of sense name strings
senses_str = ["see", "feel", "hear", "smell", "taste"]

## Code

# For each sense in the senses array:
for i in range(len(senses)):

    # Print the input prompt
    if i < 4:
        print("Name", str(senses[i]), "things you can", senses_str[i] + ".")
    else:
        print("Name", str(senses[i]), "thing you can", senses_str[i] + ".")

    # For the number of times as the sense's count:
    for j in range(senses[i]):

        # Request user input
        x = input()

        # Print the remaining number of inputs
        if j < senses[i] - 1:
           print(str(senses[i] - 1 - j) + "...")
        else:
            print()

# Print a congratulatory message
print("Well done!")

# Delay the script's end
time.sleep(3)