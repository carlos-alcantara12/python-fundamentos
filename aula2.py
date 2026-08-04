# \n -> LF
# \r\n -> CRLF

# CORRIGIDO: o original usava barra normal ('/n', '/r/n'), que é só
# texto literal e não tem efeito de quebra de linha. A sequência de
# escape correta usa contrabarra: '\n' e '\r\n'.
print("123, 234", sep=" ---", end='\r\n')
print("567, 8910", sep=" ---", end='\n')

# ISTO É O ARGUMENTO PRINT.
