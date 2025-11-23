from threading import Thread,Lock
from hal import hal_lcd as LCD
import time 

lcd = LCD.lcd()
lcd_lock = Lock()

def time_show():
    while True:
        local_time = time.localtime()
        
        time_string_hour = time.strftime("%H %M %S", local_time)    
        date_string_year = time.strftime("%Y %m %d", local_time)
        with lcd_lock: 
            lcd.lcd_display_string(time_string_hour, 1)   
            lcd.lcd_display_string(date_string_year, 2) 

        time.sleep(1)   
def show_colon(): 
    show = True
    while True:
        if show: 
            ch = ":"
        else: 
            ch = " "
        with lcd_lock: 
        
            lcd.lcd_display_string(ch, 1, 2)
            lcd.lcd_display_string(ch, 1, 5)
            lcd.lcd_display_string(ch, 2, 4)
            lcd.lcd_display_string(ch, 2, 7)
        show = not show
        time.sleep(1)


def main(): 
    t1 = Thread(target=time_show)
    t2 = Thread(target=show_colon)
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()