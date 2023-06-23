import RPi.GPIO as GPIO
import time

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings

# 모터 핀 번호 설정
motor1_pin = 18
motor2_pin = 19
GPIO.setup(motor1_pin, GPIO.OUT)
GPIO.setup(motor2_pin, GPIO.OUT)

# 모터 제어(pwm) 설정
# 50Hz
motor1 = GPIO.PWM(motor1_pin, 50)
motor2 = GPIO.PWM(motor2_pin,50)

# 모터 초기 시작
motor1.start(0)
motor2.start(0)

# 주축 모터 회전 함수
def under_rotate_motor(motor, angle):
    duty_cycle = .25 + (10.5 - 2.5) * angle / 360
    motor.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
    motor.ChangeDutyCycle(0)

# 카드 모터 회전 함수
def top_rotate_motor(motor, angle):
    duty_cycle = .5 + (10.5 - 2.5) * angle / 360
    motor.ChangeDutyCycle(duty_cycle)
    time.sleep(1.25)
    motor.ChangeDutyCycle(0)


def motor_function():
    while True:
    # 사용자 입력 받음
        start = input("시작하려면 's'를 입력하세요: ")

        # 입력이 "s"이면 동작 시작
        if start == "s":
            num_people = int(input("인원 수를 입력하세요 (최대 4명): "))

            if (num_people < 0 and num_people > 4):
                print("인원수를 잘못 입력했습니다. 다시 입력해주세요.")


            num_people = min(4, num_people)

            current_count = 1

            if current_count <= num_people:
                # 1번 모터 작동
                under_rotate_motor(motor1, 360)

                # 1번 모터가 작동을 마치면 숫자를 라즈베리파이로 보냄
                time.sleep(1)

                # 2번 모터 작동
                top_rotate_motor (motor2, 450)
                   
                 # 2번 모터가 작동을 마치면 숫자를 증가시킴 후 라즈베리파이로 보냄
                current_count += 1
                time.sleep(1)

                # 현재 숫자가 인원수를 넘으면 반복 종료
                if current_count > num_people:
                    break
            
        # 모터 정지 및 GPIO 클린업
        motor1.stop()
        motor2.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    motor_function()
