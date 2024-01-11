def simpleArraySum(matrix):
    return print(f"La suma de la matriz es: {sum(int(elem) for elem in matrix)}")


def get_matrix_size():
    while True:
        size = int(input("Introduzca cual va a ser el tamaño de la matriz: "))
        try:
            if size > 0:
                return size
            else:
                print("El tamaño de la matriz debe ser mayor que cero.")
        except ValueError:
            print("Por favor, ingresa un número válido para el tamaño.")

def matrix():
    size = get_matrix_size()
    while True:
        matrix_input = input("Introduzca los elementos de la matriz separados únicamente por espacios: ").rstrip().split()
        while len(matrix_input) != size:
            print("La dimensión de tu matriz no es correcta")
            matrix_input = input("Introduzca los elementos de la matriz separados únicamente por espacios: ").rstrip().split()
        try:
            matrix = [int(elem) for elem in matrix_input]
            return matrix
        except ValueError:
            print("Por favor, ingresa números enteros válidos.")

    
if __name__ == '__main__':
    simpleArraySum(matrix())