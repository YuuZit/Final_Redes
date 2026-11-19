# Laboratorio de Redes - Topología Corporativa (Kathará)

Este repositorio contiene el despliegue automatizado de una topología de red corporativa utilizando **Kathará** y **Docker**. El proyecto implementa enrutamiento dinámico, resolución de nombres, asignación dinámica de IPs y servicios web, garantizando la conectividad total y el acceso a Internet.

## Tecnologías y Requisitos
* **Entorno de simulación:** [Kathará](https://github.com/KatharaFramework/Kathara)
* **Contenedores:** Docker
* **Imágenes utilizadas:** `kathara/base` (Quagga/FRRouting, BIND9, ISC-DHCP-Server, Apache2, Python3).

## Instrucciones de Uso

Para levantar la topología completa de 20 nodos, simplemente clona el repositorio y ejecuta el comando de inicio en la raíz del proyecto:

bash
# 1. Clonar el repositorio
git clone [https://github.com/YuuZit/Final_Redes.git](https://github.com/YuuZit/Final_Redes.git)
cd Final_Redes/Kathara

# 2. Iniciar el laboratorio (tarda unos segundos en arrancar los contenedores)
kathara lstart
