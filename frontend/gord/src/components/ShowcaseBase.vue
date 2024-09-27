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
                <span class="li"><RouterLink :to="props.details"><span class="nk">Voir plus ...</span></RouterLink></span>
            </div>
            <footer>
                <Button type="inside-button"  @click="toggleComments">
                    <span class="nbr-comments">{{ props.comments }} commentaire(s)</span>
                </Button>
            </footer>
        </div>
    </article>
</template>
  
<style lang="scss" scoped>
article {
    height: 300px;
    width: 300px;
    background-color: #1C1A1A;
    border-style: solid;
    border-width: 1px;
    border-radius: 14px;
    border-color: #288F9E;
    box-shadow: .1em .1em .5em #505050;
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

.nk {
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
    color: #288F9E;
} 

time, .likes {
    color: #00ff00;
}

.likes {
    color: #00ff00;
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
  