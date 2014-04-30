#rpi_sensor_board
    Driver: sensor.so -- all the sensor control API
    
    Demo:
      1. mag3110.py
        test mag3110, print the magnetic data from mag3110
        you can calibrate the mag sensor by mag3110_calibrate.py
    
      2. mpl3115a2.py
        test mpl3115a2, print the Temperature and barometer or
        altimeter data from mpl3115a2
    
      3. mma8491q.py
        test mma8491q, print the Acceleration data from mma8491q
    
    All the sensor demo are working in python2.7
    
    Application:
      1. sensor_website.py
        Read the sensor data and push it to website. The script
        is working in python3.x

    Web pages
      1. compass.html
	This page display the mag3110 sensor data as a compass, you can turn the sensor board aroud, then the compass on the page will do the corresponding rotation.

      2. temper.html
	This page display the temperature value get from mpl3115 sensor, you will touch the sensor board, then the value will change correspondingly

      3. gsensor.html
	This page has a small car controled by the mma8491 sensor, you can turn the board up, down, left or right, the car will move as your board motion

