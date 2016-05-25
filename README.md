# Fundamentos de los Sistemas Inteligentes

##La heuristica

Para realizar la implementación de la heurística hemos creado las clases
VerticalHeuristic, HorizontalHeuristic, UpwardHeuristic,
DownwardHeuristic.

Estas clases representan un escaneo completo del tablero para el estado acutal.

Básicamente el escaneo consiste en mirar por columnas, (vertical y diagonales) o filas, (horizontal).
Descartando las casillas vacías, buscando el numero de ocurrencias de "X" o "O" (ocurrences_of()), y comprobando
los laterales de dicha ocurrencia (connection_breaks()), para asignar un valor a cada caso posible y para cada
valor de la ocurrencia.

Ej: para ocurrencia = 3 , los valores para los escaneos de las X serían:

           Vertical  Horizontal  Diagonales
           
XXX   ->      700       800         900

XXXO  ->      350       400         450

OXXX  ->       0        400         450

OXXXO ->       0         0           0


En el directorio /test se encuentran las clases de test unitarios para cada clase, que representan un buen numero
de posibles estados y valores.

##Dificultad

Se ha añadido 3 niveles de dificultad:

* Nivel fácil, profundidad dela busqueda es = 2;
* Nivel normal, profundidad dela busqueda es = 3;
* Nivel difícil, profundidad dela busqueda es = 4;

Seleccionables al iniciar el juego.

##Jugador inicial

Se ha rediseñado el concepto de player para poder empezar como "O" nosotros y no como "X".


##Memoization

Se ha utilizado la técnica de optimización memoization para mejorar el rendimiento de la heuriscitca, que
consiste en guardar en un diccionario la clave y valor de la heuristica para cada estado, de esta forma,
aprovechar las heuristicas ya calculadas para estados iguales.









