# POO - Sistema de gerenciamento de biblioteca:

Hoje iremos explorar de forma prática e introduória o paradigma de orientação a objetos, uma abordagem única e flexível de resolução intuitiva de problemas que reflete a forma como enxergamos nossso mundo físico.

Utilizando os conceitos de classes, métodos e instâncias de objeto desenvolva um sistema simples de gerenciamento de uma biblioteca. O sitema deve conter no mínimo 3 classes principais: biblioteca, livro e usuário, cada uma com seus atributos e métodos próprios de modo a simular o processo de empréstimos, devolução e inclusão de livros no acervo.

Como forma de incetívo a seguir encontam-se exemplos de atributos e métodos que podem ser implementados por cada classe, as mesmas são apenas sugestões, portanto, sinta-se a vontade para modificá-las de acordo com sua visão de mundo.

<div id="sugestoes">
    <div id="atributos">
        <h3>Sugestões de atributos:</h3>
        <table>
            <tr>
                <th colspan="3">ATRIBUTOS</th>
            </tr>
            <tr>
                <th>Livro</th>
                <th>Usuário</th>
                <th>Biblioteca</th>
            </tr>
            <tr>
                <td>Título</td>
                <td>nome</td>
                <td>Nome</td>
            </tr>
            <tr>
                <td>Autor</td>
                <td>idade</td>
                <td>Acervo</td>
            </tr>
            <tr>
                <td>isbn</td>
                <td>sexo</td>
                <td>Endereço</td>
            </tr>
            <tr>
                <td>disponível</td>
                <td>livros_pegos</td>
                <td>Horário</td>
            </tr>
        </table>
    </div>
    <div id="metodos">
        <h3>Sugestões de métodos:</h3>
        <table>
            <tr>
                <th colspan="3">MÉTODOS</th>
            </tr>
            <tr>
                <th>Livro</th>
                <th>Usuário</th>
                <th>Biblioteca</th>
            </tr>
            <tr>
                <td>__init__()</td>
                <td>pegar_livro()</td>
                <td>Adicionar_livro()</td>
            </tr>
            <tr>
                <td>__str__()</td>
                <td>devolver_livro()</td>
                <td>Remover_livro()</td>
            </tr>
            <tr>
                <td>modificar_status()</td>
                <td>listar_livros_pegos()</td>
                <td>Listar_livros()</td>
            </tr>
        </table>
    </div>
</div>


## Tópicos trabalhados:
- criação de classes e atributos
- implementação e uso de métodos especiais (construtor e __str__)
- defenição de métodos
- criação de objetos e acesso aos seus atributos e comportamento
- atributos de classe

## Exemplos de teste: 
Ao término da implementação do sistema, tomando como base as sugestões acima, você deve ser capaz de executar plenamente as funcionalidades descritas. Através dos seus métodos construídos tente executar as seguintes operações abaixo:

- criar dois ou mais livros
- criar biblioteca
- adicionar livros criados ao acervo da biblioteca
- listar livros do acervo
- remover um dos livros do acervo
- listar novamente livros do acervo para verificar remoção
- criar usuário
- pegar emprestado um dos livros
- listar livros que usuário pegou emprestado
- devolver livro
- listar novamente livros disponíveis na biblioteca

