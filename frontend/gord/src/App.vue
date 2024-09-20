<script setup>
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
</script>

<template>
  <Header />
  <div class="container">
   <div class="left-layout">
    <LeftLayout />
   </div>
    <hr class="hr-one">
    <main>
      <h2>{{ pageTitle }}@gord:~$ <span class="cursor"></span></h2>
      <RouterView />
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
  <Footer />
</template>
  
<style scoped>
h2 {
  color: #00ff00;
  margin-top: 2em;
  margin-bottom: 1em;

  font-family: "Roboto Mono", monospace;
  font-optical-sizing: auto;
  font-style: normal;
  font-size: 20px;
}

main {
  min-width: 68vw;
  max-width: 68vw;
}

.container {
  display: flex;
  min-height: 90vh;
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
  