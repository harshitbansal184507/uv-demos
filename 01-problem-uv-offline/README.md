shows uv sync doesn't work, since resolved urls are used from uv.lock file instead of specified output directory

UV_FIND_LINKS="$(pwd)/output/deps/uv" \
UV_OFFLINE=true \
UV_NO_CACHE=true \
uv sync --frozen --no-index --verbose
