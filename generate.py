import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-5, y, z], size=[length, width, height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    # Link 0 position
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[length, width, height])
    # Joint 0-1 position
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1.0])
    # Link 1 position
    pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, -0.5], size=[length, width, height])
    # Joint 1-2 position
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1.0])
    # Final link for back leg
    pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, -0.5], size=[length, width, height])
    pyrosim.End()

Create_World()
Create_Robot()