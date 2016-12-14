#indeksowanie elementów zacząłem od numeru 1, ze względu na wartości size
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
        dodaje element na początkulisty
        :param data: dane przekazywane przy dodawaniu elementu (wartosc elementu)
        """
        node = Node(name, score)
        if self.tail is None:
            self.tail = node #jesli brakuje nam wskaznika na ostatni el, ustaiwamy go na ten który dodajemy
        if self.head is None:
            self.head = node #analogicznie, ale dla pierwszego
        else:
            tmp = self.head #zachowujemy co jest wskazywane przez głowę listy
            self.head = node # wczucamy w głowę nowy el
            node.next = tmp #dodajemy wskaznik na to co bylo wczesniej jako pierwszy element w anszym nowym
        self.size += 1

    def removeBeg(self):
        """
        usuwa pierwszy element z listy
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
        node = Node(name, score)
        if self.tail is None:
            self.tail = node #jesli brakuje nam wskaznika na ostatni el, ustaiwamy go na ten który dodajemy
        if self.head is None:
            self.head = node #analogicznie, ale dla pierwszego
        else:
            tmp = self.tail
            self.tail = node
            node.prev = tmp
        self.size += 1

    def removeLast(self):
        """
        usuwa ostatni element z listy
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
        funkcja dodaje element na ntą pozycję
        :param data: dane jakie chcemy dodać
        :param n: enty element
        :return:
        """
        if 0 < n <= self.size + 1:
            if n == self.size + 1:
                self.addLast(name, score)
            elif n == 1:
                self.addBeg(name, score)
            elif n > (self.size+1)/2:
                node = Node(name, score)
                tmp = self.tail
                for x in range(self.size - n):
                    tmp = tmp.prev
                node.prev = tmp.prev
                node.next = tmp
            else:
                node = Node(name, score)
                tmp = self.head
                for x in range(n-1):
                    tmp = tmp.next
                node.prev = tmp.prev
                node.next = tmp
            self.size += 1

    def findBest(self):
        if self.size > 0:
            best = self.head
            iterator = self.head
            for x in range(self.size):
                if iterator.score > best.score:
                    best = iterator
                iterator = iterator.next
            print("Najwyższy wynik uzyskał:", iterator.name)

    def printListBeg(self):
        n = self.head
        for x in range(self.size-1):
            print(n.name, ":", n.score)
            n = n.next
    def printListEnd(self):
        n = self.tail
        for x in range(self.size-1):
            print(n.name, ":", n.score)
            n = n.prev


kolos = BidirectionalList()
kolos.addBeg("Jan Kowalski", 15)
kolos.addBeg("Tomasz Nowak", 11)
kolos.addBeg("Bogdan Bednarski", 22)
kolos.addLast("Krzysztof Kluza", 28)
kolos.addLast("Januz Miller", 29)
# kolos.addN("Maciej Kot", 27, 22)
# kolos.addN("Krystian Karczyński", 3, 6)
# kolos.addN("Jakub Porzycki", 23, 1)
# kolos.addN("Patryk Papiór", 9, 3)

kolos.printListBeg()
# kolos.printListEnd()
