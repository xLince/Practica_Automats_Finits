AF_created = False
AF = []


# Classe que define los estado
class State:
    def __init__(self, state, transitionWithA, transitionWithB, initial, final):
        self.state = state
        self.transitionWithA = transitionWithA
        self.transitionWithB = transitionWithB
        self.initial = initial
        self.final = final

    def set_initial(self):
        self.initial = True

    def set_final(self):
        self.final = True

    def set_transitionWithA(self, transitions):
        self.transitionWithA = transitions

    def set_transitionWithB(self, transitions):
        self.transitionWithB = transitions

    def toString(self):
        print("Estado " + str(self.state) + ":")
        print(str(self.state) + " --a--> " + str(self.transitionWithA))
        print(str(self.state) + " --b--> " + str(self.transitionWithB))
        if self.initial:
            print("El estado " + str(self.state) + " es inicial.")
        if self.final:
            print("El estado " + str(self.state) + " es final.")
        print("")


# El menu del programa
def menu():
    print("Introduce el numero de la opción a realizar")
    print("1 - Crear un AF")
    print("2 - Determinizar l'AF")
    print("3 - Eliminar l'AF")
    print("4 - Mostrar l'AF")
    print("5 - Salir")
    option_selected = int(input())
    if option_selected == 1:
        create_AF()
        menu()
    elif option_selected == 2:
        if not AF_created:
            print("No existe un AF, crea uno antes")
            menu()
        else:
            determinate_AF()
            menu()
    elif option_selected == 3:
        eliminate_AF()
        menu()
    elif option_selected == 4:
        if not AF_created:
            print("No existe un AF, crea uno antes")
            menu()
        else:
            see_AF()
            menu()
    elif option_selected == 5:
        exit()
    else:
        menu()


# Función que crea el Automata
def create_AF():
    global AF_created, AF
    size_c = input("Quantos estados tendra el automata?\n")
    size = int(size_c)
    for i in range(size):
        print("Estado " + str(i))

        # Transiciones con la letra A
        AF_transitionA = []
        for j in range(size):
            sol = input("Introduce el estado al que se va con la letra a, apreta s para acabar\n")
            if sol == "s":
                break
            while sol < "0" or sol >= size_c:
                if sol == "s":
                    break
                sol = input("El estado " + sol + " no existe, introduce uno correcto\n")
            if sol == "s":
                break
            AF_transitionA.append(int(sol))

        # Transiciones con la letra B
        AF_transitionB = []
        for j in range(size):
            sol = input("Introduce el estado al que se va con la letra b, apreta s para acabar\n")
            if sol == "s":
                break
            while sol < "0" or sol >= size_c:
                if sol == "s":
                    break
                sol = input("El estado " + sol + " no existe, introduce uno correcto\n")
            if sol == "s":
                break
            AF_transitionB.append(int(sol))
        if i == 0:
            AF.append(State([i], AF_transitionA, AF_transitionB, True, False))
        elif i == size - 1:
            AF.append(State([i], AF_transitionA, AF_transitionB, False, True))
        else:
            AF.append(State([i], AF_transitionA, AF_transitionB, False, False))
    print("El estado inicial es el 0")
    state_f = str(size - 1)
    print("El estado final es el " + state_f)
    AF_created = True


# Función que determiniza el Automata
def determinate_AF():
    global AF
    AF_d = [State([0], [], [], True, False)]
    cont = 0
    for i in AF_d:
        tA = getAllTransitionsWithA(i)
        tB = getAllTransitionsWithB(i)
        if existState(AF_d, tA) and tA != []:
            AF_d.append(State(tA, [], [], False, isFinal(tA)))
        elif existState(AF_d, tA) and tA == []:
            tA = i.state
        if existState(AF_d, tB) and tB != []:
            AF_d.append(State(tB, [], [], False, isFinal(tB)))
        elif existState(AF_d, tB) and tB == []:
            tB = i.state

        AF_d[cont].set_transitionWithA(tA)
        AF_d[cont].set_transitionWithB(tB)
        cont += 1

    AF = AF_d
    see_AF()


# Elimina el Automata
def eliminate_AF():
    global AF, AF_created
    AF = []
    AF_created = False


def see_AF():
    for i in range(len(AF)):
        state = AF[i]
        state.toString()


# Coge todas las transiciones con A del estado introducido
def getAllTransitionsWithA(s):
    res = []
    for i in range(len(s.state)):
        index = s.state[i]
        for j in range(len(AF[index].transitionWithA)):
            res.append(AF[index].transitionWithA[j])
    res.sort()
    return deleteRepeatedTransitions(res)


# Coge todas las transiciones con B del estado introducido
def getAllTransitionsWithB(s):
    res = []
    for i in range(len(s.state)):
        index = s.state[i]
        for j in range(len(AF[index].transitionWithB)):
            res.append(AF[index].transitionWithB[j])
    res.sort()
    return deleteRepeatedTransitions(res)


# Elimina las transiciones repetidas
def deleteRepeatedTransitions(table):
    new_table = []
    for i in table:
        if i not in new_table:
            new_table.append(i)
    return new_table


# Mira si el estado existe
def existState(A_d, transitions):
    for i in range(len(A_d)):
        aux_s = A_d[i]
        if aux_s.state == transitions:
            return False
    return True


# Devuelve si el estado es final
def isFinal(transitions):
    for i in range(len(transitions)):
        if transitions[i] == (len(AF)-1):
            return True
    return False


# Codigo fuente
menu()
