#importações
import random #numeros aleatorios


#listas
conta = []
extrato = []  


#status conta
bloqueada = False

#Função do menu
def menu():
    print("---------MACK BANK----------")
    print("-----ESCOLHA UMA OPÇÃO------")
    print("(1) CADASTRAR CONTA")
    print("(2) DEPOSITAR")
    print("(3) SACAR")
    print("(4) CONSULTAR SALDO")
    print("(5) CONSULTAR EXTRATO")
    print("(6) FINALIZAR")
    print("----------------------------")
           
#Função cadastrar Conta
def cadastrar_conta():
    print("------CADASTRAR CONTA------")
    
    #as variaveis são globais
    global num_conta, nome, telefone, email, saldo, credito, senha, ssenha
    num_conta = random.randint(1000, 9999)
    print("Numero da conta: ", num_conta)
    conta.append(num_conta)
    nome = input("Nome: ")
    
    #Validações nome
    # Esses dois while sãp para situações diferentes, o primeiro caso a pessoa deixe o campo vazio e o segundo caso ela coloque algum numero 

    while not nome:
        print("ERRO! Campo vazio, digite!")
        nome = input("Nome: ")
        
    while not nome.replace(" ", "").isalpha(): # Replace permite os espaços e IsAlpha verifica se só ha strings no campo
            print("ERRO! Digite apenas caracteres")
            nome = input("Nome: ")
         
    conta.append(nome)
    
    #Valida o telefone
    while True:
        try:
            telefone = int(input("Telefone: "))
            if not telefone:
                raise ValueError("ERRO! Campo vazio, digite!")
            break
        except ValueError:
            print("Insira apenas números")
        
    conta.append(telefone)
    
    #Validação Email
    email = input("Email: ")
    while not email:
        print("ERRO! Campo vazio, digite!")
        email = input("Email: ")
        
    conta.append(email)
    
    #Validação saldo
    while True:
        try:
            saldo = float(input("Saldo: "))
            if saldo < 1000:
                print("ERRO! O valor do saldo deve ser igual ou maior que R$ 1000")
            else:
                break
        except ValueError:
            print("ERRO! Valor inválido, digite novamente")
            
            
    conta.append(saldo) 
    
    #Validação de crédito
    while True:
        try:
            credito = float(input("Limite de crédito: R$"))
            if saldo < 0:
                print("ERRO! O valor do saldo deve ser igual ou maior que R$ 0")
            else:
                break
        except ValueError:
            print("ERRO! Valor inválido, digite novamente")
    
     #Validação de senha 
    while True:
        try:
            senha = input("Senha: ")
            if len(senha) != 6:
                print("ERRO! A senha deve ter 6 caracteres")
            else:
                ssenha = input("Confirme a senha: ")
                if ssenha != senha:
                    print("ERRO! As senhas não coincidem")
                else:
                    break
        except ValueError:
            print("ERRO! Valor inválido")

        
        
            
        
    conta.append(senha)
    conta.append(ssenha)  
    print("--------CONTA CADASTRADA COM SUCESSO---------------")
 
    
    
 #Função mostrar conta

#Funçao mostrar conta
def mostrar_conta():
    print("------------------------------")
    print("Numero da conta: ", num_conta)  
    print("Nome: ", nome)
    print("Telefone: ", telefone)
    print("email: ", email)
    print("Senha: ", senha)
    print("------------------------------")

#Funcao Deposito
def deposito():
    global valida_numconta, valor_deposito, saldo, extrato_deposito
    print("-----MACK BANK---DEPÓSITO-----")
    
    #Solicitação do numero da conta junto com a validação se é igual a conta cadastrada, ou se vazia
    while True:
        try:
            valida_numconta = int(input("Informe o número da conta: ")) 
            if valida_numconta != num_conta:
                print("ERRO! Número da conta inválido")
            else:
                print("Nome do cliente: ", nome)
                break
        except ValueError:
                print("ERRO! Valor inválido")
                
    #Operação do depósito
    while True:
        try:
            valor_deposito = float(input("Valor do depósito: R$"))
            if valor_deposito <= 0:
                print("O valor deve ser maior que R$0 !")
            else:
                saldo += valor_deposito
                extrato_deposito = (f"Depósito de: R${valor_deposito}")
                extrato.append(extrato_deposito)
                print("------DEPÓSITO REALIZADO COM SUCESSO--------")
                break
        except ValueError:
                   print("ERRO! Valor inválido")
            
#Funcao Sacar
def sacar(): 
    global valida_senha, bloqueada, saldo, credito
    tentativas = 3
    print("-----MACK BANK---SAQUE-----")
    
    #Solicitação do numero da conta junto com a validação se é igual a conta cadastrada, ou se vazia
    while True:
        global extrato_saque
        try:
            valida_numconta = int(input("Informe o número da conta: ")) 
            if valida_numconta != num_conta:
                print("ERRO! Número da conta inválido")
            else:
                print("Nome do cliente: ", nome)
                break
        except ValueError:
                print("ERRO! Valor inválido") 
                   
     #Validação de senha e processo de saque           
    while True: 
        try:
            valida_senha = input("Senha: ")
            if valida_senha != senha:
                tentativas -= 1
                print("Senha incorreta, você tem apenas mais", tentativas, " tentativas")
                if tentativas == 0:
                     print("-------CONTA BLOQUEADA-----------")
                     bloqueada = True
                     break
            else:
                try:
                    saque = float(input("Digite o valor do saque: R$"))
                    if saque < 0:
                        print("ERRO! O Valor deve ser maior que R$0")
                    else:
                        try:
                            if saque <= saldo:
                                saldo -= saque
                                print("------SAQUE REALIZADO COM SUCESSO--------------")
                                extrato_saque = (f"Saque de: R$-{saque}")
                                extrato.append(extrato_saque)
                            if saque > saldo:
                                print("---------VOCÊ ESTÁ USANDO SEU LIMITE DE CRÉDITO---------")
                                credito -= saque
                                saldo -= saque
                                extrato_saque = (f"Saque de: R$-{saque}")
                                extrato.append(extrato_saque)
                                print("------SAQUE REALIZADO COM SUCESSO--------------")

                            
                                
                            else:
                                break
                        except ValueError:
                            print("ERRO! Valor inválido")
            
                                       
                except ValueError:
                    print("ERRO! Valor inválido")
                    break
                    
                break
        except ValueError:
            print("ERRO! Valor inválido")

#Funcao consulta saldo
def consulta():
    global bloqueada
    tentativas = 3
    print("----------MACK BANK-CONSULTAR-SALDO-------------")
    
    #Solicitação do numero da conta junto com a validação se é igual a conta cadastrada, ou se vazia
    while True:
        try:
            valida_numconta = int(input("Informe o número da conta: ")) 
            if valida_numconta != num_conta:
                print("ERRO! Número da conta inválido")
            else:
                print("Nome do cliente: ", nome)
                break
        except ValueError:
                print("ERRO! Valor inválido") 
                   
     #Validação de senha e processo de consulta           
    while True: 
        try:
            valida_senha = input("Senha: ")
            if valida_senha != senha:
                tentativas -= 1
                print("Senha incorreta, você tem apenas mais", tentativas, " tentativas")
                if tentativas == 0:
                     print("-------CONTA BLOQUEADA-----------")
                     bloqueada = True
                     break
            else:
                print("saldo: ", saldo)
                print("Limite de crédito", credito)
                print("------------------------------")
                break
        except ValueError:
            print("ERRO! Valor Inválido")

#Funcao consulta extrato                                    
def verextrato():
    global extrato, bloqueada
    tentativas = 3
    print("----------MACK BANK-CONSULTAR-EXTRATO-------------")
    
    #Solicitação do numero da conta junto com a validação se é igual a conta cadastrada, ou se vazia
    while True:
        try:
            valida_numconta = int(input("Informe o número da conta: ")) 
            if valida_numconta != num_conta:
                print("ERRO! Número da conta inválido")
            else:
                print("Nome do cliente: ", nome)
                break
        except ValueError:
                print("ERRO! Valor inválido") 
                   
     #Validação de senha e processo de consulta           
    while True: 
        try:
            valida_senha = input("Senha: ")
            if valida_senha != senha:
                tentativas -= 1
                print("Senha incorreta, você tem apenas mais", tentativas, " tentativas")
                if tentativas == 0:
                     print("-------CONTA BLOQUEADA-----------")
                     bloqueada = True
                     break
            else:
                print("Limite de crédito", credito)
                print("--------ULTIMAS OPERAÇÕES------------")
                for i in extrato:
                    print(i)
                
                if saldo > 0:
                    print(f"Saldo em conta: R${saldo}") 
                else:
                    print(f"Saldo em conta: R${saldo}") 
                    print(f"Atenção ao seu saldo!")
                print("------------------------------")
                break
        except ValueError:
            print("ERRO! Valor Inválido")
  
#Elifs dos processos    
while True:
    menu()
    opcao = int(input("Sua opção: "))
    
    

    
        
    
    if opcao < 0 or opcao > 6:
        print("NUMERO INCORRETO, DIGITE UM NUMERO DE 1 A 6")     
    else:
        
        #cadastra a conta
        if opcao == 1:
                if conta:
                    print("Já Existe uma conta cadastrada")
                    mostrar_conta()
                    
                else:
                    cadastrar_conta()
                    
        #Deposito                           
        if opcao == 2:
            if conta:
                deposito()
            else:
                print("ERRO! CONTA NÃO CADASTRADA")
        
        
        if bloqueada == True and opcao != 1 and opcao != 2 and opcao != 6:
            print("-------CONTA BLOQUEADA-----------")  
            
        #Saca   
        elif opcao == 3:
            if conta:
                sacar()
                
            else:
                print("ERRO! CONTA NÃO CADASTRADA")
                
            
        #Consulta 
        elif opcao == 4:
            if conta:
                consulta()
                
            else:
                print("ERRO! CONTA NÃO CADASTRADA")
                
            

        elif opcao == 5:
            if conta:
                verextrato()
                
            else:
                print("ERRO! CONTA NÃO CADASTRADA")
                
            

        if opcao == 6:
            print("---------MACK-BANK-SOBRE--------")
            print("Finalizando...")
            print("---ESSE PROGRAMA FOI FEITO POR:-----")
            print("Carlos Eduardo da Costa Oliveira")
            print("Cássio Silva Melo")
            break
        
        
    
    input("Pressione qualquer tecla para voltar ao menu")
       


    

    
    
