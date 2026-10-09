variable "container_app_name" {
  type = string
}

variable "container_app_environment_id" {
  type = string
}

variable "resource_group_name" {
  type = string
}

variable "container_name" {
  type = string
}

variable "container_image" {
  type = string
}

variable "cpu" {
  type    = number
  default = 0.25
}

variable "memory" {
  type    = string
  default = "0.5Gi"
}

variable "target_port" {
  type    = number
  default = 5000
}
