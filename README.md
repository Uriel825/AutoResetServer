# AutoResetServer
Esta script permite que mi servidor se auto resetee cuando detecta que esta caido 

El funcionamiento es sencillo, la script envia un ping a la instancia seleccionada, cuando la instancia responde con un 0 el servidor esta arriba

Si la respuesta es diferente la script interpreta que el servidor esta caido e inicia el proceso de reinicio, en este caso decidi que era mejor parar la instancia
y volverla a iniciar, por que existe una funcion que en teoria reinicia la instnacia pero en mis pruebas de concepto no vi ningun cambio.

Notas:

Cada vez que se reinicia la instancia toma una nueva ip, entonces la script tambien siempre esta tomando refrescando la ip que tiene la instancia 

Se realiza el proceso de comprabacion cada minuto 

Para la configuracion, se necesita el paquete AWS Cli
