# # Azure Resource Group 
# azurerm_resource_group_name = "test_resource_group"
# location                    = "uksouth"

# # Log Analytics 
# log_analytics_name     = "test_log_analytics"
# log_analytics_location = "uksouth"
# retention_in_days      = 45




# Azure Resource Group

azurerm_resource_group_name = "rg-rpsls-dev"
location                    = "uksouth"

# Log Analytics

log_analytics_name     = "law-rpsls-dev"
log_analytics_location = "uksouth"
log_analytics_sku      = "PerGB2018"
retention_in_days      = 30


# Azure Container Registry

azure_rg_location             = "uksouth"
azure_container_registry_name = "rpslsacr12345"
container_registry_location   = "uksouth"
container_registry_sku        = "Basic"

# Container App Environment

container_environment_name = "cae-rpsls-dev"



# Container App

container_app_name = "rpsls-app"
container_name     = "rpsls"
container_image    = "nginx:latest"

cpu         = 0.25
memory      = "0.5Gi"
target_port = 80
