<script setup>
import Button from './Button.vue'  
</script>

<template>
    <div class="menu">
      <nav>
        <RouterLink to="/"><Button type="menu-button"><span>Home</span></Button></RouterLink>
        <RouterLink to="/about"><Button type="menu-button"><span>About</span></Button></RouterLink>
        <RouterLink to="/portfolio"><Button type="menu-button"><span>Portfolio</span></Button></RouterLink>
        <RouterLink to="/blog"><Button type="menu-button"><span>Blog</span></Button></RouterLink>
        <RouterLink to="/projects"><Button type="menu-button"><span>Projects</span></Button></RouterLink>
        <RouterLink to="/tutorials"><Button type="menu-button"><span>Tutorials</span></Button></RouterLink>
        <RouterLink to="/faq"><Button type="menu-button"><span>FAQ</span></Button></RouterLink>
      </nav>
    </div>
</template>

<style scoped>
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
  width: 20em;
  height: 80vh;
  border-radius: 14px;
  /*border-style: solid;*/
  border-color: #288F9E;
  position: fixed;
  margin-left: 11em;
}

span {
  display: block;
  color: #288F9E;
  font-family: "Roboto", system-ui;
  font-weight: bold;
  font-style: normal;
  font-size: 32px;
}
</style>
