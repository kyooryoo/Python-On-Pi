import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# create connection to Minecraft
mc = minecraft.Minecraft.create()
# post message to the game chat
mc.postToChat("Hello Minecraft World!")
# get coordinates of the player
cur_pos = mc.player.getPos()
print "The x coordinate is:" + str(cur_pos.x)
print "The y coordinate is:" + str(cur_pos.y)
print "The z coordinate is:" + str(cur_pos.z)
# or get the coordinates by
cur_x, cur_y, cur_z = mc.player.getPos()
print "The coordinates are:" + str(cur_x) +\
"," + str(cur_y) + "," + str(cur_z)
# set the player's position
mc.player.setPos(cur_x + 10, cur_y + 10, cur_z)
# set block
mc.setBlock(cur_x + 1, cur_y, cur_z, block.ICE.id)
# some block has additional properties
for i in range(0, 15):
	mc.setBlock(cur_x + 1, cur_y + i, cur_z, block.WOOL.id, i)
# set a volume of blocks
mc.setBlocks(cur_x + 1, cur_y + 1, cur_z + 1,\
cur_x + 6, cur_y + 6, cur_z + 6, block.GOLD_BLOCK.id)
# set a three dimensional shape with loops
r = 10
for x in range(r*-1,r):
 for y in range(r*-1,r):
  for z in range(r*-1,r):
   if x**2 + y**2 + z**2 < r**2:
    mc.setBlock(cur_x+x, cur_y+y+20, cur_z-z-20, block.GOLD_BLOCK)
# set TNT block or blocks to make a explosion by clicking with sword
cur_x, cur_y, cur_z = mc.player.getPos()
mc.setBlocks(cur_x+1,cur_y,cur_z,cur_x+4,cur_y+4,cur_z+4,block.TNT.id,1)
# set a gold block below the player untill the scrip is terminated by Ctrl+C
while 1:
	cur_x, cur_y, cur_z = mc.player.getPos()
	mc.setBlock(cur_x,cur_y-1,cur_z,block.GOLD_BLOCK.id)
	time.sleep(0.1)
