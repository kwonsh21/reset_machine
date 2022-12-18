import machine
import time
# machine.reset()
p2 = machine.Pin(2)
servo = machine.PWM(p2,freq=50)
# duty for servo is between 30 - 130

def toggle(steps):
    
    servo.duty(130)
    step = int(100/steps)
    for i in range(1,steps+1):
        servo.duty(130-(step*i))
        time.sleep(0.01)
    time.sleep(0.5)
    servo.duty(130)
        # lap += 1
        
def switch():
    
    servo.duty(80)
    time.sleep(1)
    servo.duty(68)
    time.sleep(1)
    servo.duty(130)
        # lap += 1
    
# time.sleep(5)
# toggle(1)
switch()
# servo.duty(40)
time.sleep(1)
machine.reset()