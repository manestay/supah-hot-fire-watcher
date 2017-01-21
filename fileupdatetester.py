import time
count = 1
while True:
	time.sleep(1) # delays for 5 seconds
	text_file = open("static/testthis.txt", "w")
	output=count%4+1
	print (output)
	text_file.write("%s" % output)
	text_file.close()
	count=count+1

