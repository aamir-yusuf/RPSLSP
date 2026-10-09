variable "container_environment_name" {
  type    = string
  default = "my_container_environment_name"
}

variable "azurerm_resource_group" {
  type    = string
  default = "overide_this_value"

}


variable "location" {
  type    = string
  default = "uksouth"
}



variable "log_analytics_name" {
  type    = string
  default = "log_analytics_name"

}


variable "log_analytics_workspace_id" {
  type = string
}
