import os

class Aspirador_de_po():

    def __init__(self):
        self.int_direct = None
        self.diretorios_de_cache = []
        self.android = str
        self.armazenamento = int
        self.cache_0 = None
        self.cache_1 = None
        self.cache_2 = None

    def analisador_de_cache(self):
        # print(os.path('MeuAplicativo.kv'))
        # print(os.path.getsize('MeuAplicativo.kv'))
        # print(os.getcwd())
        # print('1')


        for root, folder, files in os.walk('android/'):
            if '\\cache' in root:
                self.cache_0 = root
                print('etp 2')
                for root, folder, files in os.walk(self.cache_0):
                    print(files)

        # print(os.path.getsize("android/cache.txt"))
        # size_file = os.path.getsize("android/cache.txt")

        # return size_file

        pass

    def naosei():
        pass
    

teste = Aspirador_de_po()
teste.analisador_de_cache()
