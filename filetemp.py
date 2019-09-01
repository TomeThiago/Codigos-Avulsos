import tempfile

#cria um arquivo temporario
temp = tempfile.TemporaryFile()

#Escreve no arquivo temporario
temp.write(b'Teste')

#Volta para o inicio do arquivo
temp.seek(0)

#Mostra o conteudo do arquivo
print(str(temp.read(), encoding='utf8'))

#Fecha o arquivo
temp.close()