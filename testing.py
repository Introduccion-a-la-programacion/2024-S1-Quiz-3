  
import Quiz3;
import pytest;
   
def test_numeroALista_1():
    assert Quiz3.numeroALista(256) == [6,15,18]
    
def test_numeroALista_2():
    assert Quiz3.numeroALista(2552) == [8, 20, 20, 8]
    
def test_numeroALista_3():
    assert Quiz3.numeroALista(0) == [0]
    
def test_numeroALista_4():
    assert Quiz3.numeroALista(-8018) == [-32, 0, -4, -32]
    
##############################################    

def test_listaMayoresMenores_1():
    assert Quiz3.listaMayoresMenores(256) == [[2], [5, 6]]
    
def test_listaMayoresMenores_2():
    assert Quiz3.listaMayoresMenores(2552) == [[2, 2], [5, 5]]
      
def test_listaMayoresMenores_6():
    assert isinstance(str(Quiz3.listaMayoresMenores('25633')), str) == isinstance('Error: Tipo de dato no permitido', str)

##############################################    

def test_aplanarLista_1():
    assert Quiz3.aplanarLista([[12,50,80],[2,8,6,7]]) == [12,50,80,2,8,6,7]
    
def test_aplanarLista_2():
    assert Quiz3.aplanarLista([[12,50,80],15,0,[2,8,6,7]]) == [12,50,80,15,0,2,8,6,7]

def test_aplanarLista_3():
    assert Quiz3.aplanarLista([3,6,9,12]) == [3,6,9,12]

##############################################    

def test_convertirSubListas_1():
    assert Quiz3.convertirSubListas([12,50,80,2,8,6,7]) == [[12,50], [80,2]] 

def test_convertirSubListas_2():
    assert Quiz3.convertirSubListas([12,50,80,2,10,42,8,6,7]) == [[12,50,80], [2,10,42], [8,6,7]] 
