import pybullet as p
import pybullet_data
import time as t

# Create the world
physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Add gravity to the simulated world
p.setGravity(0, 0, -9.8)

# Add a floor to the world
planeId = p.loadURDF("plane.urdf")
planeId = p.loadURDF("body.urdf")

# Add the cube object
p.loadSDF("world.sdf")

i = 0
for i in range(0, 10000):
    p.stepSimulation()
    t.sleep(1/60)
    print(i)

p.disconnect()
