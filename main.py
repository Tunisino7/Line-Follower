import time
import motors
import qtr
import wiringpi as wp

digitalSensors = [0, 0, 0, 0, 0, 0, 0, 0]
weights = [-4, -3, -2, -1, 1, 2, 3, 4]
weightedVals = [0, 0, 0, 0, 0, 0, 0, 0]


P = 0
I = 0
D = 0
correction = 0
error = 0
previous_error = 0
total_weight = 0
absolute_weight = 0

# it can be changed by calibration

min_speed = 524
new_speed = 0

kp = 50
kd = 0
ki = 0
#######

if __name__ == "__main__":

    mySensors = qtr.QTR_8RC()
    myMotors = motors.Motors()

    mySensors.calibrate_main()

    try:
        while 1:
            total_weight = 0
            absolute_weight = 0
            mySensors.read_calibrated()
            line = ''
            for i in range(0, 8):
                if mySensors.sensorValues[i] < 300:
                    digitalSensors[i] = 1
                else:
                    digitalSensors[i] = 0
                weightedVals[i] = weights[i]*digitalSensors[i]
                total_weight += weightedVals[i]
                absolute_weight += abs(weightedVals[i])

                line = line + str(digitalSensors[i]) + ' * '

            print(line)
            print(total_weight)

            current_weight = abs(total_weight)
            target_weight = 0
            error =  current_weight - target_weight
            P = error * kp

            I = (error+previous_error) * ki
            D = kd * (error - previous_error)

            correction = P + I + D
            new_speed = min_speed + correction
            print("New speed: " + str(new_speed))
            previous_error = error

            if (new_speed>1024):
                new_speed=1024
            if(absolute_weight == 20):
                myMotors.left()
                time.sleep(0.2)
            else:
                if(total_weight == 0):
                    myMotors.avgSpeed = 1024
                    myMotors.forward()
                elif(total_weight < 0):
                    myMotors.avgSpeed = new_speed
                    myMotors.right()
                else:
                    myMotors.avgSpeed = new_speed
                    myMotors.left()

    except Exception as e:
        print str(e)
