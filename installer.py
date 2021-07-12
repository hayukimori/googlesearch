import os, platform


########VARIÁVEIS PRINCIPAIS############
_HOME = os.path.expanduser('~')
_PATH = f'{_HOME}/.local/bin/'
########################################


def install():
	try:
		print(f"Instalando bin em '{_PATH}'...")


		command = f"cp ./bin/googlesearch {_PATH}"
		print(command)
		os.system(command)

		v = os.path.exists(_PATH + "/googlesearch")

		if v == True:
			print("Instalado com sucesso")
		else:
			print("Não foi possível instalar")

	except Exception as e:
		with open('error_log.txt', 'w') as f:
			f.write(str(e))
			f.close()

		print("Houve um erro durante a instalação, verifique o arquivo de erro > error_log.txt")

def uninstall():
	print("Desinstalando googlesearch")
	command = f'rm {_PATH}/googlesearch'

	print(command)
	os.system(command)







if __name__ == '__main__':

	ja_instalado = os.path.exists(_PATH + '/googlesearch')

	if ja_instalado == True:
		confirmacao = input(f"googlesearch já está instalado em {_PATH}, Desinstalar? (Y/n): ")

		if confirmacao.lower() == 'n':
			sys.exit()

		else:
			uninstall()

	else:
		install()