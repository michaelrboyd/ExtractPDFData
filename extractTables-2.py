import tabula
import os
# read PDF file
tables = tabula.read_pdf("test.pdf", pages="all")
