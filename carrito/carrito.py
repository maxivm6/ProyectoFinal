class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:                                 #Comprueba si hay un carrito de compra previo
            carrito = self.session['carrito'] = {}
        self.carrito = carrito 
            
    def agregar(self,producto):
        p = producto
        
        if (str(p.id) not in self.carrito.keys()):  #Comprueba si el producto está o no agregado al carrito previamente
            self.carrito[p.id] = {
                "producto_id":p.id,
                "nombre":p.nombre,
                "descripcion":p.descripcion,
                "precio":str(p.precio),
                "cantidad": 1,
                "imagen":p.imagen.url,
            }
        else:
            for key, value in self.carrito.items():
                if key==str(p.id):
                    value["cantidad"] += 1
                    value["precio"] = float(value["precio"])+p.precio
                    break
        self.guardar_carrito()
        
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
        
    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardar_carrito()
            
    def restar_producto(self,producto):
        for key, value in self.carrito.items():
                if key==str(producto.id):
                    value["cantidad"] -= 1
                    value["precio"] = float(value["precio"]) - producto.precio
                    if value["cantidad"] < 1:
                        self.eliminar(producto)
                    break                
        self.guardar_carrito()
        
    def limpiar_carrito(self):
        self.session['carrito'] = {}
        self.session.modified(True) 
        