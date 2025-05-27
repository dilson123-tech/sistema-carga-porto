import json
import os
import random
from datetime import datetime
import matplotlib.pyplot as plt

ARQUIVO_JSON = "data/cargas.json"

def carregar_dados():
    print(f"[DEBUG] Caminho do arquivo JSON: {ARQUIVO_JSON}")
    if not os.path.exists(ARQUIVO_JSON):
        print("[DEBUG] Arquivo não encontrado, retornando lista vazia.")
        return []
    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        try:
            dados = json.load(f)
            print(f"[DEBUG] {len(dados)} cargas carregadas com sucesso.")
            return dados
        except json.JSONDecodeError:
            print("[DEBUG] Erro ao decodificar JSON. Retornando lista vazia.")
            return []

def salvar_dados(cargas):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(cargas, f, indent=4, ensure_ascii=False)

def mostrar_estatisticas(cargas):
    if not cargas:
        print("Nenhuma carga cadastrada.")
        return
    total_cargas = len(cargas)
    peso_total = sum(c['peso'] for c in cargas)
    destinos = {}
    for c in cargas:
        destinos[c['destino']] = destinos.get(c['destino'], 0) + 1
    destino_mais_frequente = max(destinos, key=destinos.get)
    print("\n--- Estatísticas ---")
    print(f"Total de cargas: {total_cargas}")
    print(f"Peso total: {peso_total:.2f} kg")
    print(f"Destino mais frequente: {destino_mais_frequente}")

def gerar_grafico(cargas):
    if not cargas:
        print("Nenhuma carga cadastrada para gerar gráfico.")
        return
    destinos = {}
    for c in cargas:
        destinos[c['destino']] = destinos.get(c['destino'], 0) + 1

    plt.bar(destinos.keys(), destinos.values())
    plt.title("Cargas por Destino")
    plt.xlabel("Destino")
    plt.ylabel("Quantidade de Cargas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def cadastrar_carga(cargas):
    print("\n--- Cadastro de Nova Carga ---")
    codigo = input("Código da carga (único): ").strip()
    if any(c['codigo'] == codigo for c in cargas):
        print("Erro: Código já existe. Cadastro cancelado.")
        return
    destinos_validos = ["São Paulo", "Rio de Janeiro", "Fortaleza", "Porto Alegre", "Salvador", "Manaus"]
    destino = input(f"Destino ({', '.join(destinos_validos)}): ").strip()
    if destino not in destinos_validos:
        print("Destino inválido. Cadastro cancelado.")
        return
    try:
        peso = float(input("Peso (kg): ").replace(",", "."))
        if peso <= 0:
            print("Peso deve ser maior que zero. Cadastro cancelado.")
            return
    except ValueError:
        print("Peso inválido. Cadastro cancelado.")
        return

    data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nova_carga = {
        "codigo": codigo,
        "destino": destino,
        "peso": peso,
        "data_cadastro": data_cadastro
    }
    cargas.append(nova_carga)
    salvar_dados(cargas)
    print("Carga cadastrada com sucesso!")

def gerar_cargas_mock(qtd):
    destinos = ["São Paulo", "Rio de Janeiro", "Fortaleza", "Porto Alegre", "Salvador", "Manaus"]
    cargas = []
    for _ in range(qtd):
        codigo = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6))
        destino = random.choice(destinos)
        peso = round(random.uniform(100, 2000), 2)
        data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cargas.append({
            "codigo": codigo,
            "destino": destino,
            "peso": peso,
            "data_cadastro": data_cadastro
        })
    salvar_dados(cargas)
    print(f"{qtd} cargas mock geradas e salvas com sucesso!")
