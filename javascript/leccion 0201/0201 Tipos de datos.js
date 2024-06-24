// 3.3 Comentarios (sintaxis) - Tipos de datos en Javascript
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java realmente diríamos que es idéntica
*/
//3.4 Tipos de datos str, numérico y objeto
var nombre = 'Elias'; // Tipo str
console.log(typeof nombre);
nombre = 7
console.log();
var numero = 3000; // Tipo numérico
console.log(typeof numero);
nombre = 12.3;
console.log(typeof nombre);
var objeto = {   // Tipo objeto
    nombre : "Elias",
    apellido: "Jacob",
    telefono : "2454134134"
};

console.log(typeof objeto);

//Tipo de dato boolean
var bandera = true;
console.log(bandera);

//Tipo de dato función
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi símbolo");
console.log(typeof simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona);

//Tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

// null: Significa ausencia de valor
var y = null; // null no es un tipo de dato, pero su origen es de tipo object
console.log(typeof y);

//Tipo de dato array y Empty String
var autos = ['Citroen','Audi','BMW','Ford']
console.log(autos);
console.log(typeof autos);//Preguntamos qué tipo de dato es:

var z = '';
console.log(z); //Esto se refiere a que es una cadena vacia
console.log(typeof z);



