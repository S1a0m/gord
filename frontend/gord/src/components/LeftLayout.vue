<script setup>
import { ref } from 'vue';
import MenuG from './MenuG.vue';

const showMenu = ref(false);

const toggleMenu = () => {
  showMenu.value = !showMenu.value;
}
</script>

<template>
    <aside>
        <slot></slot>
        <div class="menu">
            <button class="menu-button" @click="toggleMenu">
                <div class="menu-icon"></div>
                <div class="menu-icon"></div>
                <div class="menu-icon"></div>
                <span>Menu</span>
            </button>
        </div>
    </aside>
    <Transition>
      <MenuG v-if="showMenu"/>
    </Transition>
</template>

<style lang="scss" scoped>
aside {
    width: 15vw;
    margin: 1em;
}

.menu {
    margin-left: 12em;
    margin-top: 37.9vw;
}

.menu-button {
    background-color: transparent;
    border: 2px solid #00FF00;
    color: #00FF00;
    font-size: 12px;
    padding: 10px 20px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    text-transform: uppercase;
    transition: 0.3s ease-in-out;
}

.menu-button:hover {
    background-color: #00FF00;
    color: black;
}

.menu-button span {
    display: block;
    margin-top: 10px;
}

    .menu-icon {
      width: 30px;
      height: 3px;
      background-color: #00FF00;
      margin: 6px auto;
      transition: all 0.3s;
    }

    .menu-button:hover .menu-icon {
      background-color: black;
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