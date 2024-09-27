<script setup>
import { ref } from 'vue';
import { RouterView, RouterLink, useRoute } from 'vue-router'
import { computed } from 'vue';
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import LeftLayout from './components/LeftLayout.vue'
import RightLayout from './components/RightLayout.vue'


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
    case 'tutorials':
      return 'tutorials';
    case 'faq':
      return 'faq';
    default:
      return 'Page';
  }
});

const search = ref('reduce-search-input');

const toggleSearch = () => {
  search.value = search.value ===  'reduce-search-input'? 'show-search-input': 'reduce-search-input';
}
</script>

<template>
  <Header @toggle-search="toggleSearch"/>
  <div class="container">
   <div class="left-layout">
    <LeftLayout />
   </div>
    <hr class="hr-one">
    <main>
      <h2>
        {{ pageTitle }}@gord:~$ 
        <form action="">
          <input type="search" name="search" :id="search" placeholder="Tape here to search">
        </form>
      </h2>
      <Transition name="fade" mode="out-in">
        <RouterView />
      </Transition>
    </main>
    <hr class="hr-two">
    <RightLayout>
      <div class="right-layout">
        Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium<br><a href="#">&#10140;</a>
        <br><br>
        Lorem ipsum dolor sit amet<br><a href="#">&#10140;</a>
        <br><br>
        Voir plus de détails en consultant mon <RouterLink to="/blog">blog</RouterLink>
      </div>
    </RightLayout>
  </div>
  <Footer />
</template>
  
<style lang="scss" scoped>
h2 {
  color: #00ff00;
  display: flex;
  margin: {
    top: 2em;
    bottom: 1em;
  }
  font: {
    family: "Roboto Mono", monospace;
    optical-sizing: auto;
    style: normal;
  }
}

main {
  min-width: 68vw;
  max-width: 68vw;
}

.container {
  display: flex;
  min-height: 90vh;
}


.right-layout {
  margin-top: 2em;
  font-size: 15px;
  padding: 1em;
  font: {
    family: "Roboto", system-ui;
    weight: 300;
    style: normal;
  }

  
}

section {
    padding: 1em;
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

#reduce-search-input {
    height: 30px;
    width: 10px;
    background-color: #f5f5f5;
    pointer-events: none;
    animation: blink 1.2s step-end infinite;
}

#show-search-input {
    height: 50px;
    width: 330px;
    color: #f5f5f5;
    background: #0A0A0A/*#505050*#1C1A1A*/;
    pointer-events: all;
    animation: none;
    font-size: 20px;
    /*border-radius: 14px;*/
    border-bottom-style: solid;
    border-color: #00ff00;
    border-width: 1px;
}

[type="search"] {
  border-style: none;
  outline: none;
  padding-left: 1em;
  margin-left: 5px;
  transition: all 0.5s ease;
  font-family: "Roboto Mono", system-ui;
  font-optical-sizing: auto;
  font-weight: 400;
  font-style: normal;
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
  /*transform: scale(1.1)/*translateX(80em)*/;
}
/*
.fade-leave-to {
  opacity: 0;
  transform: scale(1.1)/*translateX(80em)*;
}*/
</style>
  