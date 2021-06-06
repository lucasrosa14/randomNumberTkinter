# randomNumberTkinter
Programa que gera um número aleatório num intervalo pré-definido, recebe um input feito pelo usuário e compara os dois valores, informando se é maior, menor ou se eles são iguais. 

Como sou iniciante, o programa pode ser melhorado de muitas formas, porém, mais do que isso, preciso de ajuda para solucionar uma dificuldade neste projeto. 

No trecho de código abaixo, eu preciso retornar o valor gerado na função 'gera_aleatorio' para ser usado na função 'compara'. Entretanto, não está funcionando. 
Ao atribuir o gera_relatorio() à variável valor_aleatório, a função é executada antes de clicar no botão, gerando inconsistência na comparação dos números.


**def gera_aleatorio():
    vlr_random = randint(1, 5)
    print('Número gerado: {}'.format(vlr_random))
    return vlr_random

valor_aleatorio = gera_aleatorio()

def compara():
    #num_aleatorio = int(gera_aleatorio())
    num_aleatorio = valor_aleatorio**
    
Agradeço se alguém puder ajudar. 
