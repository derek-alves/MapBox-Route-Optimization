class No{
    constructor(pai =null, valor1=null, valor2=null,anterior=null,proximo=null){
        this.pai = pai;
        this.valor1 = valor1;
        this.valor2 = valor2;
        this.anterior = anterior;
        this.proximo = proximo;
    }
}

class lista{
    constructor(head = null, tail = null){
        this.head = head
        this.tail = tail
    }

    inserePrimeiro(v1,v2,p){
        var novo_no = new No(p,v1,v2,null,null);
        if (this.head == null){
            this.tail = novo_no;
        }else{
            novo_no.proximo = this.head
            this.head.anterior = novo_no
        }
        this.head = novo_no
    }

    insereUltimo(v1,v2,p){
        var novo_no = new No(p,v1,v2,null,null)
        if(this.head == null){
            this.head = novo_no
        }else{
            this.tail.proximo = novo_no
            novo_no.anterior = this.tail
        }
        this.tail = novo_no
    }
    deletaPrimeiro()
    {
        if (this.head == null){
            return null
        }else{
            var no = this.head
            this.head = this.head.proximo
            if (this.head != null){
                this.head.anterior = null
            }else{
                this.tail = null
            }
            return no
        }
    }

    deletaUltimo(){
        if(this.tail == null){
            return null
        }else{
            no = this.tail
            this.tail = this.tail.anterior
            if(this.tail != null){
                this.tail.proximo = null
            }else{
                this.head = null
            }
            return no
        }
    }

    vazio(){
        if(this.head == null){
            return true
        }else{
            return false
        }
    }

    exibeLista(){
        aux = this.head
        str = []
        while(aux != null){
            str.push(aux.valor1)
            aux = aux.proximo
        }
        return str
    }

    exibeArvore(){
        var atual = this.tail
        var caminho = []
        while(atual.pai != null){
            caminho.push(atual.valor1)
            atual = atual.pai
        }
        caminho.push(atual.valor1)
        return caminho
    }

    exibeArvore1(valor){
        var atual = this.head
        while(atual.valor1 != valor){
            atual = atual.proximo
        }
        var caminho = []
        atual = atual.pai
        while(atual.pai != null){
            caminho.push(atual.valor1)
            atual = atual.pai
        }
        caminho.push(atual.valor1)
        return caminho
    }

    primeiro(){
        return this.head
    }

    ultimo(){
        return this.tail
    }

}


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


class busca{

     amplitude(inicio, fim){
         var l1 = new lista()
         var l2 = new lista()
         var visitado = []
         l1.insereUltimo(inicio,0,null)
         l2.insereUltimo(inicio,0,null)
         var linha = []
         linha.push(inicio)
         linha.push(0)
         visitado.push(linha)

         var flag1 = false
         while(l1.vazio() != null && flag1 == false){
                var atual = l1.deletaPrimeiro()
                var ind = atual.valor1
                for(var i in grafo[ind]){
                    var novo = grafo[ind][i]
                    var flag = true
                    for(var j in visitado){
                        if(visitado[j][0]==novo){
                            flag=false
                            break;
                        }
                    }

                    if(flag){
                        l1.insereUltimo(novo,atual.valor2 + 1, atual)
                        l2.insereUltimo(novo, atual.valor2 + 1,atual)
                        linha = []
                        linha.push(novo)
                        linha.push(atual.valor2+1)
                        visitado.push(linha)
                        if(novo == fim){
                            flag1 = true
                            break
                        }
                    }
                }
         }

         var caminho = []
         if(flag1){
             caminho = l2.exibeArvore()
         }else{
             caminho = "Caminho não encontrado"
         }
         caminho = caminho.reverse()
         return caminho
     }
 }
//const sol = new busca()

//const caminho = sol.amplitude(0,6)
//console.log(caminho)