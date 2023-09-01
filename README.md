### ¿Por qué los restaurantes necesitan sistemas de gestión?

[Tomado del artículo: Serving Delicious Food (and Data) – A Data Model for Restaurants](https://www.vertabelo.com/blog/serving-delicious-food-and-data-a-data-model-for-restaurants/)

La gestión de un restaurante no es una tarea fácil. Cuando se trata de realizar un seguimiento y ejecutar las tareas del día a día, incluso el restaurador más experimentado puede tener más de lo que puede gestionar fácilmente. Administrar un restaurante rentable requiere administrar el inventario/existencias, minimizar el desperdicio, administrar las mesas (especialmente en las horas pico), mantener un menú amigable para el cliente, ejecutar pedidos de manera eficiente y supervisar al personal del restaurante. ¡Eso es bastante!

Un sistema de gestión de restaurantes debe realizar la mayoría de estas actividades con una mínima intervención manual. Tiene que presentar a los gerentes información precisa para que puedan mantener contentos a los clientes. Esto puede significar realizar cambios apropiados en el menú e incluso en la forma en que funciona el restaurante.

### El modelo de datos del restaurante

Este artículo trata sobre el diseño de un modelo de datos completo para un restaurante (para cenar o para llevar). También abordaremos dos grandes problemas que encuentran las personas en el negocio de la restauración en sus actividades diarias. Finalmente, pensaremos en los cambios necesarios para incorporar esas capacidades a un sistema existente.

Un modelo de datos para un negocio de restauración debe tener las siguientes características elementales:

- **Gestión de KOT (Token de pedido de cocina)**
- **Gestión KOD (entrega de pedidos de cocina)**
- **Gestión de Menú**

Veamos cada una de estas características en detalle.

### Gestión de KOT (Token de pedido de cocina)

Esta es la parte más importante de nuestro modelo de datos: se trata de recopilar detalles de los pedidos de los clientes a través de varios canales. ¿Por qué varios canales? Porque hay varias formas de realizar pedidos: en línea o mediante una aplicación móvil, mediante llamadas telefónicas o a través de camareros u otros empleados. Cada vez que un cliente realiza un pedido, se genera un KOT (Token de pedido de cocina). Finalmente, el personal de cocina preparará el KOT.

![https://www.vertabelo.com/blog/serving-delicious-food-and-data-a-data-model-for-restaurants/kot-management.png](https://www.vertabelo.com/blog/serving-delicious-food-and-data-a-data-model-for-restaurants/kot-management.png)

Crearé una tabla `**kot**`para contener los detalles del pedido preliminar. Esta tabla tiene las siguientes columnas:

  

| Nombre de columna | Descripción |
| --- | --- |
| `Id` | La clave principal para esta tabla. |
| `order_channel_id` | El canal a través del cual se realiza el pedido. |
| `dine_in_table_sitting_id` | La tabla donde se origina el pedido. Esta columna se completará solo en el caso de pedidos para cenar. |
| `order_in_time` | La marca de tiempo cuando el pedido se registra en el sistema. |
| `order_out_time` | La marca de tiempo en la que el personal de cocina entrega el pedido. |
| `staff_id` | El DNI de la persona que recoge el pedido. En el caso de pedidos para cenar en el restaurante, esta columna contiene el ID del camarero que recoge el pedido. En otras configuraciones, esta ID sería 'SISTEMA'. |
| `kot_status_id` | Define el estado actual de un KOT. |

  
Me gustaría señalar que un pedido recopilado de una mesa a la vez está etiquetado bajo one `kot_id`. Si la misma mesa luego pide más artículos, el sistema generará otro kot\_id y etiquetará todos estos artículos nuevos con esa ID. Al final, todos `kot_ids`para la misma mesa se sumarán en la factura final.

La gestión de KOT requiere tablas estáticas y transaccionales adicionales, las cuales son:

- `order_channel`– Esta tabla contiene detalles sobre los canales que utiliza un restaurante para aceptar pedidos. Los ejemplos comunes incluyen en línea, cenar en casa, llevar (llevar a cabo), etc.
- `dine_in_table_sitting`– Esta es una tabla transaccional que almacena datos de ocupación de la tabla. Sus columnas incluyen `dine_in_table_id`, `dine_in_time`, `dine_out_time`, `num_person_sitting`y `customer_id`. Tan pronto como el anfitrión asigna un cliente a una mesa e ingresa la información en el sistema, se inserta un registro en esta tabla. Para obtener el estado de ocupación actual de las mesas en un momento dado, esta es la tabla que se utilizará.
- `kot_status`– Esta tabla contiene todos los estados posibles para un KOT: _pedido recibido_ , _pedido en proceso_ , _pedido entregado_ , etc.
- `**kot_menu_item**`– Esta tabla transaccional almacena los detalles de todos los artículos en un KOT. También define la relación entre el KOT y un `menu_item`. Los campos `menu_item_id`y `quantity`junto a `kot_id`indican el artículo pedido y la cantidad que se necesita.

### Gestión KOD (entrega de pedidos de cocina)

Gran parte del desempeño de un restaurante se reduce a gestionar KOT dentro de la cocina. Por lo general, un supervisor recopila los KOT de los camareros, otros empleados o un sistema en línea. Luego, el supervisor asigna los elementos del menú a uno o más cocineros. El cocinero prepara los artículos y se los entrega al supervisor. Luego el camarero u otro miembro del personal recoge el pedido y lo entrega al cliente.

Pero eso no es todo lo que incluye la gestión de KOD. Administrar recursos, almacenar ingredientes, actualizar periódicamente el inventario restante y solicitar nuevo inventario según sea necesario también es parte del funcionamiento diario de la cocina. El supervisor desempeña un papel fundamental en el buen funcionamiento de la cocina, especialmente durante las horas punta. Un sistema se considera "inteligente" si puede replicar las funciones laborales de un supervisor, lo cual es casi imposible en la mayoría de los lugares.

![https://www.vertabelo.com/blog/serving-delicious-food-and-data-a-data-model-for-restaurants/kod-management.png](https://www.vertabelo.com/blog/serving-delicious-food-and-data-a-data-model-for-restaurants/kod-management.png)

Para construir un modelo para esta compleja parte de gestión, crearé otra tabla, llamada `**KOD**`. Esta tabla consta de las siguientes columnas:

  

| Nombre de columna | Descripción |
| --- | --- |
| `Id` | Clave principal para esta tabla |
| `kot_menu_item_id` | Significa el elemento KOT en el que el personal de cocina está trabajando actualmente. |
| `staff_id` | Almacena el ID del cocinero que está preparando el artículo. |
| `kod_status_id` | Muestra el estado actual del artículo. |

  
  

### Gestión de menú

Este componente es tan importante como la gestión de KOT y KOD. La carta –tanto en su presentación visual como en los platos que ofrece– es una de las primeras cosas que atrae a los clientes. Por eso, todo restaurador intenta que su menú sea lo más atractivo posible.

![https://www.vertabelo.com/blog/serving-delicious-food-and-data-a-data-model-for-restaurants/menu-management.png](https://www.vertabelo.com/blog/serving-delicious-food-and-data-a-data-model-for-restaurants/menu-management.png)

Creemos otra tabla para contener los detalles del menú. Agregaré columnas para todos los detalles que normalmente vemos en un menú:

  

| Nombre de columna | Descripción |
| --- | --- |
| `Id` | La clave principal de la tabla. |
| `Item_name` | Un nombre corto para un elemento del menú. |
| `Item_category_id` | Indica la categoría de cocina del artículo: italiana, continental, etc. |
| `Item_desc` | Contiene detalles del artículo, como una lista de ingredientes o cómo se prepara el artículo (al horno, al vapor, etc.) |
| `Item_image` | Una imagen llamativa del artículo. |
| `cost` | El costo del artículo. |

  
  

### Resolver problemas de restaurantes del mundo real con datos

Algunos problemas son extremadamente comunes en el mundo del servicio de alimentos. En concreto pienso en largas esperas, tanto para sentarte en una mesa como para conseguir tu comida. Estos problemas a menudo pueden resolverse, al menos parcialmente, organizando y utilizando mejor los datos de los restaurantes.

En un ambiente de cena, pocas cosas son más molestas para los clientes que tener que esperar mucho tiempo por una mesa. Minimizar los tiempos de espera de los clientes durante las horas pico requiere vigilar de cerca el estado de las mesas individuales. Si no hay una gestión adecuada de las mesas y del personal, los tiempos de espera de los clientes empiezan a crecer. Si los tiempos de espera son demasiado largos, los clientes pueden irse y buscar otro restaurante que les atienda rápidamente.

Se puede abordar esta preocupación introduciendo ciertos cambios en este modelo de datos. Estos cambios:

1. Agregue administración de mesas en tiempo real, una forma digitalizada de administrar la disponibilidad de las mesas, el seguimiento del estado y las tasas de utilización.
2. Reduzca el tiempo de respuesta de las mesas midiendo la eficiencia del personal y permitiendo una planificación eficaz de la fuerza laboral, por ejemplo, reuniendo un equipo de limpieza y asignando personal a una mesa o un grupo de mesas.
3. Publique el estado en tiempo real de tablas individuales en las pantallas de los administradores, para que puedan vigilar cualquier actividad pendiente desde hace mucho tiempo.

![https://www.vertabelo.com/blog/serving-delicious-food-and-data-a-data-model-for-restaurants/dine-in-table-management.png](https://www.vertabelo.com/blog/serving-delicious-food-and-data-a-data-model-for-restaurants/dine-in-table-management.png)

Otro problema es hacer que los clientes esperen por su comida. Tanto para los clientes que comen en el restaurante como para los que comen comida para llevar, esto se puede ayudar proporcionando actualizaciones de estado directamente al comensal. Aquí es vital monitorear el estado de los KOT individuales. A medida que el KOT avanza en la cocina, su estado se actualiza en la `**KOT**`tabla. Este mecanismo brinda una actualización en tiempo real a los clientes sobre el estado de sus pedidos.

![https://www.vertabelo.com/blog/serving-delicious-food-and-data-a-data-model-for-restaurants/kot-status.png](https://www.vertabelo.com/blog/serving-delicious-food-and-data-a-data-model-for-restaurants/kot-status.png)

### PArticularidades al Implementar microservicios