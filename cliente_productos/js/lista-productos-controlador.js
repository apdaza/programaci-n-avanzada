'use strict';
const tbody = document.querySelector('#tbl-productos tbody');

let mostrar_datos = async() => {
    let productos = await listar_productos();
    tbody.innerHTML = '';

    for (let i = 0; i < 2; i++) {
        let fila = tbody.insertRow();
        fila.insertCell().innerHTML = productos[i]['id'];
        fila.insertCell().innerHTML = productos[i]['nombre'];
        fila.insertCell().innerHTML = productos[i]['valor'];
        fila.insertCell().innerHTML = productos[i]['cantidad'];
    }


};

mostrar_datos();