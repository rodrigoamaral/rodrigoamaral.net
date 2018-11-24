Guia para os atalhos de teclado do Sublime Text
###############################################

:date: 2013-03-20 18:51
:summary: Algumas dicas para descobrir e memorizar os atalhos de teclado do Sublime Text.

.. image:: {static}/images/sublime_text.png
   :alt: Sublime Text

Todo mundo que usa o
computador para trabalhar durante muitas horas por dia já deve ter
notado que um dos segredos para ser mais produtivo é tirar as mãos do
teclado o menos possível. `Aprender a digitar
direito <http://www.typeonline.co.uk/lesson1.html>`__, eliminando alguns
vícios adquiridos ao longo dos anos, também ajuda bastante.

Quando falamos do Sublime Text, então, a importância de aprender a usar
os atalhos de teclado, ao invés de perder tempo alcançando o mouse, fica
ainda mais evidente. O Sublime Text tem atalhos de teclado para quase
tudo mas, quando se está iniciando, às vezes é um pouco difícil
descobri-los e memorizá-los. Para facilitar a tarefa, seguem algumas
dicas:

Dedique alguns minutos para explorar os menus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vasculhar os menus quando não se está procurando por nenhum comando
específico é muito útil para descobrir novos recursos. Em muitos casos,
os atalhos de teclado são mostrados ao lado de cada item. Algo que
também costumo fazer quando quero aprender os atalhos de alguma
ferramenta é me forçar a procurar pelo comando desejado no menu, usando
o mouse - para me lembrar de quanto é inconveniente, e por isso tenho
que aprender o atalho o quanto antes - ver qual é o atalho e depois
fechar o menu e usar o teclado. Faço isso toda vez que preciso executar
o comando, até memorizar.

Utilize a Command Palette
~~~~~~~~~~~~~~~~~~~~~~~~~

Após se familarizar com os menus, comece a usar a Command Palette
(``Ctrl+Shift+P``) para tudo. Com ela você poderá ter acesso a quase
todos os comandos sem precisar alcançar o mouse, mesmo se não lembrar o
atalho. Ao chamar a Command Palette, aparecerá uma lista de seleção com
o recurso de autocompletar. Depois é só começar a digitar algumas letras
da descrição do comando até encontrá-lo e pressionar ``Enter``.
Lembrando que, em muitos casos, o atalho específico de cada comando
também aparece na Command Palette.

Vasculhe os arquivos de configuração
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se ainda não achou o atalho que você queria, nem nos menus, nem na
Command Palette, não se desespere. O pulo do gato nesse caso é "partir
pra ignorância" e ir fuçar nos arquivos de configuração do Sublime Text:

#. Clique no... (oops!) Ative a Command Palette e digite "keybindings
   default" para abrir o arquivo de configuração de atalhos padrão para
   seu sistema operacional. Lá são definidos todos os atalhos de teclado
   padrão.
#. Procure por um trecho de alguma palavra que descreva o comando
   desejado. Como não existem descrições textuais de cada ação, pode não
   ser tão simples encontrar na primeira tentativa, mas se um atalho
   existe, ele estará lá.

Por exemplo, quando precisamos achar o atalho para duplicar uma linha,
basta começar a procurar (``Ctrl+F``) no arquivo de configuração por
"duplicate" e logo aparece a linha:

.. code-block:: javascript

  { "keys": ["ctrl+shift+d"], "command": "duplicate\_line" },


E eis aí nosso atalho: ``Ctrl+Shift+D``.

E os atalhos para comandos dos plugins instalados?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Os comandos dos plugins 
muitas vezes não aparecem no menu nem na Command Palette. Descobri-los
vai exigir um pouco do seu Sherlock Holmes interior, mas não é nenhum
bicho de sete cabeças. Como todos os atalhos de teclados estão definidos
em arquivos no formato JSON de fácil leitura, você vai precisar fazer o
seguinte:

#. Abrir a Command Palette.
#. Digitar "Browse Packages".
#. Procurar e abrir a pasta com o nome do plugin cujo atalho para o
   comando você quer descobrir.
#. Procurar e abrir o arquivo de configuração de atalhos, que possui a
   extensão ``sublime-keymap``. Lá estão todos os atalhos do plugin, é
   só procurar pelo que você precisa.

--------------

**Atualização:** Para conhecer mais dicas em português sobre o Sublime
Text, visite meu outro site `Sublime Text
Dicas <http://sublimetextdicas.com.br>`__!

--------------


**Referência:** dicas de `Josh Earl <http://joshearl.me/blog/>`__, autor
de `Sublime
Productivity <https://leanpub.com/sublime-productivity>`__\ .

