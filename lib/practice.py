# practice1


def owner_activity(hungry, thirsty, playful):
    if hungry:
        print("Refill food bowl")
    elif thirsty:
        print("Refill water bowl")
    elif playful:
        print("Play with the dog")
    else:
        print("Do his own things")

# Call the function with appropriate arguments
owner_activity(hungry=False, thirsty=False, playful=False)