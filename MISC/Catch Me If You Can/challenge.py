from PIL import Image
import random

def encode_image(image_path, text, key):
    img = Image.open(image_path).convert("RGB")  # Ensure image is in RGB mode
    binary_data = ''.join(format(ord(i), '08b') for i in text)

    img_data = img.load()
    width, height = img.size
    data_index = 0

    # Use the key to seed the random number generator
    random.seed(key)
    pixel_order = list(range(width * height))
    random.shuffle(pixel_order)

    for pixel_index in pixel_order:
        if data_index >= len(binary_data):
            break
        x = pixel_index % width
        y = pixel_index // width
        r, g, b = img_data[x, y]  # Extract RGB values
        new_b = (b & 0xFE) | int(binary_data[data_index])  # Modify LSB of blue channel
        img_data[x, y] = (r, g, new_b)  # Update pixel
        data_index += 1

    img.save("steg.png")

# Example usage
encode_image("pepper.jpg", "NHD{W444444_H4$$4444AAN_Rak_3ajebni}", "tabi3a-rabi3a")