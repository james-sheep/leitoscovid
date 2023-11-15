if perigo.value == False:
           
         kit.continuous_servo[2] .throttle = 0
         kit.continuous_servo[1].throttle = 0
         kit.servo[5].angle = 0
         sleep(0.1)
         kit.servo[5].angle = 160
         sleep(0.1)
         kit.servo[5].angle = 0
         sleep(0.1)
         kit.servo[5].angle = 160
         sleep(0.1)
         kit.servo[5].angle = 0
         sleep(0.1)
         kit.servo[5].angle = 160
         sleep(0.1)
         kit.servo[5].angle = 0
         sleep(0.1)
         kit.servo[5].angle = 60