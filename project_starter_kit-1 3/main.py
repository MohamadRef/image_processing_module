import pygame
import cmpt120image as img

###############################################################
# Keep this block at the beginning of your code. Use caution before you modify.
# If you want to hardcode to speed up development, you can do so

# For example, set just ENV = "v" if coding in VS Code.
# You'll need to uncomment before submission!
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using VS Code (v), Replit (r) or IDLE (i)? ").lower()
    while env not in "vri":
        print("Environment not recognized, type again.")
        env = input("Are you using VS Code (V), Replit (r) or IDLE (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# Use the playSound() function below to play sounds. 
# soundfilename does not include the .wav extension, 
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename,env):
    if env == "v" or env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
ENV = initEnv()
###############################################################






