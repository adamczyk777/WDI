"""
Indeksowanie elementóœ zaczyna się tak jakby od numeru 1, używane przyd odawaniu na ntej pozycji
"""


class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class BidirectionalList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addBeg(self, name, score):
        """
        Dodaje element na początku listy
        :param name: imie i nazwisko ucznia
        :param score: wynik z kolokwium
        :return: None, nie zwraca nic
        """
        node = Node(name, score)
        if self.tail is None:
            self.tail = node
        if self.head is None:
            self.head = node
        else:
            tmp = self.head
            self.head = node
            node.next = tmp
            tmp.prev = node
        self.size += 1

    def removeBeg(self):
        """
        Usuwa początkowy element listy
        """
        if self.size > 1:
            self.head = self.head.next
            self.size -= 1
            return True
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return True
        else:
            return False

    def addLast(self, name, score):
        """
        Dodaje element na koniec listy
        :param name: Imie i nazwisko studenta/ucznia
        :param score: wynik z kolokwium
        """
        node = Node(name, score)
        if self.tail is None:
            self.tail = node
        if self.head is None:
            self.head = node
        else:
            tmp = self.tail
            self.tail = node
            node.prev = tmp
            tmp.next = node
        self.size += 1

    def removeLast(self):
        """
        Usuwa ostatni element z listy
        """
        if self.size > 1:
            self.tail = self.tail.prev
            self.size -= 1
            return True
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return True
        else:
            return False

    def addN(self, name, score, n):
        """
        Dodaje element na N-tą pozycję na liście
        :param name: Imie i nazwisko studenta/ucznia
        :param score: wynik z kolokwium
        :param n: pozycja na liscie
        """
        if 0 < n <= (self.size + 1):
            if n == (self.size + 1):
                self.addLast(name, score)
            elif n == 1:
                self.addBeg(name, score)
            elif n > (self.size+1)/2:
                node = Node(name, score)
                tmp = self.tail
                for x in range(self.size-n-1):
                    tmp = tmp.prev
                node.prev = tmp.prev
                node.next = tmp
                tmp.prev.next = node
                tmp.prev = node
                self.size += 1
            else:
                node = Node(name, score)
                tmp = self.head
                for x in range(n-1):
                    tmp = tmp.next
                node.prev = tmp.prev
                node.next = tmp
                tmp.prev.next = node
                tmp.prev = node
                self.size += 1

    def findBest(self):
        """
        ZNajduje najlepszego studenta/ucznia, oraz drukuje jego name
        """
        if self.size > 0:
            best = self.head
            iterator = self.head
            for x in range(self.size):
                if int(iterator.score) > int(best.score):
                    best = iterator
                iterator = iterator.next
            print("Najwyższy wynik uzyskał:", best.name)

    def printListBeg(self):
        """
        Drukuje liste od początku
        """
        n = self.head
        for x in range(self.size):
            print(n.name, ":", n.score)
            n = n.next
    def printListEnd(self):
        """
        Drukuje liste od końca
        """
        n = self.tail
        for x in range(self.size):
            print(n.name, ":", n.score)
            n = n.prev

'''
TEST
tutaj są nasze testy, dodaję na początek kilka elementów
potem dodaję ajko ostatnie
następnie dodaję na Ntą pozycję, używając złego indeksu, pierwszy element, oraz ostatni element, oraz w środku
na koniec usuwam pierwszy i ostatni

drukuję od początku, oraz od końca

drukuję najlepszego studenta
'''
kolos = BidirectionalList()
kolos.addLast("Jan Kowalski", 15)
kolos.addLast("Tomasz Nowak", 11)
kolos.addLast("Bogdan Bednarski", 22)
kolos.addBeg("Krzysztof Kluza", 28)
kolos.addBeg("Januz Miller", 29)
kolos.addN("Maciej Kot", 27, 22)
kolos.addN("Krystian Karczyński", 60, 6)
kolos.addN("Jakub Kozioł", 23, 1)
kolos.addN("Patryk Papiór", 19, 3)
kolos.removeLast() #usuwa Karczynskiego
kolos.removeBeg() #usuwa Kozioła

kolos.printListBeg()
print("-----------------------------------------------------")
kolos.printListEnd()
print("-----------------------------------------------------")
kolos.findBest()
