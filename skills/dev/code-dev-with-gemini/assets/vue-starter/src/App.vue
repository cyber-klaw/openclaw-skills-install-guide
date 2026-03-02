<script setup>
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <div class="hello">
    <h1>Hello World!</h1>
    <p>Welcome to your Vue 3 app</p>
    <button @click="count++">Count is: {{ count }}</button>
  </div>
</template>

<style scoped>
.hello {
  text-align: center;
  padding: 2rem;
  font-family: system-ui, sans-serif;
}

h1 {
  color: #42b883;
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

p {
  color: #666;
  margin-bottom: 2rem;
}

button {
  background: #42b883;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: background 0.2s;
}

button:hover {
  background: #369870;
}
</style>
