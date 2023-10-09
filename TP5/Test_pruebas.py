import pytest 
from TP5_Funciones  import *
#----------------------------------------------------------------------------------------
@pytest.mark.parametrize("dni,res",[
    (43545018,True),
    (21947779,True),
    (4523,False),
    (1234567,True)

])
def test_dni_cheker(dni,res):
    assert dni_cheker(dni)==res
#----------------------------------------------------------------------------------------
@pytest.mark.parametrize("username1,usersurename,dni,res",[
    ("Maria","Pattins",25457869,"ID ->Maria7254"),
    ("Emilio","Baigorria",43545018,"ID ->Emilio9435"),
    ("Montse","Gimenez",21947779,"ID ->Montse7219"),
    ("Guadalupe","Baigorria",43545120,"ID ->Guadalupe9435")
])
def test_id_maker(username1,usersurename,dni,res):
    assert id_maker(username1,usersurename,dni)==res
#----------------------------------------------------------------------------------------
last1=[True,0]
last2=[False,1]
@pytest.mark.parametrize("username,pasword,login_attempts,res",[
    ("usuario1","asdasd",0,last1),
    ("Emilo","Papasrojas",0,last2),
    ("Gaston","Scrummaster",0,last2),
    ("Gwen","Camelot",0,last2)
])
def test_login(username,pasword,login_attempts,res):
    assert login(username,pasword,login_attempts)==res
#----------------------------------------------------------------------------------------

@pytest.mark.parametrize("num,digit,res",[
    (1123,1,2),
    (54324,4,2),
    (1500,0,2),
    (3333,3,4)
])
def test_digit_counter(num,digit,res):
    assert digit_counter(num,digit)==res
#----------------------------------------------------------------------------------------
number_list1=[12,2,5,6]
number_list2=[24,4,10,12]
@pytest.mark.parametrize("function,A,res",[
    (double,number_list1,number_list2)

])
def test_fuction_list(function,A,res):
    assert fuction_list(function,A)==res
#----------------------------------------------------------------------------------------

@pytest.mark.parametrize("num,res",[
    (12,24),
    (5,10),
    (23,46),
    (7,14),
    (3,6)

])
def test_double(num,res):
    assert double(num)==res
#----------------------------------------------------------------------------------------

@pytest.mark.parametrize("x,y,res",[
    (2,2,6),
    (10,3,19),
    (7,4,23),
    (20,6,56)
])
def test_sum_square(x,y,res):
    assert sum_square(x,y)==res
#----------------------------------------------------------------------------------------
v1=(3,2,5)
v2=(6,3)
@pytest.mark.parametrize("v,res",[
    (v1,6),
    (v2,6)
])
def test_module(v,res):
    assert module(v)==res
#----------------------------------------------------------------------------------------

@pytest.mark.parametrize("txt,res",[
    ("papas"," p a p a s "),
    ("Amarillo"," A m a r i l l o "),
    ("azul"," a z u l ")
])
def test_ExtraSpacing(txt,res):
    assert ExtraSpacing(txt)==res
#----------------------------------------------------------------------------------------

@pytest.mark.parametrize("list_num,res",[
    ([1,2,3,4,5],(5,1)),
    ([12,2,4,32,10],(32,2)),
    ([85,0,2,7,54],(85,0)),
])
def test_CalculateMaxMin(list_num,res):
    assert CalculateMaxMin(list_num)==res
#----------------------------------------------------------------------------------------
# Temperatura promedio
@pytest.mark.parametrize("a,b,res",[
    (5,6,5.5),
    (8,4,6),
    (10,20,15)
])
def test_prom_temp(a,b,res):
    assert prom_temp(a,b)==res
#----------------------------------------------------------------------------------------
# Chequeador de primos
@pytest.mark.parametrize("a,res",[
    (8, False),
    (9, False),
    (5, True),
    (13, True),
    (17, True),
    (25, False)
])
def test_prime_checker(a,res):
    assert prime_checker(a)==res
#----------------------------------------------------------------------------------------
# Longitud de la primer palabra
@pytest.mark.parametrize("word,length",[
    ("   Hola como estas  ", 4),
    ("  Abc deD fAoasdaeE ", 3),
    ("hola amigoooo", 4)
])
def test_last_word_len(word,length):
    assert last_word_len(word)==length

#----------------------------------------------------------------------------------------
# Contador de digitos en una lista
@pytest.mark.parametrize("num,digit,res",[
    ([3,2,3,4],3,2),
    ([3],4,0),
    ([5,5,5,4,2,2,5],5,4),
    ([5,5,5,4,2,2,5],2,2)
])
def test_frequency_digit_counter(num,digit,res):
    assert frequency_digit_counter(num,digit)==res
#----------------------------------------------------------------------------------------
@pytest.mark.parametrize("num,multi,res",[
    (12,6,True),
    (18,6,True),
    (10,5,True),
    (14,7,True)
])
def test_frequency_digit_counter(num,multi,res):
    assert Multi_Checker(num,multi)==res

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
