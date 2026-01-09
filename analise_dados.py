# ==================================================
# ANÁLISE DE DADOS - ACADEMIA FITNESS PRO
# Tema: Treinos e Desempenho dos Alunos
# ==================================================

import json

print("\n" + "="*60)
print("ANÁLISE DE DADOS - ACADEMIA FITNESS PRO")
print("TEMA: Treinos e Desempenho dos Alunos")
print("="*60 + "\n")

# -------------------------------------------------
# 1. LER OS DADOS DO ARQUIVO JSON
# -------------------------------------------------

with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print(f"✅ Dados carregados com sucesso!")
print(f"📊 Total de registros: {len(dados)}\n")

# -------------------------------------------------
# 2. EXIBIR OS DADOS COMPLETOS
# -------------------------------------------------

print("="*60)
print("📋 LISTA COMPLETA DOS DADOS:")
print("="*60 + "\n")

contador = 1
for registro in dados:
    print(f"Registro {contador}:")
    print(f"  Aluno: {registro['aluno']}")
    print(f"  Modalidade: {registro['modalidade']}")
    print(f"  Duração: {registro['duracao_minutos']} minutos")
    print(f"  Calorias Queimadas: {registro['calorias_queimadas']} kcal")
    print(f"  Frequência Semanal: {registro['frequencia_semanal']}x por semana")

    if registro['meta_atingida']:
        print(f"  Meta: ✅ Atingida")
    else:
        print(f"  Meta: ❌ Não atingida")

    print()
    contador += 1

# -------------------------------------------------
# 3. CALCULAR MÉTRICAS DE ACÚMULO
# -------------------------------------------------

print("="*60)
print("📈 MÉTRICAS DE ACÚMULO:")
print("="*60 + "\n")

# A) SOMA TOTAL DE CALORIAS
soma_calorias = 0
for registro in dados:
    soma_calorias += registro['calorias_queimadas']

print(f"1. TOTAL DE CALORIAS QUEIMADAS: {soma_calorias} kcal")
print(f"   (soma de todas as calorias queimadas)\n")

# B) MÉDIA DE CALORIAS POR TREINO
media_calorias = soma_calorias / len(dados)
print(f"2. MÉDIA DE CALORIAS POR TREINO: {media_calorias:.2f} kcal")
print(f"   (total de calorias ÷ quantidade de treinos)\n")

# C) DURAÇÃO MÉDIA DOS TREINOS
soma_duracao = 0
for registro in dados:
    soma_duracao += registro['duracao_minutos']

media_duracao = soma_duracao / len(dados)
print(f"3. DURAÇÃO MÉDIA DOS TREINOS: {media_duracao:.2f} minutos")
print(f"   (soma de todas as durações ÷ quantidade de treinos)\n")

# -------------------------------------------------
# 4. CONTAGEM CONDICIONAL
# -------------------------------------------------

print("="*60)
print("🎯 CONTAGEM CONDICIONAL:")
print("="*60 + "\n")

# Contar quantos alunos atingiram a meta
alunos_meta_atingida = 0
for registro in dados:
    if registro['meta_atingida']:
        alunos_meta_atingida += 1

percentual_meta = (alunos_meta_atingida / len(dados)) * 100

print(f"ALUNOS QUE ATINGIRAM A META:")
print(f"• Quantidade: {alunos_meta_atingida} de {len(dados)} alunos")
print(f"• Percentual: {percentual_meta:.1f}% dos alunos\n")

# -------------------------------------------------
# 5. ACÚMULO POR CATEGORIA
# -------------------------------------------------

print("="*60)
print("🏋️ TOTAL POR CATEGORIA:")
print("="*60 + "\n")

# Calcular total de calorias por modalidade
calorias_por_modalidade = {}

for registro in dados:
    modalidade = registro['modalidade']
    calorias = registro['calorias_queimadas']

    if modalidade in calorias_por_modalidade:
        calorias_por_modalidade[modalidade] += calorias
    else:
        calorias_por_modalidade[modalidade] = calorias

print("CALORIAS QUEIMADAS POR MODALIDADE:")
for modalidade, total_calorias in calorias_por_modalidade.items():
    print(f"• {modalidade}: {total_calorias} kcal")

print()

# -------------------------------------------------
# 6. EXIBIR PERCEPÇÕES/INSIGHTS
# -------------------------------------------------

print("="*60)
print("💡 PERCEPÇÕES OBTIDAS:")
print("="*60 + "\n")

print("Com base na análise dos dados, percebemos que:\n")

# Insight 1: Modalidade que mais queima calorias
modalidade_max = max(calorias_por_modalidade, key=calorias_por_modalidade.get)
calorias_max = calorias_por_modalidade[modalidade_max]
percentual_modalidade = (calorias_max / soma_calorias) * 100

print(f"1️⃣ A modalidade '{modalidade_max}' foi a que mais queimou calorias,")
print(f"   totalizando {calorias_max} kcal, o que representa {percentual_modalidade:.1f}%")
print(f"   do total de calorias queimadas na academia.\n")

# Insight 2: Taxa de sucesso nas metas
print(f"2️⃣ {percentual_meta:.1f}% dos alunos atingiram suas metas de treino,")
print(f"   mostrando um bom nível de comprometimento. Porém,")
print(f"   {100 - percentual_meta:.1f}% ainda precisam de mais motivação ou")
print(f"   ajuste nas metas para alcançar seus objetivos.\n")

# Insight 3: Análise da duração média
if media_duracao >= 60:
    print(f"3️⃣ A duração média dos treinos é de {media_duracao:.2f} minutos,")
    print(f"   indicando que os alunos estão dedicando um tempo adequado")
    print(f"   para seus exercícios, o que é excelente para resultados consistentes.\n")
else:
    print(f"3️⃣ A duração média dos treinos é de {media_duracao:.2f} minutos,")
    print(f"   sugerindo que alguns alunos poderiam se beneficiar de")
    print(f"   sessões um pouco mais longas para maximizar os resultados.\n")

# -------------------------------------------------
# 7. MENSAGEM FINAL
# -------------------------------------------------

print("="*60)
print("✅ ANÁLISE CONCLUÍDA COM SUCESSO!")
print("="*60)
print("\n🎯 Obrigado por usar nosso sistema de análise de dados!")
print("💪 Continue acompanhando o desempenho da academia!\n")
