<script setup>
import { RouterLink } from 'vue-router';
import ArticleBase from '../components/ArticleBase.vue';
</script>

<template>
  <div class="content">
    <div class="section">
      <ArticleBase active-page="about" section-color="section" section="Présentation Personnelle">
        <div class="backg-hov">
          <img src="../components/icons/hacker.jpg" alt="Avatar de l'auteur" class="avatar">
          <br><br>
          <p>
          Béninois, poète en mes heures perdues, passionné de technologie depuis ma tendre enfance, j'ai découvert l'essence même de l'informatique après avoir repris
          ma première année de mathématique. Depuis, je m'y suis accroché. Je suis tout le temps dans une nouvelle quête de 
          connaissance en informatique et je ne m'en lasse jamais. On peut dire que j'en suis devenu vraiment accro. Mes compétences
          en mathématique font de mes projets des outils impeccables dont je suis extrêmement fier. <br><br>
          Mes passe-temps favoris restent prioritairement les projets informatiques sur lesquels je travaille, les jeux vidéo et aussi les mangas. <br>
          Ah! J'oubliais. J'adore aussi les maths 🥰.
          </p>
        </div>
      </ArticleBase>
    </div>
    <div class="section">
      <ArticleBase active-page="about" section-color="section" section="Parcours Académiques et Professionnel">
        <div class="backg-hov">
        
        Ah! Mon parcours.🤧 <br><br>
        <ul>
          <li>2013 - 2014: <b>Obtention du Certificat d'Études Primaires (CEP)</b> au CSCP "Saint Pierre et St Paul" de Porto-Novo</li>
          <li>2017 - 2018: <b>Obtention du Brevet d'Études du Premier Cycle (BEPC)</b> au CS "La Pyramide des arts" de Porto-Novo</li>
          <li>2020 - 2021: <b>Obtention du Baccalauréat (BAC) série C</b> au CEG "DAVIE" de Porto-Novo</li>
          <li>2024 - 2025: <b>Étudiant en 3ème année (L3) de Mathématique, Informatique et Applications</b> à la FAST de l'UAC</li>
        </ul><br>
        </div>
      </ArticleBase>
    </div>
    <div class="section">
      <ArticleBase active-page="about" section-color="section" section="Projets en cours">
        <div class="backg-hov">
          <p>
            Je travaille actuellement en tant que développeur freelance sur des plateformes bien connues comme <a href="https://comeup.com/"><b>ComeUp</b></a> , <a href="https://www.upwork.com/"><b>UpWork</b></a> et <a href="https://fr.fiverr.com/"><b>Fiver</b></a>.
            Je suis également: 
          </p><br>
          <ul>
            <li><b>Co-fondateur d'un projet de commerce numérique moderne:</b> Je collabore avec des partenaires pour révolutionner les solutions de commerce électronique.</li>
            <li><b>Fondateur d'une entreprise émergente high tech (non officiel) nommée <a href="https://www.amo-iv.tech">AMO-IV</a>:</b> Nous développons actuellement notre premier produit, avec des mises à jour à suivre prochainement.</li>
          </ul>
        </div>
      </ArticleBase>
    </div>
    <div class="section">
      <ArticleBase active-page="about" section-color="section" section="Compétences">
        <div class="backg-hov">
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
                <li>Dart</li>
              </ul>
            </li><br>
            <li><b>Frameworks</b>
              <ul>
                <li>Django (REST Framework)</li>
                <li>Vue.js</li>
                <li>Qt</li>
                <li>Slint</li>
                <li>Flutter</li>
              </ul>
            </li><br>
            <li><b>Autres</b>
              <ul>
                <li>Maintenance des ordinateurs</li>
                <li>Mathématiques</li>
                <li>Hacking (CTF Player)</li>
                <li>Électronique (Systèmes embarqués - Arduino)</li>
              </ul>
            </li><br>
          </ul>
          Voila 😁.
        </div>
      </ArticleBase>
    </div>
    <div class="go-projects"> 
      Consulter <RouterLink to="/projects">mes projets</RouterLink>.
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

.backg-hov {
  padding: 1em;
  border-radius: 10px;
}

.backg-hov:hover {
  background: var(--hover-article);
}

p, ul {

  @media screen and (max-width: 1280px) {
        font-size: 1em;
    }

  @media screen and (max-width: 768px) {
      font-size: 0.9em;
  }
}

@media screen and (max-width: 744px) {
  .section .avatar {
    width: 350px;
    height: 410px;
  }
}

@media screen and (max-width: 370px) {
  .section .avatar {
    max-width: 310px;
    height: 410px;
  }
}

@media screen and (max-width: 744px) {
  .backg-hov {
        background: var(--hover-article);
    }
}
</style>
