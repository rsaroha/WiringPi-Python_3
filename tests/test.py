import wiringpi

io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO)
print (io.digitalRead(1))
print (io.analogRead(1))
