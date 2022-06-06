"""import time
import msvcrt

class keyboardDisable():

    def start(self):
        self.on = True

    def stop(self):
        self.on = False

    def __call__(self): 
        while self.on:
            msvcrt.getwch()


    def __init__(self):
        self.on = False
        import msvcrt

disable = keyboardDisable()
disable.start()
time.sleep(10)
disable.stop()"""

#### Blocking Keyboard ####
import keyboard

#blocks all keys of keyboard
for i in range(150):
    keyboard.block_key(i)