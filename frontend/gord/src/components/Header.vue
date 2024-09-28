<script setup>
import { ref } from 'vue';
import Button from './Button.vue'  
import SubscribePopup from './SubscribePopup.vue';

const showSubscribePopup = ref(false);

const toggleSubscribePopup = () => {
    showSubscribePopup.value = !showSubscribePopup.value;
}

const emit = defineEmits([ 'toggle-search' ]);

const toggleSearch = () => {
    emit('toggle-search');
}

const lightMode = ref(false);

const toggleMode = () => {
    lightMode.value = !lightMode.value;
    if(lightMode.value) {
        document.body.classList.add('light-mode');
    }
    else {
        document.body.classList.remove('light-mode');
    }
}
</script>

<template>
    <Transition>
        <SubscribePopup v-if="showSubscribePopup"/>
    </Transition>
    <div id="banner">
        <div id="logo">
            Gord
        </div>
        <div>
            <Button type="banner-button" @click="toggleSearch">
                <img src="./icons/search_blue.svg" alt="Search">
            </Button>
            <Button type="subscribe-button" @click="toggleSubscribePopup">
                <span class="subscribe">Subscribe</span>
            </Button>
            <Button type="banner-button" @click="toggleMode">
                <img src="./icons/light_mode_blue.svg" alt="Theme" v-if="lightMode === false">
                <img src="./icons/dark_mode.svg" alt="Theme" v-else>
            </Button>
        </div>
    </div>
</template>

<style lang="scss" scoped>
    $banner-background-color: var(--main-gray);
    $banner-width: 100vw;
    $banner-height: 80px;

    $logo-color: #FFD700;
    $logo-size: 40px;

    @mixin displaying($space) {
        display: flex;
        justify-content: space-$space;
        align-items: center;
    }


    #banner {
        height: $banner-height;
        background: $banner-background-color;
        @include displaying(between);
    }

    #logo {
        color: $logo-color;
        font-size: $logo-size;
        margin-left: 20px;
        font-family: "Roboto", system-ui;
        font-weight: 900;
        font-style: normal;
        
        &+div {
            @include displaying(around);
            margin-left: 78%; 
            gap: 1em;
        }
    }

    img {
        height: 40px;
        width: 40px;
    }

    .subscribe {
        display: block;
        color: var(--blue-light);
        font-family: "Roboto", system-ui;
        font-weight: bold;
        font-style: normal;
        font-size: 20px;
    }

.v-enter-active,
.v-leave-active {
  transition: 500ms;
}

.v-enter-from {
  opacity: 0;
  transform: translateY(-20em);
}

.v-leave-to {
  opacity: 0;
  transform: translateY(-20em);
}
</style>