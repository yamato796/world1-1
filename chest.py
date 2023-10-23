from escpos.printer import Usb
import RPi.GPIO as GPIO

def most_frequent(List):
	return max(set(List), key = List.count)

def print_out(index):
	p = Usb(0x04b8, 0x0202, 0, profile="TM-T88III")
	p.text("Hello Traveler!\n")
	p.qr(f"Congratulate! You are number {index} to open the chest")
	p.cut()

#TODO: gpio setup
PIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
reset_flag = 0


""" Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
while True:
	flags = []
	for i in range(0,5):
		flags.append(GPIO.input(PIN))

	avg_flag = most_frequent(flags)
	if reset_flag == 1:
		if avg_flag:
			with open('./count','r') as f: 
				index = int(f.readline())

			print_out(index)
			index = index + 1 
			with open('./count','w') as f:
				f.write(index)

	elif reset_flag == 0:
		if avg_flag:
			reset_flag = 1