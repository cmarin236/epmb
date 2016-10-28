import dryscrape
import unicodedata
from bs4 import BeautifulSoup

def normalizar(dato):
    resultado = unicodedata.normalize('NFKD', dato).encode('ascii', 'ignore')
    return resultado

print('Comienza el programa')
archivo = open('productoPrecio.csv','w')
#url = "https://www.lider.cl/walmart/catalog/product/productList.jsp?id=cat550033&cId=CF_Nivel2_000011&pId=CF_Nivel1_000003&pageSizeCategory=20"
url = "https://www.lider.cl/walmart/catalog/category.jsp?id=CF_Nivel3_000211&pId=CF_Nivel1_000003&navAction=jump&navCount=0#categoryCategory=CF_Nivel3_000211&pageSizeCategory=90&currentPageCategory=1&currentGroupCategory=1&orderByCategory=lowestPrice&lowerLimitCategory=0&upperLimitCategory=0&&279"
session = dryscrape.Session()
session.visit(url)
response = session.body()
soup = BeautifulSoup(response,"html.parser")
codigohtml = soup.find('div', {"class":"caja-resultados"})

i = 1
for productos in codigohtml.findAll('div', {"class":"elemento-recomendado"}):
    codigo = productos.find('p', {"class":"prod_referencia"}).text
    marca = productos.find('div', {"class": "nombre"}).find('p').text.split(',')[0]
    nombre = productos.find('div', {"class":"nombre"}).find('p').text.split(',')[1]
    precio = productos.find('span', {"class":"sale-price"}).text
    print(str(i) + " - " + codigo.strip() + " - " + marca.strip() + " - " + nombre.strip() + " - " + precio.strip())
    """
    codigo2 = unicodedata.normalize('NFKD', codigo).encode('ascii', 'ignore')
    marca2  = unicodedata.normalize('NFKD', marca).encode('ascii', 'ignore')
    nombre2 = unicodedata.normalize('NFKD', nombre).encode('ascii', 'ignore')
    precio2 = unicodedata.normalize('NFKD', precio).encode('ascii', 'ignore')
    """

    archivo.write(str(i) + '\t' + normalizar(codigo.strip()) + '\t' + normalizar(marca.strip()) + '\t' + normalizar(nombre.strip()) + '\t' + normalizar(precio.strip()) + '\n')
    #archivo.write(str(i) + '\n' + codigo2.strip() + '\t')
    i = i + 1

archivo.close()
print('Fin del programa')