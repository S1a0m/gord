<script setup>
import { RouterLink } from 'vue-router';
import apiClient from '../axios';

const props = defineProps([
    'name',
    'time',
    'comments',
    'sommary',
    'details',
    'views',
    'id'
])


const addNumViews = async () => {
  try {
    const response = await apiClient.post(`/projects/projects/${ props.id }/increment_view_post/`); // Requête POST
  } catch (err) {
    console.error("Erreur lors de l'action :", err);
    alert("Une erreur est survenue.");
  }
};
</script>

<template>
    <article>
        <div class="container">
            <header>
                <div class="l-p">
                    <span class="pubdate">Publié le <time datetime="">{{ props.time }}</time></span>
                </div>
            </header>
            <div class="content">
                <span class="title"><b>{{ props.name }}</b></span>
                <div class="sommary">{{ props.sommary }}</div>
                <span class="li"><a :href="props.details" @click="addNumViews" title="Allez sur github"><span class="nk">Voir plus ...</span></a></span>
            </div>
            <footer>
                <div class="views">
                    <img src="./icons/vue.svg" alt="">
                    <span>Vue: {{ props.views }}</span>
                </div>
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
    @media screen and (max-width: 1280px) {
        height: 280px;
        width: 280px;
    }
}

.title {
    color: var(--blue-dark);
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
    @media screen and (max-width: 744px) {
        font-size: 0.8em;
    }
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

.views {
    display: flex;
    gap: 0.5em;
    //justify-content: center;
    align-items: center;
}
</style>
  