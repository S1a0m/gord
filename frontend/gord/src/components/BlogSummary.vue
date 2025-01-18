<script setup>
import {RouterLink} from 'vue-router'
import apiClient from '../axios';

const props = defineProps([
  'titles',
  'blogLink',
  'id'
])// `blog/${blogLink}/${title.summary_link}`

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
  <div class="container">
    <div class="summary">
      <nav>
        <span class="title">Summary</span>
        <span v-for="title in props.titles" :key="title.id">
          <RouterLink :to="{ path: `blog/${props.blogLink}`, query: { id: props.id }, hash: `#${title.summary_link}` }" @click="addNumViews"><span>&#9900; {{ title.summary }}</span></RouterLink>
        </span>
      </nav>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
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
  max-width: 58em;
  height: 20em;
  overflow: auto;
  /*border-radius: 14px;
  border-color: #288F9E;*/
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
