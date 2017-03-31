Universidad Simon Bolivar
CI-5438 - Inteligencia Artificial
    Edward Fernandez 10-11121
    Carlos Ferreira 11-10323
    Stefani Castellanos 11-11394

    Para poder ejecutar el proyecto se necesitan de las siguientes librerias:

pygame:

    sudo apt-get install python-pygame

pyevolve:

    sudo apt-get install python-pyevolve

    Para correr el algoritmo evolutivo se ejecuta el archivo genetic

    python genetic.py

    Si se quiere empezar el entrenamiento desde el comienzo se debe
    eliminar el archivo population.txt para que inicialice la primera
    población de manera aleatoria.
    Si se quiere seguir desde un punto anterior la población se guarda
    automáticamente en el archivo population.txt cada 5 generaciones,
    y se puede continuar su corrida desde la última iteración guardada  .

    Para que la AI utilice el resultado con el mejor fitness se busca el
    individuo con mejor fitness en population.txt (última línea) y
    se coloca en tetris.py, en la linea 331, donde se encuentra
    app.ai = AI(app)
por
    app.ai = AI(<mejor individuo>)

y se ejecuta el archivo tetris.py

    python tetris.py

    Al jugar el tetris se puede bajar la velocidad con la que bajan las piezas
cambiando el atributo de app.ai.instant_play de True a False. Esto no es
recomendable a la hora de hacer el entrenamiento.
