import os
from pdfrw import PdfReader, PdfWriter

new_dir = "rendered"
dirpath = os.getcwd()
new_dir = os.path.join(dirpath, new_dir)
try:
	os.mkdir(new_dir)
except Exception as e:
	pass
	

for path in os.listdir(dirpath):
    full_path = os.path.join(dirpath, path)
    new_path = os.path.join(new_dir, path)
    if os.path.isfile(full_path) and path.endswith(".pdf"):
        pdf = PdfReader(full_path)
        Root = pdf['/Root']
        pages = Root['/Pages']
        Kids = pages['/Kids']
        for kid in Kids:
            try:
                kid['/Contents'].pop(2)
            except Exception as e:
                pass
        writer = PdfWriter()
        writer.addpages(pdf.pages)
        writer.write(new_path)

