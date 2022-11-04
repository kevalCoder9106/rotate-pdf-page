from flask import Flask, request
import PyPDF2
from flask_cors import CORS
import io

app = Flask(__name__)

@app.route('/parse', methods=['post'])
def rotate():
    data = request.json
    
    file_path = data["file_path"]
    angle_of_rotation = data["angle_of_rotation"]
    page_number = data["page_number"]
    
    pdf_data = PyPDF2.PdfReader(file_path)
    writer = PyPDF2.PdfWriter()

    i = 0
    while True:
        try:
            writer.add_page(pdf_data.pages[i])
            if i == (page_number - 1):
                writer.pages[i].rotate(angle_of_rotation)
            
            i += 1
        except:
            break

    with open("parsed_pdf.pdf", "wb") as f:
        writer.write(f)


    return 'parsed'

app.run()