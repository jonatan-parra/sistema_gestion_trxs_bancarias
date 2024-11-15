# Crear un Artifact Registry de tipo Docker
resource "google_artifact_registry_repository" "usuarios-ms" {
  repository_id = "usuarios-ms"                   # ID único del repositorio en Artifact Registry
  format        = "DOCKER"                          # Tipo de repositorio: Docker
  location      = "us-east4"                        # Región donde se crea el repositorio
  mode          = "STANDARD_REPOSITORY"                        # Modo estándar; también se puede usar "VPCSC" para compatibilidad con VPC Service Controls
  description   = "Registro de contenedores Docker para el servicio usuarios-ms"  # Descripción del repositorio
}