<script setup>
import { ref } from 'vue';
import LeftLayout from './LeftLayout.vue';
import { RouterLink } from 'vue-router';

const props = defineProps([
  'summaries'
])

const summaryStat = ref(true);

const toggleSummaryStat = () => {
    summaryStat.value = !summaryStat.value;
}

</script>

<template>
    <LeftLayout>
        <header>
            <h3 @click="toggleSummaryStat">
                Summaire
                <img src="./icons/stat_minus.svg" alt="" v-if="summaryStat">
                <img src="./icons/stat.svg" alt="" v-else>
            </h3>
            <span class="pubdate">Publié ce <time datetime="">{{ props.summaries.published_date }}</time></span>
        </header>
        <Transition>
            <div class="content" v-if="summaryStat">
                <ul>
                    <li class="article" v-for="summary in props.summaries.summaries" :key="summary.id">
                        <RouterLink :to="{ path: `${props.summaries.link}`, query: { id: props.summaries.id }, hash: `#${summary.summary_link}`}">
                            {{ summary.summary }}
                        </RouterLink>
                    </li>
                </ul>
            </div>
        </Transition>
    </LeftLayout>
</template>
  
<style lang="scss" scoped>
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: "Roboto", system-ui;
    width: fit-content;
    //padding: 1em;

    h3 {
        font-family: "Roboto Mono", system-ui;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 2em;
        width: 7em;
        margin-left: 0.5em;
        border-radius: 14px;
        color: var(--blue-light);
        cursor: pointer;
        transition: {
            property: all;
            duration: 400ms;
        }

        &:hover {
            background: var(--hover-gray);
        }
    }

    .pubdate {
        font-family: "Roboto Mono", system-ui;
        font-optical-sizing: auto;
        font-weight: 300;
        font-style: normal;
        font-size: 16px;

        time {
            color: var(--hover-gray);
        }
    }
}

.content {
    margin-left: 2em;
    margin-top: 2.5em;
}

li {
    font-family: "Roboto Mono", system-ui;
    list-style-type: none;
    margin: 1.5em;
    color: var(--blue-light);
}

.article {
    &:hover {
        cursor: pointer;
        text-decoration: underline;
    }
}
</style>
  