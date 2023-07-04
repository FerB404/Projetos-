#Criar um programa que calcula a quantidade de tinta necessaria para pintar uma parede. O usuario deverá fornecer as seguintes informações: Rendimento, Altura e Largura.abs

rendimento = int(input("Qual rendimento da lata ? "))
altura = int(input("Qual a altura? "))
largura = int(input("Qual a largura da parede? "))

def calc_tinta():
  area = altura * largura 
  total = area / rendimento

  print(f"Você precisa de {total} latas de tinta ")


calc_tinta()
