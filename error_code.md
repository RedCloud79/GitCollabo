Traceback (most recent call last):
  File "/home/pi/teampro/upper_moter.py", line 87, in <module>
    main()
  File "/home/pi/teampro/upper_moter.py", line 73, in main
    motor1 = motor_rotate(motor1, input_people, MOTOR1_PIN, ROTATE_TIME)
  File "/home/pi/teampro/upper_moter.py", line 28, in motor_rotate
    motor_start(motor_pin)
  File "/home/pi/teampro/upper_moter.py", line 18, in motor_start
    pi.set_servo_pulsewidth(motor_pin, MAX_PW)
  File "/usr/lib/python3/dist-packages/pigpio.py", line 1678, in set_servo_pulsewidth
    return _u2i(_pigpio_command(
  File "/usr/lib/python3/dist-packages/pigpio.py", line 1025, in _pigpio_command
    sl.s.send(struct.pack('IIII', cmd, p1, p2, 0))
AttributeError: 'NoneType' object has no attribute 'send'
