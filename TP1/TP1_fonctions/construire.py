import sys
# On définit l'emplacement du ficier preparation :
new = "..\\prep"
sys.path.append(new)
# puis on l'importe
from prep import*
# on lance la construction du notebook
construire('TP1_fonctions.txt')