from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()
player.cursor.visible = False

boxes = []

def add_stone(position):
  boxes.append(
    Button(color=color.white, model='cube', position=position, texture='stone.png', parent=scene, origin_y=0.5)
  )

def add_grass(i, j, k):
  add_box(i, j, k, 'grass.png', color.white)

def add_box(i, j, k, texture, color):
  boxes.append(
    Button(color=color, model='cube', position=(i,j,k), texture=texture, parent=scene, origin_y=0.5)
  )

def destroy_box(box):
  boxes.remove(box)
  destroy(box)

def build_world():
  Sky()
  
  player = FirstPersonController()
  player.cursor.visible = False
  mouse.visible = True
  
  boxes.clear()
  for box in boxes:
      destroy_box(box)

  for i in range(20):
    for j in range(20):
      add_grass(j,0,i)
    add_grass(0,1,i)
    add_grass(i,1,0)
    add_grass(20,1,i)
    add_grass(i,1,20)

def input(key):
  for box in boxes:
    if box.hovered:
      if key == 'left mouse down':
        add_stone(box.position + mouse.normal)
      if key == 'right mouse down':
        destroy_box(box)

  if key == ("escape"):
    exit()
  elif key == 'r':
    scene.clear()
    build_world()
    player.position = (0,0,0)

build_world()
app.run()
