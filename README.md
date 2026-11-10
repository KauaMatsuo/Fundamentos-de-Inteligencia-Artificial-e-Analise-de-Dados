# Python · Pandas · Seaborn

Anotações e exercícios do curso **Fundamentos de Inteligência Artificial e Análise de Dados** (SENAI-SP). O repositório reúne a evolução do aprendizado: de Python básico, passando pela manipulação de dados com **Pandas**, até visualização com **Seaborn**, além de uma planilha de estatística aplicada.

> Repositório de estudo. Os scripts são cadernos de anotações, com muitos trechos comentados de propósito para consulta e prática.

## Conteúdo

```
Python - Pandas - Seaborn/
├── Notas.py                                  # Python básico (fundamentos)
├── Notas_Pandas.py                           # Pandas: Series, DataFrame, filtros, estatística, agrupamento
├── Notas_Seaborn.py                          # Seaborn: gráficos exploratórios, categóricos e mapas de calor
├── Base Aula 002 - Exemplo.xlsx              # Base de vendas usada nas aulas de Pandas
├── Nova_planilha.xlsx                        # Exportação gerada pelo Pandas (base + coluna "comissao")
└── 02_Planilha_Estatistica_SENAI_Aluno.xlsx  # Planilha de estatística aplicada (fórmulas vivas)
```

## O que cada arquivo cobre

### `Notas.py` · Python básico
- Operações matemáticas, `print`, variáveis, f-strings e `input`
- Strings: fatiamento, `len`, `count`, `find`, `upper`, `lower`, `replace`, `split`
- Condicionais (`if/elif/else`) e operadores lógicos
- Laços `for` e `while`, tabuada, fatorial
- Mini-jogos: **Pedra, Papel e Tesoura** e **Ímpar ou Par**
- Tratamento de erros com `try/except` (`ZeroDivisionError`, `ValueError`)
- Funções, tuplas, listas (e listas aninhadas) e dicionários

### `Notas_Pandas.py` · Pandas
- `Series` (a partir de listas e dicionários) e operações alinhadas por índice
- `DataFrame`: criação, seleção com `[]`, `loc` e `iloc`, criação e remoção de colunas e linhas
- Filtros condicionais com `&`, `|`, `~` e `isin`
- Dados faltantes: `isnull`, `dropna`, `fillna` (com média e mediana)
- Importação de Excel (`read_excel`) e de páginas web (`read_html`)
- Estatística descritiva: `describe`, média, mediana, moda, desvio padrão, variância, quantis, `value_counts`, `nunique`, `cov`, `corr`, `nlargest`
- Exportação para Excel (`to_excel`) com a coluna calculada `comissao`
- Agrupamentos: `groupby` com `sum`, `mean`, `count` e `agg`

### `Notas_Seaborn.py` · Seaborn
- Análise exploratória com o dataset `tips`
- Univariados: `histplot`, `rugplot`, `kdeplot`, `ecdfplot`
- Relações entre variáveis: `scatterplot`, `jointplot` (scatter, hex, reg), `lmplot`, `pairplot`
- Categóricos: `barplot`, `countplot`, `boxplot`, `violinplot`, `stripplot`, `swarmplot`, `pointplot`, `catplot`
- Dataset `flights`: `lineplot`, `heatmap`, `clustermap` (com `standard_scale`)
- Salvando figuras em PNG com `plt.savefig`

### Planilhas
| Arquivo | Descrição |
|---|---|
| `Base Aula 002 - Exemplo.xlsx` | Base de vendas (aba `Dados Finais`) com colunas como `Loja`, `Vendedor`, `Produto`, `Quantidade`, `Preço de Compra`, `Preco`, `Desconto`, `Total`, datas de pedido, pagamento, envio e entrega, `Devolucao`, `Tipo de Envio`, `Peso` e `País`. |
| `Nova_planilha.xlsx` | Saída do `Notas_Pandas.py`: a mesma base com a coluna extra `comissao`. |
| `02_Planilha_Estatistica_SENAI_Aluno.xlsx` | Planilha com abas de Frequências, Medidas de Centro, Espalhamento e Posição, Probabilidade e a Ficha da Variável, todas com fórmulas que recalculam sozinhas. |

## Como rodar

### Requisitos
- **Python 3.12 ou superior** (os scripts usam f-strings com aspas aninhadas; o autor usa 3.14)
- Bibliotecas: `pandas`, `numpy`, `matplotlib`, `seaborn`, `openpyxl` e `lxml` (usada pelo `read_html`)

### Instalação

```bash
git clone https://github.com/KauaMatsuo/Fundamentos-de-Inteligencia-Artificial-e-Analise-de-Dados.git
cd Fundamentos-de-Inteligencia-Artificial-e-Analise-de-Dados

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

pip install pandas numpy matplotlib seaborn openpyxl lxml
```

### Execução

Execute os scripts a partir da pasta do projeto, para que os arquivos `.xlsx` sejam encontrados:

```bash
cd "Python - Pandas - Seaborn"
python Notas_Pandas.py
python Notas_Seaborn.py
```

## Dicas de uso

- **Trechos comentados:** vários blocos estão dentro de `'''...'''`. Para executar um tema, mova ou remova as aspas triplas ao redor dele.
- **Internet:** `Notas_Seaborn.py` baixa os datasets `tips` e `flights` do Seaborn, e `Notas_Pandas.py` lê uma tabela de um site (`pd.read_html`). Sem conexão, essas linhas falham.
- **Entrada do usuário:** `Notas.py` usa `input()` em vários exemplos, então rode-os de forma interativa.
- **Arquivos gerados:** `Nova_planilha.xlsx` e `Histograma.png` são criados ao executar as seções de exportação e de salvar figuras.

## Autor

**Kauã Kenzo Matsuo** · estudante de Engenharia da Computação · [@KauaMatsuo](https://github.com/KauaMatsuo)

## Licença

Projeto de estudo, sem licença definida.
