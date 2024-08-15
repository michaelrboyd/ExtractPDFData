
#import OS
import os
import fitz

# Ask for user to give path to pdf files  ..\..\pdf\Marzo 2022
def getPDFlist():
    #PDFpath = input("enter the Path to PDF files: ")
    #print("path = " + PDFpath)

    PDFlist = os.listdir(inputPath)
    #print out a list of pdf files found
    #for x in PDFlist:
    #    if x.endswith(".pdf"):    # Prints only pdf file
    #        print(x)

    #print list of files to a text files
    filecnt = 0
    logFile = os.path.join(outputPath, 'log.txt')
    f = open(logFile, 'w')
    for y in PDFlist:
        f.write(y)
        f.write('\n')
        filecnt = filecnt + 1
    f.write("Total numner of files = %d" % filecnt)
    f.close()

    print("Total number of PDF files: %d \n" % filecnt)

    return PDFlist
#============================================================
def extractImages(PDFfile):
    #open the fitz file
    inputPDF = os.path.join(inputPath,PDFfile)
    #print(inputPDF)
    nameonly = os.path.splitext(PDFfile)[0]
    #print(nameonly)
    outputPNG = os.path.join(outputPath,nameonly + ".png")
    #print(outputPNG)
    #
    pdf = fitz.open(inputPDF)
    #select the page number
    image_list = pdf.getPageImageList(0)
    #applying the loop
    for image in image_list:
       xref = image[0]
       width = image[2]
       if width > 750:
           pix = fitz.Pixmap(pdf, xref)
           if pix.n < 5:
               pix.writePNG(outputPNG)
           else:
               pix1 = fitz.open(fitz.csRGB, pix)
               pix1.writePNG(outputPNG)
               pix1 = None
           pix = None

    #print the images
    # print(len(image_list), 'detected')

    return len(image_list)
# ==================MAIN FUNCTION ============================
# Hardcode in the input and output paths
inputPath = "..\..\pdf\Marzo 2022"
outputPath = ".\output"
# get the list of files
myfiles = getPDFlist()
#extract the images from each file
for i in myfiles:
    num = extractImages(i)
