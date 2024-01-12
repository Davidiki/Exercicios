//Divisivel por 3 => Fizz
//Divisível por 5 => Buzz
//Divisível por e 5 => FizzBuzz
// Não é um núemro => 'Não é um número'



const resultado = fizzBuzz();
console.log(resultado);

function fizzBuzz(num) {
  if (typeof num === 'number') {
    if (num % 3 === 0 && num % 5 === 0) {
      return 'FizzBuzz';
    } else if (num % 3 === 0) {
      return 'Fizz';
    } else if (num % 5 === 0) {
      return 'Buzz';
    } else {
      return 'Não é Divisível';
    }
  } else {
    return 'Não é um número';
  }
}
