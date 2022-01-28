users = {'User':'123','User2':'321'}

while True:       
    def login():
        usuario = input('NOME DE ÚSUARIO: ')
        senha = input('SENHA: ')

        if usuario in users and senha == users[usuario]:
            print('\nUsúario Logado!\n')
        else:
            print('\nUsúario ou senha estão incorretos, tente novamente!\n')
        

    def cadastro():
        novo_user = input('DIGITE UM NOVO USÚARIO: ')
        nova_senha = input('DIGITE UMA SENHA: ')
        if novo_user in users:
            print('Úsuario já cadastrado, tente novamente!')
        else:
            users.setdefault(novo_user,nova_senha)
            print(f'Usúario "{novo_user}" criado com sucesso!')


    opcao = int(input('[1] LOGIN\n[2] CADASTRO\n[3] VER ÚSUARIOS(ADMIN)\n\nEscolha uma opcão: '))
    if opcao == 1:
        login()
    if opcao == 2:
        cadastro()
    if opcao == 3:
        print('Users: ', users)


