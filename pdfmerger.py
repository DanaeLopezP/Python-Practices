import os
import fitz

def unir_pdf(carpeta_entrada, archivo_salida):
    pdf_salida = fitz.open()

    for nombre_archivo in os.listdir(carpeta_entrada):
        if nombre_archivo.endswith('.pdf'):
            ruta_archivo = os.path.join(carpeta_entrada, nombre_archivo)
            pdf = fitz.open(ruta_archivo)
            pdf_salida.insert_pdf(pdf)
            pdf.close()
    
    pdf_salida.save(archivo_salida)
    pdf_salida.close()

carpeta_entrada = 'C:\\Users\\pdana\\Documents\\ejemplo'
archivo_salida =  'C:\\Users\\pdana\\Documents\\ejemplo\\pdflisto\\Terminado.pdf'

unir_pdf(carpeta_entrada, archivo_salida)
print ("PDFs Unidos correctamente")