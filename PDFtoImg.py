import os
import tempfile
from pdf2image import convert_from_path
from PyPDF3 import PdfFileWriter, PdfFileReader

path="input_path"
output_folder_path="destination_path"

for filename in os.listdir(path):
	i = 0

	pdfname=path + filename
	inputpdf = PdfFileReader(open(pdfname,"rb"))

	maxPages = inputpdf.numPages
	print("Number of pages in PDF="+str(maxPages))


	for page in range(1, maxPages, 10):
	    pil_images = convert_from_path(poppler_path="C:/poppler-0.68.0/bin",pdf_path = pdfname, dpi=200, first_page=page,
	                                                     last_page=min(page + 10 - 1, maxPages), fmt= 'jpg',
	                                                     thread_count=1, userpw=None,
	                                                     use_cropbox=False, strict=False)
	    for image in pil_images:
	        image.save(filename[:-4] + '_' + str(i) + '.jpg', 'JPEG')
	        i = i + 1
