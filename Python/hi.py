#Example form the Presentation
'''from PIL import Image

image = Image.open("Imagenes/cat.jpg")

w = image.width
h = image.height

image.thumbnail((400, 400))

image.save('cat_small.jpg')

image.show()'''


#Task 1

'''from PIL import Image

image = Image.open("Imagenes/task1.jpg")

image.thumbnail((1024, 768))
image.save('Imagenes/pic-1024x764.jpg')
image.show()

image.thumbnail((600, 400))
image.save('Imagenes/pic-600x400.jpg')
image.show()

image.thumbnail((100, 100))
image.save('Imagenes/pic-600x400.jpg')
image.show()'''

#Copy part of an image
'''from PIL import Image

image = Image.open("Imagenes/cat2.jpg")

region = image.crop((100, 10, 200, 215))


region = region.transpose(Image.ROTATE_90)                      #Rotate image 90º

region = region.rotate(45, expand = True, fillcolor = "white")  #Rotate cat 45º (diferent than transponse)

image.paste(region, (100, 125))

region.show()'''



#Task 2

from PIL import Image

image = Image.open("Imagenes/task2_1.jpg")

image.thumbnail((300, 300))


width = image.width
height = image.height


half_width = width // 2
half_height = height // 2


top_left = image.crop((0, 0, half_width, half_height))

top_right = image.crop((half_width, 0, width, half_height))

bottom_left = image.crop((0, half_height, half_width, width))

bottom_right = image.crop((half_width, half_height, width, height))




top_left = top_left.transpose(Image.ROTATE_90)

top_right = top_right.transpose(Image.ROTATE_180)

bottom_left = bottom_left.transpose(Image.ROTATE_180)

bottom_right = bottom_right.transpose(Image.ROTATE_270)


new_image = Image.new("RGB", (width, height))
new_image.paste(top_left, (0, 0))
new_image.paste(top_right, (half_width, 0))
new_image.paste(bottom_left, (0, half_height))
new_image.paste(bottom_right, (half_width, half_height))

# Save and display the result
new_image.save("output_task2_thumbnail.jpg")
new_image.show()

#Task 3

'''from PIL import Image

im1 = Image.open("Imagenes/cat.jpg")

im2 = Image.open("Imagenes/flashback.jpg")

width_1 = im1.width
height_1 = im1.height


im2 = im2.resize((width_1, height_1))

res = Image.blend(im1, im2, 0.25)
res.show()
'''


