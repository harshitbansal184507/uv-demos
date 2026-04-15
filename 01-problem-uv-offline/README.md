rm -rf .venv

UV_FIND_LINKS="$(pwd)/output/deps/uv" \
UV_OFFLINE=true \
UV_NO_CACHE=true \
uv sync --frozen --no-index --verbose