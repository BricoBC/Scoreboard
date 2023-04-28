# Scoreboard
El algoritmo Scoreboard es un método de ejecución de instrucciones en un procesador que permite una ejecución fuera de orden (out-of-order) y una gestión eficiente de los recursos del procesador. Fue desarrollado a principios de los años 60 por IBM para el procesador IBM System/360.

El algoritmo Scoreboard utiliza una tabla (o scoreboard) para controlar el estado de las instrucciones y los recursos del procesador. La tabla contiene información sobre los recursos utilizados por cada instrucción y su estado de ejecución (por ejemplo, si ha sido emitida, si está en espera, si ha terminado, etc.). Cada instrucción se emite en la tabla y se sigue su progreso a medida que se ejecuta.

El algoritmo Scoreboard utiliza técnicas de ejecución especulativa para optimizar el rendimiento del procesador. Esto significa que el procesador puede ejecutar instrucciones en un orden diferente al que aparecen en el programa, siempre y cuando no haya dependencias entre ellas. De esta manera, el procesador puede aprovechar los recursos disponibles y evitar retrasos innecesarios.

El algoritmo Scoreboard también permite el uso de recursos compartidos, como registros o unidades funcionales, de manera eficiente. La tabla scoreboard se encarga de coordinar el uso de estos recursos y garantizar que no haya conflictos.

En general, el algoritmo Scoreboard es una técnica de ejecución de instrucciones avanzada que permite un procesamiento fuera de orden eficiente y el uso eficiente de los recursos del procesador. Aunque ha sido superado por técnicas más modernas, sigue siendo una técnica valiosa para la implementación de procesadores de alto rendimiento..
![](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.slideserve.com%2Fdelilah-contreras%2Fescala-o-din-mica-algor-tmo-de-tomasulo&psig=AOvVaw0RQ8a6tv1f7ZFXV3RZU-lI&ust=1678320576129000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCPC9_b-Fy_0CFQAAAAAdAAAAABAJ)


Se utilizara un entorno virtual, las versiones de los paquetes usados se encuentran en el archivo paquetes.txt.