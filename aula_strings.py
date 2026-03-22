# 1. DEFININDO O TEXTO COM ESPAÇOS E UMA LISTA
nome = "   Cauã Diogo   "
tecnologias = ["Python", "ADS", "VS Code"]

print("--- MÉTODOS DE LIMPEZA E FORMATAÇÃO ---")

# --- lstrip() e rstrip() (Limpeza Direcionada) ---
# Diferente do strip() que limpa os dois lados:
print(f"Original: '{nome}'")
print(f"lstrip (Limpa Esquerda): '{nome.lstrip()}'")
print(f"rstrip (Limpa Direita) : '{nome.rstrip()}'")

# --- center() (Organização Visual) ---
# Centraliza o texto em um espaço de N caracteres. 
# Você pode escolher um caractere de preenchimento!
print("\n--- TESTE DO CENTER ---")
print("Menu".center(20, "#"))
print(nome.strip().center(20, "."))

# --- join() (O "Colador" de Listas) ---
# Ele pega uma lista e junta tudo em uma única String, 
# usando um separador que você escolher.
print("\n--- TESTE DO JOIN ---")
separador_traco = " - ".join(tecnologias)
separador_linha = "\n".join(tecnologias)

print("Junto com traço:", separador_traco)
print("Um por linha:\n", separador_linha)
