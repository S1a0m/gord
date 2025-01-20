<script setup>
import ArticleBase from '../components/ArticleBase.vue'
import Loader from '@/components/Loader.vue';
import apiClient from '../axios';
import { ref, onMounted } from 'vue';

const faq = ref([]);
const error = ref(null);
const isLoading = ref(true);

const fetchFaq = async () => {
  try {
    const response = await apiClient.get('/faq/faq/');
    faq.value = response.data;
  } catch(err) {
    error.value = "Une erreur est survenue."
    console.error(err);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchFaq();
})
</script>

<template>
      <p v-if="isLoading"><!--Chargement des articles...-->
        <Loader />
      </p>
      <p v-else-if="error">{{ error }}</p>
      <div class="section" v-for="i in faq" :key="i.id">
        <ArticleBase active-page="faq" section-color="section" :section="i.question">
          <div class="backg-hov">
            <p>
              {{ i.response }}
            </p>
          </div>
        </ArticleBase>
      </div>
</template>

<style lang="scss" scoped>
.section {
  margin-bottom: 2em;
}

p {
  margin-top: 0.5em;
  font-size: 16px;
  color: var(--main-white);
  font: {
    family: "Roboto Mono", monospace;
    optical-sizing: auto;
    style: normal;
  }
  @media screen and (max-width: 1280px) {
    font-size: 0.9em;
  }
}

.backg-hov {
  padding: 1em;
  border-radius: 10px;
}

.backg-hov:hover {
  background: var(--hover-article);
}

@media screen and (max-width: 744px) {
  .backg-hov {
        background: var(--hover-article);
    }
}
</style>
