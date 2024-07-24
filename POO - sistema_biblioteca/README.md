# POO - Sistema de gerenciamento de biblioteca:

Hoje iremos explorar de forma prática e introduória o paradigma de orientação a objetos, uma abordagem única e flexível de resolução intuitiva de problemas que reflete a forma como enxergamos nossso mundo físico.

Utilizando os conceitos de classes, métodos e instâncias de objeto desenvolva um sistema simples de gerenciamento de uma biblioteca. O sitema deve conter no mínimo 3 classes principais: biblioteca, livro e usuário, cada uma com seus atributos e métodos próprios de modo a simular o processo de empréstimos, devolução e inclusão de livros no acervo.

Como forma de incetívo a seguir encontam-se exemplos de atributos e métodos que podem ser implementados por cada classe, as mesmas são apenas sugestões, portanto, sinta-se a vontade para modificá-las de acordo com sua visão de mundo.

<style>
#sugestoes{
    display: flex;
    gap: 50px;
}
.tabelas{
    display: flex;
    align-items: flex-start;
    justify-content: flex-start;
}

.tabelas td, th{
    display: flex;
    justify-content: center;
}
</style>

<div id="sugestoes">
    <div id="atributos">
        <h3>Sugestões de atributos:</h3>
        <div class="tabelas">
            <table>
                <tr>
                </tr>
                <tr>
                    <th>Livro</th>
                </tr>
                <tr>
                    <td>Título</td>
                </tr>
                <tr>
                    <td>Autor</td>
                </tr>
                <tr>
                    <td>isbn</td>
                </tr>
                <tr>
                    <td>disponível</td>
                </tr>
            </table>
            <table>
                <tr>
                </tr>
                <tr>
                    <th>Usuário</th>
                </tr>
                <tr>
                    <td>nome</td>
                </tr>
                <tr>
                    <td>idade</td>
                </tr>
                <tr>
                    <td>sexo</td>
                </tr>
                <tr>
                    <td>livros_pegos</td>
                </tr>
            </table> 
            <table>
                <tr>
                </tr>
                <tr>
                    <th>biblioteca</th>
                </tr>
                <tr>
                    <td>Nome</td>
                </tr>
                <tr>
                    <td>Acervo</td>
                </tr>
                <tr>
                    <td>Endereço</td>
                </tr>
                <tr>
                    <td>Horário</td>
                </tr>
            </table>
        </div>   
    </div>
    <div id="métodos">
        <h3>Sugestões de métodos:</h3>
        <div class="tabelas">
            <table>
                <tr>
                </tr>
                <tr>
                    <th>Livro</th>
                </tr>
                <tr>
                    <td>__init__( )</td>
                </tr>
                <tr>
                    <td>__str__( )</td>
                </tr>
                <tr>
                    <td>modificar_status( )</td>
                </tr>
            </table>
            <table>
                <tr>
                    <th>Usuário</th>
                <tr>
                    <td>pegar_livro( )</td>
                </tr>
                <tr>
                    <td>devolver_livro( )</td>
                </tr>
                <tr>
                    <td>listar_livros_pegos( )</td>
                </tr>
            </table>
            <table>
                <tr>
                </tr>
                <tr>
                    <th>biblioteca</th>
                </tr>
                <tr>
                    <td>Adicionar_livro( )</td>
                </tr>
                <tr>
                    <td>Remover_livro( )</td>
                </tr>
                <tr>
                    <td>Listar_livros( )</td>
                </tr>
            </table>
        </div>
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

