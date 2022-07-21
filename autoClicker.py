import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key, Controller

keyboard = Controller()

delay = 0.2
button = Button.left
start_stop_key = KeyCode(char='=')
exit_key = KeyCode(char='-')
save_key = KeyCode(char='e')
save_key2 = KeyCode(char='r')
save_key3 = KeyCode(char='t')

firstCoordinates = [None]*2
secondCoordinates = [None]*2
thirdCoordinates = [None]*2

numOfPositions = 2

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):dw  w w w
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            #print(mouse.position[0], mouse.position[1])
            while self.running:
                #mouse.click(self.button)
                #time.sleep(self.delay)
                #print(mouse.position)
                #mouse.move(578, 337)
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                time.sleep(self.delay)
                '''
                mouse.position = (firstCoordinates[0], firstCoordinates[1])
                mouse.click(self.button)
                time.sleep(self.delay)

                mouse.position = (secondCoordinates[0], secondCoordinates[1])
                mouse.click(self.button)
                time.sleep(self.delay)

                if numOfPositions == 3:
                    mouse.position = (thirdCoordinates[0], thirdCoordinates[1])
                    mouse.click(self.button)
                    time.sleep(self.delay)
                '''
                #mouse.move(839, 300)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
    elif key == save_key:
        firstCoordinates[0] = mouse.position[0]
        firstCoordinates[1] = mouse.position[1]
    elif key == save_key2:
        secondCoordinates[0] = mouse.position[0]
        secondCoordinates[1] = mouse.position[1]
    elif key == save_key3:
        thirdCoordinates[0] = mouse.position[0]
        thirdCoordinates[1] = mouse.position[1]

        #print(firstCoordinates[0], firstCoordinates[1])

with Listener(on_press=on_press) as listener:
    listener.join()
