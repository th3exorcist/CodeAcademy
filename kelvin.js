// kelvin value
const kelvin = 293;
// celsius value
let celsius = kelvin - 273;
// fahrenheit value
let fahrenheit = celsius*(9/5) +32;
/*
Use the .floor() method from the built-in Math object to round down the Fahrenheit temperature.
*/
fahrenheit = Math.floor(fahrenheit);

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);

let newton = celsius * (33/100);
newton = Math.floor(newton);
console.log(`The temperature is ${newton} degrees Newton.`);
