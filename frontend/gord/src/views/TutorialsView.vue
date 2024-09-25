<script setup>
import ArticleBase from '../components/ArticleBase.vue'
import ShowcaseBase from '../components/ShowcaseBase.vue'
</script>

<template>
      <div class="content">
        <div class="section">
          <ArticleBase active-page="tutorials" section-color="section" section="Programmation">
            <div class="programmation">
              <ShowcaseBase likes="57" time="16/09/24" name="Tutoriel 1" sommary="Contenu sommaire du tutoriel 1" comments="03" details="/tutorials/tutorial1"/>
              <ShowcaseBase likes="11" time="16/09/24" name="Tutoriel 2" sommary="Contenu sommaire du tutoriel 2" comments="21" details="/tutorials/tutorial2"/>
            </div>
          </ArticleBase>
        </div>
        <div class="section">
          <ArticleBase active-page="tutorials" section-color="section" section="Sécurité">
            <div class="security">
              <ShowcaseBase likes="00" time="16/09/24" name="Tutoriel 3" sommary="Contenu sommaire du tutoriel 3" comments="00" details="/tutorials/tutorial1"/>
            </div>
          </ArticleBase>
        </div>
      </div>
</template>

<style lang="scss" scoped>
.programmation {
  display: flex;
  gap: 4em;
}

.section {
  margin-bottom: 2em;
}

p {
  margin-top: 0.5em;
  font-size: 20px;
  color: #f5f5f5;
  background: #1C1A1A;
  border: {
    style: solid;
    color: #288F9E;
    radius: 14px;
    width: 1px;
  }
}

.go-projects {
  margin-top: 4em;
  &, p {
    font: {
      family: "Roboto Mono", monospace;
      optical-sizing: auto;
      style: normal;
    }
  }
}
</style>
