# src/parser.py
import argparse
import os

def parse_html(file_path):
    print(f"Parsing HTML file: {file_path}")

def parse_pdf(file_path):
    print(f"Parsing PDF file: {file_path}")

def parse_doc(file_path):
    print(f"Parsing DOC file: {file_path}")

def parse_docx(file_path):
    print(f"Parsing DOCX file: {file_path}")

def parse_djvu(file_path):
    print(f"Parsing DJVU file: {file_path}")

def main():
    parser = argparse.ArgumentParser(description='Document Parser')
    parser.add_argument('--file', required=True, help='Path to the document file')
    
    args = parser.parse_args()
    
    if not os.path.isfile(args.file):
        print("File does not exist.")
        return
    
    if args.file.endswith('.html'):
        parse_html(args.file)
    elif args.file.endswith('.pdf'):
        parse_pdf(args.file)
    elif args.file.endswith('.doc'):
        parse_doc(args.file)
    elif args.file.endswith('.docx'):
        parse_docx(args.file)
    elif args.file.endswith('.djvu'):
        parse_djvu(args.file)
    else:
        print("Unsupported file format.")

if __name__ == "__main__":
    main()