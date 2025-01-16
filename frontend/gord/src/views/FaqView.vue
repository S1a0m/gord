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
          <p>
            {{ i.response }}
          </p>
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
}
</style>
