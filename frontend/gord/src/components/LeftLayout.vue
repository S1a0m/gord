<script setup>
import { ref} from 'vue';
import MenuG from './MenuG.vue';
import Button from './Button.vue';

const showMenu = ref(false);

const toggleMenu = () => {
  showMenu.value = !showMenu.value;
}
</script>

<template>
    <aside>
        <slot></slot>
    </aside>
    <Transition>
      <MenuG v-if="showMenu" @close-menu="toggleMenu"/>
    </Transition>
</template>

<style lang="scss" scoped>
aside {
    width: 18vw;
    //margin: 1em;
}

.menu {
  margin-left: 103%;//74%;//14em;
  margin-top: 0.5em;
  width: 5em;
  position: relative;
}

.menu-button {
    background-color: transparent;
    border: 2px solid var(--green-hack);
    color: var(--green-hack);
    font-size: 12px;
    padding: 10px 20px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    text-transform: uppercase;
    transition: 0.3s ease-in-out;
}

.menu-button:hover {
    background-color: var(--green-hack);
    color: var(--main-black);
}

.menu-button span {
    display: block;
    margin-top: 10px;
}

    .menu-icon {
      width: 30px;
      height: 3px;
      background-color: var(--green-hack);
      margin: 6px auto;
      transition: all 0.3s;
    }

    .menu-button:hover .menu-icon {
      background-color: var(--main-black);
    }

    /* Menu icon animation */
    .menu-button.open .menu-icon:nth-child(1) {
      transform: translateY(9px) rotate(45deg);
    }

    .menu-button.open .menu-icon:nth-child(2) {
      opacity: 0;
    }

    .menu-button.open .menu-icon:nth-child(3) {
      transform: translateY(-9px) rotate(-45deg);
    }

.v-enter-active,
.v-leave-active {
  transition: 500ms;
}

.v-enter-from {
  opacity: 0;
  transform: translateX(-20em);
}

.v-leave-to {
  opacity: 0;
  transform: translateX(-20em);
}
</style>