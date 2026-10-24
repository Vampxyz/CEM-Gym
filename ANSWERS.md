# | A. O fluxo

##  1 - Passo a passo: Inicio do projeto...
1. Foi pensado primeiro em como o projeto seria estruturado... quais seriam os nomes das pastas, variáveis, métodos, classes e etc.

2. Após ter a estrutura pronta começamos a criar o projeto chamado **"CEM Gym"** ***(Corpo em Movimento Gym)***.

```MD
git clone git@github.com:Vampxyz/CEM-Gym.git
cd CEM-Gym
code .

python -m venv .venv   # Cria o ambiente virtual
source .venv/bin/activate.fish   # Ativa a venv no workspace

pip install django   # Instala o django
pip freeze > requirements.txt   # Adiciona os requisitos no arquivo requirements.txt

django-admin startproject config .   # Cria o projeto "config" com o manage.py na raiz do projeto
python manage.py startapp gym   # Cria o app "gym"
```

3. Seguindo todos esse processo, começamos a criar as classes(tabelas) e colunas no arquivo ***models.py***, depois de tudo criado rodamos os seguintes comandos:

```MD
python manage.py makemigrations   # "Varre" todos os arquivos models.py do projeto e valida se tá tudo certo
python manage.py migrate   # Pega todas as migrações pendentes e adiciona ao arquivo db.sqlite3

py manage.py createsuperuser   # Pede informações para criar um superuser
```

4. Depois criamos nossas funções pra retornar nossos htmls no arquivo ***views.py*** e registramos nossas tabelas no painel administrativo do django no arquivo ***admin.py***.

5. O próximo passo foi criar os arquivos html e css e usar a IA para criar e polir o front-end em geral.

##  2 - Requisitos web: o que acontece por debaixo dos panos...
#### Quando acessamos o /turmas/ o navegador faz uma requisição à função que retornou esse html ***(Que fica no arquivo gym/views.py)***.

Porém além de retornar o html ele pega do banco de dados todas as turmas existentes e guarda em uma variável "classes", depois é criado uma nova variável chamada "context" que é um dicionário, como valor da chave "classes" é passado a variável classes. Assim sendo possível utilizar o que vem do JSON "context" no HTML

---
# | B. O porquê
## 3. Por que o Django precisa de dois comandos ( makemigrations e migrate ) depois que vocês escreveram o models.py ? O que cada um faz? O que aconteceria se rodassem só o primeiro?

1. O django precisa do makemigrations e o migrate porque um "complementa" o outro, esses dois comandos existem porque após criar toda a estrutura das tabelas no models.py o makemigrations é rodado, ele vai ler todos os models.py do projeto e vai, tabela por tabela, validando se está tudo como deve estar para o banco de dados do django, se estiver tudo okay ele vai adicionar em um arquivo na pasta migrations do app atual uma "pendência" das estruturas das tabelas, com isso o comando migrate vai estar disponível para ser usado... usando o migrate ele vai pegar esses arquivos de pendências nas pastas migrations e vai de fato adicionar ao banco de dados. 
2. Se rodasse apenas o primeiro comando ele faria essa verificação nos models e se estivesse tudo okay ele iria retornar que tudo está correto e mais nada.

## 4. A turma guarda a modalidade como uma referência (chave estrangeira), e não como um texto com o nome da modalidade. Que problema o texto causaria? Dê um exemplo concreto com os dados da academia.

1. Acontece que a modalidade além de ter o nome dela, tem a descrição e o status se está ativa ou não... se fosse passado apenas o nome da modalidade eu não conseguiria filtrar apenas as modalidades que tem o status ativo, não conseguiria mostrar no HTML a descrição dessa modalidade também

## 5. O que acontece quando a proprietária tenta excluir a modalidade Musculação, que tem turmas? Onde, no código, está a decisão que produz esse comportamento, e por que vocês escolheram essa opção em vez de apagar as turmas junto?

1. Não dá pra excluir uma modalidade onde existe uma turma usando ela. Localizada na linha 33 do arquivo ***gym/models.py***: `on_delete=models.PROTECT,`; essa linha fica dentro da variável que serve como coluna de modalidade da tabela de turmas, essa linha **verifica se ao deletar** a modalidade há alguma turma usando ela, se a modalidade estiver em uso ele avisa algo como: **"Deletar a modalidade selecionada requer a exclusão dos seguintes objetos relacionados protegidos: "** e aí retorna o que foi criado na função `__str__` da tabela de turmas, ficaria algo como: **"Turma: Ginástica - Quarta-feira 16:00"**. Foi escolhido essa forma porque na regra de código **RN03: "Não deve ser possível excluir uma modalidade que ainda tenha turmas cadastradas."**

## 6. O dia da semana vem de uma lista fixa e não de um campo de texto livre. O que a lista fixa garante para a cliente? O que ela ganha, na prática, quando filtra as turmas no painel?

1. Primeiro, por ser uma lista já definida os dias da semana, é uma preocupação a menos de ter que colocar inputs para o usuário digitar os dias da semana, qualquer erro de escrita já poderia ficar mais bagunçado o código, iria ficar mais longo o código por ter que ficar dando append no input que o usuário digitou e etc... colocar a possibilidade de filtrar pelos dias da semana também é mais fácil porque quando for registrar no painel essa tabela, já tem o "parâmetro" "list_filter" que a pessoa passa essa lista de dias da semana e pronto, bem mais rápido para desenvolver e essa função pra o cliente iria ter que ter de qualquer jeito por ser um requisito de funcionalidades.

## 7. Sem list_display , list_filter e search_fields , o painel continuaria funcionando. O que a cliente perderia? Relacione com a fala dela na reunião de levantamento.

1. Continuaria funcionando mas não iria ter a funcionalidade de filtrar por modalidade e/ou dia da semana e o retorno visual da tabela poderia ficar pior por não ter o display.

## 8. Por que a página inicial mostra três modalidades e não quatro? Mostre a linha de código responsável e explique-a.

1. Na verdade, na home page mostra todas as modalidades que estejam ativas:

### Código da views.py:
```py
def index(request):
    modalities = models.Modality.objects.filter(active=True)
    classes = models.Class.objects.all()

    context = {
        "modalities": modalities,
        "classes": classes,
    }

    return render(request, "index.html", context)
```

#### -> Na variável "modalities" armazena um "get" na tabela "Modality" só que passando um filtro onde "active" deve ser True, ou seja, o método .filter vai retornar apenas as modalidades onde o active é True.

### Código html:
```HTML
{% for modality in modalities %}
    <div class="card">
        <div class="card-header">
            <h3>{{ modality.name }}</h3>
        </div>

        <div class="card-body">
            <p>{{ modality.description|default:"Confira esta modalidade direto na nossa recepção." }}</p>
        </div>

        <div class="card-footer">
            <span class="card-badge">Disponível</span>
        </div>
    </div>

    {% empty %}

    <p>Nenhuma modalidade disponível no momento.</p>
{% endfor %}
```

#### -> Aqui fica a renderização de como as informações estão estruturadas de fato.

---
# | C. O processo
## 9. Cite um trecho que o Copilot gerou e que vocês tiveram que corrigir ou rejeitar. O que estava errado ou diferente do requisito? Como descobriram?

1. Não usei o copilot, usei apenas o Gemini... um uso bruto do gemini foi no front-end, dei exemplos de como queria o ***index.html*** e o ***classesList.html***, ele fez como foi pedido, apenas fui pedindo algumas coisas que percebi que poderia melhorar, como um media-query para os cards da seção "o que oferecemos" e limitar a tabela do HTML de turmas

## 10. Houve alguma decisão que o documento de requisitos não cobria? Qual foi e o que a equipe decidiu? (Se registraram no README, copie aqui.)

1. Nenhuma