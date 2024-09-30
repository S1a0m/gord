<script setup>
import { RouterLink } from 'vue-router';
import Button from './Button.vue';

const props = defineProps([
    'name',
    'time',
    'likes',
    'comments',
    'sommary',
    'details'
])

const goOnReviews = `${props.details}/#reviews`;
</script>

<template>
    <article>
        <div class="container">
            <header>
                <Button type="square-v2">
                    <img src="./icons/like_blue.svg" alt="Search" class="like-icon">
                </Button>
                <div class="l-p">
                    <span class="likes">{{ props.likes }}</span>
                    <span class="pubdate">Publié le <time datetime="">{{ props.time }}</time></span>
                </div>
            </header>
            <div class="content">
                <span class="title">{{ props.name }}</span>
                <div class="sommary">{{ props.sommary }}</div>
                <span class="li"><RouterLink :to="props.details"><span class="nk">Lire la doc ...</span></RouterLink></span>
            </div>
            <footer>
                <RouterLink :to="goOnReviews">
                    <Button type="inside-button">
                        <span class="nbr-comments">{{ props.comments }} commentaire(s)</span>
                    </Button>
                </RouterLink>
            </footer>
        </div>
    </article>
</template>
  
<style lang="scss" scoped>
article {
    height: 300px;
    width: 300px;
    background-color: var(--main-gray);
    border-style: solid;
    border-width: 1px;
    border-radius: 14px;
    border-color: var(--blue-light);
    box-shadow: .1em .1em .5em var(--hover-gray);
    transition: {
        property: all;
        duration: 1000ms;
    }

    &:hover {
        transform: scale(1.1);
    }
}

.container {
    margin-left: 1.7em;
    margin-top: 1.8em;
}

.like-icon {
    width: 30px;
    height: 30px;
}

header {
    display: flex;
    gap: 0.8em;
    margin-bottom: 2em;
}

footer {
    margin-top: 1.5em;
}

.content {
    font-size: 20px;
    width: 80%;
}

.nk, .sommary, .title {
    font-family: "Roboto Mono", system-ui;
}

.l-p {
    display: flex;
    flex-direction: column;
}

.nbr-comments{
    font-family: "Roboto Mono", system-ui;
    font-optical-sizing: auto;
    font-weight: 500;
    font-style: normal;
    font-size: 16px;
    color: var(--blue-light);
} 

time, .likes {
    color: var(--hover-gray);
}

.likes {
    color: var(--hover-gray);
    font-family: "Roboto Mono", system-ui;
    font-optical-sizing: auto;
    font-weight: 700;
    font-style: normal;
    font-size: 16px;
}

.pubdate {
    font-family: "Roboto Mono", system-ui;
    font-optical-sizing: auto;
    font-weight: 300;
    font-style: normal;
    font-size: 16px;
}
</style>
  