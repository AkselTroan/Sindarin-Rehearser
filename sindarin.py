import random


# For colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def menu():
    print(bcolors.OKGREEN + ""
          "|---------------------------------------------------|\n"
          "|---------- Welcome to the Sindarin app ------------|\n"
          "|-- Here you can learn and practice your Sindarin --|\n"
          "|---------------------------------------------------|\n\n"
          + bcolors.ENDC + bcolors.OKCYAN +
          "There are currently three gamemodes\n"
          + bcolors.ENDC + bcolors.BOLD + bcolors.OKBLUE +
          "1: Glossary\n"
          "2: Sentences\n"
          "3: Conversation\n"
          "\n"
          + bcolors.ENDC + bcolors.WARNING +
          "Different difficulties is available (Not implemented yet)\n"
          "Written by Aksel Troan\n"
          + bcolors.ENDC)
    gameMode = input("Please enter gamemode: ")

    while gameMode != "1" and gameMode != "2" and gameMode != "3":
        print("Could not find given gamemode.\n"
              "1: Glossary\n"
              "2: Sentences\n"
              "2: Conversation\n")
        gameMode = input("Please enter gamemode: ")
    return gameMode


def glossary():
    print("Playing glossary...\n")
    language = input("1: Translate Sindarin to English\n"
                     "2: Transalte English to Sindarin\n")

    while language != "1" and language != "2":
        print("Could not find given language.\n"
              "1: Translate Sindarin to English\n"
              "2: Transalte English to Sindarin\n")
        language = input("Please enter your language: ")

    if language == "1":
        lines = open("glossary.txt", "r").read().splitlines()
        playing = True
        print(bcolors.FAIL + "You can quit anytime by inputting: " + bcolors.ENDC + bcolors.OKGREEN + "!q" + bcolors.ENDC)
        while playing is True:
            currentLine = random.choice(lines).split(":")
            print(f"Translate to English: {currentLine[0]}")
            translation = input()
            if translation.upper() == "!Q":
              playing = False
              break
            elif translation.upper() == currentLine[1].upper():
                print(bcolors.OKGREEN + f"Correct! The translation goes: {currentLine[1]}\n" + bcolors.ENDC)
            else:
                print(bcolors.FAIL + f'Wrong. The translation goes: ' + bcolors.ENDC + bcolors.OKBLUE + currentLine[1]
                      + bcolors.ENDC + "\n")
        print(bcolors.OKGREEN + "Thank you for using the Sindarin Rehearser!" + bcolors.ENDC)

    if language == "2":
        lines = open("glossary.txt", "r").read().splitlines()
        playing = True
        print(bcolors.FAIL + "You can quit anytime by inputting: " + bcolors.ENDC + bcolors.OKGREEN + "!q" + bcolors.ENDC)
        while playing is True:
            currentLine = random.choice(lines).split(":")
            print(f"Translate to Sindarin: {currentLine[1]}")
            translation = input()
            if translation.upper() == "!Q":
              playing = False
              break
            elif translation.upper() == currentLine[0].upper():
                print(bcolors.OKGREEN + f"Correct! The translation goes: {currentLine[0]}\n" + bcolors.ENDC)
            else:
                print(bcolors.FAIL + f'Wrong. The translation goes: ' + bcolors.ENDC + bcolors.OKBLUE + currentLine[0]
                      + bcolors.ENDC + "\n")
        print(bcolors.OKGREEN + "Thank you for using the Sindarin Rehearser!" + bcolors.ENDC)


def sentences():
    print("Playing sentences...\n")
    language = input("1: Translate Sindarin to English\n"
                     "2: Transalte English to Sindarin\n")

    while language != "1" and language != "2":
        print("Could not find given language.\n"
              "1: Translate Sindarin to English\n"
              "2: Transalte English to Sindarin\n")
        language = input("Please enter your language: ")

    if language == "1":
        lines = open("sentence.txt", "r").read().splitlines()
        playing = True
        print(bcolors.FAIL + "You can quit anytime by inputting: " + bcolors.ENDC + bcolors.OKGREEN + "!q" + bcolors.ENDC)
        while playing is True:
            currentLine = random.choice(lines).split(":")
            print(f"Translate to English: {currentLine[0]}")
            translation = input()
            if translation.upper() == "!Q":
                playing = False
                break
            elif translation.upper().replace(" ","") in currentLine[1].upper().replace(" ", ""):
                print(bcolors.OKGREEN + f"Correct! The translation goes: {currentLine[1]}\n" + bcolors.ENDC)
            else:
                print(bcolors.FAIL + f'Wrong. The translation goes: ' + bcolors.ENDC + bcolors.OKBLUE + currentLine[1]
                  + bcolors.ENDC + "\n")
        print(bcolors.OKGREEN + "Thank you for using the Sindarin Rehearser!" + bcolors.ENDC)

    if language == "2":
        lines = open("sentence.txt", "r").read().splitlines()
        playing = True
        print(bcolors.FAIL + "You can quit anytime by inputting: " + bcolors.ENDC + bcolors.OKGREEN + "!q" + bcolors.ENDC)
        while playing is True:
            currentLine = random.choice(lines).split(":")
            print(f"Translate to Sindarin: {currentLine[1]}")
            translation = input()
            if translation.upper() == '!Q':
                playing = False
                break
            elif translation.upper() == currentLine[0].upper():
                print(bcolors.OKGREEN + f"Correct! The translation goes: {currentLine[0]}\n" + bcolors.ENDC)
            else:
                print(bcolor.FAIL + f'Wrong. The translation goes: ' + bcolors.ENDC + bcolors.OKBLUE + currentLine[0]
                  + bcolors.ENDc + "\n")
        print(bcolors.OKGREEN + "Thank you for using the Sindarin Rehearser!" + bcolors.ENDC)


def conversation():
    print("Playing conversation")


def main():
    gameMode = menu()

    if gameMode == "1":
        glossary()

    if gameMode == "2":
        sentences()

    if gameMode == "3":
        conversation()


if __name__ == "__main__":
    main()
