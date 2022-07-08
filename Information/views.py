
from itertools import count
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Employee, Trained
from .forms import EmployeeForm, TrainedForm, AddTrainedForm

myData = Employee.objects.all()
traineds = Trained.objects.all()
newEmployeeCard = []

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
        cardNumber = int(request.POST["card"])
        if cardNumber in cards:
            employee = Employee.objects.get(card=cardNumber)
            return HttpResponseRedirect(reverse("info", args=[employee.id]))
        else: 
            cards.append(cardNumber)
            return HttpResponseRedirect(reverse("new"))
    return render(request, "Information/index.html", {
        "employees" : employees
    })

@login_required(login_url="singIn")
def information(request, id): 
    addTrained = AddTrainedForm
    trainedsAll = Trained.objects.all()
    employee = Employee.objects.get(id = id)
    employeeTraineds = employee.trained.all()
    traineds = []

    for trainedName in employeeTraineds:
        traineds.append(trainedName.name)

    if request.method == "POST":
        
        if "newComment" in request.POST:
            newComment = request.POST["newComment"]
            employee.info = newComment

        if "newMerit" in request.POST:
            newMerit = request.POST["newMerit"]
            employee.merit = newMerit

        if "addTrained" in request.POST:
            addTrained = request.POST["addTrained"]
            trained = Trained.objects.get(name = addTrained)
            if addTrained in traineds:
                employee.trained.remove(trained.id)
            else:
                employee.trained.add(trained.id)
                
        employee.save()

        messages.success(request, "Informace byly úspěšně uloženy. :)")
        return redirect(reverse("info", args=[employee.id]))

    return render(request, "Information/Employee.html", {
        "name" : employee.name,
        "surname" : employee.surname,
        "card": employee.card,
        "merit" : employee.merit,
        "comment" : employee.info,
        "employee_id" : employee.id,
        "employee_traineds" : traineds,
        "trainedsAll" : trainedsAll,
    })

@login_required(login_url="singIn")
def newEmployee(request):

    card = newEmployeeCard[0]

    initial_data = {
        "name": "",
        "surname": "",
        "card": card,
    }
    newEmployee = EmployeeForm(initial=initial_data)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Zaměstnanec byl úspěčně přidán do databáze. :)")
            return HttpResponseRedirect(reverse("info"))
        else:
            form = EmployeeForm

    return render(request, "Information/newEmployee.html", {
        "newEmployee": newEmployee,
    })

@login_required(login_url="singIn")
def deteteEmployee(request, id):
    delete_employee = Employee.objects.get(id = id)
    if request.method == "POST":
        delete_employee.delete()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "Information/deleteEmployee.html", {
        "employee" : delete_employee,
    })

@login_required(login_url="singIn")
def deleteTrained(request):
    traineds = Trained.objects.all()
    if request.method == "POST":
        name_trained = request.POST["name_trained"]
        delete = Trained.objects.get(name = name_trained)
        delete.delete()
        messages.success(request, f"Školení {name_trained} bylo vymazáno.")
        return HttpResponseRedirect(reverse("trained"))
    return render(request, "Information/deleteTrained.html",{
        "trainedsAll" : traineds,
    })

@login_required(login_url="singIn")
def tableTrained(request):
    traineds = Trained.objects.all()
    employees = Employee.objects.all()
    newTrained = TrainedForm

    TrainedAllName = []
    employees_traineds = {}

    for trAll in traineds:
        TrainedAllName.append(trAll.name)

    for employee in employees:
        nameTraineds = Trained.objects.filter(employee__card = employee.card)
        nameTrainedsReallyOnlyNames = []
        for trE in nameTraineds:
            nameTrainedsReallyOnlyNames.append(trE.name)
        employeeTraineds = []
        for name in TrainedAllName:
            if name in nameTrainedsReallyOnlyNames:
                employeeTraineds.append(name)
            else:
                employeeTraineds.append("X")
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
"""