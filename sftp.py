from os import chmod
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
     try:
            cmd = input("SFTP_DO_FELIPE&CARLOS>")
            if cmd == "exit" : break

            if cmd == "get":
                # Download
                print("Baixando arquivo...")
                filepath = "/home/administrador/sftp/teste.txt"
                localpath = "/home/felipe/Documentos/sftp/teste.txt"
                sftp.get(filepath,localpath)
            elif cmd == "put":
                # Upload
                print("Atualizando arquivo...")
                filepath = "/home/administrador/sftp/teste.txt"
                localpath = "/home/felipe/Documentos/sftp/testando.txt"
                sftp.put(localpath,filepath)
            elif cmd == "rename":
                # Mundando o nome do arquivo
                print("Mudando o nome do arquivo...")
                oldPath = "/home/administrador/sftp/meuNome.txt"
                newPath = "/home/administrador/sftp/meuNovoNome.txt"
                sftp.rename(oldPath,newPath)
            elif cmd == "chmod":
                # Mudando o permissionamento do arquivo
                print("Mudando o permissionamento do arquivo!")
                path = "/home/administrador/sftp/teste.sh"
                sftp.chmod(path,0o111)
            elif cmd == "chown":
                # Mudando o proprietário e o grupo do arquivo
                print("Mudando o proprietário e o grupo do arquivo!")
                path = "/home/administrador/sftp/teste.sh"
                sftp.chown(path,0o1000,0o1000)
            elif cmd == "stat":
                # Obtendo  o status do arquivo
                print("Obtendo status do arquivo...")
                path = "/home/administrador/sftp/teste.sh"
                sftp.stat(path)
            elif cmd == "rmdir":
                # Remover um diretório
                print("Removendo diretório...")
                path = "/home/administrador/sftp/removendoDiretorio"
                sftp.rmdir(path)
            elif cmd == "chdir":
                # Mudando o caminho do diretório atual
                print("Mudando o caminho do diretório atual...")
                path = "/home/administrador/sftp/mudandoDiretorio"
                sftp.chdir(path)
            elif cmd == "mkdir":
                # Criando um diretório
                print("Diretório sendo criado")
                sftp.mkdir("/home/administrador/sftp/meuNovoDiretorio")
            elif cmd == "pwd":
                # Pegando o caminho do diretório atual
                print("Pegando o caminho do diretorio atual...")
                path = "/home/administrador/sftp/"
                sftp.chdir(path)
                sftp.getcwd()
            elif cmd == "ls":
                # Retorna a lista dos arquivos do diretório atual
                print("Retorna a lista de arquivos do diretorio atual")
                path = "/home/administrador/sftp/"
                sftp.chdir(path)
                sftp.listdir()
            elif cmd == "prename":
                print("Renomeando o diretório")
                # Renomeando um diretório
                oldPath = "/home/administrador/sftp/diretorio1"
                newPath = "/home/administrador/sftp/diretorio2"
                sftp.posix_rename(oldPath,newPath)
            elif (cmd == "?" or cmd == "help"):
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
            else:
                print("Opção inválida, Digite help ou ? para ver os comandos disponivéis")
     except KeyboardInterrupt:
        break

# Fechando a sessão sftp
if sftp: sftp.close()
if transport: transport.close()