import PyPDF2


file = open('E:\Testcases.pdf','rb')

pdfreader = PyPDF2.PdfFileReader(file)

print(pdfreader.getNumPages())

pageobj = pdfreader.getPage(0)
print(pageobj.extractText())

file.close()
