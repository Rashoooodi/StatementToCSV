import pytesseract
from pdf2image import convert_from_path
import pandas as pd
import sys

def pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    return images

def ocr_images(images):
    ocr_results = []
    for image in images:
        text = pytesseract.image_to_string(image)
        ocr_results.append(text)
    return ocr_results

def parse_ocr_results(ocr_results):
    data = []
    for result in ocr_results:
        lines = result.split('\n')
        for line in lines:
            if line.strip():
                data.append(line.strip().split())
    return data

def save_to_csv(data, output_csv_file):
    df = pd.DataFrame(data)
    df.to_csv(output_csv_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ocr_to_csv.py <path_to_pdf> <output_csv_file>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_csv_file = sys.argv[2]

    images = pdf_to_images(pdf_path)
    ocr_results = ocr_images(images)
    data = parse_ocr_results(ocr_results)
    save_to_csv(data, output_csv_file)
