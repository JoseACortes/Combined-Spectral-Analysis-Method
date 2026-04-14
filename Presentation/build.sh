#!/bin/bash

# Build script for the LaTeX paper with working files in build/
# Usage: ./build.sh [clean|quick|full]

set -e

MAIN_DIR="main"
MAIN="manuscript_revision"
BUILD_DIR="build"

mkdir -p "$BUILD_DIR"

case "${1:-full}" in
    "clean")
        echo "Cleaning auxiliary files..."
        rm -rf "$BUILD_DIR"
        rm -f "$MAIN_DIR/$MAIN.pdf"
        echo "Clean complete."
        ;;
    "quick")
        echo "Quick compilation (no bibliography)..."
        echo "Running: pdflatex -output-directory=$BUILD_DIR $MAIN_DIR/$MAIN"
        pdflatex -output-directory="$BUILD_DIR" "$MAIN_DIR/$MAIN"
        cp "$BUILD_DIR/$MAIN.pdf" . 2>/dev/null || true
        echo "Quick compilation complete."
        ;;
    "full"|*)
        echo "Full compilation with bibliography..."
        echo "Step 1: Running pdflatex -output-directory=$BUILD_DIR $MAIN"
        pdflatex -output-directory="$BUILD_DIR" "$MAIN_DIR/$MAIN".tex
        if [ -f "$BUILD_DIR/$MAIN.aux" ]; then
            echo "Step 2: Running bibtex in $BUILD_DIR"
            echo $(pwd)
            (cd "$BUILD_DIR" && bibtex "$MAIN")
            echo "Step 3: Running pdflatex (second pass)"
            pdflatex -output-directory="$BUILD_DIR" "$MAIN_DIR/$MAIN".tex
            echo "Step 4: Running pdflatex (final pass)"
            pdflatex -output-directory="$BUILD_DIR" "$MAIN_DIR/$MAIN".tex
        fi
        cp "$BUILD_DIR/$MAIN.pdf" . 2>/dev/null || true
        echo "Full compilation complete."
        ;;
esac