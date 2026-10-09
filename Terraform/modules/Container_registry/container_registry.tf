resource "azurerm_container_registry" "example" {
  name                = var.azure_container_registry_name
  resource_group_name = var.azurerm_resource_group_name
  location            = var.location
  sku                 = var.container_registry_sku
}
