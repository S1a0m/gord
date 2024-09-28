<script setup>
import Button from './Button.vue'  

const props = defineProps([
    "name",
    "date",
    'likes'
])
</script>

<template>
    <article>
        <header>
            <span class="name">{{ props.name }}</span>
            <span class="pubdate">Publié le <time datetime="">{{ props.date }}</time></span>
        </header>
        <br>
        <div class="content">
            <slot></slot>
        </div>
        <br>
        <footer>
            <Button type="square-v2">
                <img src="./icons/like_blue.svg" alt="Search" class="like-icon">
            </Button>
            <span class="likes">{{ props.likes }}</span>
        </footer>
    </article>
</template>

<style lang="scss" scoped>
article {
    width: 33.8em;
    margin-top: 3em;
    margin-left: 2em;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

footer {
    display: flex;
    align-items: center;
    gap: 0.5em;
}

.content {
    color: var(--main-white);
    background: var(--main-gray);
    font-family: "Roboto", system-ui;
    font-size: 15px;
    font-weight: 400;
    font-style: normal;
    width: 30em;
    height: 6em;
    padding: 3em;
    border-radius: 14px;
}

.like-icon {
    width: 30px;
    height: 30px;
}

time, .likes {
    color: var(--hover-gray);
}

.name {
  font-family: "Roboto", system-ui;
  font-weight: 500;
  font-style: normal;
  font-size: 20px;
  color: var(--blue-dark);
}

.likes {
    font-family: "Roboto Mono", system-ui;
    font-optical-sizing: auto;
    font-weight: 700;
    font-style: normal;
    font-size: 16px;
}

.pubdate {
    font-size: 16px;
    font: {
        family: "Roboto Mono", system-ui;
        optical-sizing: auto;
        style: normal;
        weight: 300;
    }
}
</style>
