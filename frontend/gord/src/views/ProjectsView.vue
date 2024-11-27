<script setup>
import ArticleBase from '../components/ArticleBase.vue'
import ShowcaseBase from '../components/ShowcaseBase.vue'
</script>

<template>
      <div class="content">
        <div class="section">
          <ArticleBase active-page="projects" section-color="section" section="Developpement">
            <div class="programmation">
              <ShowcaseBase likes="11" time="16/09/24" name="PxDev" sommary="Contenu sommaire du projet" comments="21" details="/projects/project2-details"/>
              <ShowcaseBase likes="11" time="16/09/24" name="GLYC" sommary="Contenu sommaire du projet" comments="21" details="/projects/project2-details"/>
              <ShowcaseBase likes="11" time="16/09/24" name="WikiAlgo" sommary="Contenu sommaire du projet" comments="21" details="/projects/project2-details"/>
              <ShowcaseBase likes="11" time="16/09/24" name="PX" sommary="Contenu sommaire du projet" comments="21" details="/projects/project2-details"/>
            </div>
          </ArticleBase>
        </div>
        <div class="section">
          <ArticleBase active-page="projects" section-color="section" section="Hacking">
            <div class="security">
              <ShowcaseBase likes="57" time="16/09/24" name="coDS" sommary="Contenu sommaire du projet" comments="03" details="/projects/project1-details"/><!--/*HERE/*/-->
              <ShowcaseBase likes="11" time="16/09/24" name="Racine" sommary="Contenu sommaire du projet" comments="21" details="/projects/project2-details"/><!--/*HERE/*/-->
              <ShowcaseBase likes="57" time="16/09/24" name="Wind" sommary="Contenu sommaire du projet" comments="03" details="/projects/project1-details"/>
            </div>
          </ArticleBase>
        </div>
        <div class="section">
          <ArticleBase active-page="projects" section-color="section" section="Intelligence Artificielle">
            <div class="ia">
              <ShowcaseBase likes="11" time="16/09/24" name="Morgane" sommary="Contenu sommaire du projet" comments="21" details="/projects/project2-details"/>
            </div>
          </ArticleBase>
        </div>
        <div class="section">
          <ArticleBase active-page="projects" section-color="section" section="Mathématique">
            <div class="ia">
              <ShowcaseBase likes="11" time="16/09/24" name="Appal" sommary="Contenu sommaire du projet" comments="21" details="/projects/project2-details"/>
            </div>
          </ArticleBase>
        </div>
      </div>
</template>

<style lang="scss" scoped>
.programmation, .security {
  display: flex;
  flex-wrap: wrap;
  gap: 4em;
}

.section {
  margin-bottom: 2em;
}

.go-projects {
  margin-top: 4em;
  & {
    font: {
      family: "Roboto Mono", monospace;
      optical-sizing: auto;
      style: normal;
    }
  }
}
</style>
