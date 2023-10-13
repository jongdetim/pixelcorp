import requests
import json
import PIL.Image as Image

clamp = lambda n, minn, maxn: max(min(maxn, n), minn)

url = 'https://pixelcorp.nl/api/single'
headers = {'Content-Type': 'application/json'}

img = Image.open(r'C:\Users\Tim\Desktop\200-fractal.jpg')
# img.show()

start_pos = (0, 0)

width = img.size[0]
print(width)
for i, pixel_color in enumerate(img.getdata()):
    # clamp between 0 and 199 for x and y
    x = clamp(start_pos[0] + (i % width), 0, 199)
    y = clamp(start_pos[1] + (i // width), 0, 199)

    # print(pixel_color)
    # Pixel information in JSON format.
    pixel = {'x': x, 'y': y, 'color': pixel_color, 'key': 'NDYQMNCY' }
    response = requests.post(url, headers=headers, data=json.dumps(pixel))

    if response.ok:
        print("Success!", response.content.decode())
    else:
        print("Error!", response.content.decode())
