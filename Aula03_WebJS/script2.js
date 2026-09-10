// tipo primitivos
var boolean = false;
console.log('## tipos primitivos');
console.log('o valor da variavel boolean é ', boolean);
// template string 
console.log(`a variavel ${boolean} tem o tipo ${typeof (boolean)}`);

var nome = 'Cuiudasso'
var nome = 'LUIZ'

// let sobrenone = 'selim'
// let sobrenome = 'SELIM'

// const nomeDoMeio = 'henrique'
// const nomeDoMeio = 'Enrique'

function funcaoCamelCase() {
    var sobrenome = 'Selim'
    console.log(sobrenome)
};

console.log(nome);
funcaoCamelCase();

// comparacao
var igual = '0' == 0
console.log(igual)

var igualIdentico = '0' === 0
console.log(igualIdentico)

// operadores 
// +, -, *, /, %, ** 

var adicao = 2 + 5
console.log(adicao)

var somarTexto = 'ola' + 'devaldo'
console.log(somarTexto)

// operadores relacionais
// <, >, <=, >=, !=, !==
var menorQue = 5 < 2;
var maiorQue = 5 > 2;
var maiorOuIgual = 5 >= 2;
var menorOuIgual = 5 <= 2;
var diferente = '5' != 5;
var diferenteEstrito = 5 !== 5;

console.log(`
    o valor da variavel menorQue é ${menorQue};
    o valor da variavel maiorQue é ${maiorQue};
    o valor da variavel menorOuIgual é ${menorOuIgual};
    o valor da variavel maiorOuIgual é ${maiorOuIgual};
    o valor da variavel diferente é ${diferente};
    o valor da variavel diferenteEstrito é ${diferenteEstrito};
    `)

// operadores logicos 
// &&, ||, ! 
var e = true && true;
console.log(e)

var ou = true || false;
console.log(e)

var nao = true && true;
console.log(e)


