//var btn = document.getElementById('okBtn')
counter = 1;
var update = document.getElementById("num")

var wm = new Set();

function chnageText(){
    update.innerText = counter
    counter--;
    
    var word = document.getElementById("word").value
    var meaning  = document.getElementById("meaning").value
    
    wm.add(word);
    wm.add(meaning)

    if(counter == 0){
        document.getElementById("btn").disabled  = false
        document.getElementById("btn").style.display = "block";
        document.getElementById("note").style.display = "block";
        document.getElementById('pbtn').style.display = "none";
    }
    var word = document.getElementById("word").value = ''
    var meaning  = document.getElementById("meaning").value = ''
}