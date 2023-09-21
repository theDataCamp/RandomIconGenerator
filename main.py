# import pyautogui
import random

from PIL import Image,ImageGrab


def capture_screenshot():
    return ImageGrab.grab()


class IconGenerator:
    def __init__(self, size=256, output_png='forIcon.png', output_icon='AppIcon.ico'):
        self.size = size
        self.output_png = output_png
        self.output_icon = output_icon
        self.icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256,256)]

    def capture_random_square(self, image):
        # Get image dimensions
        width, height = image.size

        # Generate random coordinates for the top-left corner of the square
        x = random.randint(0, width - self.size)
        y = random.randint(0, height - self.size)

        # Crop the image to the specified square size
        return image.crop((x, y, x + self.size, y + self.size))

    def generate_icon(self):
        # Take a screenshot
        screenshot_image = capture_screenshot()

        # Get a random square from the screenshot
        icon_image = self.capture_random_square(screenshot_image)

        # Save the square
        icon_image.save(self.output_png)
        logo = Image.open(self.output_png)

        logo.save(self.output_icon, format='ICO', sizes=self.icon_sizes)


if __name__ == '__main__':
    generator = IconGenerator()
    generator.generate_icon()
