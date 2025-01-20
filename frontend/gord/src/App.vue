<script setup>
import { ref } from 'vue';
import { RouterView, useRoute } from 'vue-router';
import { computed } from 'vue';
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
import LeftLayout from './components/LeftLayout.vue';
import BlogSummaries from './components/BlogSummaries.vue';

const route = useRoute();

// Un mapping des noms de routes à leurs titres
const pageTitles = {
  home: 'home',
  about: 'about',
  portfolio: 'portfolio',
  blog: 'blog',
  projects: 'projects',
  faq: 'faq',
  details: 'details',
};


// Stocker les données récupérées
const blogSummaries = ref([]);

// Fonction pour mettre à jour les données
const updateBlogSummaries = (data) => {
  blogSummaries.value = data;
};

// Utilisation de computed pour récupérer le titre dynamiquement
const pageTitle = computed(() => pageTitles[route.name] || route.name);

const search = ref('reduce-search-input');
const hideGoSearch = ref(false);

const toggleSearch = () => {
  search.value = search.value === 'reduce-search-input' ? 'show-search-input' : 'reduce-search-input';
  hideGoSearch.value = !hideGoSearch.value;
};

//
// 
</script>


<template>
  <Header @toggle-search="toggleSearch"/>
  <div class="container">
   <div class="left-layout">
    <BlogSummaries v-if="route.name === 'blog-lecture'" :summaries="blogSummaries"/>
    <LeftLayout/>
   </div>
    <main>
      <h2>
        <span class="page-title">{{ pageTitle }}@pxdev:~$</span> 
        <form action="">
          <input type="search" name="search" :id="search" placeholder="Search a blog...">
        </form>
      </h2>
      <Transition name="fade" mode="out-in">
        <RouterView @blog-summary="updateBlogSummaries" />
      </Transition>
    </main>
  </div>
  <Footer />
</template>
  
<style lang="scss" scoped>
h2 {
  color: var(--green-hack);
  display: flex;
  margin: {
    //top: 5em;
    top: 1em;
    bottom: 1em;
  }
  font: {
    family: "Roboto Mono", monospace;
    optical-sizing: auto;
    style: normal;
  }

  @media screen and (max-width: 768px) {
      font-size: 1.1em;
  }
}

main {
  // width: 66vw;
  border-left-style: solid;
  // border-right-style: solid;
  border-width: 1px;
  border-color: var(--main-gray);
  overflow: auto;
}

.container {
  display: flex;
  min-height: 90vh;
  width: 100%;
}

section {
    padding: 1em;
}

#reduce-search-input {
    height: 30px;
    width: 10px;
    background-color: var(--main-white);
    pointer-events: none;
    animation: blink 1.2s step-end infinite;
    @media screen and (max-width: 1280px) {
      height: 28px;
    }
}

#show-search-input {
    height: 50px;
    width: 330px;
    color: var(--main-white);
    background: var(--main-black);
    pointer-events: all;
    animation: none;
    font-size: 20px;
    border-bottom-style: solid;
    border-color: var(--green-hack);
    border-width: 1px;
}

[type="search"] {
  border-style: none;
  outline: none;
  padding-left: 1em;
  margin-left: 10px;
  transition: all 0.5s ease;
  font-family: "Roboto Mono", system-ui;
  font-optical-sizing: auto;
  font-weight: 400;
  font-style: normal;
}

.go-search {
  background: none;
  font-weight: bold;
  font-size: 20px;
  font-family: "Roboto Mono", system-ui;
  border-style: none;
  color: var(--green-hack);
  cursor: pointer;
}

@keyframes blink {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(15px);
}

@media (prefers-reduced-motion: reduce) {
  .fade-enter-active,
  .fade-leave-active {
    transition: none;
  }
}


@media screen and (max-width: 1280px) {
  .left-layout {
    display: none;
  }
  main {
    width: 100%;
  }
}
</style>
  