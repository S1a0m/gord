<script setup>
import Button from './Button.vue'  

const emit = defineEmits([ 'close-menu' ])

const closeMenu = () => {
    emit('close-menu');
}
</script>

<template>
  <div class="container">
    <div class="menu">
      <nav>
        <RouterLink to="/" @click="closeMenu"><Button type="menu-button"><span>Home</span></Button></RouterLink>
        <RouterLink to="/about" @click="closeMenu"><Button type="menu-button"><span>About</span></Button></RouterLink>
        <RouterLink to="/portfolio" @click="closeMenu"><Button type="menu-button"><span>Portfolio</span></Button></RouterLink>
        <RouterLink to="/blog" @click="closeMenu"><Button type="menu-button"><span>Blog</span></Button></RouterLink>
        <RouterLink to="/projects" @click="closeMenu"><Button type="menu-button"><span>Projects</span></Button></RouterLink>
        <RouterLink to="/faq" @click="closeMenu"><Button type="menu-button"><span>FAQ</span></Button></RouterLink>
      </nav>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
  position: absolute;
  left: 20em;
  top: 8em;
  z-index: 3;
}

nav {
  display: flex;
  flex-direction: column;
  gap: 2em;
}

.menu {
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--main-gray);
  width: 25em;
  min-height: 78vh;
  border-radius: 14px;
  border-color: var(--blue-light);
}

span {
  display: block;
  color: var(--blue-light);
  font-family: "Roboto Mono", system-ui;
  font-weight: bold;
  font-style: normal;
  font-size: 32px;
}
</style>
