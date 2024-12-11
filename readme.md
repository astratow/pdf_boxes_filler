# PDF Box Filler

This Python script automates the process of filling specified text boxes in a PDF file. It supports customization of text placement, font size, and color, and offers user-friendly options for file handling, including checks for overwriting existing files.

---

## Features

- **Customizable Text Placement**: Specify coordinates (`x`, `y`) for each text box.
- **Font Styling**: Define font size and color for each text box, with defaults available.
- **Overwrite Check**: Prompts the user if the output file already exists.
- **Command-Line Interface**: Easily specify input and output files via arguments.
- **Extensible Design**: Easily add more boxes or functionality.

---

## Requirements

Ensure you have the following installed on your system:

- Python 3.6 or later
- Required Python packages:
  - `PyPDF2`
  - `reportlab`

You can install the dependencies using:

```bash
pip install PyPDF2 reportlab

# Options

- `-i, --input`: Specify the input PDF file. Defaults to `Tarjeta-FUTVOLT-Puntajes_v2.pdf` if not provided.
- `-o, --output`: Specify the output PDF file. If not provided, it defaults to `updated_<input_filename>`.

# Example Commands

## Basic Usage
(uses default input file and generates an updated file):

```bash
python script_name.py

## Specify Input File:
```bash
python script_name.py -i my_input.pdf

## Specify Output File:

```bash
python script_name.py -i my_input.pdf -o my_output.pdf  

## Handle Overwrite: If the specified output file already exists, the script will prompt you:

- Choose Y to overwrite the file.
- Enter a new filename to save the output under a different name.
# Text Box Details
The script fills predefined text boxes with content. You can modify the generate_text_data() function to customize the text, coordinates, font size, and color.

Here is an example of the text box data structure used:

```python
boxes = [  
    {'name': 'example-box', 'x': 100, 'y': 200, 'text': "Sample Text", 'font_size': 12, 'font_color': (0, 0, 0)},  
    # Add more boxes as needed  
]  
## Notes
- Ensure the input PDF file exists and is accessible before running the script.
- Modify the page dimensions in the canvas initialization if your PDF has a custom size.
- Use this script responsibly, and ensure you have the right to modify the PDF files you use.
# How It Works
- Input File Validation: The script checks if the input file exists and is non-empty.
- Merge New Content: Text is drawn onto the first page of the input PDF at the specified coordinates and styles.
- Save Updated File: The modified content is saved to the specified output file, with overwrite checks to prevent accidental data loss.
