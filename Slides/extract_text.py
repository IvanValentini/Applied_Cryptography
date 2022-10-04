import PyPDF2
import sys
import re
if len(sys.argv) < 2:
	print(f"Usage: {sys.argv[0]} file.pdf")
	sys.exit(1)
pdfFileObj = open(sys.argv[1], 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


for page in pdfReader.pages:
    text = page.extractText()
    text = text.replace("•", "\item ")
    text = text.replace("▪", "\item ")
    text = text.replace("’", "'")
    text = text.replace(" -", "-")
    text = text.replace("→", "->")
    text = text.replace("“",'"')
    text = text.replace("”",'"')
    text = re.sub(r'^o[Z-a]*',"\\\\item ",text, flags=re.MULTILINE)
    print(text)
pdfFileObj.close()
