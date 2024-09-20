<script setup>
import { RouterLink } from 'vue-router'
import ArticleBase from '../components/ArticleBase.vue'
</script>

<template>
      <div class="content">
        <div class="section">
          <ArticleBase active-page="portfolio" section-color="section" section="Certifications et Récompenses">
            <div class="c-r">
              <div class="certificates">
                <p>Certifications</p>
              </div>
              <div class="rewards">
                <p>Récompenses</p>
              </div>
            </div>
          </ArticleBase>
        </div>
        <div class="section">
          <ArticleBase active-page="portfolio" section-color="section" section="Témoignages">
            <div class="testimony">
              <p>Témoignages</p>
            </div>
          </ArticleBase>
        </div>
        <div class="go-projects">
          Consultez <RouterLink to="/projects">ici mes projets</RouterLink>
        </div>
      </div>
</template>

<style scoped>

.section {
  margin-bottom: 2em;
}

.c-r {
  display: flex;
  gap: 6em;
}

.certificates, .rewards, .testimony {
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
