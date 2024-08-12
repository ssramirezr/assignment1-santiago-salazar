def read_input():
    # Leer el número de casos
    c = int(input().strip())

    cases = []

    for _ in range(c):
        # Leer el número de estados
        n = int(input().strip())

        # Leer el alfabeto
        alphabet = input().strip().split()

        # Leer los estados finales
        final_states = set(map(int, input().strip().split()))

        # Leer la tabla de transiciones
        transitions = []
        for i in range(n):
            transitions.append(list(map(int, input().strip().split())))

        # Guardar los datos del caso
        cases.append((n, alphabet, final_states, transitions))

    return cases

def minimize_dfa(n, alphabet, final_states, transitions):
    # Inicializar la tabla de distinción
    distinguishable = [[False for _ in range(n)] for _ in range(n)]

    # Marcar los estados distinguibles por pertenencia a estados finales
    for i in range(n):
        for j in range(i + 1, n):
            if (i in final_states) != (j in final_states):
                distinguishable[i][j] = True

    # Propagar la distinción a través de las transiciones
    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(i + 1, n):
                if not distinguishable[i][j]:
                    for a in range(len(alphabet)):
                        if distinguishable[transitions[i][a]][transitions[j][a]]:
                            distinguishable[i][j] = True
                            changed = True
                            break

    # Encontrar los pares equivalentes
    equivalent_pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if not distinguishable[i][j]:
                equivalent_pairs.append((i, j))

    return equivalent_pairs

def main():
    # Leer los casos de prueba
    cases = read_input()

    # Procesar cada caso
    for n, alphabet, final_states, transitions in cases:
        equivalent_pairs = minimize_dfa(n, alphabet, final_states, transitions)

        # Ordenar las parejas en orden lexicográfico y formatear la salida
        equivalent_pairs.sort()
        output = ' '.join(f"({i},{j})" for i, j in equivalent_pairs)

        print(output)

if __name__ == "__main__":
    main()
