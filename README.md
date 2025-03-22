# EvilDoS - Advanced Denial of Service Toolkit 🚨

![Banner](https://cdn.qwenlm.ai/output/25e42d2a-a4b5-4744-ac79-c82feb02a09f/t2i/f09da361-4dd2-4fc7-8a8b-f995f146b87c/d29ee8a3-26b9-406f-b6c9-00c8d65b71a1.png?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXNvdXJjZV91c2VyX2lkIjoiMjVlNDJkMmEtYTRiNS00NzQ0LWFjNzktYzgyZmViMDJhMDlmIiwicmVzb3VyY2VfaWQiOiJkMjllZThhMy0yNmI5LTQwNmYtYjZjOS0wMGM4ZDY1YjcxYTEiLCJyZXNvdXJjZV9jaGF0X2lkIjpudWxsfQ.YhVhartmnlkn6cFsMG1aAiEW2-wCEcqcVugQJueqG80)  
*(Banner placeholder - replace with actual ASCII art or logo)*

---

## **⚠️ ADVERTENCIA LEGAL**
Este proyecto es **SOLO PARA FINES EDUCATIVOS Y DE PRUEBA**.  
El uso no autorizado contra sistemas o redes sin permiso explícito es **ILEGAL**.  
Los desarrolladores no asumen responsabilidad por daños o mal uso.

---

## **Descripción**
EvilDoS es una herramienta avanzada de pruebas de estrés que implementa múltiples técnicas de Denegación de Servicio (DoS) para:

- Evaluar la resiliencia de servidores web
- Simular ataques en entornos controlados
- Capacitar en ciberseguridad ofensiva

---

## **Características Principales** 🛠️
| Ataque          | Descripción                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| **HTTP Flood**  | Inunda el servidor con solicitudes GET usando User-Agents aleatorios        |
| **SYN Flood**   | Envía paquetes TCP SYN spoofeados para agotar conexiones (requiere Scapy)   |
| **UDP Flood**   | Satura el ancho de banda con paquetes UDP de tamaño variable                |
| **Ping Flood**  | Bombardea con paquetes ICMP de diferentes tamaños (requiere Scapy)          |
| **Slowloris**   | Mantiene conexiones HTTP abiertas enviando headers lentamente               |

---

## **Instalación** 💻
```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/EvilDoS.git
cd EvilDoS

# Instalar dependencias
pip install -r requirements.txt
