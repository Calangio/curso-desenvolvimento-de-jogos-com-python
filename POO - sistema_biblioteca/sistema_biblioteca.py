class Biblioteca:
    def __init__(self, nome, endereco, horario):
        self.nome=nome;
        self.acervo=[];
        self.endereco=endereco;
        self.horario=horario;

    def __str__(self):
        return f"{self.nome}, endereço: {self.endereco}, horário de funcionamento: {self.horario}";

    def listar_livros(self):
        for livro in self.acervo:
            print(livro);

    def add_livro(self, livro):
        if isinstance(livro, Livro):
            self.acervo.append(livro);
            print("livro adicionado com sucesso!");
        else:
            print("insira uma livro pre-cadastrado!");

    def remover_livro(self, livro):
        if isinstance(livro, Livro) and livro in self.acervo:
            self.acervo.remove(livro);
            print("livro removido com sucesso!");
        else:
            print("livro inexistente ou não cadastrado no acervo!");


class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo=titulo;
        self.autor=autor;
        self.isbn=isbn;
        self.disponivel=True;

    def __str__(self):
        apresentação_livro=f"{self.isbn}, título: {self.titulo}, autor: {self.autor}";
        if self.disponivel==True:
            apresentação_livro+=f", status: disponível";
        else:
            apresentação_livro+=f", status: indisponível";
        
        return apresentação_livro;

    def modificar_status(self):
        if self.disponivel:
            self.disponivel=False;
        else:
            self.disponivel=True;

class Usuario:
    def __init__(self, nome, idade, sexo):
        self.nome=nome;
        self.idade=idade;
        self.sexo=sexo;
        self.livros_emprestados=[];

    def __str__(self):
        return f"usuário: {self.nome}, idade: {self.idade}, sexo: {self.sexo}";

    def listar_livros_emprestados(self):
        for livro in self.livros_emprestados:
            print(livro);

    def pegar_livro(self, livro):
        if isinstance(livro, Livro):
            if livro.disponivel==True:
                livro.modificar_status();
                self.livros_emprestados.append(livro);
                print("livro emprestado com sucesso!");
            else:
                print("livro indisponível!");
        else:
            print("livro inexistente!");

    def devolver_livro(self, livro):
        if isinstance(livro, Livro):
            if livro in self.livros_emprestados:
                livro.modificar_status();
                self.livros_emprestados.remove(livro);
                print("livro devolvido com sucesso!");
            else:
                print("o livro indicado não consta como pego pelo usuário");
        else:
            print("ensira um livro válido");

    def listar_livros_emprestados(self):
        for livro in self.livros_emprestados:
            print(livro.titulo);

#exemplos de teste
#execute os casos de teste abaixo, de preferência de forma sequencial, para obsevar o comportamento dos nossos métodos

#criando livros:
livro1 = Livro("pequeno princípe", "Antoine de Saint-Exupéry", "978-65-5552-136-8");
livro2 = Livro("as reinações de narizinho", "Monteiro Lobato", "978-65-84879-38-6");
livro3 = Livro("O Orfanato da Srta. Peregrine", "Ransom Riggs", "978-85-8044-699-9");

#criando biblioteca:
biblioteca = Biblioteca("biblioteca nacional", "Av. Rio Branco, 219 - Centro, RJ", "10 as 16");

#adicionando livro a biblioteca criada:
biblioteca.add_livro(livro1);
biblioteca.add_livro(livro2);
biblioteca.add_livro(livro3);

#exibindo livros adicionados ao acervo:
biblioteca.listar_livros();

#removendo livro do acervo:
biblioteca.remover_livro(livro3);

#listando livros para verificar a remoção:
biblioteca.listar_livros();

#criando um novo usuário:
usuario1 = Usuario("joão", 22, "masculino");

#usuário pega emprestado um dos livros do acervo:
usuario1.pegar_livro(livro1);

#listando livros pegos emprestados pelo usuário:
usuario1.listar_livros_emprestados();

#verificando status dos livros no acervo:
biblioteca.listar_livros();

#usuário devolve livro pego emprestado:
usuario1.devolver_livro(livro1);

#listar novamente livros do acervo para verificar se o livro1 se encontra dispoível:
biblioteca.listar_livros();


