from PIL import Image, ImageDraw, ImageFont
import pdf2image
from pathlib import Path
import urllib.request
import shutil
import hashlib

def text_to_thumbnail(text):
	img = Image.new('RGB', (300,300), color=(255,255,255))
	font = ImageFont.truetype("arial", 45)
	d = ImageDraw.Draw(img)
	d.text((20,80), text, (0, 0, 0), font=font)
	img.save('temp_thumbnail.jpg')

	return Path('./temp_thumbnail.jpg')

def pdf_to_thumbnail(pdf_file_path, page_no):
	pdf_file_path = Path(pdf_file_path)
	thumbnail_path = pdf_file_path.with_suffix('.jpg')
	thubmnail = pdf2image.convert_from_path(pdf_file_path, first_page=page_no, last_page=page_no)[0]
	thubmnail.save(thumbnail_path, 'JPEG')

	return thumbnail_path

def download_file(url, output_fname, mode):
	output_file = output_fname
	with urllib.request.urlopen(url) as response, open(output_file, mode) as out_file:
		shutil.copyfileobj(response, out_file)
		
def MD5(ctyp, titl):
	uuid = hashlib.md5((''.join((ctyp, titl))).encode()).hexdigest()
	return uuid		
