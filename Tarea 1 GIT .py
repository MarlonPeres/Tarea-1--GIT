#!/usr/bin/env python
# coding: utf-8

# # GIT

# Git es un sistema de control de versiones de codigo abierto, el cual permite crear varias versiones de algun proyecto y a su vez ir almancenando todos los cambios realizados sin perder las versiones previas y dejando un historial de todos los cambios realizados, esto lo hace GIT desde el etendimiento de la gran cantidad de versiones que pueden tener los codigos de un proyectos durante su elaboracion y la confusion que esto puede crear, asi como la seguridad que tambien otorga en caso el codigo se pueda  perder o sea borrado por equivocacion, esta caracteristica hace que GIT sea una herramienta adecuada para un equipo de trabajo que busca realizar proyectos largos, tediosos o que conlleven muchas modificaciones.
# 
# 
# Otra caracteristica de GIT es que puede crear versiones del mismo proyecto en modo paralelo y trabajarlas al mismo tiempo, esto quiere decir que a un codigo se le pueden hacer modificaciones diferentes ya sea por necesidad del proyecto o por alguna otra razon y comparar el funcionamiento de las diferentes versiones para analizar cual tiene mas ventajas , esto sin perder ninguno de los codigos; otra caracteristica importante es que varios usuarios pueden interactuar con el ya sea para mejorar el codigo o corregir algun error.
# 
# El funcionamiento de GIT puede ser un poco complejo por su linea de comandos y la estructura que posee la cual esta basada en directorios de trabajo, arboles (tree), blobs entre otros, para ser mas detallados nombraremos algunos objetos importantes de GIT a continuacion:
# 
# 1. Tree(arbol): Almacena directorios
# 2. Commit: Se refiere a las versiones de un proyecto o los cambios realizados en el
# 3. Annotated: Almacena texto persistente de un Commit 
# 
# Nota: Un Tree puede tener un grupo de Blobs y otros trees.
# 
# + Blobs: Puede ser un archivo o se refiere a una gran cantidad de bytes. 
# 
# Tambien podemos citar otro elemento importante de GIT:
# 
# + Branch o ramas: Estas son las encargadas de apuntar hacia la confirmacion de cada version creada de un codigo de un proyecto almacenado en GIT donde habra una rama master que es la que lleva la version del proyecto principal y las otras ramas apuntaran hacia versiones clonadas que se pueden despues unificar o eliminar segun la finalidad del proyecto.
# 
# 
# Una peculiaridad de GIT es que se puede trabajar el codigo de forma Remoto o ya sea en la nube por ejemplo usando GITHUB, por lo que cada usuario tendra una version del proyecto en su ordenador remoto, esto es una gran respaldo por si alguno de los usuarios llegara a perderlo, se cuenta con mas copias en cada remoto del resto de los usuarios y a la vez tambien se tiene una version en la nube en la aplicacion de preferencia de los dueños del proyecto.
# 
# A continuacion algunas ilustraciones para tener una mejor comprension:
# 
# 
# ![flecha%201-2.png](attachment:flecha%201-2.png)
# 
# 
# 
# La main branch sera la principal para entregar el proyecto final al cliente por lo cual no se debe modificar, simultaneamente estara la lina develop que sera la que compartira el proyecto con los diferentes usuarios, los cuales a su vez podran trabajar por su cuenta en el desarrollo o contenido delegado, una vez finalicen su parte tendran que integrar nuevamente su codigo a la linea develop para que sea examinado y si es viable los codigos seran integrados a la linea principal de proyecto, para poder hacer esto se necesitan ciertos comandos como git-branch, git-checkout, git-status, git-add, git-commit, git-push, git-pull.
# 
# 

# ## Ejemplo: 
# 
# En el ejemplo de abajo podemos observar como un proyecto inicial se destino a los usuarios, los cuales hicieron varias modificaciones en el usando ramas adicionales para cada version, teniendo un total de 9 versiones diferentes hasta la ultima y podemos observar como se integra cada version a la rama DEV que posteriormente se integrara al rama principal.
# 
# 
# ![flechas%202.PNG](attachment:flechas%202.PNG)
# 
# La nomenclatura usada es la siguient:
# 
# 0 = commit o snapshots
# -- = Branch
# 

# ## Conclusiones
# 
# 1. GIT creara un historial de todas las versiones de un proyecto, indicando quien realizo cada modificion y cuando.
# 2. GIT permitara la visualizacion y edicion de todas las versiones de un proyecto.
# 3. Los diferentes usuarios pueden trabajar simultaneamente en el proyecto sin afectar el proyecto principal al cual seran integrados despues de ser analizado.
# 4. Es necesario aprender los diferentes comandos de GIT para poder llamar, guardar, editar y obtener la ultima version de un proyecto ya sea en un remoto o en un programa en la nube.
# 5. Los commits son los comandos mas usados y son las diferentes versiones de un proyecto.

# ## Comentarios
# 
# + Es necesario estudiar todo los comandos para entender el procedimiento correcto para trabajar los repositorios de GIT.
# + El historial de las versiones nos ayudara para mejorar nuestro codigo o ya sea para no perderlo.
# + Es importante entender la diferencia entre trabajar en el remoto de GIT y la nube, ya que siempre hay que llamar la ultima version de la nube para trabajar el proyecto desde su ultima version. 

# ### Marlon Daniel Perez Garcia

# In[ ]:




