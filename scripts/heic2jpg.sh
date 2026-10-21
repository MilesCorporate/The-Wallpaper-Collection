#!/usr/bin/env bash
# Convert every HEIC/HEIF in the collection to a JPEG sibling (for Windows/Linux).
#
#   ./scripts/heic2jpg.sh              # whole repo
#   ./scripts/heic2jpg.sh "Apple Park" # one folder
#
# Existing .jpg files are never overwritten.
set -euo pipefail

root="${1:-.}"
count=0

while IFS= read -r -d '' f; do
  out="${f%.*}.jpg"
  if [ -e "$out" ]; then
    continue
  fi
  sips -s format jpeg -s formatOptions 92 "$f" --out "$out" >/dev/null
  echo "→ $out"
  count=$((count + 1))
done < <(find "$root" -type f \( -iname '*.heic' -o -iname '*.heif' \) -not -path '*/.*' -print0)

echo "converted $count file(s)"
