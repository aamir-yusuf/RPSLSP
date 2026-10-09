resource "azurerm_container_app_environment" "my_container_app_environment" {
  name                       = var.container_environment_name
  location                   = var.location
  resource_group_name        = var.azurerm_resource_group
  logs_destination           = var.log_analytics_name
  log_analytics_workspace_id = var.log_analytics_workspace_id
}
