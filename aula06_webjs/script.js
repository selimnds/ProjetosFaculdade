function pares(){
    let numero = parseInt(prompt("digite um numero: "))
    if (isNaN(numero)){
        alert('porfavor digite um numero valido')
        return;
    }
    if (numero % 2 === 0){
            console.log("É par")
        }
        else {
            console.log("É ímpar")
        }
}

pares();
pares();
pares();

var res = 0;
let n1 = parseInt(prompt("digite o primeiro valor"))
let n2 = parseInt(prompt("digite o segundo valor"))

function somar(num1, num2){ 
    res = num1 + num2
}

function mostrar(msg){
    alert(`o resultado da soma é ${msg}`)
}

somar(n1,n2)
mostrar(res);

let n1 = parseFloat(prompt('digite o primeiro numero: '))
let n2 = parseFloat(prompt('digite o segundo numero: '))
var operacao = prompt('digite a operacao: \n+\n-\n*\n/')
function calculadora(v1, v2, op){
    if(op === '+'){
        return v1 + v2;
    }
    else if(op === '-'){
        return v1 - v2;
    }
    else if(op === '*'){
        return v1 * v2;
    }
    else if(op === '/'){
        return v1 / v2;
    }
    else{

    }
};
alert(calculadora(n1,n2,operacao))