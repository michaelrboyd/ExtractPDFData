# =======================================
# extracttables.property
# Given a directory of PDF files
# this program will extract the data from the file and output a table
#
# Author: Michael Boyd
# Date: 6/6/2022
# =======================================
import camelot
import os
import pandas as pd
import numpy as np
from csv import writer

# File locations
#inputPath = os.path.join("..", "..", "pdf", "test")
#outputPath = os.path.join(".","table")
#tablefile = os.path.join(outputPath, 'table.csv')

inputPath = os.path.join("..", "..", "pdf", "hotels")
outputPath = os.path.join("..", "..", "pdf", "hotels")
tablefile = os.path.join(outputPath, 'hotels.csv')




# Function getPDFlist looks in the inputPath directory and returns a list
# of filenames to be used
def getPDFlist():
    PDFlist = os.listdir(inputPath)
    filecnt = 0
    logFile = os.path.join(outputPath, 'log_tables.txt')
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

def extractTables(PDFfile):
    inputPDF = os.path.join(inputPath,PDFfile)
    # https://www.geeksforgeeks.org/python-pandas-dataframe/
    # extract all the tables in the PDF file
    tables = camelot.read_pdf(inputPDF)

    # number of tables extracted
    print("Total tables extracted:", tables.n)

    # print the first table as Pandas DataFrame
    print(tables[0].df)

    mypanda = tables[0].df

    posarray = []
    myarray = [None] * (len(spHeaders)+1)
    #print( range(len(spHeaders)) )
#    print( mypanda.loc[mypanda[0] == 'CH'])
    temp = mypanda[mypanda[0].str.contains("interno")]
    print( temp.iat[0,1])

    for z in range(len(spHeaders)):
#        temp = mypanda[mypanda[0].str.contains(spHeaders[z])]
#        print(spHeaders[z])
#        print(z)
#        print(temp.iat[0,1])
        myarray[z] = temp.iat[0,1]
        # Problem is here - if the value is not found what is the error handling?
#        print (tables.loc[tables[0] == spHeaders[3]])
#        found = mypanda.loc[mypanda[0] == spHeaders[3]].index.values[0]
#        print(found)
    #    found = mypanda.loc[mypanda[0] == spHeaders[z]].index.values[0]
    #    print(found)
#        found = mypanda.loc[mypanda[0] == spHeaders[z]].index.values[0]
#        print(found)

        #posarray[z] = mypanda.loc[mypanda[0] == spHeaders[z]].index.values[0]
        #myarray[z] = mypanda.at[posarray[z], 1]
    #
    #print(posarray)
    #mydate = mypanda.at[2, 1]
    #myapp = mypanda.at[3, 1]
    #mypart = mypanda.at[5, 1]
    #mycable = mypanda.at[6, 1]
    #mycross = mypanda.at[7, 1]
    #myarray = [mydate, myapp, mypart, mycable, mycross]
#    print(myarray)
    # export individually as CSV
    #tables[0].to_csv("test.csv")
    return myarray
# ==================MAIN FUNCTION ============================
# Hardcode in the input and output paths
ColumnHeadings = ["File Name", "Date", "Applicator", "Terminal", "Wire", "Cross-Section", "Grommet"]
#spHeaders = ["Fecha de creación","Código interno del Aplicador","Numero de parte de la Terminal","Tipo de Cable","Calibre del cable","CH","CW","Rebaba-Izq","Rebaba-Der","Compresión"]
spHeaders = ["Fecha","Aplicador","Terminal","Tipo","Calibre","CH","CW","Rebaba-Izq","Rebaba-Der","Compres"]


#DataLocation = []


# f = open(tablefile, 'w')

with open(tablefile, 'a') as f_object:

    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(f_object)

    # Pass the list as an argument into
    # the writerow()
    writer_object.writerow(ColumnHeadings)

    #Close the file object
    f_object.close()


# get the list of files
myfiles = getPDFlist()

for i in myfiles:
    myrow = extractTables(i)
    # insert filename at beginning of list
    myrow.insert(0,i)
    with open(tablefile, 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(myrow)
        f_object.close()
