'use strict';
let listar_productos = async() => {
    let productos;

    await axios({
            method: 'get',
            url: 'http://127.0.0.1:5000/',
            responseType: 'json'
        }).then(function(res) {
            productos = res.data.productos;
        })
        .catch(function(err) {
            console.log(err);
        });

    return productos;
};