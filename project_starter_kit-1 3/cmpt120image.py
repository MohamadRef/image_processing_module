# cmpt120image.py
# CMPT 120
# November 2023
# Some helper functions to wrap the Pygame image functions

import pygame
import numpy

def get_image(filename):
  """
  Input: filename - string containing image filename to open
  Returns: 3d list of lists (a height-by-width-by-3 list)
  """
  image = pygame.image.load(filename)

  # do a transpose so its rows correspond to height of the image
  return pygame.surfarray.array3d(image).transpose(1, 0, 2).tolist()

def save_image(pixels, filename):
  """
  Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
          filename - string containing filename to save image
  Output: Saves a file containing pixels
  """
  # do a transpose so its rows correspond to width of the image (used by Pygame)
  nparray = numpy.asarray(pixels).transpose(1, 0, 2)
  surf = pygame.surfarray.make_surface(nparray)
  (width, height, colours) = nparray.shape
  surf = pygame.display.set_mode((width, height))
  pygame.surfarray.blit_array(surf, nparray)
  pygame.image.save(surf, filename)

def show_image(pixels):
  """
  Input:  pixels - 3d list of list of RGB values (a height-by-width-by-3 list)
  Output: show the image in a window
  *this function uses the Pygame to display a window in a not-so-conventional way
  (without an event loop) so it might appear frozen.
  Suggested use: use it at the end of the program to show how the image looks like
  and make it stay by a this line:
  print("Press enter to quit")
  """
  # do a transpose so its rows correspond to width of the image (used by Pygame)
  nparray = numpy.asarray(pixels).transpose(1, 0, 2)
  surf = pygame.surfarray.make_surface(nparray)
  (width, height, _) = nparray.shape # not using colours here
  screen = pygame.display.set_mode((width, height))
  screen.fill((225, 225, 225))
  screen.blit(surf, (0, 0))
  pygame.display.update()

def get_black_image(width, height):
  """
  Input:  width - width of the image
          height - height of the image
  Output: 3d list of lists of a black image (a height-by-width-by-3 list)
  """
  return [[[0, 0, 0] for i in range(width)] for j in range(height)]

def get_white_image(width, height):
  """
  Input:  width - width of the image
          height - height of the image
  Output: 3d list of lists of a white image (a height-by-width-by-3 list)
  """
  return [[[255, 255, 255] for i in range(width)] for j in range(height)]
