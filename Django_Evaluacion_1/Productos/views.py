from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "templateAPP2/index.html")

def computadores(request):
    data = {"nombre" : "Computadores", "foto1":"pc1.jpg", "foto2":"pc2.jpg", "foto3":"pc3.jpg", "producto1":"Notebook HP Gamer Victus 16-D0500LA", "producto2":"All in One Dell Optiplex 5480 AiO", "producto3":"Dell OptiPlex 7050 Tiny"}
    return render(request, "templateAPP2/producto.html", data)

def camaras(request):
    data2 = {"nombre" : "Camaras", "foto1":"camara1.jpg", "foto2":"camara2.jpg", "foto3":"camara3.jpg", "producto1":"Canon EOS 3000D", "producto2":"Insta360 X3", "producto3":"Drone Semiprofesional DJI Mini 3 Pro"}
    return render(request, "templateAPP2/producto2.html", data2)

def telefonos(request):
    data3 = {"nombre" : "Telefonos", "foto1":"celular1.jpg", "foto2":"celular2.jpg", "foto3":"celular3.jpg", "producto1":"Celular Smartphone Oppo A78 5G", "producto2":"Samsung Galaxy Z Flip 5", "producto3":"iPhone 13 Pro Max 128 GB"}
    return render(request, "templateAPP2/producto3.html", data3)

def user(request):
    user_data = {"username": "FelipeAE", "nombre":"Felipe Alvarez" , "email": "felipe.alvarez90@inacapmail.cl", "rut": "19478868-1"}
    return render(request, "templateAPP2/user.html", user_data)

def descripcion_producto(request, producto_id):
    if producto_id == 1:
        producto = {"nombre": "Notebook HP Gamer Victus 16-D0500LA", "descripcion": "Alimentada por la nueva generación de gráficos NVIDIA GeForce RTX y procesador Intel Core, el notebook gaming Victus tiene todo lo que necesitas para jugar y gestionar tus tareas diarias respetando el medio ambiente gracias a los materiales reciclados que integra. Mantén la temperatura ideal en cada juego con el sistema de refrigeración mejorado y lleva tu experiencia de juego más allá gracias a OMEN Gaming Hub.", "precio": "$819.990", "foto": "pc1.jpg"}
    elif producto_id == 2:
        producto = {"nombre": "All in One Dell Optiplex 5480 AiO", "descripcion": "Potencia y productividad, Una todo en uno de 24” inteligente y de diseño sustentable que ofrece seguridad y productividad mejoradas en un diseño que ahorra espacio. Con procesadores Intel® de 10.ª generación.", "precio": "$539.990", "foto": "pc2.jpg"}
    elif producto_id == 3:
        producto = {"nombre": "Dell OptiPlex 7050 Tiny", "descripcion": "Tamaño micro. Máximo rendimiento, La computadora de escritorio micro pequeña con tecnología Intel vPro ofrece rendimiento de escritorio de tamaño completo y cuenta con opciones de montaje versátil.", "precio": "$189.990", "foto": "pc3.jpg"}
    elif producto_id == 4:
        producto = {"nombre": "Canon EOS 3000D", "descripcion": "Con la función Wi-Fi incorporada de EOS 3000D, los usuarios pueden disfrutar de disparos remotos de Live View desde teléfonos inteligentes a través de la aplicación Camera Connect, lo que hace que sea más conveniente tomar autorretratos o fotos grupales, o explorar más creatividad disparando desde alto o ángulos bajos La conectividad inalámbrica también facilita la fácil navegación y descarga de fotos en teléfonos inteligentes, así como el intercambio en sitios de redes sociales como Facebook, Instagram o YouTube, cumpliendo con los hábitos de disparo y uso compartido de los usuarios de hoy.", "precio": "$403.990", "foto": "camara1.jpg"}
    elif producto_id == 5:
        producto = {"nombre": "Insta360 X3", "descripcion": "FOTOGRAFÍAS 360 DE 72 MEGAPÍXELES y un sensor más grande de 1/2, La mayor cantidad de megapíxeles jamás vista en una cámara de acción 360. El nuevo sensor de 1/2 de X3 capta la acción en vívido 5.7K 360. Captura fotos 360 con más detalle que nunca a 72 MP.", "precio": "$579.990", "foto": "camara2.jpg"}
    elif producto_id == 6:
        producto = {"nombre": "Drone Semiprofesional DJI Mini 3 Pro", "descripcion": "Con evasión de obstáculos, una cámara capaz de tomar fotografías RAW de 48 MP y un cardán giratorio vertical, DJI Mini 3 Pro redefine lo que significa volar Mini. Ah, y sí, todavía pesa menos de 249 g", "precio": "$939.990", "foto": "camara3.jpg"}
    elif producto_id == 7:
        producto = {"nombre": "Celular Smartphone Oppo A78 5G", "descripcion": "Diseñamos productos espectaculares que llaman la atención y deleitan al usuario. El proceso único de OPPO crea colores resplandecientes y fuera de este mundo.", "precio": "$219.990", "foto": "celular1.jpg"}
    elif producto_id == 8:
        producto = {"nombre": "Samsung Galaxy Z Flip 5", "descripcion": "    Ventana flexible de 3,4.Talla única para todos los bolsillos,Conoce la pantalla Flex Window de3,4 pulgadas diseñada para expresarte. Con una bisagra Flex Hinge rediseñada,Galaxy Z Flip5 ahora se pliega firmemente para deslizarse tan fácilmente en tu bolsillo como en tus manos.", "precio": "$1.008.990", "foto": "celular2.jpg"}
    elif producto_id == 9:
        producto = {"nombre": "iPhone 13 Pro Max 128 GB", "descripcion": "Muy muy Pro, un sistema de cámaras mucho más poderoso. Una pantalla con respuesta inmediata en cada interacción. Una pantalla Super Retina XDR con ProMotion que ofrece una experiencia rápida y fluida. Un gran avance en el sistema de cámaras que te brinda posibilidades increíbles. Un diseño con una resistencia excepcional. Chip A15 Bionic ultrarrápido. Y una extraordinaria duración de la batería. Saca tu lado Pro. Un diseño espectacular con acero inoxidable de calidad quirúrgica, Ceramic Shield y resistencia al agua IP68, líder en la industria. Un hardware de última generación y un software superinteligente se combinan para traer fotografía macro en la cámara ultra gran angular, zoom óptico de 3x en la cámara teleobjetivo y modo Noche en todas las cámaras. La fotografía macro le da un tono épico a cada pequeño detalle, captura hasta 2,2 veces más la luz para lograr mejores fotos y videos.", "precio": "$1.199.990", "foto": "celular3.jpg"}
    return render(request, "templateAPP2/descripcion.html", producto)


