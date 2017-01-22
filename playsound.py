import os
import simpleaudio as sa
wave_obj1 = sa.WaveObject.from_wave_file("static/status1sound.wav")
wave_obj2 = sa.WaveObject.from_wave_file("static/status2sound.wav")
wave_obj3 = sa.WaveObject.from_wave_file("static/status3sound.wav")
wave_obj4 = sa.WaveObject.from_wave_file("static/status4sound.wav")
stop1 = False
stop2 = False
stop3 = False
stop4 = False
while stop1 == False:
    with open('static/testthis.txt') as fp:
        for line in fp:
        	if line == "1":
        	    print (line)
        	    stop1=True
        	    play_obj = wave_obj1.play()
        	    play_obj.wait_done()
while stop2 == False:
    with open('static/testthis.txt') as fp:
        for line in fp:
        	if line == "2":
        		print (line)
        		stop2=True
        		play_obj = wave_obj2.play()
        		play_obj.wait_done()
while stop3 == False:
    with open('static/testthis.txt') as fp:
        for line in fp:
        	if line == "3":
        	    print (line)
        	    stop3=True
        	    play_obj = wave_obj3.play()
        	    play_obj.wait_done()
while stop4 == False:
    with open('static/testthis.txt') as fp:
        for line in fp:
        	if line == "4":
        	    print (line)
        	    stop4=True
        	    play_obj = wave_obj4.play()
        	    play_obj.wait_done()



