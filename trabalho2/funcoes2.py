def loginUsuario(perfil):
    perfil = perfil.lower()
    if perfil == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuario')
loginUsuario('root')
loginUsuario('root123')
