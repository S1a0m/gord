<script setup>
import Button from './Button.vue' 
import CommentsPopup from './CommentsPopup.vue';
import { ref } from 'vue';

const props = defineProps([
    'likes',
    'comments'
])

const showComments = ref(false);

const toggleComments = () => {
  showComments.value = !showComments.value;
}
</script>

<template>
        <div class="footer">
            <div class="likes">
                <Button type="square-v2">
                    <img src="./icons/like_blue.svg" alt="Search" class="like-icon">
                </Button>
                <span>{{ props.likes }}</span>
            </div>
            <div class="comments" @click="toggleComments">
                <Button type="inside-button">
                    <span class="nbr-comments">{{ props.comments }} commentaire(s)</span>
                </Button>
            </div>
        </div>
        <Transition>
            <CommentsPopup v-if="showComments"/>
        </Transition>
</template>

<style lang="scss" scoped>
.like-icon {
    width: 30px;
    height: 30px;
}

.footer {
    margin-top: 1.5em;

    &, .likes, .comments {
        display: flex;
    }
}

.likes {
    align-items: center;
    gap: 0.5em;

    span {
        color: #00ff00;
        font: {
            weight: 700;
            size: 20px;
        }

        &, .nbr-comments, .comment {
            font: {
                family: "Roboto Mono", system-ui;
                optical-sizing: auto;
                style: normal;
            }
        }
    }
}

.comments {
    gap: 1.5em;
    margin-left: 5em;
}

.nbr-comments {
    color: #288F9E;
}

.nbr-comments {
    font: {
        weight: 500;
        size: 16px;
    }
} 

.v-enter-active,
.v-leave-active {
  transition: 500ms ease-out;
}

.v-enter-from {
  opacity: 0;
  transform: scale(1.1)/*translateX(80em)*/;
}

.v-leave-to {
  opacity: 0;
  transform: scale(1.1)/*translateX(80em)*/;
}
</style>
