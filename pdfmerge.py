import sys
try:
    from PyPDF2 import PdfFileMerger
except ImportError:
    from pyPdf import PdfFileMerger

if len(sys.argv) == 1:
    sys.exit("No merged file name or input files given")
elif len(sys.argv) == 2:
    sys.exit("No input files given")

merger = PdfFileMerger()
pdfs = sys.argv[2:]

for pdf in pdfs:
    merger.append(pdf)

try: 
    merger.write(sys.argv[1])
except:
    sys.exit("Operation failed")

print("Successfully merged PDFs:%s into %s" % (str(pdfs), sys.argv[1])) 
merger.close()