<script setup>
import { RouterLink } from 'vue-router'
import LeftLayout from '../components/LeftLayout.vue'
import RightLayout from '../components/RightLayout.vue'
import ArticleBase from '../components/ArticleBase.vue'
</script>

<template>
  <div class="container">
    <LeftLayout />
    <hr class="hr-one">
    <main>
      <h2>faq@gord:~$ <span class="cursor"></span></h2>
      <div class="section">
      <ArticleBase active-page="faq" section-color="section" section="Question 1">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim  veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate  velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint  occaecat cupidatat non proident, sunt in culpa qui officia deserunt  mollit anim id est laborum  
          Ou allez directement sur cette page pour consulter les
        </p>
      </ArticleBase>
      <div class="section">
        <ArticleBase active-page="faq" section-color="section" section="Question 2">
          <p>
            Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi temporaincidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam
          </p>
        </ArticleBase>
      </div>
      <div class="section">
        <ArticleBase active-page="faq" section-color="section" section="Question 3">
          <p>
            Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur,
          </p>
        </ArticleBase>
      </div>
      <div class="section">
        <ArticleBase active-page="faq" section-color="section" section="Question 4">
          <p>
            Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi temporaincidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam
          </p>
        </ArticleBase>
      </div>
      </div>
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
}

.right-layout, section {
  padding: 1em;
}

.section {
  margin-bottom: 2em;
}

.right-layout {
  margin-top: 2em;
  font-size: 15px;
  font-family: "Roboto", system-ui;
  font-weight: 300;
  font-style: normal;
}

p {
  margin-top: 0.5em;
  padding-right: 10em;
  font-size: 16px;
  color: #f5f5f5;

  font-family: "Roboto Mono", monospace;
  font-optical-sizing: auto;
  font-style: normal;
}

h2 {
  color: #00ff00;
  margin-top: 2em;
  margin-bottom: 1em;

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
