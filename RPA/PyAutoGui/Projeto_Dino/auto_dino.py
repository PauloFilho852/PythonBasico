from PIL import ImageGrab
import pyautogui as p


while True:
    image = ImageGrab.grab().convert('L')
    data = image.load()

    for x in range(765, 805):
        for y in range(210, 230):

            if data[x, y] < 100:
                print(f'(x,y) = {data[x, y]}')
                p.keyDown('up')
                break
        if data[x, y] < 100:
            break

   # image.show()
   # break
