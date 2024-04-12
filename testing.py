  
import Quiz2;
import pytest;
   
def test_numeroALista_1():
    assert Quiz2.numeroALista(256) == [18, 15, 6]
    
def test_numeroALista_2():
    assert Quiz2.numeroALista(2552) == [8, 20, 20, 8]
    
def test_numeroALista_3():
    assert Quiz2.numeroALista(0) == [0]
    
def test_numeroALista_4():
    assert Quiz2.numeroALista(-8018) == ["-", 32, 4, 0, 32]
    
##############################################    

def test_listaMayoresMenores_1():
    assert Quiz2.listaMayoresMenores(256) == [[2], [5, 6]]
    
def test_listaMayoresMenores_2():
    assert Quiz2.listaMayoresMenores(2552) == [[2, 2], [5, 5]]
      
def test_listaMayoresMenores_6():
    assert isinstance(str(Quiz2.listaMayoresMenores('25633')), str) == isinstance('Error: Tipo de dato no permitido', str)
