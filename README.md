## Caesar Word Encryptor
## Project Description
This Python-based project provides a utility to encrypt specific paragraphs within a Microsoft Word document (.docx files) using the classic Caesar cipher algorithm. Specifically, it targets and encrypts every second paragraph of the document, leaving the other paragraphs untouched. This tool can be useful for demonstrating basic encryption concepts or for simple, non-secure text obfuscation within documents.

## Features
Reads content from a .docx file.

Applies the Caesar cipher encryption to every second paragraph.

Allows customization of the Caesar cipher shift value.

Saves the modified content to a new .docx file, preserving the original document.

Handles basic paragraph extraction and insertion.

## Prerequisites
Before you begin, ensure you have the following installed:

Python 3.6 or higher

python-docx library

## Installation
Clone the repository (if applicable) or download the project files:

git clone https://github.com/Bram1956/caesar-cypher.git
cd caesar-cypher


Install the required Python library:

pip install python-docx

## Usage
Prepare your Word document: Ensure your .docx file is in the same directory as the script, or provide the full path to it.

Run the script:

python encryptor.py <input_file.docx> <output_file.docx> [shift_value]

<input_file.docx>: The path to the Word document you want to encrypt.

<output_file.docx>: The desired name for the output encrypted Word document.

[shift_value]: (Optional) An integer representing the Caesar cipher shift. If not provided, a default shift (e.g., 3) will be used.

Example:

python encryptor.py my_document.docx encrypted_document.docx 5

This command will encrypt every second paragraph of my_document.docx with a shift of 5 and save the result as encrypted_document.docx.

## How It Works
The script performs the following steps:

Opens the specified input .docx file using python-docx.

Iterates through all paragraphs in the document, keeping a count.

For every paragraph at an even index (i.e., the second, fourth, sixth, etc., paragraphs), it applies the Caesar cipher.

The Caesar cipher works by shifting each letter in the plaintext by a certain number of places down the alphabet. For example, with a shift of 3, 'A' would become 'D', 'B' would become 'E', and so on.

Creates a new .docx document and copies all paragraphs, applying the encryption to the designated ones.

Saves the new document with the specified output filename.
## Contributing
Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeature).

Make your changes.

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeature).

Open a Pull Request.

License
This project is open-source and available under the MIT License.
(Note: A LICENSE file would typically be included in the project root.)
