import time

see = 5
feel = 4
hear = 3
smell = 2
taste = 1

senses = [see, feel, hear, smell, taste]

senses_str = ["see", "feel", "hear", "smell", "taste"]

for i in range(len(senses)):
    if i < 4:
        print("Name", str(senses[i]), "things you can", senses_str[i] + ".")
    else:
        print("Name", str(senses[i]), "thing you can", senses_str[i] + ".")
    for j in range(senses[i]):
        x = input()
        if j < senses[i] - 1:
           print(str(senses[i] - 1 - j) + "...")
        else:
            print()

print("Well done!")

time.sleep(3)


