package kubernetes.validating.privileged

deny[msg] {
    some http-api
    input_container[http-api]
    http-api.securityContext.privileged
    msg := sprintf("Container '%v' should not run in privileged mode.", [http-api.name])
}

input_container[container] {
    container := input.request.object.spec.containers[_]
}

input_container[container] {
    container := input.request.object.spec.initContainers[_]
