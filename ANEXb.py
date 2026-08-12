# Analizador de Eventos de Seguridad Windows
from collections import defaultdict

class SecurityEventAnalyzer:
    def __init__(self):
        self.failed_attempts = defaultdict(int)
        self.suspicious_ips = defaultdict(int)
        self.events = []
    
    def add_event(self, event):
        """Agregar evento de seguridad"""
        self.events.append(event)
        
        if event["event_id"] == 4625:
            self.failed_attempts[event["account_name"]] += 1
            self.suspicious_ips[event["source_ip"]] += 1
    
    def detect_brute_force(self, threshold=5):
        """Detectar intentos de fuerza bruta"""
        return {
            account: count 
            for account, count in self.failed_attempts.items() 
            if count >= threshold
        }
    
    def get_suspicious_ips(self, threshold=3):
        """Obtener IPs sospechosas"""
        return {
            ip: count 
            for ip, count in self.suspicious_ips.items() 
            if count >= threshold
        }
    
    def generate_report(self):
        """Generar reporte de análisis"""
        print("\n--- REPORTE DE SEGURIDAD ---")
        print(f"Total eventos: {len(self.events)}")
        
        brute_force = self.detect_brute_force(threshold=3)
        if brute_force:
            print("\n⚠️  Intentos de Fuerza Bruta Detectados:")
            for account, attempts in brute_force.items():
                print(f"   • {account}: {attempts} intentos")
        
        suspicious_ips = self.get_suspicious_ips(threshold=2)
        if suspicious_ips:
            print("\n⚠️  IPs Sospechosas Detectadas:")
            for ip, attempts in suspicious_ips.items():
                print(f"   • {ip}: {attempts} intentos")
        
        if not brute_force and not suspicious_ips:
            print("\n✓ Sin patrones sospechosos detectados")

if __name__ == "__main__":
    analyzer = SecurityEventAnalyzer()
    
    event = {
        "event_id": 4625,
        "account_name": "admin_temp",
        "source_ip": "192.168.100.52",
        "domain": "UNIV-DOMINICANA"
    }
    
    analyzer.add_event(event)
    analyzer.generate_report()
