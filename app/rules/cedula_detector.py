import re
from app.core.models import PIIFinding
from app.utils.config_loader import load_compliance_config

def detect_cedulas(text: str) -> list[PIIFinding]:
    """Detecta cédulas colombianas utilizando la configuración dinámica del JSON."""
    # 1. Cargamos las reglas desde el archivo de configuración externa
    config = load_compliance_config()
    rule_config = config["compliance_rules"]["ley_1581_2012"]
    
    # 2. Extraemos las variables normativas
    min_digits = rule_config["validation"]["min_digits"]
    max_digits = rule_config["validation"]["max_digits"]
    exclude_sequences = rule_config["validation"]["exclude_sequences"]
    
    entity_type = rule_config["entity_type"]
    sensitivity = rule_config["sensitivity"]
    legal_foundation = rule_config["legal_foundation"]
    
    # 3. Construimos la expresión regular dinámica según los límites de la ley
    pattern = rf"\b\d{{{min_digits},{max_digits}}}\b"
    matches = re.findall(pattern, text)
    
    findings = []
    for match in matches:
        # 4. Aplicamos el filtro de mitigación de falsos positivos (Lista negra del JSON)
        if match in exclude_sequences:
            continue
            
        # 5. Estructuramos el hallazgo con su correspondiente sustento jurídico
        findings.append(
            PIIFinding(
                type=entity_type,
                value=match,
                sensitivity=sensitivity,
                norm=legal_foundation
            )
        )
        
    return findings