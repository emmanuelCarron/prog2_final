class Multiconjunto():

    def __init__(self):
        """
        Inicialización del Multiconjunto Ordenado
        """
        self.__multiconjunto = []
                  

    def ordenar(self):
        self.ordenamientoRapidoAuxiliar(self.__multiconjunto, 0, len(self.__multiconjunto) - 1)
    

    def ordenamientoRapidoAuxiliar(self, unaLista, primero, ultimo):
        if primero < ultimo:
            puntoDivision = self.particion (unaLista, primero, ultimo)
            self.ordenamientoRapidoAuxiliar(unaLista, primero, puntoDivision-1)
            self.ordenamientoRapidoAuxiliar(unaLista, puntoDivision + 1, ultimo)
    

    def particion(self, unaLista, primero, ultimo):
        valorPivote = unaLista[primero][0]
        marcaIzq = primero + 1
        marcaDer = ultimo
        hecho = False
        while not hecho:
            while marcaIzq <= marcaDer and unaLista[marcaIzq][0] <= valorPivote:
                marcaIzq = marcaIzq + 1
            while unaLista[marcaDer][0] >= valorPivote and marcaDer >= marcaIzq:
                marcaDer = marcaDer - 1
            if marcaDer < marcaIzq:
                hecho = True
            else:
                temp = unaLista[marcaIzq]
                unaLista[marcaIzq] = unaLista[marcaDer]
                unaLista[marcaDer] = temp
        temp = unaLista[primero]
        unaLista[primero] = unaLista[marcaDer]
        unaLista[marcaDer] = temp
        return marcaDer


    def agregar(self, elem):
        """
        Función que permite agregar un par (item, cantidad)
        """
        if self.existe(elem):
            indice = self.devolver_indice(elem)
            self.__multiconjunto[indice] = (elem, self.__multiconjunto[indice][1] + 1)
        else:
            self.__multiconjunto.append((elem, 1))
            self.ordenar()

    
    def quitar_uno(self, elem):
        """
        Borra un elemento del multiconjunto.
        """
        if self.existe(elem):
            lugar = self.devolver_indice(elem)
            if self.repeticiones_e(elem) > 1:
                self.__multiconjunto[lugar] = (self.__multiconjunto[lugar][0], self.__multiconjunto[lugar][1] - 1)
            else:
                self.eliminar(elem)


    def eliminar(self, elem):
        """
        Recibe un elemento y elimina todas las existencias de éste
        en el conjunto.
        """ 
        if self.existe(elem):
            del(self.__multiconjunto[self.devolver_indice(elem)])


    def busqueda_binaria(self, elem, l: []):
        pto_medio = len(l) // 2
        if l == []:
            return False
        else:
            if elem == l[pto_medio][0]:
                return True
            elif elem < l[pto_medio][0]:
                return self.busqueda_binaria(elem, l[:pto_medio])
            else:
                return self.busqueda_binaria(elem, l[pto_medio + 1:])
        
        
    def existe(self, elem):
        """
        Verifica que exista el elemento en el multiconjunto
        """
        return self.busqueda_binaria(elem, self.__multiconjunto)


    def repeticiones_e(self, elem):
        """
        Cantidad de veces repetidas que aparece el elemento e en el multiconjunto
        """
        if self.existe(elem):
            lugar = self.devolver_indice(elem)
            return self.__multiconjunto[lugar][1]
        else:
            return 0

        
    def primero(self):
        """
        Devuelve el primer elemento del multiconjunto
        """
        return self.__multiconjunto[0][0]


    def ultimo(self):
        """
        Devuelve el último elemento del multiconjunto
        """
        return self.__multiconjunto[-1][0]
        

    def devolver_indice(self, elem):
        """
        Devuelve el numero de orden del elemento e
        """
        indice = None
        if self.existe(elem):
            #ponemos en una tupla el objeto filter con la tupla buscada
            tupla = tuple(filter(lambda x: x[0] == elem, self.__multiconjunto)) 
            #asigno a indice el indice de la tupla devuelta por filter
            indice = self.__multiconjunto.index(tupla[0])
        return indice

        
    def devolver_elemento(self, i):
        """
        Devolveme el elemento que está en el lugar i
        """
        return self.__multiconjunto[i][0]
        

    def es_vacia(self):
        """
        Devuelve si el multiconjunto es el vacío
        """
        return (self.__multiconjunto == [])


    def tamanio(self):
        """
        Devuelve la cantidad de elementos diferentes del multiconjunto
        """
        return len(self.__multiconjunto)


    def tamanio_rep(self):
        """
        Devuelve la cantidad de elementos del multiconjunto contando repetidos
        """
        accu = 0
        for elem in self.__multiconjunto:
            #elem -> (elemento, cardinalidad) 
            accu += elem[1]
        return accu
    

    def mostrar(self):
        """
        Muestra el multiconjunto (hace el print del multiconjunto) (traduccion a string)
        """
        return f'{self.__multiconjunto}'


m = Multiconjunto() # m = {}
#assert True == m.es_vacia(), "Multiconjunto es vacio"
m.agregar(1) # m = {1}
assert False == m.es_vacia(), "Multiconjunto no es vacio"
assert 1 == m.tamanio(), "Tamanio del multiconjunto es 1"
assert True == m.existe(1), "El elemento 1 existe en el multiconjunto"
assert False == m.existe(-1), "El elemento -1 existe en el multiconjunto"
m.agregar(1) # m = {1,1}
m.agregar(1) # m = {1,1,1}
assert m.tamanio() == 1, "El multiconjunto tiene un elemento"
assert m.tamanio_rep() == 3, "El multiconjunto tiene un elemento"
assert 3 == m.repeticiones_e(1), "Cantidad de repeticiones del elemento 1 es 3"
assert 0 == m.repeticiones_e(20), "Cantidad de repeticiones del elemento 20 es 0"
m.agregar(2) # m = {1,1,1,2}
m.agregar(3) # m = {1,1,1,2,3}
m.agregar(2) # m = {1,1,1,2,2,3}
assert 2 == m.repeticiones_e(2), "Cantidad de repeticiones del elemento 2 es 2"
m.agregar(5) # m = {1,1,1,2,2,3,5}
assert 5 == m.ultimo(), "El ultimo elemento del multiconjunto es 5"
assert 1 == m.primero(), "El primer elemento del multiconjunto es 1"
m.agregar(3) # m = {1,1,1,2,2,3,3,5}
m.quitar_uno(3) # m = {1,1,1,2,2,3,5}
assert True == m.existe(3), "Borramos solo una ocurrenicia de 3"
assert 1 == m.repeticiones_e(3), "Cantidad de repeticiones del elemento 3 es 1"
m.eliminar(3) # m = {1,1,1,2,2,5}
assert False == m.existe(3), "No existe el elemento 3"
m.agregar(1) # m = {1,1,1,1,2,2,5}
m.agregar(15) # m = {1,1,1,1,2,2,5,15}
m.agregar(3) # m = {1,1,1,1,2,2,3,5,15}
m.agregar(20) # m = {1,1,1,1,2,2,3,5,15,20}
m.agregar(18) # m = {1,1,1,1,2,2,3,5,15,18,20}
m.agregar(11) # m = {1,1,1,1,2,2,3,5,11,15,18,20}
m.agregar(0) # m = {0,1,1,1,1,2,2,3,5,11,15,18,20}
m.agregar(10) # m = {0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
assert 10 == m.tamanio(), "El multiconjunto tiene 10 elementos distintos"
assert 14 == m.tamanio_rep(), "El multiconjunto tiene 14 elementos contando repeticiones"
assert 5 == m.devolver_indice(10), "El 10 esta en el indice 5"
assert 11 == m.devolver_elemento(6), "El elemento del indice 6 es el 11"
m.agregar(-1) # m = {-1,0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
m.agregar(-20) # m = {-20,-1,0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
m.agregar(-3) # m = {-20,-3,-1,0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
m.agregar(-3) # m = {-20,-3,-3,-1,0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
assert False == m.existe(22), "No existe el elemento 22"
assert 4 == m.repeticiones_e(1), "Cantidad de repeticiones del 1 es 4"
assert -20 == m.primero(), "El primer elemento del multiconjunto es -20"
assert 20 == m.ultimo(), "El ultimo elemento del multiconjunto es 20"