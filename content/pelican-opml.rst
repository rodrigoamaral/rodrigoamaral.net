Compartilhando listas de podcasts em sites Pelican
##################################################

:date: 2020-11-27
:summary: Como criar um plugin do Pelican para publicar uma página com uma lista de links para podcasts a partir de um arquivo no formato OPML


.. image:: {static}/images/podcast-microphone.jpg
    :alt: Podcast microphone

.. Por quê?

No último ano, os podcasts começaram a fazer parte do cotidiano de muitas pessoas. Contando com a entrada de expoentes da chamada grande mídia, o formato tem crescido em popularidade. Com isso, é comum que as pessoas procurem indicações de programas para ouvir, geralmente vindas de amigos ou de alguém cujo trabalho admiram. Sendo assim, não seria legal poder responder à pergunta *"E aí, quais podcasts você tem escutado?"* dos nossos amigos com um único link? 

.. OPML

A maneira mais comum de compartilhar listas de feeds é usando arquivos no padrão OPML_ (*Outline Processor Markup Language*). A funcionalidade de exportar e compartilhar o OPML com a lista de podcasts - que grande parte dos aplicativos possui - certamente é suficiente para usuários intermediários de tecnologia. Porém, seria útil que as pessoas pudessem simplesmente visualizar a lista de forma amigável, sem precisar importá-la no seu aplicativo. Para isso, nada melhor que uma simples página web.


.. Explicação sobre o plugin e seu desenvolvimento

Pensando nesse tipo de necessidade, criei um pequeno plugin para Pelican que basicamente lê um arquivo OPML e gera uma lista dos feeds em formato HTML para ser inserida em páginas do site. A abordagem utilizada foi a mais "ingênua" possível. Por enquanto, implementei apenas o suficiente para ler os arquivos gerados pelo `Pocket Casts`_ , aplicativo de podcasts que uso atualmente. Optei por não utilizar nenhuma biblioteca pronta para lidar com o formato OPML porque 1) não queria adicionar dependências extras além do Pelican e 2) queria aprender um pouco sobre como lidar com arquivos XML. Para isso, o uso da popular biblioteca `lxml`_ foi o caminho escolhido.


Lendo arquivos XML com lxml
===========================

A biblioteca ``lxml`` pode ser instalada via pip:

::

  $ pip install lxml

Após a instalação, o primeiro passo foi aprender como ler arquivos XML usando o lxml. Para fazer o *parse* de um arquivo que contém uma estrutura XML, usamos o método ``parse()``  o módulo ``lxml.etree``. O método recebe um arquivo (ou objeto *file-like*) aberto e retorna um objeto do tipo ``ElementTree``. Outra opção é passar diretamente uma string com o caminho do arquivo.

::

  from lxml import etree

  # opção 1
  f = open("arquivo.xml", "r")
  tree = etree.parse(f)
  f.close()

  # opção 2
  tree = etree.parse("arquivo.xml")

Uma vez que já temos o nosso  ``ElementTree`` carregado com a estrutura do XML, precisamos obter o nó inicial (*root*) para percorrer a estrutura a partir dele. Para isso, vamos usar o método ``getroot()``. No nosso caso específico - arquivos que seguem a especificação `OPML`_ - o elemento do XML que nos interessa é o ``<outline>``. Sendo assim, podemos usar o método ``iter()`` do elemento inicial para encontrar todas as ocorrências de ``<outline>`` que partem dele. Por fim, usamos o método ``get()`` para obter o valor dos atributos que nos interessam, que no caso são o ``text`` e ``xmlUrl``, e armazená-los em alguma estrutura:

:: 

  root = tree.getroot()
  elements = []
  for e in root.iter("outline"):
      text = e.get("text")
      url = e.get("xmlUrl")
      elements.append((text, url))

(...)

Criando um plugin para Pelican
==============================

Após conseguir a leitura e transformação do OPML, o passo seguinte foi aprender como funciona um plugin do Pelican, para que eu pudesse transformar meu script em algo que pudesse ser usado para formatar automaticamente a página do site.

Um plugin do Pelican consiste em módulo que possui uma função chamada ``register()``. Essa função é responsável por registrar as funções que serão executadas pelo Pelican para executar a lógica do plugin. Isso é feito conectando cada uma delas a ``signals``, que são sinais emitidos pelo Pelican em cada etapa da geração do site. Segue um exemplo retirado da própria documentação do Pelican:

:: 
  
  import logging

  from pelican import signals

  log = logging.getLogger(__name__)

  def test(sender):
      log.debug("%s initialized !!", sender)

  def register():
      signals.initialized.connect(test)



.. Conclusão

O código completo com os detalhes da implementação está disponível em `<https://github.com/rodrigoamaral/pelican-opml>`__ e contribuições são muito bem vindas!


Image by `StockSnap <a href="https://pixabay.com/users/stocksnap-894430/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2618102">`_ from `Pixabay <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2618102">`_.

.. Referências

.. _OPML: http://dev.opml.org/
.. _Pocket Casts: https://www.pocketcasts.com/
.. _lxml: https://lxml.de/