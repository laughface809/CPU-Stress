import os

if os.getloadavg()[2] >= 3.3:
	print('>>critical')
if os.getloadavg()[2] >= 2.8:
	print('>>be-aware')
if os.getloadavg()[1] >= 1:
	print('>>average')
elif os.getloadavg()[0] >= 2:
	print('>>average-2')
elif os.getloadavg()[0] <= 0.6:
	print('>>slow')
else:
	print('>>smooth')