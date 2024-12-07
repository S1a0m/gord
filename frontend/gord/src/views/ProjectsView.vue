<script setup>
import ArticleBase from '../components/ArticleBase.vue'
import ShowcaseBase from '../components/ShowcaseBase.vue'
import apiClient from '../axios';
import { ref, onMounted } from 'vue';


const articles = ref([]);
const error = ref(null);
const isLoading = ref(true);

const categories = [
  { label: 'Development', key: 'dev' },
  { label: 'Cybersecurity', key: 'cyber' },
  { label: 'Artificial Intelligence', key: 'ia' },
  { label: 'Mathematics', key: 'math' },
  { label: 'Electronic', key: 'elec' },
];

const fetchArticles = async () => {
  try {
    const response = await apiClient.get('/projects/projects/');
    articles.value = response.data;
  } catch (err) {
    error.value = "Une erreur est survenue lors du chargement des articles.";
    console.error(err);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchArticles();
});
</script>

<template>
  <p v-if="isLoading">Chargement des articles...</p>
  <p v-else-if="error">{{ error }}</p>
  <div class="content" v-else>
    <div 
      class="section" 
      v-for="category in categories" 
      :key="category.key"
    >
      <ArticleBase 
        active-page="projects" 
        section-color="section" 
        :section="category.label"
      >
        <div class="articles">
          <!-- Filtrer les articles par catégorie -->
          <div 
            class="article" 
            v-for="article in articles.filter(a => a.category === category.label)" 
            :key="article.id"
          >
            <ShowcaseBase 
              :id="article.id"
              :time="article.release_date" 
              :name="article.name" 
              :sommary="article.summary" 
              :details="article.link" 
              :views="article.number_read" 
            />
          </div>
          <!-- Message si aucun article dans cette catégorie -->
          <div v-if="articles.filter(a => a.category === category.label).length === 0">
            <p>Aucun projet disponible pour {{ category.label }}.</p>
          </div>
        </div>
      </ArticleBase>
    </div>
  </div>
</template>


<style lang="scss" scoped>
.programmation, .security {
  display: flex;
  flex-wrap: wrap;
  gap: 4em;
}

.section {
  margin-bottom: 2em;
}

.go-projects {
  margin-top: 4em;
  & {
    font: {
      family: "Roboto Mono", monospace;
      optical-sizing: auto;
      style: normal;
    }
  }
}

.articles {
  display: flex;
  flex-wrap: wrap;
  gap: 3em;
}
</style>
