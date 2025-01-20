<template>
  <div v-if="visible" :class="['success-message', typeClass]" @click="close">
    <slot></slot>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const visible = ref(false);
const typeClass = ref('');

const emit = defineEmits(['success-displayed']); // Déclare l'événement personnalisé

function show(type = 'success') {
  visible.value = true;
  typeClass.value = type;

  if (type === 'success') {
    emit('success-displayed'); // Émet un événement lorsque le type est "success"
  }

  setTimeout(() => {
    close();
  }, 3000);
}

function close() {
  visible.value = false;
}

defineExpose({
  show,
});
</script>

<style scoped>
.success-message {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px 20px;
  border-radius: 5px;
  color: white;
  opacity: 0.9;
  transition: opacity 0.5s;
  cursor: pointer;
}

.success {
  background-color: green;
}

.error {
  background-color: red;
}

.success-message:hover {
  opacity: 1;
}
</style>
