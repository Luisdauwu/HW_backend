class Carro:

  def __init__(self, marca, modelo, año, precio, kilometraje, color, imagen_principal, imagenes_adicionales, caracteristicas, descripcion):
    self.marca = marca
    self.modelo = modelo
    self.año = año
    self.precio = precio
    self.kilometraje = kilometraje
    self.color = color
    self.imagen_principal = imagen_principal
    self.imagenes_adicionales = imagenes_adicionales
    self.caracteristicas = caracteristicas
    self.descripcion = descripcion

  def obtener_precio_formateado(self):
    return ""

  def tiene_caracteristica(self, nombre_caracteristica):
    return False

class Imagen:

  def __init__(self, ruta, titulo, descripcion):
    self.ruta = ruta
    self.titulo = titulo
    self.descripcion = descripcion

class Caracteristica:

  def __init__(self, nombre, valor):
    self.nombre = nombre
    self.valor = valor

class Comparador:

  def __init__(self):
    self.carros_seleccionados = []

  def agregar_carro(self, carro):
    self.carros_seleccionados.append(carro)

  def remover_carro(self, carro):
    self.carros_seleccionados.remove(carro)

  def obtener_diferencias(self, carro1, carro2):
    diferencias = {}
    for atributo in carro1.__dict__:
      if carro1.__dict__[atributo] != carro2.__dict__[atributo]:
        diferencias[atributo] = (carro1.__dict__[atributo], carro2.__dict__[atributo])
    return diferencias

class Filtro:

  def __init__(self):
    self.marca = None
    self.modelo = None
    self.año_desde = None
    self.año_hasta = None
    self.precio_desde = None
    self.precio_hasta = None
    self.kilometraje_desde = None
    self.kilometraje_hasta = None
    self.colores = []
    self.caracteristicas = []

  def aplicar_filtro(self, carros):

    carros_filtrados = []
    for carro in carros:
      cumple_filtro = True
      if self.marca and self.marca != carro.marca:
        cumple_filtro = False    
      if self.modelo and self.modelo != carro.modelo:
        cumple_filtro = False
      if cumple_filtro:
        carros_filtrados.append(carro)
    return carros_filtrados

class Ordenador:

  def __init__(self):
    self.criterio_orden = None
    self.orden_ascendente = True

  def ordenar_carros(self, carros):
    if self.criterio_orden == "precio":
      carros.sort(key=lambda carro: carro.precio, reverse=not self.orden_ascendente)
    elif self.criterio_orden == "año":
      carros.sort(key=lambda carro: carro.año, reverse=not self.orden_ascendente)
    return carros