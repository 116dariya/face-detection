from PIL import Image, ImageDraw
im = Image.open("1.jpg")
rgb_im = im.convert("RGB").resize((100, 100))
size = rgb_im.size
h, w = size
pix = rgb_im.load()
colors = [(range(245,256),range(162,167),range(130,136))]
for y in range(0, w):
	for x in range(0, h):
		r, g, b = pix[x, y]
		if ((abs(r-255) < 5)and (abs(g-255) < 5) and (abs(b-255) <5)):
			pass
		if (r, g, b) in colors:
			r = 0
			g = 0 
			b = 0
			pix[x, y] = (r, g, b)

max_r = 0 
max_g = 0 
max_b = 0 

points = {}
for y in range(0, w):
	for x in range(0, h):
		r, g, b = pix[x, y]

		if ((abs(r-max_r) < 5) and (abs(g-max_g) < 5) and (abs(b-max_b) <5)):
			x = x1
			y = Y1
			points.update({'x1': X})
			points.update({'y1': Y})

			for y in range(Y, w):
				for x in range(X, h):
					if abs(r-max_r) < 5 and abs(g-max_g) < 5 and abs(b-max_b) <5:
						x = X2
						y = Y2
						points.update({'x2': X2})
						points.update({'y2': Y2})
if y2 == y1:
	if (x2 - x1) < 10:
		print("it is eyes!")


rgb_im.save("test02.jpg")

# 		if (r, g, b) in colors:
# 			colors[r, g, b] += 1
# 		else:
# 			colors[r, g, b] = 1
# max_color = 0, 0, 0
# max_value = 0
# for k in colors:
# 	r, g, b = k
# 	value = colors[r, g, b]
# 	if value > max_value:
# 		max_color = (r, g, b)
# 		max_value = value

# print(max_color)
# for y in range(0, size[1]):
# 	for x in range(0, size[0]):
# 		r, g, b = pix[x, y]
# 		#s = (r + g + b) // 3
# 		r = min(r + max_color[0]*2 + 40, 255)
# 		g = min(g + max_color[1]*2 + 20, 255) 
# 		b = min(b + max_color[2]*2, 255)
# 		pix[x, y] = (r, g, b)

rgb_im.save("test02.jpg")