# Builder Pattern
**Builder** é um padrão de design criacional no qual permite você construir objetos grandes e complexos em partes. O padrão permite a criação de diferentes tipos de objetos usando o mesmo código de construção.

### Problema
Suponhamos que temos que instanciar várias cópias do mesmo objetos, porém, para cada cópia, um objeto terá particularidades distintas um dos outros. No entanto, essas particularidades não devem ser suficientes para exigir a criação de um outro modelo.

Usando o exemplo do site [Refactoring.guru](https://refactoring.guru/design-patterns/builder), imagine um objeto do tipo **casa**. Desejamos instanciar várias casas, porém, algumas casas terão piscinas, outras terão garagens com mais vagas, algumas serão apenas a casa simples e entre outros exemplos.

Umas das abordagens seria criar uma super classe para o comportamento fundamental e, a partir dai, criar subclasses que fazeriam o papel das particularidades. Porém, eventualmente, você se deparia com um vasto número de subclasses e a cada parâmetro, aumentaria ainda mais a complexidades delas.

Outra abordagem seria criar um mega construtor com todos os parâmetros que engloba todas as particularidades do objeto. O problema dessa técnica é que para todas as instâncias, a maioria dos valores dos atriburos seriam nulos e seria extremamente dificultoso escreve-los, sem mencionar a poluição visual do código.

### Solução
A solução que este padrão nos traz é separar a lógica de construção do objeto para um outro objeto chamado *builder*. Este padrão organiza a construção do objeto passo a passo. A parte ideal é que você não precise chamar todos os passos da construção do objeto e sim somente as que interessam.

### Diagrama UML
![Diagrama UML do padrão Builder](structure.png)

fonte: [Refactoring.guru](https://refactoring.guru/design-patterns/builder)

### Explicando o código de exemplo
O código foi retirado da IA Gemini com o seguinte prompt: "crie para mim, uma implementação do padrão Builder" e adaptado para o contexto do objeto *Casa*.

**Classe** `Computer`: Representa o produto final (a casa).

**Classe** `ComputerBuilder`: O objeto onde fica a lógica de construção de casa.

**Métodos** `set_comodo`, `set_garagem`, etc.: Permitem configurar as diferentes partes da casa de forma fluente. O método retorna o próprio objeto do builder, permitindo encadear as chamadas.

**Método** `build`: Cria uma instância da classe Casa com as configurações definidas.
