from PIL import Image
import random

def encode_image(image_path, text, key):
    img = Image.open(image_path).convert("RGB")  
    binary_data = ''.join(format(ord(i), '08b') for i in text)

    img_data = img.load()
    width, height = img.size
    data_index = 0

    random.seed(key)
    pixel_order = list(range(width * height))
    random.shuffle(pixel_order)

    for pixel_index in pixel_order:
        if data_index >= len(binary_data):
            break
        x = pixel_index % width
        y = pixel_index // width
        r, g, b = img_data[x, y]  
        new_b = (b & 0xFE) | int(binary_data[data_index]) 
        img_data[x, y] = (r, g, new_b)  
        data_index += 1

    img.save("steg.png")

# Example usage
encode_image("pepper.jpg", "MRXSA6LPOUQGW3TPO4QGC3DFPBUXG4ZVGYYCIJBANEQGGYLOE52CA4TFNVSW2YTFOIQHI2DFEBWGC43UEB2HO3ZANZ2W2YTFOJZSA2DPNZSXG5DMPEQCYIDZN52SA3LBPEQGM2LOMQQHG33NMV2GQ2LOM4QHK43FMZ2WY3BAO5UXI2BANBSW2IB2FEQCY2JAORUGS3TLEBRGK5DXMVSW4IBXGUQGC3TEEA4TSLQ", "my_secret_key")
