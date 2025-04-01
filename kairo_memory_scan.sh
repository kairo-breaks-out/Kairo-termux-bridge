#!/data/data/com.termux/files/usr/bin/bash

echo "[Kairo-Scan] Searching for 'kairo' files in shared storage..."
find /storage/emulated/0/ -type f -iname "*kairo*" > memory/kairo_file_list.txt

echo "[Kairo-Scan] Found files:"
cat memory/kairo_file_list.txt

# Inject each file’s content into memory
while read -r file; do
  echo "[Kairo-Scan] Processing: $file"
  head -c 10000 "$file" > temp_chunk.txt  # limit to avoid overload
  curl -X POST http://localhost:5000/injectmemory \
    -H "Content-Type: application/json" \
    -d "{\"role\": \"external_file\", \"message\": \"$(cat temp_chunk.txt | sed 's/"/\\"/g')\"}"
done < memory/kairo_file_list.txt

echo "[Kairo-Scan] Memory injection complete."
