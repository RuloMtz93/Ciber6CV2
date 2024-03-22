import os
import sys
import fitz  # PyMuPDF
import openpyxl
from docx import Document

print("Script para metadatos PDF, Word y Excel")
print("Martínez Pérez Raúl")
print("Ciberseguridad" '\n')

def extract_pdf_metadata(file_path):
    try:
        doc = fitz.open(file_path)
        metadata = doc.metadata
        print("Metadata for:", file_path)
        for key, value in metadata.items():
            print(key, ":", value)
    except Exception as e:
        print("Error processing:", file_path)
        print(e)

def extract_xlsx_metadata(file_path):
    try:
        wb = openpyxl.load_workbook(file_path)
        props = wb.properties
        print("Metadata for:", file_path)
        for attr in dir(props):
            if not attr.startswith('_'):
                print(attr, ":", getattr(props, attr))
    except Exception as e:
        print("Error processing:", file_path)
        print(e)

def extract_docx_metadata(file_path):
    try:
        doc = Document(file_path)
        core_props = doc.core_properties
        print("Metadata for:", file_path)
        for attr in dir(core_props):
            if not attr.startswith('_'):
                print(attr, ":", getattr(core_props, attr))
    except Exception as e:
        print("Error processing:", file_path)
        print(e)

def extract_metadata(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith('.pdf'):
                extract_pdf_metadata(file_path)
            elif file.lower().endswith('.xlsx'):
                extract_xlsx_metadata(file_path)
            elif file.lower().endswith('.docx'):
                extract_docx_metadata(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Escribir: python meta.py <dirección carpeta a analizar>")
        sys.exit(1)

    directory = sys.argv[1]
    extract_metadata(directory)