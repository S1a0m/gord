<script setup>
import ArticleBase from '../components/ArticleBase.vue'
</script>

<template>
  <div class="content">
    <div class="section"><!--/*HERE/*/ ID-->
      <ArticleBase active-page="projetDetails" section-color="section" section="Introduction">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim  veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate  velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint  occaecat cupidatat non proident, sunt in culpa qui officia deserunt  mollit anim id est laborum  
          Ou allez directement sur cette page pour consulter les
      </ArticleBase>
    </div>
    <div class="section"><!--/*HERE/*/ ID-->
      <ArticleBase active-page="projetDetails" section-color="section" section="Section 1" />
    </div>
    <div class="section"><!--/*HERE/*/ ID-->
      <ArticleBase active-page="projetDetails" section-color="article" section="Partie 1">
          Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi temporaincidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam
      </ArticleBase>
    </div>
    <div class="section"><!--/*HERE/*/ ID-->
      <ArticleBase active-page="projetDetails" section-color="article" section="Partie 2">
          Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi temporaincidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam
      </ArticleBase>
    </div>
    <div class="section"><!--/*HERE/*/ ID-->
      <ArticleBase active-page="projetDetails" section-color="section" section="Section 2" />
    </div>
    <div class="section"><!--/*HERE/*/ ID-->
      <ArticleBase active-page="projetDetails" section-color="article" section="Partie 1">
          Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi temporaincidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam
      </ArticleBase>
    </div>
    <div class="section"><!--/*HERE/*/ ID-->
      <ArticleBase active-page="projetDetails" section-color="article" section="Partie 2">
          Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi temporaincidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam
      </ArticleBase>
    </div>
    <div class="section"><!--/*HERE/*/ ID-->
      <ArticleBase active-page="projetDetails" section-color="section" section="Conclusion">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim  veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate  velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint  occaecat cupidatat non proident, sunt in culpa qui officia deserunt  mollit anim id est laborum  
          Ou allez directement sur cette page pour consulter les
      </ArticleBase>
    </div>
  </div>
  <div id="reviews">
    <Appreciations likes="41" comments="20"/>
  </div>
</template>
  
<style lang="scss"  scoped>
.section {
  margin-bottom: 2em;

  .avatar {
    border-radius: 14px;
    width: 411px;
    height: 331px;
  }
}

.go-projects {
  font: {
    family: "Roboto Mono", monospace;
    optical-sizing: auto;
    style: normal;
  }
}
.go-projects {
  margin-top: 4em;
}

#reviews {
  margin-top: 4em;
  margin-left: 1em;
}
</style>
  