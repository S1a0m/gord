<script setup>
import BlogArticle from '../components/BlogArticle.vue' 
import Loader from '@/components/Loader.vue';
import apiClient from '../axios';
import { ref, onMounted } from 'vue';

const articles = ref([]);
const error = ref(null);
const isLoading = ref(true);

const fetchArticles = async () => {
  try {
    const response = await apiClient.get('/blog/blog-posts/');
    articles.value = response.data;
  } catch(err) {
    error.value = "Une erreur est survenue."
    console.error(err);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchArticles();
})
</script>

<template>
      <div class="content">
        <p v-if="isLoading"><!--Chargement des articles...-->
          <Loader />
        </p>
        <p v-else-if="error">{{ error }}</p>
        <div class="section" v-for="article in articles" :key="article.id">
          <BlogArticle :time="article.published_date" :section="article.title" :views="article.number_read" :titles="article.summary" :link="article.link">
            <p>
              {{ article.outline }}
            </p>
          </BlogArticle>
        </div>
      </div>
</template>

<style lang="scss" scoped>
.section {
  margin-bottom: 2em;
}

p {
  font-size: 16px;
  color: var(--main-white);
  font: {
    family: "Roboto Mono", monospace;
    optical-sizing: auto;
    style: normal;
  }
}
</style>
