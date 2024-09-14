<script setup>
import { RouterLink } from 'vue-router'
import LeftLayout from '../components/LeftLayout.vue'
import RightLayout from '../components/RightLayout.vue'
</script>

<template>
  <div class="container">
    <LeftLayout />
    <hr class="hr-one">
    <main>
      <h2>acceuil@gord:~$ <span class="cursor"></span></h2>
        <section>
          <img src="../components/icons/hacker-gord.jpg" alt="" width="500px" height="420px" class="avatar">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim  veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate  velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint  occaecat cupidatat non proident, sunt in culpa qui officia deserunt  mollit anim id est laborum
            Voir plus de détails en cliquant <span class="link"><RouterLink to="/about">ici</RouterLink></span>
            Ou allez directement sur cette page pour consulter les <span class="link"><RouterLink to="/projects">projets</RouterLink></span>
          </p>
        </section>
    </main>
    <hr class="hr-two">
    <RightLayout>
      <div class="right-layout">
        Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
        <br><br>
        Lorem ipsum dolor sit amet
        <br><br>
        Orem ipsum dolor sit amet. Lorem ipsum dolor sit amet
        <br><br>
        Lorem ipsum dolor sit amet
        <br><br>
        Sed ut perspiciatis unde
        <br>
        Voir plus de détails en consultant mon <RouterLink to="/blog">blog</RouterLink>
      </div>
    </RightLayout>
  </div>
</template>

<style scoped>

.container {
  display: flex;
  height: 90vh;
}

.right-layout, section {
  padding: 1em;
}

.right-layout {
  margin-top: 2em;
  font-size: 15px;
  font-family: "Roboto", system-ui;
  font-weight: 300;
  font-style: normal;
}

section {
  margin-top: 1.5em;
}

section p {
  margin-top: 2em;
  padding-right: 10em;
  font-size: 16px;
  color: #f5f5f5;

  font-family: "Roboto Mono", monospace;
  font-optical-sizing: auto;
  font-style: normal;
}

.avatar {
  border-radius: 14px;
  width: 411px;
  height: 331px;
}

h2 {
  color: #00ff00;
  margin-top: 1em;

  font-family: "Roboto Mono", monospace;
  font-optical-sizing: auto;
  font-style: normal;
  font-size: 20px;
}

hr {
  width: 1px;
  color: #1C1A1A;
}

.hr-one {
  height: 40vh;
}

.hr-two {
  height: 70vh;
}

.cursor {
      display: inline-block;
      width: 10px;
      height: 24px;
      background-color: #f5f5f5; /* Même couleur que le texte */
      animation: blink 1s step-end infinite;
      vertical-align: bottom;
}

@keyframes blink {
      0%, 100% {
        opacity: 1;
      }
      50% {
        opacity: 0;
      }
    }
</style>
