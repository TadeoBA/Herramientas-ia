-- 1. Asegurar la extensión para generación automática de UUIDs v4
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 2. Crear tabla de Contratos Analizados
CREATE TABLE IF NOT EXISTS contracts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    filename TEXT NOT NULL,
    analyzed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    jurisdiction TEXT NOT NULL DEFAULT 'Colombia'
);

-- 3. Crear tabla de Hallazgos de PII (Ley 1581/2012)
CREATE TABLE IF NOT EXISTS pii_findings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    contract_id UUID NOT NULL REFERENCES contracts(id) ON DELETE CASCADE,
    pii_type TEXT NOT NULL, -- Ej: 'CEDULA'
    pii_value TEXT NOT NULL,
    sensitivity TEXT NOT NULL, -- PRIVADO / SENSIBLE / SEMIPRIVADO
    norm TEXT NOT NULL, -- Ej: 'Art. 5 Ley 1581/2012'
    detected_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 4. Crear tabla de Hallazgos de Cumplimiento Normativo (SARLAFT / Circulares SFC)
CREATE TABLE IF NOT EXISTS compliance_findings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    contract_id UUID NOT NULL REFERENCES contracts(id) ON DELETE CASCADE,
    requirement_id TEXT NOT NULL, -- Ej: 'REQ_01'
    status TEXT NOT NULL, -- CUMPLE / NO_CUMPLE
    norm TEXT NOT NULL, -- Ej: 'Circular Básica Jurídica SFC — Cap. IV'
    checked_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 5. Crear índices estratégicos para optimizar consultas de auditoría ultra rápidas
CREATE INDEX IF NOT EXISTS idx_pii_findings_contract_id ON pii_findings(contract_id);
CREATE INDEX IF NOT EXISTS idx_compliance_findings_contract_id ON compliance_findings(contract_id);