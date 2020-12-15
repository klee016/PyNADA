from PIL import Image, ImageDraw, ImageFont

def text_to_thumbnail(text):
	img = Image.new('RGB', (300,300), color=(255,255,255))
	font = ImageFont.truetype("arial", 45)
	d = ImageDraw.Draw(img)
	d.text((20,80), text, (0, 0, 0), font=font)

	img.save('temp_thumbnail.jpg')