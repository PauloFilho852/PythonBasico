import unittest
from app import somar, dividir


#Testando a função testar do módulo app (testes unitários)
#Cada função é um unidade. Imprimi '.' para teste OK e 'F' para falha.
#Para exibir mais detalhes executar 'python [module_name.py] -v

class AppTest(unittest.TestCase):
    
    def setUp(self): #Executado antes de cada teste (aloca recursos para os testes)
        print('setUp() sendo executado.')
           
    def test_somar(self):
        """
        Testando a função somar
        """
        self.assertEqual(somar(5,5), 11, 'Uma mensagema aqui') #Mais assertions podem ser vistas da documentação.
    
    def test_dvidir(self):
        """
        Testando a função dividir
        """
        self.assertEqual(dividir(5,5),1)
    
    def tearDown(self):#Executado após cada teste (desaloca recursos para os testes)
        print('tearDown() sendo executado.')

if __name__ == '__main__':
    unittest.main()
