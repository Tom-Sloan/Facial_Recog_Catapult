import RPi.GPIO as GPIO
import time 


class motor_controls():
    
    def __init__(self):

        self.servoPIN = 19
        self.stepper_control_pins = [13,11,15,12]
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.servoPIN, GPIO.OUT)
        
        self.servo = GPIO.PWM(self.servoPIN, 50)
        self.current_duty_cycle = 6.5
        self.servo.start(self.current_duty_cycle)    
           
        self.halfstep_seq = [
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]
        ]

        for pin in self.stepper_control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
        
        
    def move_stepper(self):
        for i in range(512):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.stepper_control_pins[pin], self.halfstep_seq[halfstep][pin])
                # time.sleep(0.2)
        


    def move_servo(self, direction):
        if direction:
            if self.current_duty_cycle < 12.5:
                self.servo.ChangeDutyCycle(self.current_duty_cycle + 0.5)
        else:
            if self.current_duty_cycle > 2.0:
                self.servo.ChangeDutyCycle(self.current_duty_cycle - 0.5)


    def destroy(self):
        self.servo.stop()
        GPIO.cleanup()            


if __name__ == "__main__":

    s = motor_controls()
    # print('Done')
    # time.sleep(2)

    # s.move_servo(1)
    # print('Done1')
    # time.sleep(2)

    # s.move_servo(0)
    # print('Done1')
    # time.sleep(2)

    s.move_stepper()
    print('Done2')
    time.sleep(2)

    s.destroy()
    print('Done3')