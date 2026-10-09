resource "azurerm_container_app" "my_container_app" {
  name                         = var.container_app_name
  container_app_environment_id = var.container_app_environment_id
  resource_group_name          = var.resource_group_name

  revision_mode = "Single"

  template {
    container {
      name   = var.container_name
      image  = var.container_image
      cpu    = var.cpu
      memory = var.memory
    }
  }

  ingress {
    external_enabled = true
    target_port      = var.target_port

    traffic_weight {
      percentage      = 100
      latest_revision = true
    }
  }
}
