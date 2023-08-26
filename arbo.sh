#!/bin/bash

# Chemin vers le dossier racine de votre projet
PROJECT_PATH="/home/s1e3b/Bureau/PyOps/middleware/"

# Chemin vers le fichier de sortie .md
OUTPUT_FILE="arborescence.md"

# Supprimer le fichier de sortie s'il existe déjà
if [ -f "$OUTPUT_FILE" ]; then
    rm "$OUTPUT_FILE"
fi

# Fonction récursive pour parcourir et générer l'arborescence
generate_tree() {
    local path="$1"
    local prefix="$2"
    local folders=()
    local files=()

    for item in "$path"/*; do
        local name=$(basename "$item")
        if [ -d "$item" ]; then
            folders+=("$name")
        else
            files+=("$name")
        fi
    done

    # Trier les fichiers dans l'ordre souhaité
    IFS=$'\n' files=($(printf "%s\n" "${files[@]}" | grep -E "^__" && printf "%s\n" "${files[@]}" | grep -vE "^__"))

    for file in "${files[@]}"; do
        echo "$prefix|-- $file" >> "$OUTPUT_FILE"
    done

    for folder in "${folders[@]}"; do
        echo "$prefix|-- $folder/" >> "$OUTPUT_FILE"
        generate_tree "$path/$folder" "$prefix|   "
    done   
}

# En-tête du fichier Markdown
echo "# Arborescence du projet PyOps" > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Générer l'arborescence en appelant la fonction récursive
generate_tree "$PROJECT_PATH" ""

# Afficher les fichiers à la racine du projet
root_files=$(ls -p "$PROJECT_PATH" | grep -v /)
for root_file in $root_files; do
    echo "|-- $root_file" >> "$OUTPUT_FILE"
done

echo "Arborescence générée dans $OUTPUT_FILE"
