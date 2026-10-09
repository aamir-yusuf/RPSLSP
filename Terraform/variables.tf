# # # # # # # # # # # # #  Azure Resource Group # # # # # # # # # # # # # 

variable "azurerm_resource_group_name" {
  type    = string
  default = "my_rg_name"

}

variable "location" {
  type    = string
  default = "uksouth"

}



# # # # # # # # # # # # Log Analytics Variables Below # # # # # # # # # # # # # 
variable "log_analytics_name" {
  type    = string
  default = "log_analytics_name"

}



variable "log_analytics_location" {
  type    = string
  default = "uksouth"

}




variable "log_analytics_sku" {
  type    = string
  default = "PerGB2018"

}


variable "retention_in_days" {
  type    = number
  default = 30
}


variable "azure_rg_location" {
  type    = string
  default = "uksouth"

}


variable "azure_container_registry_name" {
  type    = string
  default = "my_cr"

}


variable "container_registry_location" {
  type    = string
  default = "uksouth"

}



variable "container_registry_sku" {
  type    = string
  default = "Basic"

}









variable "container_environment_name" {
  type    = string
  default = "my_container_environment_name"
}










variable "container_app_name" {
  default = "rpsls-app"
}

variable "container_name" {
  default = "rpsls"
}

variable "container_image" {
  default = "nginx"
}

variable "cpu" {
  default = 0.25
}

variable "memory" {
  default = "0.5Gi"
}

variable "target_port" {
  default = 80
}
