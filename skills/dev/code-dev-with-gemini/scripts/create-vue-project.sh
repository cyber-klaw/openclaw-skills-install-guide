#!/bin/bash
# create-vue-project.sh - Create a new Vue 3 project with Gemini

PROJECT_NAME="${1:-vue-app}"
PROJECT_DIR="${2:-.}"
FULL_PATH="$PROJECT_DIR/$PROJECT_NAME"

echo "Creating Vue 3 project: $PROJECT_NAME"
echo "Location: $FULL_PATH"

# Create directory
mkdir -p "$FULL_PATH"
cd "$FULL_PATH"

# Generate project files with Gemini
echo "Generating project files with Gemini..."

# package.json
gemini "Create a package.json for Vue 3 project named $PROJECT_NAME with Vite, Vue 3, and dev script" > package.json

# vite.config.js
gemini "Create a vite.config.js for Vue 3 project with @vitejs/plugin-vue" > vite.config.js

# index.html
gemini "Create an index.html for Vue 3 project with div id=app and script src=/src/main.js" > index.html

# Create src directory
mkdir -p src

# main.js
gemini "Create a Vue 3 main.js that imports { createApp } from vue, imports App from ./App.vue, and mounts to #app" > src/main.js

# App.vue
gemini "Create a Vue 3 App.vue with Hello World message, counter button using Composition API, and nice CSS styling" > src/App.vue

echo "Project created at $FULL_PATH"
echo "To start:"
echo "  cd $FULL_PATH"
echo "  npm install"
echo "  npm run dev"
