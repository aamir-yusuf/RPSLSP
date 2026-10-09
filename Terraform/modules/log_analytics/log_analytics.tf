
resource "azurerm_log_analytics_workspace" "my_log_analytics" {
  name                = var.log_analytics_name
  location            = var.log_analytics_location
  resource_group_name = var.azurerm_resource_group
  sku                 = var.log_analytics_sku
  retention_in_days   = var.retention_in_days
}
