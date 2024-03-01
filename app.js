function berekensom() {
var getal_1 = document.getElementById("getal_1").value;

var getal_2 = document.getElementById("getal_2").value;

var som = parsefloat(getal_1) + parsefloat("getal_2");

var uitkomst = document.getElementById("uitkomst");

var eigenberekening = document.getElementById("eigenberekening");

eigenberekening.innerHTML = "Het door jouw berekende antwoord is fout";

eigenberekening.style.color = "blue";



uitkomst.innerHTML = "De som van " + getal_1 + " + " + getal_2 + " = " + som;


} 