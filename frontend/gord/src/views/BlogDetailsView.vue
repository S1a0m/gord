<script setup>
import ArticleBase from '../components/ArticleBase.vue'
import Loader from '@/components/Loader.vue';
import { useRoute } from 'vue-router';
import apiClient from '../axios';
import { ref, onMounted } from 'vue';

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
    <div class="illustration" v-if="blog_sections.illustration">
      <img :src="blog_sections.illustration" alt="">
    </div>
    <div class="section" v-for="section in blog_sections.summaries" :id="section.summary_link">
      <ArticleBase :active-page="blog_sections.title" section-color="section" :section="section.summary" id="">
        <div class="backg-hov">
          {{ section.section.section_content }}
        </div>
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

.backg-hov {
  padding: 1em;
  border-radius: 10px;
}

.backg-hov:hover {
  background: var(--hover-article);
}

.illustration {
  margin-left: 2em;

  img {
    width: 48em;
    height: 26em;
    border-style: solid;
    border-width: 1em;
    border-radius: 10px;
    border-color: var(--hover-article);
    @media screen and (max-width: 842px) {
        width: 30em;
        height: 22em;
    }
    @media screen and (max-width: 553px) {
        width: 20em;
        height: 12em;
    }
  }
}

@media screen and (max-width: 744px) {
  .backg-hov {
        background: var(--hover-article);
    }
}
</style>
  