from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from home.models import Contact, TCS, Accenture,Atos,Amazon,Capgemini,Coginzant,Delloite,IBM,Microsoft,Facebook,Apple,Netflix,Google,Infosys,Wipro,TM,Adobe,Cisco,EY,PWC
from django.contrib import messages
# imports for compiler
from django.http import HttpResponse
import subprocess
import os
# Create your views here.
# def contactView(request):
#     return render(request,'contact.html')
@login_required()
def service_based(request):
    return render(request,'service_based.html')
@login_required()
def product_based(request):
    return render(request,'product_based.html')
@login_required()
def faang(request):
    return render(request,'faang.html')
@login_required()
def bigcom(request):
    return render(request,'bigcom.html')
def indexView(request):
    return render(request,'index.html')
@login_required()
def dashboardView(request):
    return render(request,'dashboard.html')
def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
        
    return render(request, 'contact.html')

# compiler
import requests
import json

@login_required()
def tcs(request):
    code = request.POST.get('code', '')
    input_data = request.POST.get('input', '')
    selected_theme = request.POST.get('selected-theme', 'dracula')
    selected_language = request.POST.get('selected-language', 'python')
    output = ""

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = TCS.objects.get(id=question_id)
        except TCS.DoesNotExist:
            question = None
    else:
        question = TCS.objects.first()

    if request.method == 'POST':
        try:
            api_url = "https://us-central1-codeexecuter-430112.cloudfunctions.net/codeExecuter"
            payload = {
                'code': code,
                'input_data': input_data,
                'language': selected_language
            }
            response = requests.post(api_url, json=payload)
            output = response.json().get('output', 'Error occurred')
        except Exception as e:
            output = "An error occurred: " + str(e)

    return render(request, 'tcs.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})
#@login_required()
#def tcs(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = TCS.objects.get(id=question_id)
        except TCS.DoesNotExist:
            question = None
    else:
        question = TCS.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = TCS.objects.get(id=question_id)
        except TCS.DoesNotExist:
            question = None
    else:
        question = TCS.objects.first()

    return render(request, 'tcs.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def accenture(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Accenture.objects.get(id=question_id)
        except Accenture.DoesNotExist:
            question = None
    else:
        question = Accenture.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Accenture.objects.get(id=question_id)
        except Accenture.DoesNotExist:
            question = None
    else:
        question = Accenture.objects.first()

    return render(request, 'accenture.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def amazon(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Amazon.objects.get(id=question_id)
        except Amazon.DoesNotExist:
            question = None
    else:
        question = Amazon.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Amazon.objects.get(id=question_id)
        except Amazon.DoesNotExist:
            question = None
    else:
        question = Amazon.objects.first()

    return render(request, 'amazon.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def capgemini(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Capgemini.objects.get(id=question_id)
        except Capgemini.DoesNotExist:
            question = None
    else:
        question = Capgemini.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Capgemini.objects.get(id=question_id)
        except Capgemini.DoesNotExist:
            question = None
    else:
        question = Capgemini.objects.first()

    return render(request, 'capgemini.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def cognizant(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Coginzant.objects.get(id=question_id)
        except Coginzant.DoesNotExist:
            question = None
    else:
        question = Coginzant.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Coginzant.objects.get(id=question_id)
        except Coginzant.DoesNotExist:
            question = None
    else:
        question = Coginzant.objects.first()

    return render(request, 'cognizant.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def atos(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Atos.objects.get(id=question_id)
        except Atos.DoesNotExist:
            question = None
    else:
        question = Atos.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Atos.objects.get(id=question_id)
        except Atos.DoesNotExist:
            question = None
    else:
        question = Atos.objects.first()

    return render(request, 'atos.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def delloite(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Delloite.objects.get(id=question_id)
        except Delloite.DoesNotExist:
            question = None
    else:
        question = Delloite.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Delloite.objects.get(id=question_id)
        except Delloite.DoesNotExist:
            question = None
    else:
        question = Delloite.objects.first()

    return render(request, 'delloite.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def ibm(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = IBM.objects.get(id=question_id)
        except IBM.DoesNotExist:
            question = None
    else:
        question = IBM.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = IBM.objects.get(id=question_id)
        except IBM.DoesNotExist:
            question = None
    else:
        question = IBM.objects.first()

    return render(request, 'ibm.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def microsoft(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Microsoft.objects.get(id=question_id)
        except Microsoft.DoesNotExist:
            question = None
    else:
        question = Microsoft.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Microsoft.objects.get(id=question_id)
        except Microsoft.DoesNotExist:
            question = None
    else:
        question = Microsoft.objects.first()

    return render(request, 'microsoft.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def facebook(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Facebook.objects.get(id=question_id)
        except Facebook.DoesNotExist:
            question = None
    else:
        question = Facebook.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Facebook.objects.get(id=question_id)
        except Facebook.DoesNotExist:
            question = None
    else:
        question = Facebook.objects.first()

    return render(request, 'meta.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def apple(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Apple.objects.get(id=question_id)
        except Apple.DoesNotExist:
            question = None
    else:
        question = Apple.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Apple.objects.get(id=question_id)
        except Apple.DoesNotExist:
            question = None
    else:
        question = Apple.objects.first()

    return render(request, 'apple.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def netflix(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Netflix.objects.get(id=question_id)
        except Netflix.DoesNotExist:
            question = None
    else:
        question = Netflix.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Netflix.objects.get(id=question_id)
        except Netflix.DoesNotExist:
            question = None
    else:
        question = Netflix.objects.first()

    return render(request, 'netflix.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def google(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Google.objects.get(id=question_id)
        except Google.DoesNotExist:
            question = None
    else:
        question = Google.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Google.objects.get(id=question_id)
        except Google.DoesNotExist:
            question = None
    else:
        question = Google.objects.first()

    return render(request, 'google.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def infosys(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Infosys.objects.get(id=question_id)
        except Infosys.DoesNotExist:
            question = None
    else:
        question = Infosys.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Infosys.objects.get(id=question_id)
        except Infosys.DoesNotExist:
            question = None
    else:
        question = Infosys.objects.first()

    return render(request, 'infosys.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def wipro(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Wipro.objects.get(id=question_id)
        except Wipro.DoesNotExist:
            question = None
    else:
        question = Wipro.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Wipro.objects.get(id=question_id)
        except Wipro.DoesNotExist:
            question = None
    else:
        question = Wipro.objects.first()

    return render(request, 'wipro.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def tm(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = TM.objects.get(id=question_id)
        except TM.DoesNotExist:
            question = None
    else:
        question = TM.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = TM.objects.get(id=question_id)
        except TM.DoesNotExist:
            question = None
    else:
        question = TM.objects.first()

    return render(request, 'tm.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def adobe(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Adobe.objects.get(id=question_id)
        except Adobe.DoesNotExist:
            question = None
    else:
        question = Adobe.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Adobe.objects.get(id=question_id)
        except Adobe.DoesNotExist:
            question = None
    else:
        question = Adobe.objects.first()

    return render(request, 'adobe.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def cisco(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Cisco.objects.get(id=question_id)
        except Cisco.DoesNotExist:
            question = None
    else:
        question = Cisco.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = Cisco.objects.get(id=question_id)
        except Cisco.DoesNotExist:
            question = None
    else:
        question = Cisco.objects.first()

    return render(request, 'cisco.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def ey(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = EY.objects.get(id=question_id)
        except EY.DoesNotExist:
            question = None
    else:
        question = EY.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = EY.objects.get(id=question_id)
        except EY.DoesNotExist:
            question = None
    else:
        question = EY.objects.first()

    return render(request, 'ey.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})

@login_required()
def pwc(request):
    code = request.POST.get('code', '') # get code from request, default to empty string if not found
    input_data = request.POST.get('input', '') # get input data from request, default to empty string if not found
    output = "" # initialize output to empty string
    selected_theme = request.POST.get('selected-theme', 'dracula') # get selected theme from request, default to 'dracula' if not found
    selected_language = request.POST.get('selected-language', 'python') # get selected language from request, default to 'python' if not found

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = PWC.objects.get(id=question_id)
        except PWC.DoesNotExist:
            question = None
    else:
        question = PWC.objects.first()

    if request.method == 'POST':
        try:
            if selected_language == 'python':
                with open("code.py", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["python", "code.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.py")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'java':
                with open("Main.java", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(timeout=5)
                if stderr:
                    output = stderr.decode()
                else:
                    process = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                    output = stdout.decode() + stderr.decode()
                os.remove("Main.java")
                os.remove("Main.class")
            elif selected_language == 'cpp':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["g++", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
            elif selected_language == 'c':
                with open("code.cpp", "w") as f:
                    f.write(code)
                process = subprocess.Popen(["gcc", "code.cpp", "-o", "code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                process = subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=input_data.encode(), timeout=5)
                os.remove("code.cpp")
                os.remove("code.exe")
                output = stdout.decode() + stderr.decode()
        except subprocess.TimeoutExpired:
            output = "The program exceeded the time limit of 5 seconds."
        except Exception as e:
            output = "An error occurred: " + str(e)

    if 'question_id' in request.GET:
        question_id = int(request.GET['question_id'])
        try:
            question = PWC.objects.get(id=question_id)
        except PWC.DoesNotExist:
            question = None
    else:
        question = PWC.objects.first()

    return render(request, 'pwc.html', {'code': code, 'input_data': input_data, 'output': output, 'selected_theme':selected_theme, 'selected_language':selected_language, 'question': question, 'company1_list': TCS.objects.all()})
