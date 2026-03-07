import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import math
import time as t

# Create the world
physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Add gravity to the simulated world
p.setGravity(0, 0, -9.8)

# Add a floor to the world
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

# Add the cube object
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

# Back leg motor values
ampBackLeg = numpy.pi / 6
freqBackLeg = 4
offsetBack = numpy.pi / 2
targetBack = ampBackLeg * numpy.sin(freqBackLeg * numpy.linspace(0, 2 * numpy.pi, 1000) + offsetBack)

# Front leg motor values
ampFrontLeg = numpy.pi / 4
freqFrontLeg = 4
offsetFront = 0
targetFront = ampFrontLeg * numpy.sin(freqFrontLeg * numpy.linspace(0, 2 * numpy.pi, 1000) + offsetFront)

i = 0
for i in range(0, 1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetBack,
        maxForce = 100
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetFront,
        maxForce = 100
    )
    t.sleep(1/60)

numpy.save(file="data/backLegSensorValues.npy", arr=backLegSensorValues)
numpy.save(file="data/frontLegSensorValues.npy", arr=frontLegSensorValues)

p.disconnect()