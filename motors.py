import wiringpi as wp

class Motors:

    def __init__(self):
        self.wp = wp
        self.wp.wiringPiSetupGpio()

        self.leftMotor = [4, 17]
        self.rightMotor = [2, 3]

        self.enL = 18
        self.enR = 13

        self.avgSpeed = 512
        self.init_pins()

    def init_pins(self):
        for pin in self.leftMotor:
            self.wp.pinMode(pin, self.wp.OUTPUT)
        for pin in self.rightMotor:
            self.wp.pinMode(pin, self.wp.OUTPUT)

        self.wp.pinMode(self.enL, self.wp.PWM_OUTPUT)
        self.wp.pinMode(self.enR, self.wp.PWM_OUTPUT)

    def forward(self):
        self.wp.digitalWrite(self.leftMotor[0], self.wp.HIGH)
        self.wp.digitalWrite(self.leftMotor[1], self.wp.LOW)

        self.wp.digitalWrite(self.rightMotor[0], self.wp.HIGH)
        self.wp.digitalWrite(self.rightMotor[1], self.wp.LOW)

        self.wp.pwmWrite(self.enL, self.avgSpeed)
        self.wp.pwmWrite(self.enR, self.avgSpeed)

    def backward(self):
        self.wp.digitalWrite(self.leftMotor[0], self.wp.LOW)
        self.wp.digitalWrite(self.leftMotor[1], self.wp.HIGH)

        self.wp.digitalWrite(self.rightMotor[0], self.wp.LOW)
        self.wp.digitalWrite(self.rightMotor[1], self.wp.HIGH)

        self.wp.pwmWrite(self.enL, self.avgSpeed)
        self.wp.pwmWrite(self.enR, self.avgSpeed)

    def left(self):
        self.wp.digitalWrite(self.leftMotor[0], self.wp.LOW)
        self.wp.digitalWrite(self.leftMotor[1], self.wp.HIGH)

        self.wp.digitalWrite(self.rightMotor[0], self.wp.HIGH)
        self.wp.digitalWrite(self.rightMotor[1], self.wp.LOW)

        self.wp.pwmWrite(self.enL, self.avgSpeed)
        self.wp.pwmWrite(self.enR, self.avgSpeed)

    def right(self):
        self.wp.digitalWrite(self.leftMotor[0], self.wp.HIGH)
        self.wp.digitalWrite(self.leftMotor[1], self.wp.LOW)

        self.wp.digitalWrite(self.rightMotor[0], self.wp.LOW)
        self.wp.digitalWrite(self.rightMotor[1], self.wp.HIGH)

        self.wp.pwmWrite(self.enL, self.avgSpeed)
        self.wp.pwmWrite(self.enR, self.avgSpeed)

    def stop(self):
        self.wp.digitalWrite(self.leftMotor[0], self.wp.LOW)
        self.wp.digitalWrite(self.leftMotor[1], self.wp.LOW)

        self.wp.digitalWrite(self.rightMotor[0], self.wp.LOW)
        self.wp.digitalWrite(self.rightMotor[1], self.wp.LOW)

        self.wp.pwmWrite(self.enL, 0)
        self.wp.pwmWrite(self.enR, 0)
