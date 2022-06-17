var add_trained_button = document.getElementById("add_trained_button")
var add_trained = document.getElementById("add_trained")

add_trained_button.addEventListener("click", function() {
    on_of(add_trained, add_trained_button)
});

function on_of(on, off) {
    on.style.display = "inline-block"
    off.style.display = "none"
};