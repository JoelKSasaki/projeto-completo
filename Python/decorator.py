def anuncio(f):
    def wrap():
        print("Executando a função...")
        f()
        print("Pronto")
    return wrap

@anuncio
def gemeas():
    print("Débora e Sarah")
  
gemeas()
