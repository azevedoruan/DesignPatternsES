# Padrão Command
O *Command* é um padrão comportamental que transforma solicitações em objetos independentes encapsulando todas as informações relevantes para tal solicitação. Esta técnica permite você passar solicitação como argumentos de métodos, agendar sua execução e armazena-la em um histórico para que possa ser desfeita.

### Problema
Resumindo o problema apresentado no [Refactoring.guru](https://refactoring.guru/design-patterns/command). Imagine um editor de textos que nele há vários botões que realizam varios comandos diferentes. Mas alguns desses comandos são realizados por botões em outras telas do software e por atalhos (shortcuts) no teclado. Um exemplo simples seria o *copiar* e *colar*. Uma abordagem inicial para implementar essa funcionalidade seria criar uma classe base `Button` e várias subclasses concretas para cada ação. No entanto, essa abordagem apresenta três problemas: a quantidade massiva de sub-classes concretas que seria necessário ser criadas; alterações intensas na classe base quebraria todo os sistemas de botões, já que seria necessário alterar todas as outras sub-classes; dificuldade de ações vindas de objetos que não estejam diretamente associados a um botão, como por exemplo o atalho do teclado.

### Solução
O padrão Command traz uma alternativa mais flexível para este problema. Ele encapsula uma solicitação em um objeto. Dessa forma, cada ação seria representada por um objeto Command, desacoplando a invocação da ação da sua execução e permitindo que diferentes invocadores (botões, atalhos, menus, etc.) utilizem o mesmo comando.

### Diagrama UML
![Exemplo do padrão command](command-uml-example.png)

Fonte: [Refactoring.guru](https://refactoring.guru/design-patterns/command)

### Explicando as classes do código de exemplo
**Classe** `Command`: Define a interface para todos os comandos concretos.

**Classes** `CopyCommand`, `CutCommand`, `PasteCommand` e `UndoCommand`: Comandos concretos que realizam ações específicas.

**Classe** `CommandHistory`: Representa apenas uma coleção Pilha para armazenar os comandos que alteram o estado do editor.

**Classe** `Editor`: É onde é operado as alterações de texto. Todos os comandos delegam execuções para os métodos da classe Editor.

**Classe** `Application`: É a classe que instanciará todas as outras para fazer as relações e execuções.