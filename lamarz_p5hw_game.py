#Zachary LaMar
#11/19/24
#P5HW
#Create a text based game

import random
def classes():
    classes_dict={
        "bard" : {
            "hp" : 70,
            "mp" : 80,
            "str" : 1,
            "dex" : 5,
            "int" : 3,
            #To be moved to individual character skills later
            "skills" : {
                "starter" : "Inspire"
                }
            },
        "cleric" : {
            "hp" : 90,
            "mp" : 80,
            "str" : 3,
            "dex" : 2,
            "int" : 5,
            #To be moved to individual character skills later
            "skills" : {
                "starter" : "Healing Touch"
                }
            },
        "mage" : {
            "hp" : 50,
            "mp" : 120,
            "str" : 1,
            "dex" : 2,
            "int" : 7,
            #To be moved to individual character skills later
            "skills" : {
                "starter" : "Magic Missile"
                }
            },
        "ranger" : {
            "hp" : 95,
            "mp" : 50,
            "str" : 1,
            "dex" : 6,
            "int" : 2,
            #To be moved to individual character skills later
            "skills" : {
                "starter" : "Debilitating Shot"
                }
            },
        "warrior" : {
            "hp" : 125,
            "mp" : 25,
            "str" : 6,
            "dex" : 3,
            "int" : 1,
            #To be moved to individual character skills later
            "skills" : {
                "starter" : "Berserk"
                }
            }
        }
    return classes_dict
def create_character():
    extra_char="y"
    party=[]
    while extra_char=="y" and len(party)<2:
        character={
            "name" : input("Enter character's name: "),
            "class" : int(input(f"Enter character's class:\n 1. Bard\n 2. Cleric\n 3. Mage\n 4. Ranger\n 5. Warrior\n Enter the number corresponding to your choice: "))
            }
        if character.get("class")==1:
            character.update({
            "class" : "Bard",
            "hp" : 70,
            "mp" : 80,
            "str" : 1,
            "dex" : 4,
            "int" : 3,
            #To be moved to individual character skills later
            "skills" : {
                "starter" : "Inspire"}})
        elif character.get("class")==2:
            character.update({
            "class" : "Cleric",
            "hp" : 90,
            "mp" : 80,
            "str" : 3,
            "dex" : 2,
            "int" : 5,
            #To be moved to individual character skills later
            "skills" : {
                "starter" : "Healing Touch"}
                })
        elif character.get("class")==3:
            character.update({
            "class" : "Mage",
            "hp" : 50,
            "mp" : 120,
            "str" : 1,
            "dex" : 2,
            "int" : 7,
            #To be moved to individual character skills later
            "skills" : {
                "starter" : "Magic Missile"
                }})
        elif character.get("class")==4:
            character["class"]="Ranger"
        elif character.get("class")==5:
            character["class"]="Warrior"
        extra_char=input("Would you like to make another character? (max of 3) ").lower()[0]
        party.append(character)
    return character

def display_character(character):
    for key, value in character.items():
        print(f"{key.capitalize()} : {value}")

def main():
    print("Game is starting...")
    print()
    classes()
    char1=create_character()
    char2=create_character()
    char3=create_character()
    print()
    display_character(char1)
    print()
    display_character(char2)
    print()
    display_character(char3)
    '''extra_char=input("Would you like to make another character? ").lower()[0]
    if extra_char=="y":
        char2=create_character()
        extra_char=input("Would you like to make another character? ").lower()[0]
        if extra_char=="y":
            char3=create_character()
            extra_char=input("Would you like to make another character? ").lower()[0]
        else:
            char3=""
    else:
        char2=""'''
    

if __name__=="__main__":
    main()
