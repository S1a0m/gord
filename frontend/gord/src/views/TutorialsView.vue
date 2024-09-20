<script setup>
import ArticleBase from '../components/ArticleBase.vue'
import ShowcaseBase from '../components/ShowcaseBase.vue'
</script>

<template>
      <div class="content">
        <div class="section">
          <ArticleBase active-page="tutorials" section-color="section" section="Programmation">
            <div class="programmation">
              <ShowcaseBase likes="57" time="16/09/24" name="Tutoriel 1" sommary="Contenu sommaire du tutoriel" comments="03" details="/tutorials/tutorial1"/>
              <ShowcaseBase likes="11" time="16/09/24" name="Tutoriel 2" sommary="Contenu sommaire du tutoriel" comments="21" details="/tutorials/tutorial2"/>
            </div>
          </ArticleBase>
        </div>
        <div class="section">
          <ArticleBase active-page="tutorials" section-color="section" section="Sécurité">
            <div class="security">
              <ShowcaseBase likes="00" time="16/09/24" name="Tutoriel 3" sommary="Contenu sommaire du tutoriel" comments="00" details="/tutorials/tutorial1"/>
            </div>
          </ArticleBase>
        </div>
      </div>
</template>

<style scoped>
.programmation {
  display: flex;
  gap: 4em;
}

.section {
  margin-bottom: 2em;
}

.c-r {
  display: flex;
  gap: 6em;
}

p {
  margin-top: 0.5em;
  font-size: 20px;
  color: #f5f5f5;
  background: #1C1A1A;
  border-style: solid;
  border-color: #288F9E;
  border-radius: 14px;
  border-width: 1px;


  font-family: "Roboto Mono", monospace;
  font-optical-sizing: auto;
  font-style: normal;
}

.testimony {
  width: 696px;
  height: 302px;
}

.certificates, .rewards {
  width: 302px;
  height: 469px;
}

.go-projects {
  margin-top: 4em;

  font-family: "Roboto Mono", monospace;
  font-optical-sizing: auto;
  font-style: normal;
}
</style>
