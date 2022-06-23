import paramiko
paramiko.util.log_to_file("paramiko.log")

# Abrindo uma sessão ssh
ip,porta = "172.16.0.201",22
transport = paramiko.Transport((ip,porta))

# Autenticação    
usuario,senha = "administrador","pr@8308"

transport.connect(None,usuario,senha)

# client.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
# Vamos lá!    
sftp = paramiko.SFTPClient.from_transport(transport)

while True: 
    print("")


# Operação com arquivos

# Download
filepath = "/home/administrador/sftp/teste.txt"
localpath = "/home/felipe/Documentos/sftp/teste.txt"
sftp.get(filepath,localpath)

# Upload
filepath = "/home/administrador/sftp/teste.txt"
localpath = "/home/felipe/Documentos/sftp/testando.txt"
sftp.put(localpath,filepath)

# Mundando o nome do arquivo
oldPath = "/home/administrador/sftp/meuNome.txt"
newPath = "/home/administrador/sftp/meuNovoNome.txt"
sftp.rename(oldPath,newPath)

# Mudando o permissionamento do arquivo
path = "/home/administrador/sftp/teste.sh"
sftp.chmod(path,0o111)

# Mudando o proprietário e o grupo do arquivo
path = "/home/administrador/sftp/teste.sh"
sftp.chown(path,0o1000,0o1000)

# Obtendo  o status do arquivo
path = "/home/administrador/sftp/teste.sh"
sftp.stat(path)


# Operações com diretório

# Remover um diretório
path = "/home/administrador/sftp/removendoDiretorio"
sftp.rmdir(path)

# Mudando o caminho do diretório atual
path = "/home/administrador/sftp/mudandoDiretorio"
sftp.chdir(path)

# Pegando o caminho do diretório atual
path = "/home/administrador/sftp/"
sftp.getcwd()

# Retorna a lista dos arquivos do diretório atual
path = "/home/administrador/sftp/"
sftp.chdir(path)
sftp.listdir()

# Criando um diretório
sftp.mkdir("/home/administrador/sftp/meuNovoDiretorio")

# Renomeando um diretório
oldPath = "/home/administrador/sftp/diretorio1"
newPath = "/home/administrador/sftp/diretorio2"
sftp.posix_rename(oldPath,newPath)

# Close
if sftp: sftp.close()
if transport: transport.close()