from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import io
import argparse

def add_text_to_pdf(input_pdf, output_pdf, text_data, default_font_size=12, default_font_color=(1, 0, 0)):
    if not os.path.exists(input_pdf) or os.path.getsize(input_pdf) == 0:
        raise FileNotFoundError(f"Input file '{input_pdf}' is missing or empty.")

    # Read the existing PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Create a buffer to hold the new PDF content
    packet = io.BytesIO()

    # Create a canvas to draw text on the first page of the PDF
    c = canvas.Canvas(packet, pagesize=(4.13 * 72, 5.85 * 72))  # Page size in points (inches * 72)

    # Loop over all the coordinates and values for each box
    for box in text_data:
        font_size = box.get('font_size', default_font_size)
        font_color = box.get('font_color', default_font_color)

        x, y, text, name = box['x'], box['y'], box['text'], box['name']

        c.setFont("Helvetica", font_size)
        c.setFillColorRGB(*font_color)
        c.drawString(x, y, text)
        print(f"Generated box: {name}")

    c.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)

    page = reader.pages[0]
    page.merge_page(new_pdf.pages[0])

    writer.add_page(page)
    for page_num in range(1, len(reader.pages)):
        writer.add_page(reader.pages[page_num])

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

    print(f"Updated PDF saved as {output_pdf}")


def generate_text_data():
    # Example coordinates and values for boxes
    boxes = [
        {'name': 'top-right', 'x': 203, 'y': 398, 'text': "test text 1", 'font_size': 12, 'font_color': (0, 0, 0)},
        {'name': 'ranking', 'x': 225, 'y': 248, 'text': "2", 'font_size': 12, 'font_color': (0, 0, 0)},
        {'name': 'entrenamientos', 'x': 208, 'y': 218, 'text': "3", 'font_size': 12, 'font_color': (0, 0, 0)},
        {'name': 'gambeta', 'x': 35, 'y': 149, 'text': "4", 'font_size': 11, 'font_color': (0, 0, 0)},
        {'name': 'carrera', 'x': 90, 'y': 149, 'text': "5", 'font_size': 11, 'font_color': (0, 0, 0)},
        {'name': 'al-angulo_left', 'x': 126, 'y': 149, 'text': "6", 'font_size': 11, 'font_color': (0, 0, 0)},
        {'name': 'al-angulo_right', 'x': 150, 'y': 149, 'text': "7", 'font_size': 11, 'font_color': (0, 0, 0)},
        {'name': 'icon_left', 'x': 182, 'y': 149, 'text': "8", 'font_size': 11, 'font_color': (0, 0, 0)},
        {'name': 'icon_right', 'x': 205, 'y': 149, 'text': "9", 'font_size': 11, 'font_color': (0, 0, 0)},
        {'name': 'tiki-taka', 'x': 250, 'y': 149, 'text': "10", 'font_size': 11, 'font_color': (0, 0, 0)},
        {'name': 'gambeta_bottom', 'x': 30, 'y': 129, 'text': "11", 'font_size': 12, 'font_color': (0, 0, 0)},
        {'name': 'carrera_bottom-left', 'x': 73, 'y': 129, 'text': "12", 'font_size': 12, 'font_color': (0, 0, 0)},
        {'name': 'carrera_bottom-left', 'x': 97, 'y': 129, 'text': "13", 'font_size': 12, 'font_color': (0, 0, 0)},
        {'name': 'ial-angula_bottom', 'x': 140, 'y': 129, 'text': "14", 'font_size': 12, 'font_color': (0, 0, 0)},
        {'name': 'icon_bottom', 'x': 195, 'y': 129, 'text': "15", 'font_size': 12, 'font_color': (0, 0, 0)},
        {'name': 'tiki-taka_bottom', 'x': 250, 'y': 129, 'text': "16", 'font_size': 12, 'font_color': (0, 0, 0)},
        {'name': 'salto', 'x': 60, 'y': 75, 'text': "17", 'font_size': 12, 'font_color': (0, 0, 0)},
        {'name': 'ancla', 'x': 115, 'y': 75, 'text': "18", 'font_size': 12, 'font_color': (0, 0, 0)},
        {'name': 'misil', 'x': 168, 'y': 75, 'text': "19", 'font_size': 12, 'font_color': (0, 0, 0)},
        {'name': 'a-lo-rodondo', 'x': 220, 'y': 75, 'text': "20", 'font_size': 12, 'font_color': (0, 0, 0)}
     ]
    return boxes

def check_output_file(output_pdf):
    if os.path.exists(output_pdf):
        while True:
            choice = input(f"File '{output_pdf}' already exists. Overwrite? (Y/n): ").strip().lower()
            if choice in {'', 'y'}:
                print(f"Overwriting '{output_pdf}'.")
                return output_pdf
            else:
                new_filename = input("Enter a new filename (with .pdf extension): ").strip()
                if not new_filename.endswith('.pdf'):
                    print("Invalid filename. Please include a .pdf extension.")
                elif os.path.exists(new_filename):
                    print(f"File '{new_filename}' also exists. Please choose another name.")
                else:
                    print(f"Using new filename: {new_filename}")
                    return new_filename
    return output_pdf

def main():
    parser = argparse.ArgumentParser(description="Fill boxes in a PDF with text.")
    parser.add_argument('-i', '--input', type=str, default='Tarjeta-FUTVOLT-Puntajes_v2.pdf', 
                        help="Input PDF file name (default: 'Tarjeta-FUTVOLT-Puntajes_v2.pdf')")
    parser.add_argument('-o', '--output', type=str, 
                        help="Output PDF file name. Defaults to 'updated_<input_filename>'.")

    args = parser.parse_args()

    input_pdf = args.input
    output_pdf = args.output or f"updated_{os.path.basename(input_pdf)}"
    output_pdf = check_output_file(output_pdf)

    text_data = generate_text_data()
    add_text_to_pdf(input_pdf, output_pdf, text_data)

if __name__ == "__main__":
    main()
