#!/usr/bin/env python
# coding: utf-8

# In[241]:


import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


# In[242]:


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


# In[243]:


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


# In[244]:


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


# In[245]:


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


# In[246]:


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


# In[247]:


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras 
    diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


# In[248]:


def junta_lista_dupla(ListaP):
    ListaP_juntada=[]
    for i in range(0,len(ListaP)):
        for j in range(0,len(ListaP[i])):
            ListaP_juntada.append(ListaP[i][j])
    return ListaP_juntada


# In[249]:


#IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.
def calcula_assinatura(texto):
    #print(texto)

    Lista_de_sentencas = separa_sentencas(texto)
    Quant_palavras = 0
    Quant_letras = 0
    lista_para_quant_pal = []
    Quant_letras_senten = 0
    lista_para_quant_frases = []
    Quant_frases = 0
    Quant_letras_frase = 0
    
    #print(Lista_de_sentencas)

    for j in Lista_de_sentencas:
        #print(j)
        Lista_de_frases = separa_frases(j)
        #print(Lista_de_frases)
        Quant_letras_senten += len(j)
        lista_para_quant_frases.append(Lista_de_frases)

        for k in Lista_de_frases:
            #print(k)
            Lista_de_palavras = separa_palavras(k)
            #print(Lista_de_palavras)
            lista_para_quant_pal.append(Lista_de_palavras)
            Quant_palavras += (len(Lista_de_palavras))
            Quant_letras_frase += len(k)
            for ii in Lista_de_palavras:
                Quant_letras += len(ii)
        #print(lista_para_quant_pal)
        
    #função criada para juntar listas secundárias        
    Quant_palavras_diferentes = n_palavras_diferentes(junta_lista_dupla(lista_para_quant_pal))
    Quant_palavras_unicas = n_palavras_unicas(junta_lista_dupla(lista_para_quant_pal))
    Quant_frases = len(junta_lista_dupla(lista_para_quant_frases))


    #print(len(junta_lista_dupla(lista_para_pal_un)))
    #print(Quant_palavras, Quant_letras, Quant_letras / Quant_palavras)
    #print(Quant_palavras_diferentes)
    #print(Quant_palavras_unicas)

    
    wal = Quant_letras / Quant_palavras
    ttr = Quant_palavras_diferentes / Quant_palavras
    hlr = Quant_palavras_unicas / Quant_palavras
    sal = Quant_letras_senten / len(Lista_de_sentencas)
    sac = Quant_frases / len(Lista_de_sentencas)
    pal = Quant_letras_frase / Quant_frases
    
    assinatura = [wal, ttr, hlr, sal, sac, pal]
    
    #print("wal: ", Quant_letras / Quant_palavras)
    #print("ttr: ", Quant_palavras_diferentes / Quant_palavras)
    #print("hlr: ", Quant_palavras_unicas / Quant_palavras)
    #print("sal: ", Quant_letras_senten / len(Lista_de_sentencas))
    #print("sac: ", Quant_frases / len(Lista_de_sentencas))
    #print("pal: ", Quant_letras_frase / Quant_frases)
    
    return assinatura


# In[250]:


texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."
calcula_assinatura(texto)


# In[251]:


#Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.
def compara_assinatura(as_a, as_b):
    Sab = 0
    for i in range(0, len(as_a)):
        Sab += abs(as_a[i] - as_b[i])
    return Sab / 6


# In[257]:


#IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e
#deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.
def avalia_textos(textos, ass_cp):
    #posicao_do_infectado = 0
    nota_do_infectado = 9999
    for i in range(len(textos)):
        Assinatura_texto = calcula_assinatura(textos[i])
        #print(Assinatura_texto)
        Nota_de_avaliação = compara_assinatura(Assinatura_texto, ass_cp)
        #print(Nota_de_avaliação)
        if Nota_de_avaliação < nota_do_infectado:
            nota_do_infectado = Nota_de_avaliação
            posição_do_infectado = i + 1
    return posição_do_infectado


# In[258]:


#Ler a referência de assinatura
ass_ref = le_assinatura()

#Ler os textos a serem avaliados
Lista_de_textos = le_textos()

#Chamar a subrotina
n = avalia_textos(Lista_de_textos, ass_ref)

#Dar uma resposta
print("O autor do texto", n, "está infectado com COH-PIAH")


# In[ ]:




