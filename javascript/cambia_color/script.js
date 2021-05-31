function cambiar(element){
    valor = parseInt(element.value)
    switch(valor){
        case 1:
            document.getElementById("lienzo").style = "background-color : black"
            break;
        case 2:
            document.getElementById("lienzo").style = "background-color : blue"
            break;
        case 3:
            document.getElementById("lienzo").style = "background-color : green"
            break;
        default:
            document.getElementById("lienzo").style = "background-color : red"
    }
}