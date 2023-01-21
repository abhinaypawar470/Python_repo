import pyautogui as spam
import time

def spammsg():
    limit = int(input("Enter the number of message :"))
    msg = input("The message :")
    print("You have 5 seconds to go to your messenger and click !")
    time.sleep(5) 
    i = 0 
    while i <= limit:
        spam.typewrite(msg)
        spam.press('Enter')
        i += 1
        
spammsg()