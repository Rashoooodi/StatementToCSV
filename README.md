# StatementToCSV

## Project Description

This project aims to provide a Python script that can OCR (Optical Character Recognition) bank statement PDFs and convert them into CSV files. The generated CSV files are formatted to be compatible with BlueCoins and Cashew, two popular personal finance management applications.

### FYI:
May only work with: Al Salam Bank

## How to Use

1. Install the required Python packages by running:
   ```
   pip install -r requirements.txt
   ```

2. Run the script with the following command:
   ```
   python ocr_to_csv.py <path_to_pdf> <output_csv_file>
   ```

3. The script will ask if the output is for Cashew or BlueCoins, process the PDF, perform OCR, and generate a CSV file with the extracted data.

## Contributing

We welcome contributions to this project. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with a clear message.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.

Thank you for your contributions!
