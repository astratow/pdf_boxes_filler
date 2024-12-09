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

