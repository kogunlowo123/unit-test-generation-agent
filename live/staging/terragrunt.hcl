# Unit Test Generation Agent — staging environment
include "root" {
  path = find_in_parent_folders()
}

terraform {
  source = "../../../modules//appops/vectorstore"
}

inputs = {
  environment = "staging"
  agent_name  = "unit-test-generation-agent"
}
