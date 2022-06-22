from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import Employee, Trained


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "name", "surname", "card"
        labels = {
            "name": "Jméno:",
            "surname": "Příjmení:",
            "card": "Číslo karty:"
        }
        error_messages = {
            "name" : {
                "required" : "Jméno musíš vyplnit!",
                "max_lenght" : "Co to je za jmnéno? Zkus to znovu, lépa a zkráceně!"
            },
            "surname" : {
                "required" : "Příjmení musíš vyplnit!",
                "max_lenght" : "Příjmnení musí být kratší jinak se dál nedostaneš!"
            },
            "card" : {
                "required" : "Číslo karty musíš vyplnit!",
                "max_lenght" : "Číslo karty je moc dlouhé!"
            }
        }

class InfoEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "merit", "info"
        labels = {"merit" : "Klady: ", "info": "Poznámky k zamšstnanci: "}
        error_messages = {
            "merit" : { 
                "required" : "Nastala nějaká chyba, kontaktuj programátora.",
                "max_lenght" : "Bohužel jsi přesáhl maximální limit povolenách znaků!"
            },
            "info" : {
                "required" : "Nastala nějaká chyba, kontaktuj programátora",
                "max_lenght" : "Bohužel jsi přesáhl maximální limit povolenách znaků!"
            },}

class TrainedForm(forms.ModelForm):
    class Meta:
        model = Trained
        fields = "name",
        labels = {
            "name" : "Název školení "
        }
        error_messages = {
            "name" : {
                "max_lenght" : "Bohužel jsi přesáhl maximální limit povolenách znaků!"
            }
        }

class AddTrainedForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "trained",
        labels = {
            "name" : "Název školení"
        }