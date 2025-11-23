from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from hal import hal_buzzer as buzzer
password = []
index = 0
lcd = LCD.lcd()
buzzer.init()
statement = "Enter PIN: "

def key_pressed(key):
    global index, password, statement
    password.append(key)
    print(password)
    statement = statement + "*"
    lcd.lcd_display_string(statement,2)
    if(len(password) >= 4):
        if(password == [1,2,3,4]):
            lcd.lcd_clear()
            lcd.lcd_display_string("Safe Unlocked", 1)
        else: 
            index = index + 1
            lcd.lcd_clear()
            lcd.lcd_display_string("Wrong PIN",1)
            buzzer.turn_on_with_timer(1)
            password.clear()
            statement = "Enter PIN: "
            if(index >= 3):
                lcd.lcd_clear()
                lcd.lcd_display_string("Safe Disabled",1)
            else: 
                lcd.lcd_display_string("Safe Lock",1)
                lcd.lcd_display_string("Enter PIN: ",2)


def main(): 
    lcd.lcd_display_string("Safe Lock",1)
    lcd.lcd_display_string("Enter PIN: ",2)
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()


if __name__ == "__main__":
    main()