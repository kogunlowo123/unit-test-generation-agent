# Unit Test Generation Agent — prod environment
include "root" {
  path = find_in_parent_folders()
}

terraform {
  source = "../../../modules//appops/vectorstore"
}

inputs = {
  environment = "prod"
  agent_name  = "unit-test-generation-agent"
}
