<script setup>
import { RouterLink } from 'vue-router';
import { ref, onMounted, onUnmounted } from 'vue';
import ArticleBase from '../components/ArticleBase.vue';

// Témoignages fictifs
const testimonials = ref([
  "Superbe expérience de travail, très professionnel !",
  "Une expertise technique impressionnante, bravo !",
  "Créatif, efficace et agréable à collaborer.",
  "Toujours à l'écoute et fournit des solutions adaptées.",
  "Un plaisir de travailler avec quelqu'un d'aussi talentueux."
]);

// Indice du témoignage affiché
const currentIndex = ref(0);

// Défiler automatiquement les témoignages toutes les 5 secondes
let interval = null;

const startCarousel = () => {
  interval = setInterval(() => {
    currentIndex.value = (currentIndex.value + 1) % testimonials.value.length;
  }, 5000);
};

const stopCarousel = () => {
  if (interval) {
    clearInterval(interval);
    interval = null;
  }
};

// Démarrer et arrêter le carousel selon le cycle de vie du composant
onMounted(startCarousel);
onUnmounted(stopCarousel);

// Naviguer manuellement
const nextTestimonial = () => {
  currentIndex.value = (currentIndex.value + 1) % testimonials.value.length;
};

const prevTestimonial = () => {
  currentIndex.value =
    (currentIndex.value - 1 + testimonials.value.length) %
    testimonials.value.length;
};
</script>


<template>
  <div class="content">
    <div class="section">
      <ArticleBase active-page="portfolio" section-color="section" section="Certifications et Récompenses">
        <div class="c-r">
          <p>{{ testimonials[currentIndex] }}</p>
          <div class="controls">
            <button @click="prevTestimonial">◀</button>
            <button @click="nextTestimonial">▶</button>
          </div>
        </div>
        <!--<div class="c-r">
          <div class="certificates">
            <p>Certifications</p>
          </div>
          <div class="rewards">
            <p>Récompenses</p>
          </div>
        </div>-->
      </ArticleBase>
    </div>
    <div class="section">
      <ArticleBase active-page="portfolio" section-color="section" section="Témoignages">
        <div class="testimony">
          <p>{{ testimonials[currentIndex] }}</p>
          <div class="controls">
            <button @click="prevTestimonial">◀</button>
            <button @click="nextTestimonial">▶</button>
          </div>
        </div>
      </ArticleBase>
    </div>
    <div class="go-projects">
      <RouterLink to="/projects">Consultez ici mes projets</RouterLink>
    </div>
  </div>
</template>


<style lang="scss" scoped>
.content {
  .section {
    margin-bottom: 2em;
  }
}

.c-r, .testimony {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 0.5em;
  font-size: 20px;
  color: var(--main-white);
  background: var(--main-gray);
  border: {
    style: solid;
    color: var(--blue-light);
    radius: 14px;
    width: 1px;
  }
}

.c-r, .testimony {
  width: 696px;
  height: 302px;
  position: relative;

  p {
    margin: 0;
    text-align: center;
    font-size: 1em;
    padding: 0 1em;
    @media screen and (max-width: 1280px) {
        font-size: 0.8em;
    }
  }

  .controls {
    position: absolute;
    bottom: 1em;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 1em;

    button {
      background: var(--blue-light);
      border: none;
      border-radius: 50%;
      width: 40px;
      height: 40px;
      color: var(--main-white);
      cursor: pointer;
      font-size: 1.2em;
      transition: background 0.3s ease;

      &:hover {
        background: var(--main-white);
        color: var(--blue-light);
      }
    }
  }
}

.certificates, .rewards {
  width: 302px;
  height: 469px;
}

.go-projects {
  margin-top: 4em;
  margin-left: 1em;
  &, .certificates, .rewards, .testimony {
    font: {
      family: "Roboto Mono", monospace;
      optical-sizing: auto;
      style: normal;
    }
  }
}

@media screen and (max-width: 696px) {
  .testimony, .c-r {
    width: 302px;
    height: 469px;

    .controls {
      button {
        width: 30px;
        height: 30px;
        font-size: 1em;
      }
    }
  }
}

@media screen and (max-width: 335px) {
  .testimony, .c-r {
    width: 290px;
    height: 467px;

    .controls {
      button {
        width: 30px;
        height: 30px;
        font-size: 1em;
      }
    }
  }
}
</style>
