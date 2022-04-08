import qrcode

# Colocar o link que vai virar qr
imagem = qrcode.make("https://www.facebook.com/edvania.lima.583")

# Colocar o nome do arquivo e a extensão
imagem.save("Doc.jpg")
