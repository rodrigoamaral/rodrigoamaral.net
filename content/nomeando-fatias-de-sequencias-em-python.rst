Nomeando fatias de sequências em Python
#######################################

:date: 2013-06-07 17:55
:summary: Uma rápida explicação sobre como funciona a manipulção de objetos do tipo slice no Python.

.. image:: {filename}/images/pizza.jpg


Quem já precisou escrever algum programa para obter valores dentro de uma string, lista ou outra
sequência semelhante, certamente acabou envolvido em uma grande confusão
de valores fixos (*hardcoded*) de índices ao longo do código. Para
evitar isso, é bem provável que você tenha recorrido a algo como:

.. code-block:: python

  CAMPO_X_INICIO = 5
  CAMPO_X_FIM = 10
  CAMPO_Y_INICIO = 16
  CAMPO_Y_FIM = 19


Mas Python é Python: sempre dá para melhorar seu código quando você
aprende mais sobre os recursos da linguagem. Para tornar esse tipo de
código ainda mais legível e fácil de manter, podemos usar a função
built-in ``slice``. Em seu uso mais comum, a função recebe os índices
inicial e final de uma fatia e retorna um objeto do tipo
`slice <http://docs.python.org/2/glossary.html#term-slice>`__, que
representa uma porção de uma sequência.

Na prática, funciona assim: vamos supor que temos um arquivo texto no
qual cada linha é um registro contendo o número de matrícula do aluno e
as suas três notas em uma determinada disciplina:

.. code-block:: python

  >>> registro = "12345041009"


Os cinco primeiros caracteres correspondem sempre ao número de
matrícula. Os dois caracteres seguintes são a primeira nota, os dois
seguintes são a segunda e os dois restantes são a terceira.

Usando slice() para armazenar os intervalos correspondentes, temos:

.. code-block:: python

  >>> MATRICULA = slice(0, 5)
  >>> NOTA_1 = slice(5, 7)
  >>> NOTA_2 = slice(7, 9)

  >>> NOTA_3 = slice(9, 11)


Com isso, temos uma forma muito mais legível de definir os limites de
cada fatia que nos interessa na sequência, o que nos permite obter
facilmente os valores que queremos:

.. code-block:: python

  >>> registro[MATRICULA]
  '12345'
  >>> registro[NOTA_1]
  '04'
  >>> registro[NOTA_2]
  '10'
  >>> 
  registro[NOTA_3]
  '09'


**Referência:** `Python Cookbook, 3rd
Edition <http://shop.oreilly.com/product/0636920027072.do>`__ (recomendo
fortemente!)

Photo Credit: `Jorge
Quinteros <http://www.flickr.com/photos/92921037@N00/5985475727/>`__ via
`Compfight <http://compfight.com>`__
`cc <http://creativecommons.org/licenses/by-nc-nd/2.0/>`__


