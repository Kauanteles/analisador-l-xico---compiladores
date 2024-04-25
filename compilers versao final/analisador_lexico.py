# O FORMATO DE ENTRADA DO ARQUIVO TESTE.CIC 
# DEVEM CONTER UM NÃO DIGITO AO FIM
# DA CADEIA QUE DESEJA LER, A FIM DE RESPEITAR
# AS TRANSIÇÕES DO AUTOMATO, POR EXEMPLO UM ESPAÇO " "

# Parte da leitura do arquivo de entrada e separação de cada elemento da string
with open('exemplo3.cic', 'r') as file:
    string_completa = file.read()
    caracteres = list(string_completa)



def somatorio_tokens(tipo_token):
    # Dicionário para contar a ocorrência de cada token
    contador = {}
    
    # Contagem das ocorrências de cada token
    for token in tipo_token:
        contador[token] = contador.get(token, 0) + 1
    
    # Construção da string formatada
    linha_formatada = "+-----------------------+--------------------+\n"
    linha_formatada += "|  TOKEN                |   USOS             |\n"
    linha_formatada += "+-----------------------+--------------------+\n"
    
    for token, ocorrencias in contador.items():
        linha_formatada += "|  {:<20} |   {:>15}  |\n".format(token, ocorrencias)
    
    linha_formatada += "+-----------------------+--------------------+"
    
    return linha_formatada  



def lista_tokens(LIN, COL, TOKEN, LEXEMA):
    # Verificando se todas as listas têm o mesmo comprimento
    if len(LIN) != len(COL) or len(LIN) != len(TOKEN) or len(LIN) != len(LEXEMA):
        raise ValueError("As listas LIN, COL, TOKEN e LEXEMA devem ter o mesmo comprimento.")
    
    # Construção da string formatada
    linha_formatada = "+-----+-----+---------------------+---------------------+\n"
    linha_formatada += "| LIN | COL |        TOKEN        |       LEXEMA        |\n"
    linha_formatada += "+-----+-----+---------------------+---------------------+\n"
    
    for lin, col, token, lexema in zip(LIN, COL, TOKEN, LEXEMA):
        linha_formatada += "| {:^3} | {:^3} | {:<19} | {:<19} |\n".format(lin, col, token, lexema)
    
    linha_formatada += "+-----+-----+---------------------+---------------------+"
    
    return linha_formatada



def lista_erros(tokens_lidos_erro, linhas_token_erro, colunas_token_erro, tipo_token_erro):
    linhas_texto = string_completa.split('\n')
    
    for token_erro, linha_erro, coluna_erro, tipo_erro in zip(tokens_lidos_erro, linhas_token_erro, colunas_token_erro, tipo_token_erro):
        for i, linha in enumerate(linhas_texto):
            if token_erro in linha:
                mensagem_erro = f"{'-' * (coluna_erro - 1)}^\nerro na linha {linha_erro} coluna {coluna_erro}: {tipo_erro}\n"
                linhas_texto.insert(i+1, mensagem_erro)
    
    texto_corrigido = '\n'.join(linhas_texto)
    return texto_corrigido

    
    
# Função analisadora 
def analise_lexica(caracteres):
    tokens_lidos = []
    tokens_lidos_erro = []
    linhas_token = []
    linhas_token_erro = []
    colunas_token = []
    colunas_token_erro = []
    token_atual = ""
    palavras_reservadas = ["rotina", "fim_rotina", "se", "senao", "imprima", "leia", "para", "enquanto"]
    tipo_token = []
    tipo_token_erro = []
    estado = 0
    i = 0  # Índice de iteração
    linha = 1
    coluna = 1
    
    while i < len(caracteres):
        caractere = caracteres[i]
        
        if caractere == '\n':
            linha += 1
        
        # Parte dos inteiros
        if estado == 0:
            if caractere.isdigit():
                estado = 1
                token_atual += caractere
                coluna += 1
                
            elif caractere == '.':
                estado = 5
                token_atual += caractere
                coluna += 1
                
            elif caractere.isupper() and 'A' <= caractere <= 'F':
                estado = 22
                token_atual += caractere
                coluna += 1
                
            elif caractere == '(':
                tipo_token.append("Parentesis_open")
                estado = 0
                tokens_lidos.append(caractere)
                colunas_token.append(coluna)
                linhas_token.append(linha)
                coluna += 1
                if caracteres[i+1] == '\n':
                    coluna = 1
                
            elif caractere == ')':
                tipo_token.append("Parentesis_close")
                estado = 0
                tokens_lidos.append(caractere)
                colunas_token.append(coluna)
                linhas_token.append(linha)
                coluna += 1
                if caracteres[i+1] == '\n':
                    coluna = 1
                
            elif caractere == ':':
                tipo_token.append("Dois_pontos")
                estado = 0
                tokens_lidos.append(caractere)  
                colunas_token.append(coluna)
                linhas_token.append(linha)
                if caracteres[i+1] == '\n':
                    coluna = 1
                   
            elif caractere == '<':
                estado = 25
                token_atual += caractere
                coluna += 1
                
            elif caractere == '=':
                estado = 27
                token_atual += caractere
                coluna += 1
                
            elif caractere == '>':
                estado = 28
                token_atual += caractere
                coluna += 1
                
            elif caractere == '-':
                tipo_token.append("menos")
                estado = 0
                tokens_lidos.append(caractere)
                colunas_token.append(coluna)
                linhas_token.append(linha)
                coluna += 1
                if caracteres[i+1] == '\n':
                    coluna = 1
                
            elif caractere == '~':
                tipo_token.append("til")
                estado = 0
                tokens_lidos.append(caractere)
                colunas_token.append(coluna)
                linhas_token.append(linha)
                coluna += 1
                if caracteres[i+1] == '\n':
                    coluna = 1
                
            elif caractere == '+':
                tipo_token.append("mais")
                estado = 0
                tokens_lidos.append(caractere)
                colunas_token.append(coluna)
                linhas_token.append(linha)
                coluna += 1
                if caracteres[i+1] == '\n':
                    coluna = 1
                
            elif caractere == '*':
                tipo_token.append("asterisco")
                estado = 0
                tokens_lidos.append(caractere)
                colunas_token.append(coluna)
                linhas_token.append(linha)
                coluna += 1
                if caracteres[i+1] == '\n':
                    coluna = 1
                
            elif caractere == '%':
                tipo_token.append("porcento")
                estado = 0
                tokens_lidos.append(caractere)
                colunas_token.append(coluna)
                linhas_token.append(linha)
                coluna += 1
                if caracteres[i+1] == '\n':
                    coluna = 1
                
            elif caractere == '&':
                tipo_token.append("E_comercial")
                estado = 0
                tokens_lidos.append(caractere)
                colunas_token.append(coluna)
                linhas_token.append(linha)
                coluna += 1
                if caracteres[i+1] == '\n':
                    coluna = 1
                
            elif caractere == '|':
                tipo_token.append("barra_reta")
                estado = 0
                tokens_lidos.append(caractere)
                colunas_token.append(coluna)
                linhas_token.append(linha)
                coluna += 1
                if caracteres[i+1] == '\n':
                    coluna = 1
                
                
            elif caractere == '#':
                estado = 33
                token_atual += caractere
                coluna += 1
                
            elif caractere.islower():
                estado = 34
                token_atual += caractere
                coluna += 1
                
            elif caractere == '"':
                estado = 38
                token_atual += caractere
                coluna += 1
                
            elif caractere == ' ':
                coluna += 1
                
            elif caractere != '\n':
                estado = 0
                coluna += 1
                colunas_token_erro.append(coluna-1)
                linhas_token_erro.append(linha)
                
                tokens_lidos_erro.append(caractere)
                tipo_token_erro.append("token invalido")
                token_atual = ""
                
            
        elif estado == 1:
            if caractere.isdigit():
                estado = 2
                token_atual += caractere
                coluna += 1
                
            elif caractere == '.':
                estado = 6
                token_atual += caractere
                coluna += 1
                
            elif caractere == 'x':
                estado = 23
                token_atual += caractere
                coluna += 1
                
            else:
                tipo_token.append("Inteiro")
                i -= 1
                estado = 0
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            
            
            
        elif estado == 2:
            if caractere.isdigit():
                estado = 3
                token_atual += caractere
                coluna += 1
                
            elif caractere == '.':
                estado = 6
                token_atual += caractere
                coluna += 1
                
            elif caractere == '/':
                estado = 12
                token_atual += caractere
                coluna += 1
                
            elif caractere == '_':
                estado = 19
                token_atual += caractere
                coluna += 1
                
            else:
                tipo_token.append("Inteiro")
                i -= 1
                estado = 0
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            
            
            
        elif estado == 3:
            if caractere.isdigit():
                estado = 4
                token_atual += caractere
                coluna += 1
                
            elif caractere == '.':
                estado = 6
                token_atual += caractere
                coluna += 1
                
            else:
                tipo_token.append("Inteiro")
                i -= 1
                estado = 0
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            
            
            
        elif estado == 4:
            if caractere.isdigit():
                estado = 4
                token_atual += caractere
                coluna += 1
                
            else:
                tipo_token.append("Inteiro")
                i -= 1
                estado = 0
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            
            
            
        # Parte dos floats
        elif estado == 5:
            if caractere.isdigit():
                estado = 7
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("float invalido")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            
        elif estado == 6:
            if caractere.isdigit():
                estado = 7
                token_atual += caractere
                coluna += 1
            elif caractere == 'e':
                estado = 8
                token_atual += caractere
                coluna += 1
            else:
                tipo_token.append("Float")
                i -= 1
                estado = 0
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            
        elif estado == 7:
            if caractere.isdigit():
                estado = 7
                token_atual += caractere
                coluna += 1
            elif caractere == 'e':
                estado = 8
                token_atual += caractere
                coluna += 1
            else:
                tipo_token.append("Float")
                i -= 1
                estado = 0
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            
        elif estado == 8:
            if caractere.isdigit():
                estado = 10
                token_atual += caractere
                coluna += 1
            elif caractere == '-':
                estado = 9
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("float invalido")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            
        elif estado == 9:
            if caractere.isdigit():
                estado = 11
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("float invalido")  
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
              
        elif estado == 10:
            if caractere.isdigit():
                estado = 10
                token_atual += caractere
                coluna += 1
            else:
                tipo_token.append("Float")
                i -= 1
                estado = 0
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            
        elif estado == 11:
            if caractere.isdigit():
                estado = 11
                token_atual += caractere
                coluna += 1
            else:
                tipo_token.append("Float")
                i -= 1
                estado = 0
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
        
        # Parte das datas
        elif estado == 12:
            if caractere.isdigit():
                estado = 13
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("data invalida")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
        
        elif estado == 13:
            if caractere.isdigit():
                estado = 14
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("data invalida")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            
        elif estado == 14:
            if caractere == '/':
                estado = 15
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("data invalida")
                i -= 1
                estado = 0 
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha) 
                tokens_lidos_erro.append(token_atual) 
                token_atual = ""
        
        elif estado == 15:
            if caractere.isdigit():
                estado = 16
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("data invalida")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
        
        elif estado == 16:
            if caractere.isdigit():
                estado = 17
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("data invalida")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            
        elif estado == 17:
            if caractere.isdigit():
                estado = 18
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("data invalida")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            
        elif estado == 18:
            if caractere.isdigit():
                tipo_token.append("Data")
                estado = 0
                token_atual += caractere
                colunas_token.append(coluna - len(token_atual))
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            else:
                tipo_token_erro.append("data invalida")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            
        elif estado == 19:
            if caractere.isdigit():
                estado = 20
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("data invalida")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            
        elif estado == 20:
            if caractere.isdigit():
                estado = 21
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("data invalida")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            
        elif estado == 21:
            if caractere == '_':
                estado = 15
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("data invalida")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
        
        # Endereços
        elif estado == 22:
            if caractere == 'x':
                estado = 23
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("endereço invalido")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            
        elif estado == 23:
            if caractere.isdigit() or ( caractere.isupper() and 'A' <= caractere <= 'F' ):
                estado = 24
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("endereço invalido")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            
        elif estado == 24:
            if caractere.isdigit() or ( caractere.isupper() and 'A' <= caractere <= 'F' ):
                estado = 24
                token_atual += caractere
                coluna += 1
            else:
                tipo_token.append("Endereço")
                i -= 1
                estado = 0    
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
        
        # Operadores começados em < = >
        elif estado == 25:
            if caractere == '>':
                tipo_token.append("TAG")
                estado = 0
                token_atual += caractere
                coluna += 1
                colunas_token.append(coluna - len(token_atual))
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            elif caractere == '=':
                estado = 26
                token_atual += caractere
                coluna += 1
            elif caractere == '<':
                estado = 29
                token_atual += caractere
                coluna += 1
            else:
                tipo_token.append("Menor")
                i -= 1
                estado = 0
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            
        elif estado == 26:
            if caractere == '=':
                tipo_token.append("Atribuição")   
                estado = 0
                token_atual += caractere
                coluna += 1
                colunas_token.append(coluna - len(token_atual))
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            else:
                tipo_token.append("Menor_igual")
                i -= 1
                estado = 0
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            
        elif estado == 27:
            if caractere == '=':
                tipo_token.append("Comparação")
                estado = 0
                token_atual += caractere
                coluna += 1
                colunas_token.append(coluna - len(token_atual))
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            else:
                tipo_token_erro.append("operador invalido")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            
        elif estado == 28:
            if caractere == '=':
                tipo_token.append("Maior_igual")
                estado = 0
                token_atual += caractere
                coluna += 1
                colunas_token.append(coluna - len(token_atual))
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            else:
                tipo_token.append("Maior")
                i -= 1
                estado = 0
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            
        # Comentários com <<< >>>
        elif estado == 29:
            if caractere == '<':
                estado = 30
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("operador invalido")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            
        elif estado == 30:
            if caractere == '>':
                estado = 31
                token_atual += caractere
                coluna += 1
            elif caractere == '\n':
                coluna = 1
                token_atual += caractere
            else:
                estado = 30
                token_atual += caractere
                coluna += 1
                
        elif estado == 31: 
            if caractere == '>':
                estado = 32
                token_atual += caractere
                coluna += 1
            elif caractere == '\n':
                linha -= 1
                coluna = 1
                token_atual += caractere
                estado = 30
            else:
                estado = 30
                token_atual += caractere
                coluna += 1
                
        elif estado == 32:
            if caractere == '>':
                estado = 0
                token_atual = ""
                coluna = 1
            elif caractere == '\n':
                linha -= 1
                coluna = 1
                token_atual += caractere
                estado = 30
            elif caractere == '\0':
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                linha -= 1
                coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            else:
                estado = 30
                token_atual += caractere
                coluna += 1

        elif estado == 33:
            if caractere == '\n': 
                i -= 1
                estado = 0
                linha -= 1
                token_atual = ""
                coluna = 1
            else:
                estado = 33
                token_atual += caractere
                coluna += 1
             
        elif estado == 34:
            if caractere.islower():
                estado = 37
                token_atual += caractere
                coluna += 1
            elif caractere.isupper():
                estado = 35
                token_atual += caractere
                coluna += 1
            else:
                tipo_token_erro.append("no minimo 2 caracteres")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            
        elif estado == 35:
            if caractere.islower():
                estado = 36
                token_atual += caractere
                coluna += 1
            else:
                tipo_token.append("Variavel")
                i -= 1
                estado = 0
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            
        elif estado == 36:
            if caractere.isupper():
                estado = 35
                token_atual += caractere
                coluna += 1
            else:
                tipo_token.append("Variavel")
                i -= 1
                estado = 0
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            
        elif estado == 37:
            if (caractere.islower() or caractere == '_'):
                estado = 37
                token_atual += caractere
                coluna += 1
            elif token_atual in palavras_reservadas:
                tipo_token.append("Palavra_Reservada")
                i -= 1
                estado = 0
                colunas_token.append(coluna - len(token_atual))
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            else:
                tipo_token_erro.append("palavra reservada invalida")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
                
            
        elif estado == 38:
            if caractere == '"':
                tipo_token.append("Cadeia")
                estado = 0
                token_atual += caractere
                coluna += 1
                colunas_token.append(coluna - len(token_atual))
                linhas_token.append(linha)
                tokens_lidos.append(token_atual)
                token_atual = ""
            elif caractere == '\n':
                tipo_token_erro.append("cadeia não fechada")
                i -= 1
                estado = 0
                colunas_token_erro.append(coluna-1)
                if caractere == '\n':
                    linha -= 1
                    coluna = 1
                linhas_token_erro.append(linha)
                tokens_lidos_erro.append(token_atual)
                token_atual = ""
            else:
                estado = 38
                token_atual += caractere
                coluna += 1
             
        i += 1   
    return tipo_token, tokens_lidos, linhas_token, colunas_token, tipo_token_erro, tokens_lidos_erro, linhas_token_erro, colunas_token_erro
       
       
       
# Print do resultado da função  
resultado = analise_lexica(caracteres)
print("\n"+somatorio_tokens(resultado[0]))
print("\n\n\n"+lista_tokens(resultado[2],resultado[3],resultado[0],resultado[1]))
#print("\n\n\n",resultado[2],len(resultado[2]),"\n\n",resultado[3],len(resultado[3]),"\n\n",resultado[0],len(resultado[0]),"\n\n",resultado[1],len(resultado[1]))
#print ("\n\n\n",resultado[5],resultado[6],resultado[7],resultado[4])
print ("\n\n\n",lista_erros(resultado[5],resultado[6],resultado[7],resultado[4]))