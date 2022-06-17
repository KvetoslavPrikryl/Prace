
from itertools import count
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Employee, Trained
from .forms import EmployeeForm, TrainedForm, InfoEmployeeForm

myData = Employee.objects.all()
traineds = Trained.objects.all()
def traineds_name():
    trained_list = []
    for name in traineds:
        trained_list.append(name.name)
    return trained_list
        
def employeeCard():
    cards = []
    for data in Employee.objects.all():
        cards.append(data.card)
    return cards


def singIn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else: 
            messages.error(request, "Jméno nebo heslo nejsou správně!")
            return redirect("singIn")

    return render(request, "Information/singIn.html")

def singUp(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["password1"]
        myUser = User.objects.create_user(username, email, pass1)
        myUser.save()
        return HttpResponseRedirect(reverse("singIn"))

    return render(request, "Information/singUp.html", {
    })

def logOut(request):
    logout(request)
    return redirect("singIn")

@login_required(login_url="singIn")
def index(request):
    employees = Employee.objects.all()
    cards = employeeCard()
    if request.method == "POST":
        global cardNumber
        cardNumber = int(request.POST["card"])
        if cardNumber in cards:
            return HttpResponseRedirect(reverse("info"))
        else: 
            return HttpResponseRedirect(reverse("new"))
    return render(request, "Information/index.html", {
        "employees" : employees
    })

@login_required(login_url="singIn")
def information(request): 

    employee = Employee.objects.get(card = cardNumber)
    employeeTraineds = Trained.objects.filter(employee__card = cardNumber)
    trained = []

    for trainedName in employeeTraineds:
        trained.append(trainedName.name)

    if request.method == "POST":

        newComment = request.POST["newComment"]
        employee.info = newComment
        employee.save()

        newMerit = request.POST["newMerit"]
        employee.merit = newMerit
        employee.save()

        messages.success(request, "Informace byly úspěšně uloženy. :)")
        return redirect("info")

    return render(request, "Information/Employee.html", {
        "name" : employee.name,
        "surname" : employee.surname,
        "card": employee.card,
        "merit" : employee.merit,
        "comment" : employee.info,
        "traineds" : trained,
    })

@login_required(login_url="singIn")
def newEmployee(request):
    initial_data = {
        "name": "",
        "surname": "",
        "card": cardNumber
    }
    newEmployee = EmployeeForm(initial=initial_data)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Zaměstnanec byl úspěčně přidán do databáze. :)")
            cards = employeeCard()
            if cardNumber in cards:
                return HttpResponseRedirect(reverse("info"))
            
        else:
            form = EmployeeForm

    return render(request, "Information/newEmployee.html", {
        "newEmployee": newEmployee,
        "cardNumber" : cardNumber,
    })

@login_required(login_url="singIn")
def deteteEmployee(request):
    delete_employee = Employee.objects.get(card = cardNumber)
    if request.method == "POST":
        delete_employee.delete()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "Information/deleteEmployee.html", {
        "employee" : delete_employee,
    })

@login_required(login_url="singIn")
def deleteTrained(request):
    if request.method == "POST":
        name_trained = request.POST["name_trained"]
        delete = Trained.objects.get(name = name_trained)
        delete.delete()
        messages.success(request, f"Školení {name_trained} bylo vymazáno.")
        return HttpResponseRedirect(reverse("index"))
    return render(request, "Information/deleteTrained.html",{
        "trainedsAll" : traineds,
    })

@login_required(login_url="singIn")
def newTrained(request):
    traineds = Trained.objects.all()
    employees = Employee.objects.all()
    newTrained = TrainedForm

    TrainedAllName = []
    employees_traineds = {}

    for trAll in traineds:
        TrainedAllName.append(trAll.name)

    for employee in employees:
        nameTraineds = Trained.objects.filter(employee__card = employee.card)
        employeeTraineds = []
        cislo = 0
        for name in nameTraineds:
            name = str(name.name)
            while cislo < len(TrainedAllName):
                if name == TrainedAllName[cislo]:
                    employeeTraineds.append(name)
                    cislo += 1
                    break
                else:
                    employeeTraineds.append("X")
                    cislo += 1

        while len(employeeTraineds) < len(TrainedAllName):
            employeeTraineds.append("X")

        employees_traineds[employee.card] = employeeTraineds

    if request.method == "POST":
        form = TrainedForm(request.POST)
        if form.is_valid:
            form.save()
        else:
            form = TrainedForm
        return HttpResponseRedirect(reverse("trained"))
        
    return render(request, "Information/trained.html", {
        "newTrained" : newTrained,
        "traineds" : traineds,
        "employees" : employees,
        "employeeTraineds" : employeeTraineds,
        "employees_traineds" : employees_traineds
    })

##### Zkouším ######
"""

traineds = Trained.objects.all()
employees = Employee.objects.all()
newTrained = TrainedForm

TrainedAllName = []
employees_traineds = {}
data = {}

for trAll in traineds:
    TrainedAllName.append(trAll.name)

for employee in employees:
    nameTraineds = Trained.objects.filter(employee__card = employee.card)
    employeeTraineds = []
    cislo = 0
    for name in nameTraineds:
        name = str(name.name)
        while cislo < len(TrainedAllName):
            if name == TrainedAllName[cislo]:
                employeeTraineds.append(name)
                cislo += 1
                break
            else:
                employeeTraineds.append("X")
                cislo += 1

    while len(employeeTraineds) < len(TrainedAllName):
        employeeTraineds.append("X")

    employees_traineds[employee.card] = employeeTraineds
    
print(employees_traineds)
"""