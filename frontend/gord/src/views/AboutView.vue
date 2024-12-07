<script setup>
import { RouterLink } from 'vue-router'
import ArticleBase from '../components/ArticleBase.vue'
</script>

<template>
      <div class="content">
        <div class="section">
          <ArticleBase active-page="about" section-color="section" section="Présentation Personnelle">
            <img src="../components/icons/hacker.jpg" alt="" class="avatar">
            <br><br>
            Béninois, poète en mes heures perdues, passionné de technologie depuis ma tendre enfance, j'ai découvert l'essence même de l'informatique après avoir repris
            ma première année de mathématique. Depuis, je m'y suis accroché. Je suis tout le temps dans une nouvelle quête de 
            connaissance en informatique et je ne m'en lasse jamais. On peut dire que j'en suis devenu vraiment accro. Mes Compétences
            en mathématique font de mes projets des outils impécables dont je suis extrêmement fière. <br><br>
            Mes passes temps favoris restent prioritairement les projets informatiques sur lesquels je travaille, les jeux vidéos et aussi les mangas. <br>
            Ah! J'oubliais. J'adore aussi les maths 🥰.
          </ArticleBase>
        </div>
        <div class="section">
          <ArticleBase active-page="about" section-color="section" section="Parcours Académiques et Professionnel">
            J'ai obtenu tous mes diplômes au Bénin. <br> <br>
              <ul>
                <li>2013 - 2014: <b>Obtention du Certificat d'Etude Primaire(CEP)</b> au CSCP "Saint Pierre et St Paul" de Porto-Novo</li>
                <li>2017 - 2018: <b>Obtention du Brevet d'Etude du Premier Cycle(BEPC)</b> au CS "La Pyramide des arts" de Porto-Novo</li>
                <li>2020 - 2021: <b>Obtention du BACCALAUREAT(BAC) série C</b> au CEG "DAVIE" de Porto-Novo</li>
                <li>2024 - 2025: <b>Étudiant en 3ème année(L3) de Mathématique, Informatique et Applications</b> à la FAST de l'UAC</li>
              </ul><br>
              Je travaille actuellement en tant que developpeur freelance sur des plateformes bien connues comme <RouterLink><b>ComeUp</b></RouterLink> et <RouterLink><b>UpWork</b></RouterLink>.
          </ArticleBase>
        </div>
        <div class="section">
          <ArticleBase active-page="about" section-color="section" section="Compétences">
              <ul>
                  <li><b>Programmation</b>
                    <ul>
                      <li>Python</li>
                      <li>JavaScript</li>
                      <li>C</li>
                      <li>C++</li>
                      <li>Rust</li>
                      <li>HTML, CSS & SASS</li>
                      <li>SQL</li>
                    </ul>
                  </li><br>
                  <li><b>Frameworks</b>
                    <ul>
                      <li>Django(REST FRAMEWORK)</li>
                      <li>Vue-ionic</li>
                      <li>Vue.js</li>
                      <li>Qt</li>
                      <li>Slint</li>
                    </ul>
                  </li><br>
                  <li><b>Autres</b>
                    <ul>
                      <li>Maintenance des ordinateurs</li>
                      <li>Mathématique</li>
                      <li>Hacking(CTF Player)</li>
                      <li>Électronique(Systèmes embarqués - Arduino)</li>
                    </ul>
                  </li><br>
              </ul>
          </ArticleBase>
        </div>
        <div class="go-projects">
          <RouterLink to="/projects"> Consulter mes projets.</RouterLink>
        </div>
      </div>
</template>

<style lang="scss" scoped>
.section {
  margin-bottom: 2em;

  .avatar {
    border-radius: 14px;
    width: 411px;
    height: 450px;
  }
}

.go-projects {
  margin-top: 2em;
  margin-left: 1em;
  font: {
    family: "Roboto Mono", monospace;
    optical-sizing: auto;
    style: normal;
  }
}

ul {
  margin-left: 1em;
}

@media screen and (max-width: 744px) {
    .avatar {
      width: 350px;
      height: 410px;
    }
}
</style>
