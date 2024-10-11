import cmpt120image
from main import initEnv, playSound

def test_playsound(env):
    playSound("apples", env)
    input("Press enter to continue after sound has played. ")

def test_get_image():
    cmpt120image.get_image("images/apples.png")

def test_save_image():
    my_image = cmpt120image.get_image("images/apples.png")
    cmpt120image.save_image(my_image, "copy_of_apples.png")

def test_show_image():
    my_image = cmpt120image.get_image("images/apples.png")
    cmpt120image.show_image(my_image)
    input("Press enter when done viewing image")

def test_get_black_image():
    b = cmpt120image.get_black_image(100, 100)
    cmpt120image.show_image(b)
    input("Press enter when done viewing image")

def test_get_white_image():
    w = cmpt120image.get_white_image(100, 100)
    cmpt120image.show_image(w)
    input("Press enter when done viewing image")

ENV = initEnv()


# ===
# CODE TO TEST SOUNDS 
# ===
# Uncomment the below code to make sure you can play a sound!
# If this doesn't run, try to debug your error message or let the instrucotrs know!
# test_playsound(ENV)


# ===
# CODE TO TEST IMAGES
# ===
# screen = cmpt120image.init()
test_get_image()
test_save_image()
test_show_image()
test_get_black_image()
test_get_white_image()