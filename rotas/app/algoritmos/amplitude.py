class No(object):
    def __init__(self, pai=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai       = pai
        self.valor1    = valor1
        self.valor2    = valor2
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, v1, v2, p):
        novo_no = No(p, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, v1, v2, p):

        novo_no = No(p, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no

    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            str.append(aux.valor1)
            aux = aux.proximo
        
        return str
    
    def exibeArvore(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        return caminho
    
    def exibeArvore1(self,valor):
                
        atual = self.head
        while atual.valor1 != valor:
            atual = atual.proximo
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        return caminho

    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail




grafo = [
            [12, 16], 
            [3,6],
            [10,13],
            [1,5,8,11],
            [13,19],
            [3,6,10,15],
            [1,5,8,10],
            [14,16],
            [3,6,12],
            [10,13],
            [2,5,6,9,15],
            [3,15,16],
            [0,8],
            [2,4,9],
            [7,15,17],
            [5,10,11,14],
            [0,7,11],
            [14,18],
            [17],
            [4]
                
         ]




class busca:
    
    def amplitude(self, inicio, fim):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        flag1 = False
        while l1.vazio() is not None and flag1==False:
            atual = l1.deletaPrimeiro()
            ind = atual.valor1
            for i in range(len(grafo[ind])):
            
                novo = grafo[ind][i]
                flag = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:          
                            flag = False
                            break
                
                if flag:
                    l1.insereUltimo(novo, atual.valor2 + 1 , atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2+1)
                    visitado.append(linha)
                    if novo == fim:
                        #6 = 6
                        flag1 = True
                        break

        caminho = []
        if flag1:
            caminho = l2.exibeArvore()
        else:
            caminho = "Caminho não encontrado"
        caminho = caminho[::-1]
        return caminho

# sol = busca()



# caminho = sol.amplitude(0,6)
# print("Amplitude.......: ",caminho[::-1])