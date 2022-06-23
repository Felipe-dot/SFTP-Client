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

# Operação com arquivos

# Download
filepath = "/home/administrador/sftp/teste.txt"
localpath = "/home/felipe/Documentos/sftp/teste.txt"
sftp.get(filepath,localpath)

# Upload
filepath = "/home/administrador/sftp/teste.txt"
localpath = "/home/felipe/Documentos/sftp/testando.txt"
sftp.put(localpath,filepath)

# Operações com diretório

# Remover um diretório
path = "/home/administrador/sftp/teste"
sftp.rmdir(path)

# Close
if sftp: sftp.close()
if transport: transport.close()