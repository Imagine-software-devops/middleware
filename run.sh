#!/bin/bash

function delete_pycache() {
    for entry in "$1"/*; do
        if [[ -d "$entry" ]]; then
            if [[ "$entry" == *'__pycache__' ]]; then
                echo "Suppression de $entry"
                rm -rf "$entry"
            else
                delete_pycache "$entry"
            fi
        fi
    done
}

target_directory="./"

delete_pycache "$target_directory"

