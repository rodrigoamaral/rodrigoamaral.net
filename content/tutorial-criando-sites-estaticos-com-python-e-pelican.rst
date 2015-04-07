Tutorial: Criando sites estáticos com Python e Pelican
######################################################

:date: 2013-07-16 20:37
:summary: Aprenda os primeiros passos para criar um site de forma rápida usando o Pelican, um gerador de sites estáticos escrito em Python.


Por que um site estático? 
-------------------------

Com as facilidades proporcionadas por serviços como Blogger, Tumblr,
Wordpress e similares, por que alguém deveria optar por um site
estático? Alguns motivos:

-  Hospedagem mais barata e independente da continuidade de um serviço
   específico
-  Controle total sobre o layout e conteúdo
-  Portabilidade
-  Trabalhar com arquivos de texto puro é mais simples e mantém você
   focado no conteúdo
-  Você pode usar o editor de texto de sua preferência
-  Mais fácil de manter controle de versões, backup etc.
-  **É mais divertido!**

O que é o Pelican?
------------------

`Pelican <http://docs.getpelican.com/en/latest/>`__ é um gerador de
sites estáticos escrito em Python que permite criar conteúdo diretamente
em arquivos de texto nos formatos
`RestructuredText <http://docutils.sourceforge.net/rst.html>`__
(default), `Markdown <http://daringfireball.net/projects/markdown/>`__
ou `AsciiDoc <http://www.methods.co.nz/asciidoc/index.html>`__. Além
disso, inclui uma ferramenta de linha de comando que facilita a geração
do site, convertendo os arquivos texto para HTML.

Com o Pelican, é possível gerar sites estáticos que, na prática, têm as
mesmas funcionalidades de sites dinâmicos. Um blog feito com o Pelican,
por exemplo, disponibiliza conteúdo em formato de artigos ou de páginas,
comentários (via serviços externos), suporte a templates, publicação de
artigos em mais de um idioma, feeds RSS do conteúdo, realce de sintaxe
em trechos de código-fonte, geração de PDF dos artigos/páginas,
integração com serviços externos como Twitter e Google Analytics, entre
outros.

Abaixo, segue um breve tutorial sobre o uso do Pelican:

Instalação
----------

Antes de instalar, é recomendado criar um ambiente virtual separado para
o seu projeto, usando
`virtualenv <http://www.virtualenv.org/en/latest/>`__. A instalação do
Pelican é feita como um pacote Python comum. A maneira mais fácil é usar
o `pip <http://www.pip-installer.org/en/latest/>`__:

::

    $ pip pelican

Para gerar sites a partir de arquivos no formato Markdown, é necessário
instalar também o pacote correspondente:

::

    $ pip Markdown

Neste tutorial, vamos assumir que o módulo Markdown foi instalado e que
vamos trabalhar com arquivos nesse formato.

O comando pelican
-----------------

Após a instalação, o comando ``pelican`` fica disponível para uso.
Quando invocamos o comando sem parâmetros adicionais, o Pelican procura
por arquivos de conteúdo no mesmo diretório em que o comando foi chamado
e gera toda a estrutura padrão de um blog estático no diretório
``output``.

Para testar o funcionamento, crie um arquivo chamado ``hello.md`` com o
seguinte conteúdo:

::

    Title: Hello!
    Date: 2013-07-10 17:00

    Hello, Pelican!

Após executar o comando ``pelican``, note que foi criado o diretório
``output`` contendo, entre outros, o arquivo ``hello.html`` com o
conteúdo que criamos no ``hello.md``. Abra o arquivo ``index.html`` no
browser de sua preferência e veja o resultado.

Aparentemente, o HTML foi gerado, mas a página está sem os estilos e os
links estão quebrados, certo? Isso acontece porque ainda não
configuramos alguns detalhes do nosso site. Felizmente, o Pelican traz o
comando ``pelican-quickstart`` para facilitar nossa vida.

O comando pelican-quickstart
----------------------------

O que o comando pelican-quickstart faz é criar o esqueleto de um site
interativamente, através de uma série de perguntas nas quais informamos
os principais parâmetros de configuração sem precisar editar diretamente
os arquivos correspondentes (os quais veremos mais à frente neste
tutorial).

No diretório do seu projeto, digite no terminal:

::

    $ pelican-quickstart

O configurador interativo fará as seguintes perguntas:

#. **Onde você quer criar seu web site?** Aqui devemos informar o
   diretório no qual desejamos que o pelican crie a estrutura do site. O
   valor padrão é o próprio diretório no qual o pelican-quickstart foi
   chamado.
#. **Qual será o título deste web site?** Informe o título do site. Este
   é o valor que irá aparecer no na tag ``<title>`` e no cabeçalho do
   template padrão.
#. **Qual será o autor deste web site?** Informe o nome do principal
   autor do site.
#. **Qual será o idioma padrão deste web site?** O valor padrão é ``en``
   (inglês). Se quisermos nosso site em português, devemos informar
   ``pt``.
#. **Você quer especificar um URL de prefixo?** Se a resposta for sim, o
   programa solicitará em seguida o URL.
#. **Você quer habilitar a paginação de artigos?**\ Se a resposta for
   sim, o programa solicitará em seguido número máximo de artigos que
   devem ser exibidos numa mesma página. Nesse caso, o valor padrão é
   10.
#. **Você quer gerar um Makefile para facilitar o gerenciamento do seu
   website?** É muito imporante responder "*sim*\ " a esta pergunta.
   Como veremos em detalhes mais à frente, muitos aspectos do
   desenvolvimento, geração e publicação do site são automatizados com o
   uso do Makefile gerado pelo Pelican.
#. **Você quer um script de auto-reload e simpleHTTP para auxiliar no
   desenvolvimento do tema e do site?** Esta opção cria o arquivo
   ``develop_server.sh``, que é responsável por habilitar o servidor de
   desenvolvimento e recarregar o site após cada modificação no conteúdo
   que está sendo desenvolvido. O valor padrão recomendado é "*sim*\ ".
#. **Você quer fazer o upload do seu site usando FTP?** O valor padrão
   recomendado é *não*, mas sempre é possível modificar o arquivo de
   configurações para configurar o upload via FTP posteriormente, caso
   necessário.
#. **Você quer fazer o upload do seu site usando SSH?** Vale a mesma
   explicação da pergunta anterior.\ **
   **
#. **Você quer fazer o upload do seu site usando Dropbox?** Aqui também
   vale a mesma explicação dos dois itens anteriores.
#. **Você quer fazer o upload do seu site usando S3?** Idem itens
   anteriores.

Pronto. Ao fim da execução do ``pelican-quickstart``, o Pelican terá
criado para você toda a estrutura básica do site, com todos os arquivos
de configuração necessários. A estrutura fica assim:

-  ``content`` - Diretório no qual colocaremos os arquivos de conteúdo
   (arquivos \*.md, no nosso caso)
-  ``output`` - Diretório no qual serão gerados os arquivos HTML gerados
   pelo Pelican
-  ``develop_server.sh`` - Shell script que inicia o servidor de
   desenvolvimento do Pelican em modo debug
-  ``pelicanconf.py`` - Arquivo de configuração no qual são definidas
   algumas variáveis usadas ao longo do desenvolvimento do site
-  ``publishconf.py`` - Arquivo de configuração contendo parâmetros
   relativos à publicação do site
-  ``Makefile`` - Contém um conjunto de tarefas do ``make`` que servem
   para automatizar a geração do site, como veremos na seção seguinte.

Usando o Makefile
-----------------

Entre outras tarefas, o Makefile gerado pelo Pelican nos permite
"levantar" o site localmente de maneira rápida e fácil. Basta fazer:

::

    $ make devserver

Com isso, o servidor de desenvolvimento do Pelican é iniciado. Para
testar, acesse http://localhost:8000/ no browser e veja que agora o site
aparece com a formatação correta do tema padrão do Pelican.

Além de devserver, o Makefile disponibiliza outras tarefas:

clean
    Apaga o conteúdo do diretório de saída (``output``).
html
    Gera novamente os arquivos HTML do site no diretório de saída.
regenerate
    Gera os arquivos HTML toda vez que uma mudança nos arquivos de
    conteúdo é detectada.
stopserver
    Encerra a execução do servidor de desenvolvimento.
publish
    Gera o site usando as configurações do ambiente de produção
    definidas no módulo ``publishconf.py``.

Criando o conteúdo do seu site
------------------------------

O Pelican trabalha com os conceitos de *artigos* e *páginas*. Artigos
são organizados cronologicamente, como um blog. Páginas são atemporais,
como por exemplo a seção "Sobre" ou "Contato" de um blog.

O tipo de conteúdo padrão do Pelican é o artigo. Para criar um artigo no
formato Markdown, é necessário informar, no mínimo, o título do artigo e
a data de publicação. Foi isso o que fizemos no arquivo ``hello.md`` do
início deste tutorial. No entanto, se quisermos aproveitar todas as
funcionalidades do Pelican para organizar o conteúdo do nosso site,
devemos incluir mais algumas tags no nosso arquivo:

::

    Title: Hello!
    Date: 2013-07-10 17:00
    Category: Python
    Tags: pelican, markdown
    Slug: primeiro-artigo
    Author: Rodrigo Amaral
    Summary: Este é um resumo do conteúdo do artigo

    Olá!
    Este é o **primeiro** artigo do nosso site criado com o [Pelican](http://getpelican.com).

As primeiras 7 linhas correspondem aos metadados do nosso artigo. Depois
delas, vem o conteúdo em formato Markdown. Crie um arquivo com o
conteúdo acima, coloque-o no diretório content do seu projeto e gere
novamente o site. Abra o site no navegador e perceba que agora a página
contém informações novas, tais como tags, categoria e nome do autor.
Perceba também que o nome do arquivo HTML gerado é o mesmo nome que
informamos na tag *Slug*.

Para criar conteúdo do tipo página, basta criar um diretório chamado
``pages`` dentro do diretório ``content`` do seu projeto. Os arquivos
que estiverem dentro de ``pages`` são, por padrão, automaticamente
gerados como páginas.

Conclusão
---------

Esta foi uma breve descrição de como dar os primeiros passos com essa
fantástica ferramenta para geração de sites estáticos. Futuramente,
pretendo entrar em maiores detalhes sobre configurações e recursos
avançados do Pelican.

