<script setup>
import ArticleBase from '../components/ArticleBase.vue'
</script>

<template>
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
</template>

<style lang="scss" scoped>
.section {
  margin-bottom: 2em;
}

p {
  margin-top: 0.5em;
  font-size: 16px;
  color: var(--main-white);
  font: {
    family: "Roboto Mono", monospace;
    optical-sizing: auto;
    style: normal;
  }
}
</style>
