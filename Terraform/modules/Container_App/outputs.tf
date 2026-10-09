output "fqdn" {
  value = azurerm_container_app.my_container_app.latest_revision_fqdn
}
