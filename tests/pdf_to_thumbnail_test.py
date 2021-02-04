from pynada import utils

pdf_file_path = './WPS8038.pdf'
thumbnail_path = utils.pdf_to_thumbnail(pdf_file_path, page_no = 1)
print(thumbnail_path)
