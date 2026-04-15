cd ~/uv-demos/00-pip-baseline

# Fetch
hermeto fetch-deps --source . --output ./hermeto-output \
  '{"type": "pip", "requirements_files": ["requirements.txt"], "requirements_build_files": ["requirements-build.txt"]}'

# Generate env
hermeto generate-env ./hermeto-output -o ./hermeto.env --for-output-dir /tmp/hermeto-output

# Inject files
hermeto inject-files ./hermeto-output --for-output-dir /tmp/hermeto-output

# Build offline
podman build . \
  --volume "$(realpath ./hermeto-output)":/tmp/hermeto-output:Z \
  --volume "$(realpath ./hermeto.env)":/tmp/hermeto.env:Z \
  --network none --no-cache --tag pip-baseline

# Verify
podman run --rm pip-baseline