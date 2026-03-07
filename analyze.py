import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load(file="data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load(file="data/frontLegSensorValues.npy")
matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=7)
matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()