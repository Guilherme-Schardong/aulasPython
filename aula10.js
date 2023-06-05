/*
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
No final da série de saltos de cada atleta,o melhor e o pior resultados são eliminados.
O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas 
pelo atleta em seus saltos e depois informe a média dos saltos conforme a 
descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). 
Faça uso de uma lista para armazenar os saltos. 
Os saltos são informados na ordem da execução, portanto não são ordenados.
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m 
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m


com a entrada de 3 valores ordenalos de forma crescente


*/







//const { obterTexto, obterNumero, obterInteiroPositivo } = require("./util");






// function main(){
// const idade = 36;
// const peso = 105;
// console.log(soma(idade, peso));
    
// }
// main()


// function soma(valorA, valorB){
//     let resultado = valorA + valorB
//     return resultado;

// }

// function eh_par(valor){
//     if(valor%2==0){
//         return true
//     }else{
//         return false
//     }

// }



// function saudacao(){
//     console.log('ola boa noite');
// }




// var prompt = require('prompt-sync')();


// function calcular_consumo_viagem(tempo, velocidade){       ////  os nomes dos paramentro nao importa 
// 								//o que importa é a ordem
//     const distancia = tempo * velocidade;
//     const consumo = distancia / 12;

//     return consumo;
// }


// function main(){
//     console.log('consumo veiculo');

//     //entrada
//     const tempo = Number(prompt('Tempo (h): '));
//     const velocidae = Number(prompt('Velocidae (km/h): '));


//     // processamento
//     const consumo = calcular_consumo_viagem(tempo, velocidae);     //  argumentos na funcão sao os paramentros 
// 									//no principal sao argumentos

//     //saida
//     console.log(consumo.toFixed(3));

// }
//   main()


// const frase = 'Ola a todos';

// frase[7] = 'a';

//console.log(frase[7]);


//.charCodeAt() passando a posição ele retorna o valor da tabela ascii


//String.fromCharCode() passando o numero ele retorna o valor desse numero na tabela ascii

// console.log(frase.split('o'));

// const nome = obterTexto('seu nome ');
// const idade = obterInteiroPositivo(' sua idade');
// console.log(nome);