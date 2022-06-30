import paramiko
import os
paramiko.util.log_to_file("paramiko.log")

# Abrindo uma sessão ssh
ip,porta = "172.16.0.201",22
transport = paramiko.Transport((ip,porta))

# Autenticação    
usuario,senha = "administrador","pr@8308"

transport.connect(None,usuario,senha)

# Vamos lá!    
sftp = paramiko.SFTPClient.from_transport(transport)


def get(sftp):
    print("Baixando arquivo...")
    filepath = input("Digite o caminho do arquivo no servidor:")
    localpath = input("Digite o caminho local para armazenar o arquivo:")
    try:
        sftp.get(filepath, localpath)
        print("Arquivo baixado")
    except:
        print("Nome do diretório inválido")

def put(sftp):
    print("Atualizando arquivo...")
    filepath = input("Digite o caminho do arquivo no servidor:")
    localpath = input("Digite o caminho local do arquivo:")
    try:
        sftp.put(localpath,filepath)
        print("Arquivo atualizado")
    except:
        print("Nome do diretório inválido")

def rename(sftp):
    print("Mudando o nome do arquivo...")
    oldPath = input("Digite o caminho do arquivo no servidor:")
    newPath = input("Digite o novo caminho do arquivo no servidor:")
    try:
        sftp.rename(oldPath,newPath)
        print("Nome do arquivo mudado")
    except: 
        print("Nome do diretório inválido")

def chmod(sftp):
    print("Mudando o permissionamento do arquivo!")
    path = input("Digite o caminho do arquivo no servidor:")
    permissionCode = input("Digite o código  binário de permissionamento pro arquivo:")
    try:
        sftp.chmod(path,oct(int(permissionCode)))
        print("Permissionamento mudado")
    except:
        print("Erro ao mudar o permissionamento")

def chown(sftp):
     print("Mudando o proprietário e o grupo do arquivo!")
     path = input("Digite o caminho do arquivo no servidor:")
     uid = input("Digite o id do usuário no servidor:")  
     gid = input("Digite o id do grupo no servidor:")
     try:
        sftp.chown(path,oct(int(uid)),oct(int(gid)))
        print("Proprietário e grupo mudado")
     except:
        print("Erro ao mudar o proprietário do arquivo")

def stat(sftp):
    print("Obtendo status do arquivo...")
    path = input("Digite o caminho do arquivo no servidor:")
    try:
        status = sftp.stat(path)
        print("______Status do arquivo______")
        print(status)
    except:
        print("Nome do Diretório inválido")

def rmdir(sftp):
    print("Removendo diretório...")
    path = input("Digite o caminho do diretório no servidor:")
    try:
        sftp.rmdir(path)
        print("Diretório removido")
    except:
        print("Nome do diretório inválido")

def mkdir(sftp):
    print("Diretório sendo criado")
    path = input("Digite o caminho para o novo diretório no servidor:")
    try:
        sftp.mkdir(path)
        print("Diretório criado")
    except:
        print("Nome do diretório inválido")

def chdir(sftp):
    print("Mudando o caminho do diretório atual...")
    path = input("Digite o caminho pro novo diretório no servidor:")
    try:
        sftp.chdir(path)
        pwd = sftp.getcwd()
        print("Novo caminho:"+ pwd)
        print("Caminho alterado")
    except:
        print("Nome do diretório inválido")

def pwd(sftp):
    print("Pegando o caminho do diretorio atual...")
    try:
        pwd = sftp.getcwd()
        print("Diretório atual:"+pwd)
    except:
        print("Ocorreu um erro ao pegar o caminho atual")

def ls(sftp):
    print("Retorna a lista de arquivos do diretorio atual")
    try:
        ls = sftp.listdir()
        print("____Arquivos presentes no diretório atual____")
        print(ls)
    except:
        print("Ocorreu um erro ao listar os arquivos do diretório atual")

def prename(sftp):
    print("Renomeando o diretório")
    oldPath = input("Digite o caminho antigo do diretório no servidor")
    newPath = input("Digite o caminho novo pro diretório no servidor")
    try:
        sftp.posix_rename(oldPath,newPath)
        print("Diretório renomeado")
    except:
        print("Nome do diretório inválido")

def help(sftp):
    print("Comandos disponivéis")
    print("get \t Baixar o arquivo")
    print("put \t Atualizar o arquivo")
    print("rename \t Mudar o nome do arquivo")
    print("chmod \t Mudar o permissionamento do arquivo")
    print("chown \t Mudar o proprietário/grupo do arquivo")
    print("stat \t Obtendo status do arquivo")
    print("rmdir \t Removendo um diretório")
    print("mkdir \t Criando um diretório")
    print("pwd \t Pegando o caminho do diretório atual")
    print("ls \t Retorna a lista de arquivos do diretório atual")
    print("prename \t Renomeando um diretório")
    print("clear \t Limpa o console")
    print("?/ help \t Mostra a lista de comandos disponivéis")

def clear(sftp):
    os.system('clear')

sftpOpcoes = {
    "get": get,
    "put": put, 
    "rename": rename,
    "chmod": chmod,
    "chown":chown,
    "stat":stat,
    "rmdir": rmdir,
    "mkdir": mkdir,
    "chdir": chdir,
    "pwd":pwd, 
    "ls": ls,
    "prename": prename, 
    "help": help,
    "?":help,
    "clear": clear
}

while True: 
     try:
            cmd = input("SFTP_DO_FELIPE&CARLOS>")
            if cmd == "exit" : break

            if(sftpOpcoes.__contains__(cmd)):
                sftpOpcoes[cmd](sftp)
            else:
                print("Opção inválida, Digite help ou ? para ver os comandos disponivéis")
     except KeyboardInterrupt:
        break

# Fechando a sessão sftp
if sftp: sftp.close()
if transport: transport.close()