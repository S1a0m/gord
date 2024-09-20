<script setup>
import ArticleBase from '../components/ArticleBase.vue'
import Appreciations from './Appreciations.vue'

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
            <div class="content">
                <slot></slot>
            </div>
            <footer>
                <Appreciations :likes="props.likes" :comments="props.comments"/>
            </footer>
        </article>
    </ArticleBase>
</template>

<style scoped>
time {
    color: #00ff00;
}

.pubdate {
    font-family: "Roboto Mono", system-ui;
    font-optical-sizing: auto;
    font-weight: 300;
    font-style: normal;
}

</style>
