/*
Dado um vetor de números, como poderia ser realizada a soma de todos os valores utilizando reduce.
*/

let array = [1, 2, 3, 4, 5];

const sum = array.reduce(add, 0)

function add(accumulator, num) {
    return accumulator + num;
}

console.log(sum);
