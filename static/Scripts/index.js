var butt_list_of_employee = document.getElementById("butt_list_of_employee");
var table_list_of_employee = document.getElementById("table_list_of_employee");
var button_close_list = document.getElementById("button_close_list");
var this_card = document.querySelectorAll("#this_card");
var input_card = document.getElementById("card");

this_card.forEach(function(card){
    card.addEventListener("click", function(event){
        number = event.target.innerText
        input_card.value = number
    })
})

butt_list_of_employee.addEventListener("click", function() {
    on_of(table_list_of_employee, butt_list_of_employee)
})
button_close_list.addEventListener("click", function(){
    on_of(butt_list_of_employee, table_list_of_employee)
})

function on_of(on, off) {
    on.style.display = "block"
    off.style.display = "none"
}
// Zkoušíme //
const filters = {
    employee_card: ""
}

input_card.addEventListener("input", function(event){
    filters.employee_card = event.target.value
})