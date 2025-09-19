DIR="${1:-.}"
DIR=$(realpath "$DIR")  # Ensure absolute paths

find "$DIR" -type f -printf "%s %p\n" | sort -nr | head -n 3
