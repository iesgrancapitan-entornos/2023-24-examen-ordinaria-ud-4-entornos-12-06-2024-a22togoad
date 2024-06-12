# Examen Tema 4 Entornos de Desarrollo - 1DAW

***Refactorización, Documentación y control de versiones***

El examen se divide en 3 bloques claramente diferenciados: Refactorización, Documentación y control de versiones. Cada uno de ellos con una puntuación sobre 10. **Para dar por superado el RA relacionado con el tema 4, se deben aprobar las 3 partes**.

En cada apartado se indica la puntuación y que parte corresponden. Las 3 se puntúan sobre 10

Sigue detalladamente las instrucciones del examen. Cualquier duda, pregunta a tu profesor.

1. En el repositorio tienes en código fuente que será la base sobre la cual desarrollaremos el examen. Dividiremos el examen en 3 partes, y las utilizaremos para desarrollar las versiones de git y github. Evidentemente, usaremos las buenas prácticas de git y github que hemos estado trabajando durante el curso

### Ramas y Merge I

1. Para el workflow del examen, utilizaremos las siguientes ramas: desarrollo, refactorización, documentación. Créalas cuando se te indique.

2. Crea la rama "desarrollo"

## Refactorización

3. Crea la rama "refactorizacion" a partir de la rama desarrollo y cambiate a esa rama ***(CV - 0.125 puntos)***

4. Haz las refactorizaciones que necesites para que "Guau" sea un campo de la clase Perro llamado "ladra". ***(RF - 4 puntos)***
   
5. Compromete el estado actual con el mensaje "Refactorizacion 1 Perro - Nombre y Apellidos" ***(CV - 0.25 puntos)***

6. Extrae una superclase a partir de la clase "Coche" llamada "Vehículo" con los campos:

   1. num_serie
   2. fabricante
   3. color

7. Compromete el estado actual con el mensaje "Refactorizacion 2 Superclase Vehículo - Nombre y Apellidos". ***(RF - 6 puntos)***

8. Fusiona la rama "refactorizacion" en la rama "desarrollo" ***(CV - 0.25 puntos)***

## Documentación

9. Crea la rama "documentacion" a partir de la rama desarrollo y cambiate a esa rama ***(CV - 0.25 puntos)***

10. Documenta con el formato Docstring "reStructuredText" las clases y los métodos para que aparezcan sus descripciones, autor, descripción de los parámetros y devoluciones de cada método. Compromete el estado actual con el mensaje "Documentación 1 - Nombre y Apellidos" ***(DOC - 2.5 puntos)***

11. Añade todos los rst necesarios para que aparezca la documentación de todos las clases ***(DOC - 1 punto)***

12. Añade en el index un rst para que haya un enlace donde aparezca el enunciado completo del examen ***(DOC - 1 punto)***

13. Añade en la documentación: ***(DOC - 3 puntos)***
    1. Autor: Tu nombre y apellidos
    2. Nombre del proyecto "Examen Entornos"
    3. Versión: una versión con notación ***"versionado semántico"***
    4. copyright: El que tu quieras
    5. Añade las extensiones "autodoc, intersphinx, todo, mathjax, napoleon, autosummary
    6. Usa el tema "sphinx_rtd_theme"

14. Genera la documentación html usando la generación de documentación sphinx y guárdalo en tu repositorio en una carpeta que se llame "doc". Compromete el estado actual con el mensaje "Documentación 2 Sphinx - Nombre y Apellidos" ***(DOC - 2.5 puntos)***

## Control de Versiones

### Pull Request

15. Abre un pull request llamado "añadir sphinx" para añadir los cambios de la rama "documentación" en la rama "desarrollo" ***(CV - 0.25 puntos)***

16. Realiza lo siguiente en el pull request:  ***(CV - 1 punto)***

        1. Añade a tu profesor como Reviewers
        2. Asignate el pull request
        3. Aplica al pull request el label documentation
        4. Crea el milestone "examen"

    
17. Incorpora los cambios a la rama desarrollo comentando y cerrando el pull request a la vez con el siguiente mensaje y referenciando a tu profesor al final: "Refactorizando y añadiendo documentación" ***(CV - 0.5 puntos)***

### Fork y Pull Request

18. Actualiza tu repositorio, si no lo has hecho ya.

19. Antes de hacer el fork, tienes que configurar tu repositorio como público.

20. Realiza un fork del repositorio del examen a tu cuenta de github. ***(CV - 0.5 puntos)***

21. En el repositorio forkado, crea una rama a partir de la rama desarrollo llamada "add_title" y modifica la etiqueta title del index.html con tu nombre y apellidos

22. Compromete los cambios con la etiqueta "pull request add title Nombre y apellidos" ***(CV - 0.125 puntos)***

23. Realiza un pull request de la rama **add_title** de tu repositorio forkado sobre la rama **desarrollo** del repositorio del examen llamado "Añadir título" ***(CV - 1 punto)***

24. Acepta los cambios y haz un merge de tu pull request ***(CV - 0.5 puntos)***

25. No borres el repositorio de tu cuenta hasta que el examen esté corregido

### Issues

26. Observa los issues que deberías tener en tu repositorio de examen.

27. Enlaza uno de ellos al pull request Feedback que ya tienes abierto en tu repositorio del examen ***(CV - 0.375 puntos)***

28. Ciérralos con un solo commit que contenga en la etiqueta "Cerrando Issues - Nombre y Apellidos" ***(CV - 1 punto)***

### Ramas y Merge II

29. Fusiona la rama desarrollo en la rama main ***(CV - 0.25 puntos)***

### Github Pages

30. Crea una página con tu repositorio de la rama main. En la url "tu_url_github_page/repositorioexamen/ruta_hacia_index.html_generado_por_sphinx" debe aparecer tu documentación html generada ***(CV - 0.5 puntos)***

### Tags y Releases

31. Añade un tag en el primer commit del repositorio de la rama main con la v0.0.1 y la descripción "Primera versión alpha - Nombre y Apellidos" ***(CV - 1 punto)***

32. Añade otro tag en el último commit (sin crear otro commit nuevo) con la v1.0.0 "Primera Release Candidate - Nombre y Apellidos" ***(CV - 0.5 puntos)***

33. Sube sólo los tags al repositorio y comprueba que se han añadido mirando en la pestaña release ***(CV - 0.5 puntos)***

###  Gitlab

34. Crea un repositorio en el grupo de Entornos de gitlab. Añádelo a tu repositorio local y súbelo. Deberás tener el mismo repositorio tanto en github como gitlab ***(CV - 1.25 puntos)***

##  Nota

***En caso de cualquier duda y/o errata, será resuelta durante la realización del examen***
