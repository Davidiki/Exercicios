const mouse = {
    cor: 'red',
    marcar: 'dazz'
}
mouse.velocidade = 5000
mouse.trocarDPI = function () {
}

delete mouse.velocidade
delete mouse.trocarDPI
console.log(mouse)