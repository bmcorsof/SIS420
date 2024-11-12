# Tablas de Pruebas de Auditoría

## Vulnerabilidad: Violación del Control de Acceso OAUTH

| ID | Nombre Prueba | Herramienta | Criterio de Auditoría |
|----|---------------|-------------|----------------------|
| 1 | Verificación de Implementación OAuth | Burp Suite Professional | OWASP ASVS v4.0 - Requisito 3.1 |
| 2 | Análisis de Flujo de Tokens OAuth | OWASP ZAP | OAuth 2.0 Security Best Practices (RFC 6819) |
| 3 | Prueba de Endpoints OAuth | Postman | CWE-287 (Improper Authentication) |

## Vulnerabilidad: Web Services utilizados por usuarios no autenticados

| ID | Nombre Prueba | Herramienta | Criterio de Auditoría |
|----|---------------|-------------|----------------------|
| 1 | Escaneo de Endpoints Expuestos | Acunetix | OWASP API Security Top 10 2023 - API1 |
| 2 | Análisis de Autenticación de APIs | SoapUI Pro | NIST SP 800-95 |
| 3 | Verificación de Control de Acceso | Burp Suite Professional | CWE-306 |

## Vulnerabilidad: Certificados SSL/TLS inválido para el sitio

| ID | Nombre Prueba | Herramienta | Criterio de Auditoría |
|----|---------------|-------------|----------------------|
| 1 | Análisis de Configuración SSL/TLS | SSLyze | NIST SP 800-52 Rev. 2 |
| 2 | Verificación de Validez de Certificados | Qualys SSL Labs | CAB Forum Baseline Requirements |
| 3 | Análisis de Vulnerabilidades SSL/TLS | TestSSL.sh | OWASP TLS Protection Cheat Sheet |

# Procedimientos Detallados por Prueba

## Vulnerabilidad 1: Violación del Control de Acceso OAUTH

### Prueba 1: Verificación de Implementación OAuth
1. Configurar Burp Suite Professional
   - Iniciar Burp Suite en modo profesional
   - Configurar el navegador para usar el proxy de Burp
   - Activar el certificado SSL de Burp en el navegador

2. Capturar el flujo de autenticación
   - Iniciar el proceso de login OAuth
   - Capturar todas las redirecciones
   - Guardar los tokens y parámetros

3. Analizar los parámetros
   - Verificar scope de permisos
   - Analizar el formato de los tokens
   - Comprobar la presencia de state parameter

### Prueba 2: Análisis de Flujo de Tokens OAuth
1. Configurar OWASP ZAP
   - Iniciar ZAP Proxy
   - Importar contexto si existe
   - Configurar las reglas de escaneo

2. Realizar pruebas automatizadas
   - Ejecutar Spider activo
   - Realizar escaneo de tokens
   - Verificar manejo de sesiones

3. Analizar resultados
   - Revisar hallazgos de alto riesgo
   - Documentar vulnerabilidades encontradas
   - Verificar falsos positivos

### Prueba 3: Prueba de Endpoints OAuth
1. Configurar Postman
   - Crear nueva colección
   - Configurar variables de entorno
   - Importar endpoints OAuth

2. Ejecutar pruebas de endpoints
   - Probar authorization endpoint
   - Verificar token endpoint
   - Probar refresh token endpoint

## Vulnerabilidad 2: Web Services no autenticados

### Prueba 1: Escaneo de Endpoints Expuestos
1. Configuración inicial Acunetix
   - Crear nuevo escaneo
   - Configurar alcance
   - Definir políticas de escaneo

2. Ejecutar escaneo
   - Iniciar escaneo completo
   - Monitorear progreso
   - Capturar hallazgos

3. Análisis de resultados
   - Revisar endpoints descubiertos
   - Clasificar por nivel de riesgo
   - Documentar hallazgos

### Prueba 2: Análisis de Autenticación de APIs
1. Preparar SoapUI Pro
   - Crear nuevo proyecto
   - Importar definiciones de API
   - Configurar environments

2. Ejecutar pruebas de seguridad
   - Probar endpoints sin autenticación
   - Verificar métodos HTTP permitidos
   - Analizar respuestas

3. Documentar resultados
   - Listar endpoints vulnerables
   - Capturar evidencias
   - Preparar informe

### Prueba 3: Verificación de Control de Acceso
1. Configurar Burp Suite
   - Activar extensiones relevantes
   - Configurar scope
   - Preparar diccionarios

2. Realizar pruebas manuales
   - Probar bypass de autenticación
   - Verificar escalación horizontal
   - Comprobar escalación vertical

## Vulnerabilidad 3: Certificados SSL/TLS inválidos

### Prueba 1: Análisis de Configuración SSL/TLS
1. Ejecutar SSLyze
```bash
sslyze --regular ccbol2024.usfx.bo
```

2. Analizar resultados
   - Revisar protocolos soportados
   - Verificar cipher suites
   - Comprobar perfect forward secrecy

3. Documentar hallazgos
   - Capturar salida de comando
   - Clasificar vulnerabilidades
   - Preparar recomendaciones

### Prueba 2: Verificación de Validez de Certificados
1. Análisis con SSL Labs
   - Acceder a https://www.ssllabs.com/ssltest/
   - Ingresar dominio ccbol2024.usfx.bo
   - Iniciar nuevo escaneo

2. Revisar resultados
   - Verificar calificación general
   - Analizar chain de certificados
   - Comprobar revocación

3. Documentar hallazgos
   - Capturar reporte completo
   - Identificar problemas críticos
   - Listar recomendaciones

### Prueba 3: Análisis de Vulnerabilidades SSL/TLS
1. Ejecutar TestSSL.sh
```bash
./testssl.sh --full ccbol2024.usfx.bo
```

2. Analizar vulnerabilidades
   - Revisar vulnerabilidades conocidas
   - Verificar configuración
   - Analizar compatibilidad

3. Documentar resultados
   - Capturar evidencias
   - Clasificar hallazgos
   - Preparar informe final
