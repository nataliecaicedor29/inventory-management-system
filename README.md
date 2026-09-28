# Sistema de Gestión de Inventario

Aplicación de consola creada con Python para administrar los productos de un inventario.

## Funcionalidades

- Agregar productos al inventario.
- Mostrar todos los productos disponibles.
- Buscar productos por su código.
- Vender productos y actualizar el stock.
- Mostrar un mensaje cuando no hay suficiente stock para realizar una venta.
- Validar que el precio y la cantidad sean números.

## Programación Orientada a Objetos

El proyecto utiliza dos clases principales:

- `Product`: representa un producto y guarda su nombre, código, precio y cantidad disponible.
- `Inventory`: administra el catálogo de productos y permite agregarlos, buscarlos, mostrarlos y venderlos.

También utiliza una excepción personalizada llamada `NotEnoughStockError` para manejar el caso en que se intenta vender una cantidad mayor al stock disponible.

## Cómo ejecutar el proyecto

1. Asegúrate de tener Python instalado.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el siguiente comando:

```bash
python main.py
```

## Estructura del proyecto

```text
main.py        # Menú e interacción con la persona usuaria
models.py      # Clases Product e Inventory
exceptions.py  # Excepción personalizada
README.md      # Documentación del proyecto
```

## Autora

Nataly Caicedo