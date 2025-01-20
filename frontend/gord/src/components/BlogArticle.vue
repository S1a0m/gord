<script setup>
import ArticleBase from '../components/ArticleBase.vue'
import BlogSummary from './BlogSummary.vue';
import {RouterLink} from 'vue-router'
import apiClient from '../axios';

const props = defineProps([
    'section',
    'time',
    'likes',
    'comments',
    'views',
    'titles',
    'link',
    'id',
    'illustration'
])

const addNumViews = async () => {
  try {
    const response = await apiClient.post(`/blog/blog-posts/${ props.id }/increment_view_post/`); // Requête POST
  } catch (err) {
    console.error("Erreur lors de l'action :", err);
    alert("Une erreur est survenue.");
  }
};
</script>

<template>
    <ArticleBase active-page="blog" section-color="section" :section="props.section">
        <article>
            <header>
                <span class="pubdate">Publié le <time datetime="">{{ props.time }}</time></span>
                <div class="views">
                    <img src="./icons/vue.svg" alt="">
                    <span>Vue: {{ props.views }}</span>
                </div>
            </header>
            <BlogSummary :titles="props.titles" :blog-link="props.link" :id="props.id" :illustration="props.illustration" />
            <RouterLink :to="{ path: `blog/${props.link}`, query: { id: props.id } }" @click="addNumViews">
                <div class="content">
                        <slot></slot>
                </div>
            </RouterLink>
        </article>
    </ArticleBase>
</template>

<style lang="scss" scoped>
time {
    color: var(--hover-gray);
}

.pubdate {
  font: {
    family: "Roboto Mono", system-ui;
    optical-sizing: auto;
    style: normal;
    weight: 300;
  }
}

.content {
    height: 8em;
    padding: 1em;
    cursor: pointer;
    overflow: hidden;
    max-width: 900px;
    max-height: 200px;
    text-overflow: ellipsis;
    border-bottom-style: solid;
    border-bottom-width: 0.5px;
    border-bottom-left-radius: 14px;
    border-bottom-right-radius: 14px;
    background: var(--main-black);
}
article {
    width: 50vw;//60em;
    padding: 1em;
    border-radius: 14px;
}
article:hover {
    background: var(--hover-article);
}

.views {
    display: flex;
    gap: 0.5em;
    align-items: center;
}

header {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    gap: 1em;
    padding: 0.2em;
}

@media screen and (max-width: 744px) {
    article {
        width: 80vw;
        background: var(--hover-article);
    }
}
</style>
