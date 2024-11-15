resource "null_resource" "docker_commands" {
  provisioner "local-exec" {
    command = "docker tag usuarios-ms us-east4-docker.pkg.dev/cbse-2024ii-438703/usuarios-ms/usuarios-ms"
  }

  provisioner "local-exec" {
    command = "docker push us-east4-docker.pkg.dev/cbse-2024ii-438703/usuarios-ms/usuarios-ms"
  }
}