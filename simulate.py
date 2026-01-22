import pybullet as p
import time as t

physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")

i = 0
for i in range(0, 1000):
    p.stepSimulation()
    t.sleep(1/10)
    print(i)

p.disconnect()
