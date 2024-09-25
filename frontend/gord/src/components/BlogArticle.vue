<script setup>
import ArticleBase from '../components/ArticleBase.vue'
import Appreciations from './Appreciations.vue'
import BlogSummary from './BlogSummary.vue';

const props = defineProps([
    'section',
    'time',
    'likes',
    'comments'
])
</script>

<template>
    <ArticleBase active-page="blog" section-color="section" :section="props.section">
        <article>
            <header>
                <span class="pubdate">Publié le <time datetime="">{{ props.time }}</time></span>
            </header>
            <BlogSummary />
            <div class="content">
                <slot></slot>
            </div>
            <footer>
                <Appreciations :likes="props.likes" :comments="props.comments"/>
            </footer>
        </article>
    </ArticleBase>
</template>

<style lang="scss" scoped>
time {
    color: #00ff00;
}

.pubdate {
  font: {
    family: "Roboto Mono", system-ui;
    optical-sizing: auto;
    style: normal;
    weight: 300;
  }
}
</style>
