import picamera
camera = picamera.PiCamera()
for i in range(1,4):
	try:
		input("press enter to continue...")
	except SyntaxError:
		pass
	camera.capture('image' + str(i) + '.jpg')
print('thanks')
