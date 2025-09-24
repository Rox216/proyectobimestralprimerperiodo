import flet as ft


def main(page: ft.Page):
    page.title="Galeria"
    page.bgcolor=ft.Colors.BLACK38

    sobrevivientes = [
        {
            "nombre": "NOOB",
            "tipo": "sobreviviente",
            "habilidades": "cola bloxy,pocion piel de hierro,hamburguesa fnatasma",
            "historia": "se dice que alguna vez fue un Robloxiano extrovertido y alegre, aunque no tenía muchos amigos. El Invitado 666 era uno de sus compañeros más cercanos, pero tras una prueba no revelada, se separaron, dejando a Noob más callado y retraído",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/probicional-en-lo-que-pasan-sus-correos/refs/heads/main/noob.jpg", 
        },  
        { 
            "nombre": "007n7",
            "tipo": "sobreviviente",
            "habilidades": "DEX,Clon,c00lgui,inyectar",
            "historia": "007n7 era un hacker y explotador retirado, conocido por causar estragos en Roblox. Un día, 007n7 encontró a un bebé píldora en su puerta, c00lkidd , a quien acogió, retirándose del hacking para convertirse en una figura paterna.",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/probicional-en-lo-que-pasan-sus-correos/refs/heads/main/burguer.jpg",  
        },
        {
            "nombre": "Dusekkar",
            "tipo": "soporte",
            "habilidades": "levitation,spawn protection,plasma beam,",
            "historia": "El verdadero nombre de Dusekkar es Matthew Dusekkar, como se revela en un diálogo de Shedletsky,Se da a entender vagamente que Dusekkar era amigo cercano de Shedletsky , dado que es el único que se refiere a él como Matt. Como lo revela el render completo de Milestone II (normalmente no visible en el juego), los dos fueron emboscados por 1x1x1x1 , que logró matar a Shedletsky",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/probicional-en-lo-que-pasan-sus-correos/refs/heads/main/calabaza.jpg", 
        },  
        {
            "nombre": "taph",
            "tipo": "soporte",
            "habilidades": "tripwire,subspace tripmin,",
            "historia": "Antes de ser abandonado, Taph era un justiciero demoledor que servía a los administradores de Roblox, especialmente a Builderman , destruyendo experiencias sin moderación. Aunque nunca fue empleado oficialmente de Roblox, Taph creía que Builderman los consideraba su segundo al mando.",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/probicional-en-lo-que-pasan-sus-correos/refs/heads/main/cultista.jpg", 
        },
        {
            "nombre": "two time",
            "tipo": "sentinel",
            "habilidades": "oblation,sacrifical dagger,crouch,ritual",
            "historia": "Two Time fue miembro del Culto Spawn , un grupo dedicado a la creencia en la reaparición y la resurrección, junto con Azure . Ambos eran compañeros cercanos, y a menudo aparecen juntos en varias representaciones (incluyendo Milestones I y II y Chrisaken), así como en una fotografía tomada antes de la muerte de Azure . ",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/probicional-en-lo-que-pasan-sus-correos/refs/heads/main/el%20pelos.jpg", 
        },
        {
            "nombre": "Guest 1337",
            "tipo": "sentinel",
            "habilidades": "made to last,block,charge,punch,",
            "historia": "El Invitado 1337 llevaba una vida normal hasta que sus padres fueron asesinados por el General Bacon . Tras su muerte, fue enviado a un orfanato, donde conoció a sus amigos de la infancia, Daisy y Matt . Diez años después, tras casarse con Daisy y tener un hijo, el Invitado 1337 descubrió trágicamente que era el último Invitado que quedaba. Decidido, se unió al Ejército de Roblox junto a Matt.",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/probicional-en-lo-que-pasan-sus-correos/refs/heads/main/guest.jpg", 
        },
        {
            "nombre": "chance",
            "tipo": "sentinel",
            "habilidades": "unpredictable fate,coin flip,one shot,reroll,hat fix",
            "historia": "Chance mantuvo una buena relación con la familia mafiosa Sonnelino y frecuentaba su casino. Sin embargo, tras ganar un juego amañado y robarles el premio, su relación con la familia se deterioró, dejándolo endeudado y prófugo.",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/probicional-en-lo-que-pasan-sus-correos/refs/heads/main/lentes.jpg", 
        },
        {
            "nombre": "eliot",
            "tipo": "soporte",
            "habilidades": "orden up¡,deliverers resolve,pizza throw,ruhs hour",
            "historia": "Elliot era el mejor empleado de Builder Brothers Pizza la pizzería de  Trabaja en una Pizzería , habiendo trabajado prácticamente en todos los puestos. Tuvo que soportar los estragos que c00lkidd causó en el restaurante. ",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/probicional-en-lo-que-pasan-sus-correos/refs/heads/main/pizza.jpg", 
        },    
        {
            "nombre": "builderman",
            "tipo": "soporte",
            "habilidades": "sentry construction,dispenser construction",
            "historia": "Builderman y todos los demás administradores de Roblox son considerados corruptos por Doombringer . Como se observa enel render de Doombringer , Builderman y Shedletsky estaban atrapados en jaulas. También fue él quien baneó al Invitado 666 , aunqueeste lo desconoce",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/probicional-en-lo-que-pasan-sus-correos/refs/heads/main/original.jpg", 
        },   
        {
            "nombre": "shedlesky",
            "tipo": "setinel",
            "habilidades": "slash,fried chicken",
            "historia": "Shedletsky es conocido por ser el portador de las siete espadas SFOTH , el creador del concurso de comer pollos y también amigo de Builderman . Su mayor enemigo, 1x1x1x1 , lo odia porqueesla personificación del odio de Shedletsky.",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/probicional-en-lo-que-pasan-sus-correos/refs/heads/main/pollo.jpg",
        },
    ]

    indice_actual=[0]

    contenedor=ft.Container(
        content=ft.Column([]),
        width=500,
        height=580,
        bgcolor=ft.Colors.BLUE_300,
        alignment=ft.alignment.center,
        padding=30
    )

    boton_siguiente = ft.ElevatedButton(text="Siguiente sobreviviente")

    def mostrar_sobreviviente():
        sobreviviente=sobrevivientes[indice_actual[0]]
        contenedor.content=ft.Column([
            ft.Image(src=sobreviviente["imagen"],width=300,height=300,fit=ft.ImageFit.CONTAIN),
            ft.Text(sobreviviente["nombre"],size=20,weight=ft.FontWeight.BOLD),
            ft.Text(f"Tipo: {sobreviviente ['tipo']}",size=16),
            ft.Text(f"Habilidades: {sobreviviente['habilidades']}",size=16),
            ft.Text(f"Historia: {sobreviviente ["historia"]}",size=14,italic=True)
        ],alignment=ft.MainAxisAlignment.CENTER)
        
        if indice_actual[0]==len(sobreviviente)-1:
            boton_siguiente.text="Volver al inicio"
        else:
            boton_siguiente.text="Siguiente sobreviviente"
        page.update()

    def siguiente_click(e):
        indice_actual[0]=(indice_actual[0]+1)%len(sobrevivientes)
        mostrar_sobreviviente()
    boton_siguiente.on_click=siguiente_click



    page.add(
        ft.Container(
            content=ft.Column([
                contenedor,
                boton_siguiente
            ],alignment=ft.MainAxisAlignment.CENTER,
              horizontal_alignment=ft.CrossAxisAlignment.CENTER,
              spacing=20
        ),

            alignment=ft.alignment.center,
            expand=True
        )
    )
    mostrar_sobreviviente()


ft.app(main)
