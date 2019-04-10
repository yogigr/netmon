#write by Yogi gilang Ramadhan
#github https://github.com/yogigr

import threading
import subprocess
from subprocess import Popen, PIPE
from pydub import AudioSegment
from pydub.playback import play
import logging

emergency = AudioSegment.from_wav("/home/ogi/netmon/emergency.wav")
hosts = ['8.8.8.8']
interval = 6

def writeLog(msg):
	logging.basicConfig(filename='/home/ogi/netmon/netmon.log', format='%(asctime)s - %(message)s', level=logging.DEBUG)
	logging.debug(msg)

def pinging(hosts, emergency):
	for h in hosts:
		toping = Popen(['ping', '-c', '1', h], stdout=PIPE)
		output = toping.communicate()[0]
		hostlive = toping.returncode
		if hostlive != 0:
			play(emergency)
			writeLog(h + ' is unreachable')

def startTimer():
	threading.Timer(interval, startTimer).start()
	pinging(hosts, emergency)


startTimer()