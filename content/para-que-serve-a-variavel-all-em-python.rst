Para que serve a variável __all__ em Python?
############################################

:date: 2021-05-29
:summary: Uma breve explicação sobre como a variável especial __all__ pode ser útil na organização do código de pacotes Python
:cover: images/python-code.jpg

Quando importamos os submódulos de um pacote usando asterisco - como em ``from pacote import *`` - o intepretador importa o pacote ``pacote`` e também todos nomes definidos nele. Quando isso acontece, corremos o risco de que haja conflito entre os nomes que já estivermos usando no código, o que pode provocar efeitos imprevisíveis no programa.

Para reduzir o risco de que isso aconteça, podemos usar uma característica do comando ``import``. Ao ser utilizado com ``*``, o comando procura pela variável especial ``__all__`` no código-fonte do pacote que está sendo importado. Caso o pacote seja composto por vários arquivos, o comando procura no arquivo ``__init__.py``. A variável ``__all__`` define a lista dos nomes de submódulos que serão importados quando a operação usar ``*``. Quando falamos em submódulos, estamos falando de qualquer nome que esteja dentro do pacote, seja ele uma variável, função, classe ou mesmo outro pacote. 

Portanto, uma boa prática na organização do código de pacotes que serão reutilizados por outros programas é declarar a variável ``__all__`` contendo unicamente os submódulos que devem estar públicos para uso. Além de reduzir o risco de conflitos de nomes, essa prática de certa forma também ajuda na documentação do pacote.

**EXEMPLO**

**pacote.py**

::

  __all__ = ["foo", "bar"]

  def foo():
      return "foo"

  def bar():
      return "bar"

  def nao_usar():
      return "Não use esta!"


**programa.py**

::

  from pacote import *

  print(foo())
  print(bar())
  print(nao_usar())
  
**Resultado:**

::

  foo
  bar
  Traceback (most recent call last):
    File "programa.py", line 5, in <module>
      print(nao_usar())
  NameError: name 'nao_usar' is not defined


**IMPORTANTE:** Em todo caso, devemos lembrar que usar o ``import *`` é algo que **deve ser evitado**, conforme deixa claro o próprio de guia de estilo do Python (`PEP-8 <https://www.python.org/dev/peps/pep-0008/#imports>`__).

