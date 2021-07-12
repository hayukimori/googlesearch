import webbrowser, sys

def main(site, pesquisa):	
	webbrowser.open((site + pesquisa))


if __name__ == '__main__':
	args = sys.argv[1:]
	args = '+'.join(args)

	site = 'https://google.com/search'
	sist_pesquisa = "?q="

	print(f"[Info] Procurando por {args}")

	main((site+sist_pesquisa), args)