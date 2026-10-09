terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
}


module "resource_group" {
  azurerm_resource_group_name = var.azurerm_resource_group_name
  source                      = "./modules/resource_group"
  location                    = var.location

}



module "Log_analytics" {
  source                 = "./modules/log_analytics"
  azurerm_resource_group = module.resource_group.resource_group_name
  log_analytics_name     = var.log_analytics_name
  log_analytics_location = var.log_analytics_location
  retention_in_days      = var.retention_in_days
  log_analytics_sku      = var.log_analytics_sku
}


module "azurerm_container_registry" {
  source                        = "./modules/Container_registry"
  azure_container_registry_name = var.azure_container_registry_name
  azurerm_resource_group_name   = module.resource_group.resource_group_name
  container_registry_location   = var.container_registry_location
  container_registry_sku        = var.container_registry_sku
}


module "container_environment_name" {
  source                     = "./modules/Container_environment"
  container_environment_name = var.azure_container_registry_name
  log_analytics_workspace_id = module.Log_analytics.workspace_id
  azurerm_resource_group     = module.resource_group.resource_group_name
  location                   = var.location


}




module "container_app" {
  source = "./modules/container_app"

  container_app_name           = var.container_app_name
  container_app_environment_id = module.container_environment_name.container_app_environment_id

  resource_group_name = module.resource_group.resource_group_name

  container_name  = var.container_name
  container_image = var.container_image

  cpu         = var.cpu
  memory      = var.memory
  target_port = var.target_port
}



















