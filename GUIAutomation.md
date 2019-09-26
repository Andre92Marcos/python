
We are gonna Use the module pyautogui:
	pip install pyautogui


pyautogui.size():

	returns the screen resolution


pyautogui.position(): 

	returns the current mouse position

pyautogui.moveTo(x,y, duration):

	moves the cursor to x and y coordinates in duration seconds

pyautogui.movRel(xOffset, yOffset, duration)

	moves the cursor to the x and y relative to the current mouse position

pyautogui.click(x,y)
pyautogui.doubleClick(x,y)
pyautogui.rightClick(x,y)
pyautogui.leftClick(x,y)

	moves the cursor to x and y and clicks

pyautogui.dragRel(x,y,duration)
	same as move but now it holds the left mouse button


Pyautogui Failsafe:

	If you want to cancel a pyautogui execution, move the mouse to (0,0) top, left corner to cancel the execution


pyautogui.displayMousePosition()

	Displays the current mouse position in real time.

	Good to find out widgets positons.


