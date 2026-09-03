from pypdf import PdfReader, PdfWriter

pdf1 = "1.pdf"
pdf2 = "2.pdf"
salida = "Lopez_P_tc2_act1u1_03sep26.pdf"

reader1 = PdfReader(pdf1)
reader2 = PdfReader(pdf2)

writer = PdfWriter()

# 1. Agregar la portada del PDF 1
writer.add_page(reader1.pages[0])

# 2. Insertar completo el PDF 2
for page in reader2.pages:
    writer.add_page(page)

# 3. Agregar el resto del PDF 1
for page in reader1.pages[1:]:
    writer.add_page(page)

# 4. Guardar el resultado
with open(salida, "wb") as f:
    writer.write(f)

print(f"PDF creado: {salida}")