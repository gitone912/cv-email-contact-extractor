from django.shortcuts import render
from django.http import HttpResponse
import fitz
import os
import tempfile
import openpyxl
from .nlp import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def extract_text_from_pdf(pdf_file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_pdf:
        for chunk in pdf_file.chunks():
            tmp_pdf.write(chunk)
        tmp_pdf_path = tmp_pdf.name

    doc = fitz.open(tmp_pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    os.unlink(tmp_pdf_path)  # Clean up temporary file
    return text

@csrf_exempt
def upload_cv(request):
    if request.method == 'POST' and request.FILES.getlist('cv_files'):
        cv_data = []
        for cv_file in request.FILES.getlist('cv_files'):
            overall_text = extract_text_from_pdf(cv_file)
            email = extract_email_regex(overall_text)
            phone_num = extract_phone_regex(overall_text)
            cv_data.append({'email': email, 'phone_num': phone_num, 'overall_text': overall_text})  # Include overall text

        # Render the data in a new HTML page
        return render(request, 'cv_list.html', {'cv_data': cv_data})

    return render(request, 'upload_cv.html')


@csrf_exempt
def export_to_excel(request):
    if request.method == 'POST' and 'export' in request.POST:
        cv_data = request.POST.getlist('cv_data[]')  # Adjust here to get a list
        
        # Create a new Excel workbook
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['Email', 'Phone Number', 'Overall Text'])  # Add column for overall text

        # Add data to the Excel workbook
        for cv in cv_data:
            cv_dict = eval(cv)  # Convert string representation of dictionary to actual dictionary
            ws.append([cv_dict['email'], cv_dict['phone_num'], cv_dict['overall_text']])  # Include overall text

        # Save the Excel file to a temporary location
        excel_file_path = tempfile.NamedTemporaryFile(delete=False).name
        wb.save(excel_file_path)
        
        # Prepare the response to serve the Excel file for download
        with open(excel_file_path, 'rb') as excel_file:
            response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=cv_data.xlsx'
        
        # Clean up temporary file
        os.unlink(excel_file_path)
        
        return response

