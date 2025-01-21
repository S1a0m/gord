<script setup>
import Button from './Button.vue'  

const emit = defineEmits([ 'close-menu' ])

const closeMenu = () => {
    emit('close-menu');
}
</script>

<template>
  <div class="container">
    <span class="button-close" @click="closeMenu"><Button type="square-v1"><img src="./icons/close_blue.svg" alt=""></Button></span>
    <div class="menu">
      <nav>
        <RouterLink to="/" @click="closeMenu"><Button type="menu-button"><span>Acceuil</span></Button></RouterLink>
        <RouterLink to="/about" @click="closeMenu"><Button type="menu-button"><span>À propos</span></Button></RouterLink>
        <RouterLink to="/portfolio" @click="closeMenu"><Button type="menu-button"><span>Portfolio</span></Button></RouterLink>
        <RouterLink to="/blog" @click="closeMenu"><Button type="menu-button"><span>Blog</span></Button></RouterLink>
        <RouterLink to="/projects" @click="closeMenu"><Button type="menu-button"><span>Projets</span></Button></RouterLink>
        <RouterLink to="/faq" @click="closeMenu"><Button type="menu-button"><span>FAQ</span></Button></RouterLink>
      </nav>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
  opacity: 0.3;
  width: fit-content;
  z-index: 3;

  &:hover {
    opacity: 1;
  }
}

nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5em;
}

.menu {
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--main-gray);
  width: fit-content;
  height: 3em;
  padding: 1em;
  // border-radius: 14px;
    border-style: solid;
    border-width: 1px;
    border-radius: 10px;
    border-color: var(--green-hack);
    background-color: var(--mp-background);
}

span {
  display: block;
  color: var(--blue-light);
  font-family: "Roboto Mono", system-ui;
  font-weight: bold;
  font-style: normal;
  font-size: 32px;

  @media screen and (max-width: 768px) {
      font-size: 1.2em;
  }
}

.active {
  pointer-events: none;
}

.button-close {
  display: none;
}

@media screen and (max-width: 1280px) {
.container {
  opacity: 1;
  width: fit-content;
  position: absolute;
  top: 5em;
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
  width: 20em;
  height: 70vh;
  padding: 1em;
  // border-radius: 14px;
    border-style: solid;
    border-width: 1px;
    border-color: var(--green-hack);
    background-color: var(--mp-background);

  @media screen and (max-width: 768px) {
    width: 18em;
  }
}

.button-close {
  display: block;
  position: absolute;
  transform: translate(0.5em, 0.5em);
}
}
</style>
