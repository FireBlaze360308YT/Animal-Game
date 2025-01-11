# Import necessary packages
import random as rm
import time as tm
import sys

# Setup the game by storing animals in a tuple and their dietry habits in a dictionary of tuples
animal_list :tuple[str] = ("dog", "cat", "porcupine", "whale", "rat", "rabbit", "pig", "horse", "lion", "bat", "ibex", "penguin")
animal_food :dict[str, tuple[str]] = {"dog": ("beef", "chicken", "rice"),
                                      "cat": ("mice", "eggs", "cereal"),
                                      "porcupine": ("worms", "beetles", "ants"),
                                      "whale": ("prawns", "fish", "seals"),
                                      "rat": ("corn", "fruit", "biscuits"),
                                      "rabbit": ("carrots", "lettuce", "nuts"),
                                      "pig": ("potatoes", "turnips", "cabbage"),
                                      "horse": ("hay", "sugar cubes", "vegetables"),
                                      "lion": ("deer", "buffalo", "zebra"),
                                      "penguin": ("kfc", "subway", "dominos"),
                                      "ibex": ("grass", "flowers", "herbs"),
                                      "bat": ("beetles", "beef", "cereal"),
                                      "seal": ("krills", "fish", "penguin")}
animal_gender :tuple[str] = ("girl", "boy")
HEALTH_BAR :int = 100 # Size of heath bar which is printed to console
animal_images :dict[str, str] = {
    "dog": "🐕",
    "cat": "🐈",
    "porcupine": "🦔",
    "whale": "🐋",
    "rat": "🐀",
    "rabbit": "🐇",
    "pig": "🐷",
    "horse": "🐎",
    "lion": "🦁",
    "penguin": "🐧",
    "ibex": "🐐",
    "bat": "🦇",
    "seal": "🦭"}
available_foods :set[str] = set()
count :int = 0
rounds :int = 0

# Functions
def death(animal_name :str) -> None:
    # Final message to game player
    print(f"sorry {animal_name} is dead :( ")
    return None

def health_bar_code(random_health :int) -> None:
    # Health bar code
    sys.stdout.write("[%s]" % (" " * HEALTH_BAR))
    sys.stdout.flush()
    sys.stdout.write("\b" * (HEALTH_BAR + 1))  # Return to start of line, after '['
    Health_width = random_health
    for i in range(Health_width):
        tm.sleep(0.1)
        sys.stdout.write("-")
        sys.stdout.flush()
    Sick_width = HEALTH_BAR - Health_width
    for i in range(Sick_width):
        tm.sleep(0.01)
        sys.stdout.write("0")
        sys.stdout.flush()
    sys.stdout.write("]\n")  # This ends the health bar
    return None

def main() -> None:
    global count
    global rounds

    while True:
        game_mode = input("Would you like to play infinite mode or limited mode? Type 1 for infinite and 2 for limited! ")
        try:
            game_mode = int(game_mode)
            if game_mode in {1, 2}:
                break
            print("Choose between 1 or 2\n")
        except ValueError:
            print("Choose between 1 or 2\n")

    # Start the game by randomly selecting an animal, a health score and a gender
    random_animal = rm.choice(animal_list)
    random_health = rm.randint(1, 100)
    random_gender = rm.choice(animal_gender)

    # Tell the user what their animal is and ask to name the animal
    print(f"Your animal is a {random_gender} {random_animal} {animal_images.get(random_animal)}. It has a health score of {random_health}")
    animal_name = input("Give your animal a name: ")

    available_foods.update(food for animal, foods in animal_food.items() if animal != random_animal for food in foods)

    # Keeps asking the user to select a food and adjusts the health score and displays the health bar
    # Main loop
    while random_health > 0:
        if (game_mode == 2 and rounds >= 100) or (game_mode == 2 and random_health >= 300):
            print("100 rounds have passed or 300 health has been reached, limited gamemode doesnt allow more gaming!")
            break
        rounds += 1
        decoy_animal = rm.choice([animal for animal in animal_list if animal != random_animal])
        print(f"{animal_name} {animal_images.get(random_animal)} is currently fine")
        mixed_list = set(animal_food[random_animal]).union(animal_food[decoy_animal])
        chosen_food = input(f"What would you like to feed {animal_name}, choose from {sorted(mixed_list)}? ").lower().replace(" ", "")
        if chosen_food not in mixed_list and chosen_food in available_foods:
            print(f"Sorry, {chosen_food} wasn't in the options!")
            random_health -= 5
            health_bar_code(random_health)
            count += 1
            if count >= 5:
                print("Stop being a pain! Choose from the given options")
                count = 0
            continue
        elif chosen_food in animal_food[random_animal]:
            random_health += 10
            print(f"{animal_name} enjoyed that. Their score is now {random_health}")
            health_bar_code(random_health)
            continue
        elif chosen_food in animal_food[decoy_animal]:
            random_health -= 10
            print(f"{animal_name} didn't like that. Their score is now {random_health}")
            health_bar_code(random_health)
            continue
        else:
            if rm.randint(1, 3) >= 2:
                random_health -= 10
                print(f"{chosen_food} cannot be eaten by {animal_name}, but luckily nothing happened! Their score is now {random_health}")
            else:
                random_health -= 20
                print(f"While trying to give {chosen_food} to {animal_name}, your animal got food poisoning :( Their score is now {random_health}")
                print("Try not doing it again")
            health_bar_code(random_health)
            count += 2
            if count >= 5:
                print(f"Stop trying to poison {animal_name}! It's evil")
                count = 0
            continue
    if random_health <= 0:
        death(animal_name)
    return None

# Start of the program
if __name__ == "__main__":
    main()
