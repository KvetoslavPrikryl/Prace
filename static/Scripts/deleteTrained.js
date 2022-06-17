var trainedsName = document.querySelectorAll("#trainedsName")
var input = document.getElementById("name_trained")

trainedsName.forEach(function(name) {
    name.addEventListener("click", function(event){
        trained = event.target.innerText
        input.value = trained
    })
});