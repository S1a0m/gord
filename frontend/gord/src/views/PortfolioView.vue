<script setup>
import { RouterLink } from 'vue-router';
import { ref, onMounted, onUnmounted } from 'vue';
import apiClient from '../axios';
import ArticleBase from '../components/ArticleBase.vue';

// Références pour les carrousels
const professionalExperiences = ref([]);
const testimonials = ref([]);

// Indices pour les carrousels
const currentExperienceIndex = ref(0);
const currentTestimonialIndex = ref(0);

// Intervalle pour les carrousels
let experienceInterval = null;
let testimonialInterval = null;

// Charger les données depuis le backend
const fetchData = async () => {
  try {
    // Adapter les URLs selon vos endpoints backend
    const experienceResponse = await apiClient.get('portfolio/experiences');
    const testimonialResponse = await apiClient.get('portfolio/testimonials');
    professionalExperiences.value = experienceResponse.data;
    testimonials.value = testimonialResponse.data;
  } catch (error) {
    console.error('Erreur lors du chargement des données :', error);
  }
};

// Gestion des carrousels
const startExperienceCarousel = () => {
  experienceInterval = setInterval(() => {
    currentExperienceIndex.value = 
      (currentExperienceIndex.value + 1) % professionalExperiences.value.length;
  }, 5000);
};

const startTestimonialCarousel = () => {
  testimonialInterval = setInterval(() => {
    currentTestimonialIndex.value = 
      (currentTestimonialIndex.value + 1) % testimonials.value.length;
  }, 5000);
};

const stopCarousels = () => {
  if (experienceInterval) clearInterval(experienceInterval);
  if (testimonialInterval) clearInterval(testimonialInterval);
};

// Cycle de vie du composant
onMounted(async () => {
  await fetchData();
  startExperienceCarousel();
  startTestimonialCarousel();
});

onUnmounted(() => {
  stopCarousels();
});

// Navigation manuelle
const nextExperience = () => {
  currentExperienceIndex.value = 
    (currentExperienceIndex.value + 1) % professionalExperiences.value.length;
};

const prevExperience = () => {
  currentExperienceIndex.value =
    (currentExperienceIndex.value - 1 + professionalExperiences.value.length) %
    professionalExperiences.value.length;
};

const nextTestimonial = () => {
  currentTestimonialIndex.value = 
    (currentTestimonialIndex.value + 1) % testimonials.value.length;
};

const prevTestimonial = () => {
  currentTestimonialIndex.value =
    (currentTestimonialIndex.value - 1 + testimonials.value.length) %
    testimonials.value.length;
};
</script>



<template>
  <div class="content">
    <!-- Section Expériences Professionnelles -->
    <div class="section">
      <ArticleBase active-page="portfolio" section-color="section" section="Certifications et Récompenses">
        <div class="c-r">
          <p v-if="professionalExperiences.length">
            {{ professionalExperiences[currentExperienceIndex].about }}
            <a :href="professionalExperiences[currentExperienceIndex].proof_link" v-if="professionalExperiences[currentExperienceIndex].proof_link.length">ici</a>
          </p>
          <div class="controls">
            <button @click="prevExperience">◀</button>
            <button @click="nextExperience">▶</button>
          </div>
        </div>
      </ArticleBase>
    </div>

    <!-- Section Témoignages -->
    <div class="section">
      <ArticleBase active-page="portfolio" section-color="section" section="Témoignages">
        <div class="testimony">
          <p v-if="testimonials.length">
            <span class="quotes">"</span>
            {{ testimonials[currentTestimonialIndex].message }}
            <span class="quotes">"</span>
          </p>
          <div class="about-author">
            <img 
              v-if="testimonials.length"
              :src="testimonials[currentTestimonialIndex].avatar" 
              alt="" 
              class="avatar">
            <b v-if="testimonials.length" class="author-name">
              {{ testimonials[currentTestimonialIndex].author_name }}
            </b>
          </div>
          <div class="controls">
            <button @click="prevTestimonial">◀</button>
            <button @click="nextTestimonial">▶</button>
          </div>
        </div>
      </ArticleBase>
    </div>

    <!-- Lien vers les projets -->
    <div class="go-projects">
      Consultez ici <RouterLink to="/projects">mes projets</RouterLink>.
    </div>
  </div>
</template>



<style lang="scss" scoped>
.content {
  .section {
    margin-bottom: 2em;
  }
}

.about-author {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 0.5em;
}

.author-name {
  font-style: oblique;
  color: var(--blue-light);
  @media screen and (max-width: 1280px) {
    font-size: 0.8em;
  }
}

.quotes {
  font-weight: bold;
  font-size: 3em;
  font-style: italic;
}

.c-r, .testimony {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 0.5em;
  font-size: 20px;
  color: var(--main-white);
  background: var(--main-gray);
  overflow: auto;
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
    text-align: center;
    font-size: 1em;
    //padding: 0 1em;
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

.avatar {
  width: 5em;
  height: 5em;
  border-radius: 50%;
  position: relative;
}

@media screen and (max-width: 696px) {
  .testimony, .c-r {
    width: 302px;
    height: 410px;

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
    height: 410px;

    .controls {
      button {
        width: 30px;
        height: 30px;
        font-size: 1em;
      }
    }
  }
}

@media screen and (max-width: 744px) {
  .backg-hov {
        background: var(--hover-article);
    }
}
</style>
