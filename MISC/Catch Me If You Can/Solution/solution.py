from PIL import Image
import random

def decode_image(image_path, key):
    img = Image.open(image_path).convert("RGB")  # Ensure image is in RGB mode
    img_data = img.load()
    width, height = img.size

    # Use the key to seed the random number generator (same as during encoding)
    random.seed(key)
    pixel_order = list(range(width * height))
    random.shuffle(pixel_order)

    binary_data = ""
    for pixel_index in pixel_order:
        x = pixel_index % width
        y = pixel_index // width
        r, g, b = img_data[x, y]  # Extract RGB values
        lsb = str(b & 1)  # Extract LSB of the blue channel
        binary_data += lsb

        # Stop decoding if we've reached the end of the message
        if len(binary_data) % 8 == 0 and len(binary_data) >= 8:
            # Check if the last 8 bits are a null character (end of message)
            if binary_data[-8:] == "00000000":
                break

    # Convert binary data to text
    text = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if byte == "00000000":  # Stop if null character is encountered
            break
        text += chr(int(byte, 2))  # Convert binary to character

    return text

# Example usage
decoded_message = decode_image("steg.png", "tabi3a-rabi3a")
print("Decoded Message:", decoded_message)