<script setup>
import { RouterLink } from 'vue-router'
import ArticleBase from '../components/ArticleBase.vue'
</script>

<template>
        <ArticleBase active-page="home" section-color="section" section="Hola I'm Gord">
          <img src="../components/icons/hacker-gord2.gif" alt="" class="avatar">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim  veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate  velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint  occaecat cupidatat non proident, sunt in culpa qui officia deserunt  mollit anim id est laborum
            Voir plus de détails en cliquant <span class="link"><RouterLink to="/about">ici</RouterLink></span>
            Ou allez directement sur cette page pour consulter les <span class="link"><RouterLink to="/projects">projets</RouterLink></span>
          </p>
        </ArticleBase>
</template>

<style lang="scss" scoped>
.avatar {
  border-radius: 14px;
  width: 411px;
  height: 331px;
}

p {
  margin-top: 2em;
  padding-right: 10em;
  font-size: 16px;
  color: var(--main-white);
  font: {
    family: "Roboto Mono", monospace;
    optical-sizing: auto;
    style: normal;
  }
}
</style>
