from funcionalidades import *

tv = Televisor('SONY', 'Sony UltraWide')

controle = ControleRemoto(tv)

controle.sintonizaCanal('SBT')
controle.trocaCanal('SBT')

print(tv.canal_atual)