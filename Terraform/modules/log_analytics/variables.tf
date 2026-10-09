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



variable "azurerm_resource_group" {
  type    = string
  default = "overide_this_value"

}
