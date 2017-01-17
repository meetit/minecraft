# Import the minecraft library
import mcpi.minecraft as minecraft
import time

# connect to the minecraft client
mc = minecraft.Minecraft.create()

# cobblestone
blockType = 4

# place blocks under the player
while True:
  pos = mc.player.getTilePos()
  height = mc.getHeight(pos.x, pos.y)
  mc.setBlock(pos.x, pos.y - 1, pos.z, blockType)
  time.sleep(0)

