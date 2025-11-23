from hal import hal_servo as servo 
from hal import hal_adc as adc_value 
import time

def main(): 
    servo.init()
    adc_value.init()
    while (True):
        raw = adc_value.get_adc_value(1) 
        print("ADC Raw:", raw)

        angle = int((1023 - raw) * 180 / 1023)

        print("Servo Angle:", angle)

        servo.set_servo_position(angle)
        time.sleep(0.5)

if __name__ == "__main__":
    main()