# The Dating Sim Engine was written by PyTom, 
# with updates added by Andrea Landaker (qirien),
# and contributions by Edmund Wilfong (Pneumonica)
#
# For support, see the Lemma Soft forums thread:
# http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=31571
#
# It is released under the MIT License - see DSE-LICENSE.txt
#
#
# This is the main part of the program, where you setup your schedule and
# the options for the user. You can change the stats, periods, and choices
# here; just make sure they match up with the events setup in
# dse-events.rpy.  You can even have different time periods (months, instead
# of times of day, for example).

###########################################################################

# Set up a default schedule.
   
# Characters define here
define pj = Character("[pjname]", color="#30b6ea")
define laura = Character("Laura", color="#ea308e")
# Characters Images define here
image Laura Normal Close = im.Scale("LaurenCasualCloseNormal.png", 302, 640)
image Laura Normal Close Eyes = im.Scale("LaurenCasualCloseEyes.png", 302, 640)
image Laura Angry Close = im.Scale("LaurenCasualCloseAngry.png", 302, 640) 
image Laura Normal Stand = im.Scale("LaurenCasualStandNormal.png", 302, 640)


# Background Images define here
image bg space = im.Scale("backgrounds/space.jpg",1066, 600)
image bg sky = "backgrounds/sky.jpg"
image bg_bedroom = im.Scale("backgrounds/bedroom.jpg", 1066, 600)

#############################################################################

init python:
    
    register_stat("Energia", "energy", 100, 100)
    register_stat("Fuerza", "strength", 0, 100)
    register_stat("Inteligencia", "intelligence", 0, 100)    
    register_stat("Carisma", "charm", 0, 100)
    register_stat("Felicidad", "happyness", 0, 100)
    # register_stat("Felicidad1", "happyness1", 0, 100)
    # register_stat("Felicidad2", "happyness2", 0, 100)
    # register_stat("Felicidad3", "happyness3", 0, 100)
    # register_stat("Felicidad4", "happyness4", 0, 100)
    # register_stat("Felicidad5", "happyness5", 0, 100)
    # register_stat("Felicidad6", "happyness6", 0, 100)
    # register_stat("Felicidad7", "happyness7", 0, 100)
    # register_stat("Felicidad8", "happyness8", 0, 100)
    # register_stat("Felicidad9", "happyness9", 0, 100)
    # register_stat("Felicidad11", "happyness11", 0, 100)
    # register_stat("Felicidad12", "happyness12", 0, 100)
    # register_stat("Felicidad13", "happyness13", 0, 100)
    # register_stat("Felicidad14", "happyness14", 0, 100)

    register_stat("Relaxation", "relaxation", hidden=True)

    dp_period("Mañana", "morning_act")
    dp_choice("Ir a clases", "class")
    dp_choice("Faltar a clases", "cut")
    
    # This is an example of an event that should only show up under special circumstances
    dp_choice("Fly to the Moon", "fly", show="strength >= 100 and intelligence >= 100")

    dp_period("Tarde", "afternoon_act")
    dp_choice("Estudiar", "study")
    dp_choice("Salir a pasear", "hang")

    dp_period("Anochecer", "evening_act")
    dp_choice("Hacer Ejercicio", "exercise")
    dp_choice("Jugar videojuegos", "play")


    
# This is the entry point into the game.
label start:

    # Initialize the default values of some of the variables used in
    # the game.
    $ day = 0

    # Show a default background.
    scene bg space

    # The script here is run before any event.
    "Es el año 2023"
    "La sonda New Horizons III ha entrado en contacto con Proxima B, en el Sistema Alpha di Centauri, un planeta en la zona habitable, tal como nuestra Tierra"
    "Entonces ha ocurrido lo poco probable, la sonda detecto emisiones de carbono, eso significa una cosa... Vida. Muchas vidas de hecho"
    "Se formó un comitté de urgencia de Naciones Unidas, esto excedia a cualquier pais"
    "El 12 de Octubre del 2023 anunciaron la noticia al mundo, no estabamos solos en el universo... Esto fue solo el pre-ambulo, tambien se anunciaron un paquete de medidas"
    "Paquete de medidas que revolucionaron la sociedad mundial"
    "Y aqui es donde comienza mi historia, la historia de probablemente el tipo mas común del planeta."
    
    scene bg sky
    with fade
    
    "Los primeros rayos del sol anuncian la primavera, estación que vibra en consonancia con mi entrada en la madurez"    
    
    python:
        pjname = renpy.input("Antes que nada me presento, mi nombre es")
        pjname = pjname.strip()

        if not pjname:
            renpy.input("{i}Ya que no elegiste nombre, yo te bautizo como el santo evangelio: {/i} {color=#30b6ea}Juan{/color}")
            pjname = "Juan"

    menu:
        "y me caracterizo por ser una persona:"

        "Fuerte. (+20 de Fuerza)":
            "Siento el espiritu de Hercules el dios de la fuerza fluir por mi cuerpo"
            $ strength +=20
        "Inteligente. (+20 de Inteligencia)":
            "Siento el espiritu de Ceo el dios de la Inteligencia fluir por mi cuerpo"
            $ intelligence +=20
        "Carismática. (+20 de Carisma)":
            "Siento el espiritu de Apolo el dios de la Belleza y Carisma fluir por mi cuerpo"
            $ charm +=20

    pj "Tengo la sensación que hoy será un dia especial, aunque no tengo como argumentarlo, quizás es solo el buen clima quien me carga de tanto optimismo"
    pj "el parque esta bastante cerca, es ahí hacia donde me dirijo"     
    
    show Laura Normal Close
    with fade
    laura "Pst! ... hey, [pjname] ... acaso soy transparente?"
    show Laura Normal Close Eyes
    "Esta blonda pesadilla de voz estridente es Laura, nos conocemos desde niños"
    show Laura Normal Close  
    "Su belleza es directamente proporcional a su capacidad de irritar al objetivo durante una conversación ..."    
    "basicamente lo que trato de decir es que innegablemente bella, asi como molesta ..."    
    "10 años de conocerla hacen que te quedes con lo último"        
    pj "Aqui se termina mi suerte ..."    
    pj "¿Puedo saber por que alteras mi paz, esbirro del infierno?"    
    "Olvide agregar que su sentido del humor es practicamente inexistente"
    
    
    


    # We jump to day to start the first day.
    jump day


# This is the label that is jumped to at the start of a day.
label day:
    scene bg_bedroom
    # Increment the day it is.
    $ day += 1

    # We may also want to compute the name for the day here, but
    # right now we don't bother.

    "Hoy es el día %(day)d."

    # Here, we want to set up some of the default values for the
    # day planner. In a more complicated game, we would probably
    # want to add and remove choices from the dp_ variables
    # (especially dp_period_acts) to reflect the choices the
    # user has available.

    $ morning_act = None
    $ afternoon_act = None
    $ evening_act = None
    $ narrator("Un dia más...¿Qué debería hacer Hoy?", interact=False)
    window show
    

    # Now, we call the day planner, which may set the act variables
    # to new values. We call it with a list of periods that we want
    # to compute the values for.
    call screen day_planner(["Mañana", "Tarde", "Anochecer"])
    window auto
    
    # We process each of the three periods of the day, in turn.
label morning:

    # Tell the user what period it is.
    centered "Mañana"

    # Set these variables to appropriate values, so they can be
    # picked up by the expression in the various events defined below. 
    $ period = "morning"
    $ act = morning_act
    
    # Execute the events for the morning.
    call events_run_period

    # That's it for the morning, so we fall through to the
    # afternoon.

label afternoon:

    # It's possible that we will be skipping the afternoon, if one
    # of the events in the morning jumped to skip_next_period. If
    # so, we should skip the afternoon.
    if check_skip_period():
        jump evening

    # The rest of this is the same as for the morning.

    centered "Tarde"

    $ period = "afternoon"
    $ act = afternoon_act

    call events_run_period


label evening:
    
    # The evening is the same as the afternoon.
    if check_skip_period():
        jump night

    centered "Anochecer"

    $ period = "evening"
    $ act = evening_act
    
    call events_run_period


label night:

    # This is now the end of the day, and not a period in which
    # events can be run. We put some boilerplate end-of-day text
    # in here.

    centered "Noche"

    "Se hizo muy tarde, creo que iré a dormir."

    # We call events_end_day to let it know that the day is done.
    call events_end_day

    # And we jump back to day to start the next day. This goes
    # on forever, until an event ends the game.
    jump day
         

