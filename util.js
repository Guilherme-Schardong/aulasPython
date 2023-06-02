var prompt = require('prompt-sync')();


function obterTexto(dsecricao){
    return prompt(dsecricao);
}

function obterNumero(dsecricao){
    return Number(obterTexto(dsecricao));
}

function obterInteiro(descricao){
    return Math.trunc(obterNumero(descricao))
}

function obterInteiroPositivo(descricao){
    let numero = obterInteiro(descricao);
    while(numero < 0){
        numero = obterInteiro('Valor Invalido, '+descricao)
    }
    return numero
}


//CommonJS
module.exports={
    obterTexto, obterNumero, obterInteiro, obterInteiroPositivo
}