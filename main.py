# Ниже прикрепил файлы которые использовались и файлы при выводе
import glob
import tabula
pdf_files = glob.glob('C:\\Users\\777\\Downloads\\*.pdf')
table = tabula.read_pdf(pdf_files[17], pages=1)[0]
tabula.convert_into(pdf_files[17], 'C:\\Users\\777\\Downloads\\output.csv')
