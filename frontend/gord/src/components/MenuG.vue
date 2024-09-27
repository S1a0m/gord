<script setup>
import Button from './Button.vue'  
</script>

<template>
  <div class="container">
    <div class="menu">
      <nav>
        <RouterLink to="/"><Button type="menu-button"><span class="active">Home</span></Button></RouterLink>
        <RouterLink to="/about"><Button type="menu-button"><span>About</span></Button></RouterLink>
        <RouterLink to="/portfolio"><Button type="menu-button"><span>Portfolio</span></Button></RouterLink>
        <RouterLink to="/blog"><Button type="menu-button"><span>Blog</span></Button></RouterLink>
        <RouterLink to="/projects"><Button type="menu-button"><span>Projects</span></Button></RouterLink>
        <RouterLink to="/tutorials"><Button type="menu-button"><span>Tutorials</span></Button></RouterLink>
        <RouterLink to="/faq"><Button type="menu-button"><span>FAQ</span></Button></RouterLink>
      </nav>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
  position: fixed;
  left: 19em;
  top: 9em;
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
  background: #1C1A1A;
  width: 25em;
  min-height: 80vh;
  border-radius: 14px;
  border-color: #288F9E;
}

span {
  display: block;
  color: #288F9E;
  font-family: "Roboto Mono", system-ui;
  font-weight: bold;
  font-style: normal;
  font-size: 32px;
}
/*
.active {
  color: #505050;
  
}*/
</style>
