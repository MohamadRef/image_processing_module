#Mohamad Refaai
# November 29, 2023


import cmpt120image
import pygame
import random
pygame.display.set_mode((1, 1))



def recolor_image(img, color):
  new_img = cmpt120image.get_black_image(len(img), len(img[0]))
  for row in range(len(img)):
    for column in range(len(img[0])):
      pixel = img[row][column]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]
      if [r,g,b] != [255,255,255]:
        new_img[row][column] = color
      else:
        new_img[row][column] = pixel

  return new_img

def minify(img):
  new_img = cmpt120image.get_black_image(len(img), len(img[0]))
  for row in range(0,len(img),2):
    for column in range(0,len(img[0]),2):

      pixel1 = img[row][column]
      pixel2 = img[row][column+1]
      pixel3 = img[row+1][column]
      pixel4 = img[row+1][column+1]

      average_r = (pixel1[0] + pixel2[0] + pixel3[0] + pixel4[0]) // 4
      average_g = (pixel1[1] + pixel2[1] + pixel3[1] + pixel4[1]) // 4
      average_b = (pixel1[2] + pixel2[2] + pixel3[2] + pixel4[2]) // 4

      new_img[row//2][column//2] = [average_r, average_g, average_b]
  
  return new_img
  
def mirror(img):
  new_img = cmpt120image.get_black_image(len(img), len(img[0]))
  for row in range(len(img)):
    new_img[row] = img[row][::-1]
  
  return new_img
  
def draw_item(canvas, item, row, col):
  for i in range(len(item)):
    for j in range(len(item[0])):
      canvas_row = row + i
      canvas_col = col + j
      canvas[canvas_row][canvas_col] = item[i][j]

  return canvas
      
  
def distribute_items(canvas, item, n):
  for i in range(n):
      row = random.randint(0, len(canvas) - len(item))
      col = random.randint(0, len(canvas[0]) - len(item[0]))
      draw_item(canvas, item, row, col)
  return canvas

