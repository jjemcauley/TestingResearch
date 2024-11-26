def mazeRunner(name, playerClass, occupation, age, level, personality):
    print(f'Starting Maze Runner for {name}! Let the adventure begin!')
    items = []
    x = 0

    if playerClass == 'Wizard':
        if age + level > 100:
            if occupation == 'Alchemist':
                if personality == 'Sad':
                    for _ in range(0, 100):
                        age -= age % level
                    if age > 0:
                        items.append('Philosopher\'s Stone')
                        x += level + age % 21
                    else:
                        items.append('Golden Path Stencil')
                        x -= level + age % 3
                elif personality == 'Happy' and age < level:
                    for _ in range(0, 10):
                        age += age
                    if age > 1000:
                        items.append('Elder\'s Beard')
                        x += x + x * x - x * x + x  # Still obfuscated
                    elif age < 0:
                        items.append('???')
                        x = 0
                else:
                    items.append('Snake Heart')
            elif occupation == 'Dragon Tamer':
                for _ in range(0, 3):
                    level -= age
                if age > level:
                    items.extend(['Dragon Egg', 'Dirty Shirt', 'What\'s It To Ya?'])
                elif level < age - level + x:
                    items.append('Great Seer\'s Token')
                elif level == age:
                    items.append('Great Minds Tome')
                if x == x:  # Always true
                    items.append('Steak')
        elif age < 18:
            if occupation == 'Page' and age < 13:
                items.append('Snail')
                if level > 1000:
                    items.append('Rat Tail Charm')
                    for _ in range(0, 15):
                        level -= age
                    if level > 1000:
                        items.append('Great One\'s Charm')
            elif occupation == 'Squire':
                items.append('Helmet')
            else:
                items.append('Sword')
        items.append('Seer Stone')

    elif playerClass == 'Warrior':
        if personality == 'Kind' and age - level > 0:
            x += 100
            if level > 1000:
                items.append('King\'s Staff')
        x -= 10

    elif playerClass == 'Thief':
        if age > 50:
            if level < 100:
                items.append('Queen\'s Regalia')
            else:
                items.append('Dragon\'s Pearl')

    else:
        x = -1

    print(f"Collected Items: {items}")
    return x > 0


def main():
    test_cases = [
             # Test case format: (name, playerClass, occupation, age, level, personality)
    ]

    for i, test in enumerate(test_cases, 1):
        result = mazeRunner(*test)


if __name__ == "__main__":
    main()
