import paramiko
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
    filepath = "/home/administrador/sftp/teste.txt"
    localpath = "/home/felipe/SFTP-Client/teste.txt"
    sftp.get(filepath, localpath)
    print("Arquivo baixado")

def put(sftp):
    print("Atualizando arquivo...")
    filepath = "/home/administrador/sftp/teste.txt"
    localpath = "/home/felipe/Documentos/sftp/testando.txt"
    sftp.put(localpath,filepath)
    print("Arquivo atualizado")

def rename(sftp):
    print("Mudando o nome do arquivo...")
    oldPath = "/home/administrador/sftp/meuNome.txt"
    newPath = "/home/administrador/sftp/meuNovoNome.txt"
    sftp.rename(oldPath,newPath)
    print("Nome do arquivo mudado")

def chmod(sftp):
    print("Mudando o permissionamento do arquivo!")
    path = "/home/administrador/sftp/teste.sh"
    sftp.chmod(path,0o111)
    print("Permissionamento mudado")

def chown(sftp):
     print("Mudando o proprietário e o grupo do arquivo!")
     path = "/home/administrador/sftp/teste.sh"
     sftp.chown(path,0o1000,0o1000)
     print("Proprietário e grupo mudado")

def stat(sftp):
    print("Obtendo status do arquivo...")
    path = "/home/administrador/sftp/teste.sh"
    status = sftp.stat(path)
    print(status)

def rmdir(sftp):
    print("Removendo diretório...")
    path = "/home/administrador/sftp/removendoDiretorio"
    sftp.rmdir(path)
    print("Diretório removido")

def mkdir(sftp):
    print("Diretório sendo criado")
    path = "/home/administrador/sftp/meuNovoDiretorio"
    sftp.mkdir(path)
    print("Diretório criado")

def chdir(sftp):
    print("Mudando o caminho do diretório atual...")
    path = "/home/administrador/sftp/mudandoDiretorio"
    sftp.chdir(path)
    print("Caminho alterado")

def pwd(sftp):
    print("Pegando o caminho do diretorio atual...")
    path = "/home/administrador/sftp/"
    sftp.chdir(path)
    pwd = sftp.getcwd()
    print(pwd)

def ls(sftp):
    print("Retorna a lista de arquivos do diretorio atual")
    path = "/home/administrador/sftp/"
    sftp.chdir(path)
    ls = sftp.listdir()
    print(ls)

def prename(sftp):
    print("Renomeando o diretório")
    oldPath = "/home/administrador/sftp/diretorio1"
    newPath = "/home/administrador/sftp/diretorio2"
    sftp.posix_rename(oldPath,newPath)
    print("Diretório renomeado")

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
    print("?/ help \t Mostra a lista de comandos disponivéis")

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