# EntregaIntermediaLoboPablo
Página de contenido de tecnologia de Marcos Paz  (PYthon y Django)
El Tp tiene como aplicación la app "AppTecnoWolf", donde se almacenan todas las URLS de los templates, la URL de la App queda en las URLS del proyecto, por prolijidad y practicidad.
Al ingresar a AppTecnoWolf/inicio se accede al inicio, el cual consta de botones Inicio (para poder volver siempre al inicio una vez terminado el ingreso o la búsqueda de productos
a través de las migraciones a DB en SQLite).
El entregable pedía búsqueda en DB de una categoría, por lo que se optó por búsqueda de Discos. 
Cada botón dirige a un template mediante su respectiva URL.
La lógica de los templates se puede encontrar en las funciones generadas en views (con la importación de las clases Form y Models),(Métodos GET Y POST, definición de funciones de 
categorías de productos, definición de funciones tanto de búsqueda como de agregar productos). Se creó una carpeta static, la cual contiene el contenido de templates bajado de bootstrap
Se creó un SuperUser como admin con su respectivo usuario y contraseña, con el fin de que tenga acceso a la DB y poder modificar información pero sin acceder al código.





