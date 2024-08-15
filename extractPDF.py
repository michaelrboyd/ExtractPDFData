#import the library
import fitz

file = 'sample.pdf'

#open the fitz file
pdf = fitz.open(file)

#select the page number
image_list = pdf.getPageImageList(0)

#applying the loop
for image in image_list:
   xref = image[0]
   pix = fitz.Pixmap(pdf, xref)
   if pix.n < 5:
       pix.writePNG(f'{xref}.png')
   else:
       pix1 = fitz.open(fitz.csRGB, pix)
       pix1.writePNG(f'{xref}.png')
       pix1 = None
   pix = None

#print the images
print(len(image_list), 'detected')
