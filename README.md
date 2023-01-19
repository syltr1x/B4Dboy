# B4Dboy

## Installation
```
git clone https://www.github.com/r4yx/b4dboy
cd b4dboy
pip3 install -r requirements.txt
```
## Configure path before start
```
python3 main.py -c /root/
```
or
```
B4Dboy > config -p=/home/us3r/work_dir/
```


## B4Dboy guide of usage

### Language/Lenguaje : Spanish/Español
[Info] se señalara con * los parametros obligatorios.
## Generate command : Usar para generar la puerta trasera
* -os : sirve para especificar el sistema operativo de la victima. b4dboy crea puertas traseras tanto para windows como para linux.
-lip : sirve para especificar la ip del atacante. En caso de no usarse se obtendra automaticamente
-t : el modo simple permite conexiones entre la victima y el atacante en LAN, si se configura un token y se selecciona el modo global puede acceder al sistema victima desde cualquier parte del mundo. (default : simple)
-T : define si iniciar la escucha justo despues de ejecutar o almacenar la sesion. La maquina victima intentara conectarse al puerto asignado cada 5 minutos en caso de almacenar la sesion

[Info] tenga en cuenta que este comando usa dos configuraciones : "packages" que se encarga de escanear x paquetes durante con el fin de obtener la IP victima que creara una peticion HTTP a la maquina atacante ejecutando la carga útil. "token" si bien el token no es obligatorio para su uso, si es necesario configurarlo en caso de querer crear conexiones fuera de la red local de la victima.

## Payload command : Usar para crear cargas útiles ejecutables una vez iniciada la reverse shell en la maquina victima
-ip : crea una carga útil que obtiene la ip publica y datos de geolocalizacion de la maquina victima que puede usar para añadir informacion a el registro de sus sesiones
-os : obtiene informacion de la maquina victima como : nombre del dispositivo y usuario.

[Info] este comando soporta un solo parametro de uso.

## Log command : Usar para modificar o remover sessiones, o eliminar todas del registro.
-m/--mod : modifica valores especificos del registro de una sesion. Ej : log -m:<id> port=443
-r/--remove : elimina una sesion del registro. Ej : log --remove=<id>
-c/--clean : elimina todas las sesiones.
-g/--geo : crea un registro de geolocalizacion. Modo de uso :log -g:<id> -ip=<public ip>
-gm/--geo-mod : modifica un registro de geolocalizacion. Modo de uso: log -gm=<id> -ip=

[Info] Lista de valores a modificar : os="sistema operativo", ip="ip LAN", port="puerto de conexion con la maquina atacante", system="sistena operativo en detalle", pubip="ip publica". Los ultimos dos se agregan de forma manual obteniendo la informacion mediante el uso de payloads

## Start command : Use para iniciar la escucha de una determinada sesion o de un determinado puerto
-s/--session : seleccione la sesion que quiere iniciar. Modo de uso :start -s:<id>
-l/--listen : ingrese manualmente un puerto al cual permanecer en escucha. Modo de uso :start -l=443

## Show command : Muesta el registro tanto de sesiones almacenadas como su informacion geografica
-s/--sessions : muesta todas las sesiones almacenadas
-g/--geo : muestra la informacion geografica de todas las sesiones que la posean
-c/--config : muestra la configuracion de ejecucion

## Config command : Usar para configurar parametros de ejecucion en los comandos
* -i/--interface : configura la interfaz de red para los escaneos de peticiones que obtienen la ip de la victima
-p/--packages : configura la cantidad de paquetes maxima durante el escaneo. Recomendamos aumentar a 20 si esta realizando muchas peticiones desde su ip, ¡TENGA EN CUENTA QUE AUMENTAR EL NUMERO DE PAQUETES AUMENTARA LA DEMORA DE EJECUCION! (default : 15)
-t/--token : en caso de tener un token de ngrok puede configurarlo. Modo de uso :config -t=<token>
-d/--dictionary : modifique el diccionario que se usa para generar las id de sesiones
--path : modifique la ubicacion de b4dboy. Modo de uso :config --path=/home/us3r/tools/

[Info] Por mas que se aconseja la modificacion de ciertos parametros para un uso mas comodo y practico, asegurese de saber lo q hace antes de configurar.
