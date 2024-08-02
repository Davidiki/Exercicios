filo = input()
reino = input()
alimentacao = input()

if filo == 'vertebrado':
    if reino == 'ave':
        if alimentacao == 'carnivoro':
            print('aguia')
        if alimentacao == 'onivoro':
            print('pomba')
    if reino == 'mamifero':
        if alimentacao == 'onivoro':
            print('homem')
        if alimentacao == 'herbivoro':
            print('vaca')
if filo == 'invertebrado':
    if reino == 'inseto':
        if alimentacao == 'hematofago':
            print('pulga')
        if alimentacao == 'herbivoro':
            print('lagarta')
    if reino =='anelideo':
        if alimentacao == 'hematofago':
            print('sanguessuga')
        if alimentacao == 'onivoro':
            print('minhoca')