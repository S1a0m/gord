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

<style lang="scss" scoped>
.content {
  .section {
    margin-bottom: 2em;
  }
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
  box-shadow: .1em .1em 2em #505050;
  border: {
    style: solid;
    color: #288F9E;
    radius: 14px;
    width: 1px;
  }
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
  &, .certificates, .rewards, .testimony {
    font: {
      family: "Roboto Mono", monospace;
      optical-sizing: auto;
      style: normal;
    }
  }
}
</style>
