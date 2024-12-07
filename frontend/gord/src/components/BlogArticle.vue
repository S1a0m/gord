<script setup>
import ArticleBase from '../components/ArticleBase.vue'
import BlogSummary from './BlogSummary.vue';
import {RouterLink} from 'vue-router'

const props = defineProps([
    'section',
    'time',
    'likes',
    'comments',
    'views',
    'titles',
    'link'
])

const goOnBlog = `/blog/${props.section}`;
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
            <BlogSummary :titles="props.titles"/>
            <RouterLink :to="props.link">
                <div class="content">
                        <slot></slot>
                </div>
            </RouterLink>
            <footer>
                <!--<Appreciations :likes="props.likes" :comments="props.comments"/>-->
            </footer>
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
    //border-bottom-color: linear-gradient(to right, rgb(61, 63, 61), rgb(61, 63, 61));
    //background: linear-gradient(to right, rgb(61, 63, 61), rgb(61, 63, 61));
}
article {
    width: 60vw;//60em;
    padding: 1em;
    border-radius: 14px;
}
article:hover {
    background: var(--hover-article);
}

.views {
    display: flex;
    gap: 0.5em;
    //justify-content: center;
    align-items: center;
}

header {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    gap: 1em;
    padding: 0.2em;
}

/*.content:hover {
    border-style: solid;
    border-radius: 14px;
    border-width: 1px;
}*/

@media screen and (max-width: 744px) {
    article {
        width: 80vw;
    }
}
</style>
