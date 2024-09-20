<script setup>
import Button from './Button.vue' 

const props = defineProps([
    'likes',
    'comments'
])
</script>

<template>
        <div class="footer">
            <div class="likes">
                <Button type="square-v2">
                    <img src="./icons/like.svg" alt="Search" class="like-icon">
                </Button>
                <span>{{ props.likes }}</span>
            </div>
            <div class="comments">
                <Button type="inside-button">
                    <span class="comment">Commentez</span>
                </Button>
                <Button type="inside-button">
                    <span class="nbr-comments">{{ props.comments }} commentaire(s)</span>
                </Button>
            </div>
        </div>
</template>

<style scoped>
.like-icon {
    width: 30px;
    height: 30px;
}

.footer, .likes, .comments {
    display: flex;
} 

.footer {
    margin-top: 1.5em;
}

.likes {
    align-items: center;
    gap: 0.5em;
}

.likes span {
    color: #00ff00;
    font-family: "Roboto Mono", system-ui;
    font-optical-sizing: auto;
    font-weight: 700;
    font-style: normal;
    font-size: 20px;
}

.comments {
    gap: 1.5em;
    margin-left: 5em;
}

.comment {
    color: #f5f5f5;
}

.nbr-comments {
    color: #288F9E;
}

.nbr-comments, .comment {
    font-family: "Roboto Mono", system-ui;
    font-optical-sizing: auto;
    font-weight: 500;
    font-style: normal;
    font-size: 16px;
} 
</style>
