Compartilhando listas de podcasts em sites Pelican
##################################################

:date: 2020-04-20
:summary: Est ea mollit nulla velit non Lorem reprehenderit aliquip ut irure ullamco irure non eu. Laboris eiusmod qui laborum ut amet culpa. Ipsum nostrud sunt officia voluptate commodo ipsum veniam aute elit cillum exercitation culpa exercitation sint. 


.. Por quê?

No último ano, os podcasts começaram a fazer parte do cotidiano de muitas pessoas. Contando com a entrada de expoentes da chamada grande mídia, o formato tem crescido em popularidade. Com isso, é comum que as pessoas procurem indicações de programas para ouvir, geralmente vindas de amigos ou de alguém cujo trabalho admiram. Sendo assim, não seria legal poder responder à pergunta *"E aí, quais podcasts você tem escutado?"* dos nossos amigos com um único link? 

.. OPML

A maneira mais comum de compartilhar listas de feeds é usando arquivos no padrão OPML_ (*Outline Processor Markup Language*). A funcionalidade de exportar e compartilhar o OPML com a lista de podcasts - que grande parte dos aplicativos possui - certamente é suficiente para usuários intermediários de tecnologia. Porém, seria útil que as pessoas pudessem simplesmente visualizar a lista de forma amigável, sem precisar importá-la no seu aplicativo. Para isso, nada melhor que uma simples página web.


.. Explicação sobre o plugin e seu desenvolvimento

Pensando nesse tipo de necessidade, criei um pequeno plugin para Pelican que basicamente lê um arquivo OPML e gera uma lista dos feeds em formato HTML para ser inserida em páginas do site. A abordagem utilizada foi a mais "ingênua" possível. Por enquanto, implementei apenas o suficiente para ler os arquivos gerados pelo `Pocket Casts`_ , aplicativo de podcasts que uso atualmente. Optei por não utilizar nenhuma biblioteca pronta para lidar com o formato OPML porque 1) não queria adicionar dependências extras além do Pelican e 2) queria aprender um pouco sobre como lidar com arquivos XML. Como o próprio Pelican já tem como dependência externa a popular biblioteca `lxml`_, esse foi o caminho escolhido.


.. lxml

O primeiro passo foi aprender como ler arquivos XML usando o lxml. (...)


.. Plugins do Pelican

Com a leitura e transformação do OPML na string que eu queria, o passo seguinte foi aprender como funciona um plugin do Pelican, para que eu pudesse transformar meu script em algo que pudesse ser usado para para formatar automaticamente a página do site. (...)

.. Conclusão

O código está disponível em `<https://github.com/rodrigoamaral/pelican-opml>`__ e contribuições são muito bem vindas!

.. Referências

.. _OPML: http://dev.opml.org/
.. _Pocket Casts: https://www.pocketcasts.com/
.. _lxml: https://lxml.de/