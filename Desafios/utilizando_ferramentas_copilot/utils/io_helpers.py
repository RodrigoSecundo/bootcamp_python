def read_int(prompt: str = "") -> int:
    """
    Lê um inteiro do usuário, repetindo até receber uma entrada válida.
    """
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def read_float(prompt: str = "") -> float:
    """
    Lê um número decimal do usuário, repetindo até receber uma entrada válida.
    Aceita vírgula ou ponto.
    """
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print("Entrada inválida. Digite um número (ex.: 7.5).")
