# WOW: Wow Observational Work ![](http://carina.fcaglp.unlp.edu.ar/~guevaran/wow/wowlogo4.png)
### _Trabajo Final de Astronomía Observacional_

Creado por [Natalia Guevara](mailto:nataliaguevaramandri@gmail.com) y [Tomás Regna](mailto:ttomasagustin@gmail.com).

Esquema del programa main:


* **Backup de archivos en crudo.**

* **Pre-reducción de imágenes.**

  + Trimming

  + Overscan
  
  + MasterBias.

  + MasterDark.

  + Separar por filtros a los flats y las imagenes de ciencia.
  
    - MasterFlat por filtro.

    - Procesamiento de imagenes de ciencia por filtro.

* **Fotometría de apertura.**
  
  + Estimación de FWHM y StdevSky.
  
  + Identificación de estrellas y sus coordenadas.
  
  + Fotometría de apertura con Phot.

* **Formateo de tablas .phot.**
  
  
  
  # Instalación
  
  Correr en una terminal :
  ```
  cd $HOME
  git clone https://github.com/tomasregna/WOW.git
  cd WOW
  ```
  Para hacerlo ejecutable:
  ```
  mv wow $HOME"/bin"
  mv wowconfig $HOME"/bin"
  chmod +x  $HOME"/bin/wow" $HOME"/bin/wowconfig"
  ```
  
  # Uso

  Corriendo en una terminal *wowconfig* se abrirá la interfaz gráfica para editar los parámetros del archivo de configuración. Desde allí se puede correr el programa.
  Adicionalmente, se puede corrier *wow* desde una terminal. Así,el programa ejecutará la lista de tareas indicada en el archivo _parameters.yaml_.

 
 * Nota: En la Sala Informatizada de Carina (FCAG), para correr este programa, se debe proceder de la siguiente manera*
  ```
    cd $HOME
    xterm -ls &
  ```
   Una vez dentro del xterm:
   ```
    conda_init
  ```
   Si usted no tiene un entorno de python en anaconda, puede crear uno de la siguiente manera:
  ```
    conda create -n python2.7 python=2.7 anaconda
 ```
  Luego, abra el entorno de python:
  ```
    conda activate python2.7
  ```
  Y yá podrá correr el programa sin inconvenientes.
 
 
Para más detalles, ver la [web del proyecto](http://carina.fcaglp.unlp.edu.ar/~guevaran/wow).
