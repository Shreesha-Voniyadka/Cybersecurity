''' Using pynput which provides the control over mouse and keyboard '''
import sys
from pynput.mouse import Controller
from pynput import keyboard
class KeyLog:
    ''' Logger class '''
    def __init__(self):
         # ...or, in a non-blocking fashion:
        pass
    
    def on_press(self,key):
        ''' on press '''
        var = key

    def on_release(self,key):
        ''' on release '''
        if key == keyboard.Key.esc:
            # Stop listener
            sys.exit(0)
    def mouserpointer(self):
        '''read mouse controller'''
        mouse = Controller()
        # Read pointer position
        print(f'The current pointer position is {mouse.position}')

    # Collect events until released
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
    listener = keyboard.Listener(on_press=on_press,on_release=on_release)
    listener.start()

   
if __name__=="__main__":
    keylogobj = KeyLog()
