Last login: Mon Jan 20 17:33:42 on ttys012
(base) shaurya@Shauryas-MacBook-Air-2 ~ % ssh raj@192.168.83.212
raj@192.168.83.212's password: 
Linux raspberrypi 6.6.62+rpt-rpi-2712 #1 SMP PREEMPT Debian 1:6.6.62-1+rpt1 (2024-11-25) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jan 25 04:38:29 2025
(venv-ardupilot) raj@raspberrypi:~ $ deactiavte
-bash: deactiavte: command not found
(venv-ardupilot) raj@raspberrypi:~ $ deactivate
raj@raspberrypi:~ $ ls
25.py      camera2.py         focus2.py      rtl8812au
BMP        camera_test        focus3.py      scripts
BMP180     captured_images    gps.py         sensor
Bookshelf  ch.py              heartbeat.py   sensor-isdc
Desktop    check.py           isdc           sensor2.py
Documents  code.py            mav.parm       sensorR.py
Downloads  connect.py         mav.tlog       takeoff.py
Music      connection.py      mav.tlog.raw   test.py
Pictures   delivery_drone     mavproxy_env   test1.py
Public     dlib               myenv          test_camera_images
Sensor     drone_check.py     nitish_bmp     venv
Templates  drone_gps.py.save  nitish_ms8607  venv-ardupilot
Videos     fetch.py           nitish_test    venv-dronekit
ardupilot  focus.py           piTunnel       yuvaan
raj@raspberrypi:~ $ source venv/bin/activate
(venv) raj@raspberrypi:~ $ cd sensor-isdc
(venv) raj@raspberrypi:~/sensor-isdc $ ls
msAllData.py    sensor_code2.py  sensor_final   sp_pr.py       storee.py
nit.py          sensor_data.csv  smbus_test.py  sp_temp.py
nit2.py         sensor_data.py   sp_hum.py      sp_temp_pr.py
sensor_code.py  sensor_data1.py  sp_hum1.py     sparklex.py
(venv) raj@raspberrypi:~/sensor-isdc $ nano nit2.py
(venv) raj@raspberrypi:~/sensor-isdc $ python3 storee.py
Traceback (most recent call last):
  File "/home/raj/sensor-isdc/storee.py", line 1, in <module>
    import smbus2
ModuleNotFoundError: No module named 'smbus2'
(venv) raj@raspberrypi:~/sensor-isdc $ nano storee.py

  GNU nano 7.2                        storee.py                                 
    try:
        print("Initializing MS8607 sensor...")
        sensor.reset_pressure_sensor()

        while True:
            # Get temperature and pressure data
            temperature, pressure = sensor.get_sensor_data()

            # Print the data
            print(f"Temperature: {temperature:.2f}   C, Pressure: {pressure:.2f>

            # Write data to CSV
            write_to_csv(file_name, temperature, pressure)

            # Wait for 1 second before the next reading
            time.sleep(1)

    except Exception as e:
        print(f"Error: {e}")
