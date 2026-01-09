# Projeto de Análise de Dados - Academia Fitness Pro

## 👤 Integrantes
- FRANCIVALDO DO NASCIMENTO LIMA
- [Nome do segundo integrante aqui]

## 🎯 Tema Escolhido
**Treinos e Desempenho dos Alunos de uma Academia de Ginástica**

Este projeto analisa dados fictícios de treinos realizados por 20 alunos de uma academia, incluindo informações sobre modalidades praticadas, duração dos treinos, calorias queimadas, frequência semanal e se as metas foram atingidas.

## 🤖 Geração dos Dados
- **IA utilizada:** Claude (Anthropic)
- **Prompt usado:**
```
Crie 20 registros de treinos de academia em formato JSON.
Cada registro deve ter:
- aluno (nome completo variado, ex: 'Ana Silva', 'Carlos Souza')
- modalidade (ex: 'Musculação', 'Crossfit', 'Yoga', 'Spinning', 'Natação')
- duracao_minutos (número entre 40 e 90)
- calorias_queimadas (número entre 150 e 600)
- meta_atingida (true ou false, com aproximadamente 65% true)
- frequencia_semanal (número entre 2 e 5)

Deixe o JSON pronto para ser salvo em arquivo.
```

## 🚀 Como Executar o Programa

1. Baixe os arquivos `analise_dados.py` e `dados.json`
2. Coloque-os na mesma pasta
3. Certifique-se de ter o Python 3 instalado no seu computador
4. Abra o terminal na pasta onde estão os arquivos
5. Execute no terminal:
   ```bash
   python analise_dados.py
   ```
   ou
   ```bash
   python3 analise_dados.py
   ```

## 📊 O que o Programa Exibe

O programa realiza uma análise completa dos dados da academia e exibe as seguintes seções:

1. **Cabeçalho com informações do projeto** - Nome da academia e tema
2. **Confirmação de leitura dos dados** - Quantos registros foram carregados
3. **Lista completa de todos os treinos** - Detalhes de cada aluno: nome, modalidade, duração, calorias, frequência e se atingiu a meta
4. **Métricas de acúmulo** - Total de calorias queimadas, média de calorias por treino, e duração média dos treinos
5. **Contagem condicional** - Quantidade e percentual de alunos que atingiram suas metas
6. **Acúmulo por categoria** - Total de calorias queimadas por cada modalidade (Musculação, Crossfit, Yoga, etc.)
7. **Percepções/Insights** - Três descobertas importantes baseadas na análise dos dados
8. **Mensagem final** - Confirmação de que a análise foi concluída com sucesso

## 💡 Percepções Obtidas

**COM BASE NOS NOSSOS DADOS, DESCOBRIMOS QUE:**

1. **O Crossfit é o campeão em queima de calorias:**
   A modalidade Crossfit foi responsável pela maior queima total de calorias na academia, totalizando 2.130 kcal (aproximadamente 26% do total). Isso mostra que treinos de alta intensidade são extremamente eficientes para quem busca perder peso ou aumentar o condicionamento físico. Mesmo com menos praticantes que a Musculação, o Crossfit apresentou a maior média de calorias por sessão.

2. **Taxa de sucesso acima da média:**
   65% dos alunos (13 de 20) conseguiram atingir suas metas de treino, demonstrando um bom nível de comprometimento geral. No entanto, isso também revela que 35% dos alunos ainda precisam de mais motivação, orientação personalizada ou ajuste nas metas para alcançar seus objetivos. A academia pode focar em estratégias para aumentar esse percentual, como acompanhamento mais próximo dos alunos que não atingem as metas.

3. **Duração ideal dos treinos:**
   A duração média dos treinos é de aproximadamente 61 minutos, o que está dentro do intervalo recomendado por especialistas em fitness (45 a 75 minutos). Isso indica que os alunos estão dedicando tempo adequado para seus exercícios, permitindo aquecimento apropriado, execução dos exercícios principais e alongamento final. Treinos nessa faixa de duração tendem a gerar melhores resultados sem causar fadiga excessiva.

## 📚 O que Aprendemos

### Sobre Python:
- Como ler e processar arquivos JSON usando a biblioteca `json` e o comando `json.load()`
- Como usar estruturas de repetição (`for`) para percorrer listas de registros
- Como usar condicionais (`if/else`) para filtrar dados e fazer análises condicionais
- Como trabalhar com dicionários para acumular valores por categoria
- Como formatar strings com f-strings para criar saídas organizadas e profissionais
- Como usar a função `max()` com parâmetro `key` para encontrar valores máximos em dicionários

### Sobre Análise de Dados:
- A importância de calcular métricas de acúmulo (soma, média) para entender o panorama geral
- Como contagens condicionais ajudam a identificar padrões de comportamento (ex: quantos atingiram metas)
- Como agrupar dados por categoria revela insights importantes sobre diferentes segmentos
- Que os dados brutos sozinhos não são úteis - é preciso calcular métricas e extrair percepções
- Como percentuais facilitam a compreensão e comparação de dados
- Que insights devem ser específicos e baseados nos números calculados, não apenas observações genéricas

### Desafios que Superamos:
- Entender a estrutura do JSON e como acessar os campos corretamente usando colchetes e aspas
- Criar dicionários dinâmicos para acumular valores por categoria sem saber previamente quais categorias existem
- Calcular percentuais e formatar números decimais de forma apropriada com `.2f` e `.1f`
- Organizar o código de forma sequencial e legível, com comentários claros separando cada seção
- Garantir que os insights escritos realmente refletissem os dados calculados, sendo específicos e úteis

## 🔧 Estrutura do Projeto

```
📂 repositorio-dupla/
│
├── 📄 analise_dados.py    (código Python completo - 180 linhas)
├── 📄 dados.json          (20 registros de treinos da academia)
├── 📄 README.md           (este arquivo de documentação)
└── 📄 analise de requisitos.txt (especificações da atividade)
```

## ✅ Checklist de Requisitos Atendidos

- ✅ Arquivo `dados.json` com dados fictícios gerados por IA
- ✅ Arquivo `analise_dados.py` com código Python sequencial (sem funções `def`)
- ✅ Leitura dos dados usando `json.load()` e `with open()`
- ✅ Exibição completa de todos os 20 registros formatados
- ✅ 3 métricas de acumulação (total de calorias, média de calorias, duração média)
- ✅ 1 contagem condicional (alunos que atingiram a meta)
- ✅ 1 acumulação por categoria (calorias por modalidade)
- ✅ 3 percepções/insights detalhados e baseados nos dados
- ✅ Mensagens claras de início e fim da análise
- ✅ Arquivo `README.md` com documentação completa
- ✅ Código com comentários explicativos em cada seção

## 📈 Exemplo de Saída

```
==================================================
ANÁLISE DE DADOS - ACADEMIA FITNESS PRO
TEMA: Treinos e Desempenho dos Alunos
==================================================

✅ Dados carregados com sucesso!
📊 Total de registros: 20

==================================================
📋 LISTA COMPLETA DOS DADOS:
==================================================

Registro 1:
  Aluno: Ana Silva
  Modalidade: Musculação
  Duração: 90 minutos
  Calorias Queimadas: 450 kcal
  Frequência Semanal: 5x por semana
  Meta: ✅ Atingida

[... outros registros ...]

==================================================
📈 MÉTRICAS DE ACÚMULO:
==================================================

1. TOTAL DE CALORIAS QUEIMADAS: 8190 kcal
   (soma de todas as calorias queimadas)

2. MÉDIA DE CALORIAS POR TREINO: 409.50 kcal
   (total de calorias ÷ quantidade de treinos)

3. DURAÇÃO MÉDIA DOS TREINOS: 61.25 minutos
   (soma de todas as durações ÷ quantidade de treinos)

[... e assim por diante ...]
```

---

**🎓 Projeto desenvolvido para a disciplina de Programação em Python**

**📅 Data de entrega:** [Preencher com a data]

**🏫 Instituição:** [Preencher com o nome da escola/universidade]