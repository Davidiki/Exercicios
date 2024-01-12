/* Criar Função para mostrar os números primos
*/

numerosPrimos(35);

function numerosPrimos(num) {
  for (let i = 2; i <= num; i++) {
    let ehPrimo = true;

    for (let j = 2; j < i; j++) {
      if (i % j === 0) {
        ehPrimo = false;
        break;
      }
    }

    if (ehPrimo) {
      console.log(i);
    }
  }
}
