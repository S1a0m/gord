<script setup>
import {RouterLink} from 'vue-router'
import apiClient from '../axios';

const props = defineProps([
  'titles',
  'blogLink',
  'id',
  'illustration'
])

const addNumViews = async () => {
  try {
    const response = await apiClient.post(`/blog/blog-posts/${ props.id }/increment_view_post/`); // Requête POST
  } catch (err) {
    console.error("Erreur lors de l'action :", err);
    alert("Une erreur est survenue.");
  }
};
</script>

<template>
  <div class="container" :style="{ backgroundImage: `url(${props.illustration})` }">
    <div class="summary">
      <nav>
        <span class="title">Sommaire</span>
        <span v-for="title in props.titles" :key="title.id">
          <RouterLink :to="{ path: `blog/${props.blogLink}`, query: { id: props.id }, hash: `#${title.summary_link}` }" @click="addNumViews"><span>&#9900; {{ title.summary }}</span></RouterLink>
        </span>
      </nav>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
  padding: 3em;
  background-image: url('./icons/1.jpg');
  background-repeat: no-repeat;
  background-size: cover;
    margin: {
        bottom: 2em;
        top: 1em;
    }
}

nav {
  display: flex;
  flex-direction: column;
  gap: 1.5em;
}

.summary {
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--main-gray);
  opacity: 0.9;
  max-width: 58em;
  height: 20em;
  overflow: auto;
}

.title {
    font-family: "Roboto Mono", system-ui;
    font-optical-sizing: auto;
    font-weight: 500;
    font-style: normal;
    font-size: 20px;
    display: block;

    &::before {
        content: '';
        display: block;
        height: 5px;
        background: var(--blue-light);
    }

    @media screen and (max-width: 1280px) {
        font-size: 1em;
    }

    @media screen and (max-width: 768px) {
        font-size: 0.9em;
    }
}

a span {
  display: block;
  color: var(--blue-light);
  font-family: "Roboto Mono", system-ui;
  font-optical-sizing: auto;
  font-weight: 300;
  font-style: normal;

  &:hover {
    font-weight: 400;
  }
  @media screen and (max-width: 1280px) {
        font-size: 1em;
    }

  @media screen and (max-width: 768px) {
      font-size: 0.9em;
  }
}
</style>
