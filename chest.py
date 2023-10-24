from escpos.printer import Usb
import RPi.GPIO as GPIO

def most_frequent(List):
	return max(set(List), key = List.count)

def print_out(index):
	#p = Usb(0x04b8, 0x0e11, 0, profile="TM-T88II")
	p = Usb(0x04b8, 0x0e11, 0)
	p.set('CENTER',width=2,height=2)
	p.text("Hello Traveler!\n\n")
	p.text("\n")
	p.qr(f"Congratulate! You are number {index} to have open this chest!", size=10)
	p.cut(mode='PART')

PIN = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
reset_flag = 0
#print(GPIO.input(PIN))
#print_out(11)

""" Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
index = 0
while True:
	flags = []
	for i in range(0,60):
		flags.append(GPIO.input(PIN))
    
	avg_flag = most_frequent(flags)
	#print(avg_flag)
	#print(flags)
	if reset_flag == 1:
		#print('reset')
		if avg_flag == 0:
			#with open('./count','r') as f:
			#	index = int(f.readline())
			#f.close()
			#print_out(index)
			print('print la')
			index = index + 1 
			#with open('./count','w') as f:
			#	f.write(str(index))
			#f.close()
			reset_flag = 0

	elif reset_flag == 0:
		#print('non-reset')
		if avg_flag == 1:
			#print('reset')
			reset_flag = 1


