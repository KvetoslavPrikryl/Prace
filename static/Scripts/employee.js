var butt_edit_comment = document.getElementById("butt_edit_comment");
var butt_edit_merit = document.getElementById("butt_edit_merit");
var new_comment = document.getElementById("new_comment");
var new_merit = document.getElementById("new_merit");
var send_edits = document.getElementById("send_edits");

butt_edit_comment.addEventListener("click", function(){
    on_of(new_comment, butt_edit_comment)
    send_edits.style.display = "block"
});
butt_edit_merit.addEventListener("click", function(){
    on_of(new_merit, butt_edit_merit)
    send_edits.style.display = "block"
});

function on_of(on, off) {
    on.style.display = "block"
    off.style.display = "none"
};