<script setup>
import { ref } from 'vue';
import { RouterView, useRoute } from 'vue-router'
import { computed } from 'vue';
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import LeftLayout from './components/LeftLayout.vue'
import RightLayout from './components/RightLayout.vue'
import ProjTutSummary from './components/ProjTutSummary.vue';
import MenuG from './components/MenuG.vue';


const route = useRoute();

const pageTitle = computed(() => {
  switch (route.name) {
    case 'home':
      return 'home';
    case 'about':
      return 'about';
    case 'portfolio':
      return 'portfolio';
    case 'blog':
      return 'blog';
    case 'projects':
      return 'projects';
    case 'faq':
      return 'faq';
    case 'details':
      return 'details';
    default:
      return 'Page';
  }
});

const search = ref('reduce-search-input');
const hideGoSearch = ref(false);

const toggleSearch = () => {
  search.value = search.value ===  'reduce-search-input'? 'show-search-input': 'reduce-search-input';
  hideGoSearch.value = !hideGoSearch.value;
}
</script>

<template>
  <Header @toggle-search="toggleSearch"/>
  <div class="container">
   <div class="left-layout">
    <ProjTutSummary v-if="route.name === 'project-details' || route.name === 'blog-details'"/>
    <LeftLayout v-else/>
   </div>
    <main>
      <h2>
        <span class="page-title">{{ pageTitle }}@pxdev:~$</span> 
        <form action="">
          <input type="search" name="search" :id="search" placeholder="Write here to search">
          <!--<Button type="square-v2" v-if="hideGoSearch"><input type="submit" value="Go" class="go-search"></Button>-->
        </form>
      </h2>
      <Transition name="fade" mode="out-in">
        <RouterView />
      </Transition>
    </main>
    <div class="right-layout">
      <RightLayout>
          Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium<br><a href="#">&#10140;</a>
          <br><br>
          Lorem ipsum dolor sit amet<br><a href="#">&#10140;</a>
          <br><br>
          <!--Voir plus de détails en consultant mon <RouterLink to="/blog">blog</RouterLink>-->
      </RightLayout>
    </div>
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
}

main {
  width: 66vw;
  border-left-style: solid;
  border-right-style: solid;
  border-width: 1px;
  border-color: var(--main-gray);
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
  transition: opacity 1.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@media screen and (max-width: 1280px) {
  .left-layout, .right-layout {
    display: none;
  }
  main {
    width: 100%;
  }
}
</style>
  