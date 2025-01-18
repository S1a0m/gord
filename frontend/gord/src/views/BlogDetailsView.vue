<script setup>
import ArticleBase from '../components/ArticleBase.vue'
import Loader from '@/components/Loader.vue';
import { useRoute } from 'vue-router';
import apiClient from '../axios';
import { ref, onMounted } from 'vue';
import BlogSummaries from '@/components/BlogSummaries.vue';

const blog_sections = ref([]);
const error = ref(null);
const isLoading = ref(true);
const route = useRoute();

    
const emit = defineEmits(['blog-summary']);

const fetchArticles = async () => {
  try {
    const response = await apiClient.get(`/blog/blog-posts/${route.query.id}/with-sections/`);

    blog_sections.value = response.data;
    emit('blog-summary', blog_sections.value);
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
    <p v-if="isLoading"><!--Chargement des articles...-->
      <Loader />
    </p>

    <!-- Gestion des erreurs -->
    <div v-else-if="error" class="error">
      {{ error }}
    </div>
  <div class="content" v-else>
    <div class="section" v-for="section in blog_sections.summaries" :id="section.summary_link">
      <ArticleBase :active-page="blog_sections.title" section-color="section" :section="section.summary" id="">
        {{ section.section.section_content }}
      </ArticleBase>
    </div>
  </div>
</template>
  
<style lang="scss"  scoped>
.section {
  margin-bottom: 2em;

  .avatar {
    border-radius: 14px;
    width: 411px;
    height: 331px;
  }
}

.go-projects {
  font: {
    family: "Roboto Mono", monospace;
    optical-sizing: auto;
    style: normal;
  }
}
.go-projects {
  margin-top: 4em;
}

#reviews {
  margin-top: 4em;
  margin-left: 1em;
}
</style>
  