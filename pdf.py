import os
import PyPDF2
import sys
os.system("cls")

# _______________________________________________________
# This takes a pdf file and adds a watermark on every page.
# _______________________________________________________
template = PyPDF2.PdfFileReader(open("super.pdf", "rb"))
watermark = PyPDF2.PdfFileReader(open("wtr.pdf", "rb"))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open("watermarked_output.pdf", "wb") as file:
        output.write(file)


# _________________________________________________________
# ADDS ALL THE CHOSEN PDF FILES AND MERGES THEM INTO 1 FILE
# ________________________________________________________
# inputs = sys.argv[1:]

# watermark = "watermark.pdf"

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write("super.pdf")


# pdf_combiner(inputs)

# __________________________________________________________
# opens dummy.pdf and saves a new copy of it in a tilted mode
# with the name "tilt.pdf"
#_____________________________________________________________#
# with open("dummy.pdf", "rb") as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open("tilt.pdf", "wb") as new_file:
#         writer.write(new_file)
