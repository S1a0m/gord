<script setup>
import { RouterLink } from 'vue-router'
import ArticleBase from '../components/ArticleBase.vue'
</script>

<template>
        <ArticleBase active-page="home" section-color="section" section="Hola, je suis Précieux Samson AMOUSSOU">
          <img src="../components/icons/hacker.jpg" alt="" class="avatar">
          <p>
            Développeur Full-Stack et passionné de technologie, je propose mes services pour la conception et le développement de projets web, mobiles et logiciels sur mesure. Mon expertise couvre une large gamme de technologies, dont HTML, CSS, JavaScript, Vue.js, Django, Qt et Rust, ainsi que l'intégration de bases de données SQL. <br><br>

Je réalise des sites web modernes et performants, des applications mobiles intuitives et des outils logiciels robustes adaptés aux besoins spécifiques de mes clients. Par ailleurs, ma passion pour la cybersécurité me permet d'offrir des solutions sûres et optimisées. <br><br>

Que ce soit pour créer une interface utilisateur attractive, développer un système backend puissant ou sécuriser vos projets, je mets tout en œuvre pour répondre à vos attentes avec rigueur et créativité. Mon objectif est de transformer vos idées en solutions concrètes et efficaces. <br>
            <span class="link"><RouterLink to="/about">Voir plus de détails en cliquant ici</RouterLink></span> <br><br>
            Ou allez sur cette page pour <span class="link"><RouterLink to="/projects">consulter mes projets</RouterLink></span>
          </p>
        </ArticleBase>
</template>

<style lang="scss" scoped>
.avatar {
  border-radius: 14px;
  width: 411px;
  height: 450px;

  @media screen and (max-width: 744px) {
    width: 350px;
    height: 410px;
  }

  @media screen and (max-width: 370px) {
    max-width: 310px;
    height: 410px;
  }
}

p {
  margin-top: 1.5em;
  font-size: 16px;
  color: var(--main-white);
  font: {
    family: "Roboto Mono", monospace;
    optical-sizing: auto;
    style: normal;
  }

  @media screen and (max-width: 1280px) {
        font-size: 1em;
    }

  @media screen and (max-width: 768px) {
      font-size: 0.9em;
  }
}
</style>
