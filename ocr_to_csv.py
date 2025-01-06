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

def save_to_csv(data, output_csv_file, app_type):
    df = pd.DataFrame(data)
    if app_type.lower() == "cashew":
        # Format the data for Cashew
        df.columns = ["Date", "Description", "Amount"]
    elif app_type.lower() == "bluecoins":
        # Format the data for BlueCoins
        df.columns = ["(1)Type", "(2)Date", "(3)Item or Payee", "(4)Amount", "(5)Parent Category", "(6)Category", "(7)Account Type", "(8)Account", "(9)Notes", "(10)Label", "(11)Status", "(12)Split"]
    df.to_csv(output_csv_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ocr_to_csv.py <path_to_pdf> <output_csv_file>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_csv_file = sys.argv[2]

    app_type = input("Is the output for Cashew or BlueCoins? ")

    images = pdf_to_images(pdf_path)
    ocr_results = ocr_images(images)
    data = parse_ocr_results(ocr_results)
    save_to_csv(data, output_csv_file, app_type)
