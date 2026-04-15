podman build \
    --volume "$(realpath ./output)":/tmp/hermeto-output:Z \
    --volume "$(realpath ./hermeto.env)":/tmp/hermeto.env:Z \
    --network none \
    --no-cache \
    -t localhost/inject-files-demo:latest .

podman run --rm localhost/inject-files-demo:latest