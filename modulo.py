from os.path import getsize, getmtime
from time import localtime, asctime
import modutils

if __name__ == "__main__":
	#Aqui o código só será executado
	#se este for o módulo principal
	#e não quando ele for importado por outro prorama
	print('inicio')

mods = modutils.find('time')

for mod in mods:
	tm = asctime(localtime(getmtime(mod)))
	kb = getsize(mod) / 1024
	print('%s: (%d kbytes, %s)' % (mod, kb, tm))