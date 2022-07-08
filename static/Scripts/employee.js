var butt_edit_comment = document.getElementById("butt_edit_comment");
var butt_edit_merit = document.getElementById("butt_edit_merit");
var butt_add_trained = document.getElementById("butt_add_trained");
var add_trained = document.getElementById("add_trained");
var new_comment = document.getElementById("new_comment");
var new_merit = document.getElementById("new_merit");
var send_edits = document.getElementById("send_edits");
var send_edits_info = document.getElementById("send_edits_info");
var name_trained = document.querySelectorAll("#name_trained");
var addTrained = document.getElementById("addTrained");

butt_edit_comment.addEventListener("click", function(){
    on_of(new_comment, butt_edit_comment)
    send_edits_info.style.display = "block"
});
butt_edit_merit.addEventListener("click", function(){
    on_of(new_merit, butt_edit_merit)
    send_edits_info.style.display = "block"
});
butt_add_trained.addEventListener("click", function(){
    on_of(add_trained, butt_add_trained)   
    send_edits.style.display = "block"
});

name_trained.forEach(function(trained){ 
    trained.addEventListener("click", function(event){
        add_name = event.target.innerText
        addTrained.value = add_name
    })
})

function on_of(on, off) {
    on.style.display = "block"
    off.style.display = "none"
};