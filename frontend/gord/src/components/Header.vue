<script setup>
import { ref } from 'vue';
import Button from './Button.vue'  
import SubscribePopup from './SubscribePopup.vue';
import MenuG from './MenuG.vue';

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

const showMenu = ref(false);

const toggleMenu = () => {
  showMenu.value = !showMenu.value;
}
</script>

<template>
    <Transition>
        <SubscribePopup v-if="showSubscribePopup" @close-subscribepopup="toggleSubscribePopup"/>
    </Transition>
    <div id="banner">
        <div id="logo">
            PxDev
        </div>
        <div>
            <span class="search-icon">
                <Button type="banner-button" @click="toggleSearch">
                    <img src="./icons/search_blue.svg" alt="Search">
                </Button>
            </span>
            <span>
                <Button type="subscribe-button" @click="toggleSubscribePopup">
                    <span class="subscribe">Subscribe</span>
                </Button>
            </span>
            <span>
                <Button type="banner-button" @click="toggleMode">
                    <img src="./icons/light_mode_blue.svg" alt="Theme" v-if="lightMode === false">
                    <img src="./icons/dark_mode.svg" alt="Theme" v-else>
                </Button>
            </span>
        </div>
    </div>
    <div class="menu">
        <div class="menu-deta">
            <MenuG />
        </div>
        <div class="menu-detb">
            <Transition>
                <MenuG v-if="showMenu" @close-menu="toggleMenu"/>
            </Transition>
        </div>
        <div class="menu-ic" @click="toggleMenu">
            <Button type="square-v1">
                <img src="./icons/menu.svg" alt="Menu">
            </Button>
        </div>
    </div>
</template>

<style lang="scss" scoped>
 /*   $banner-background-color: var(--main-gray);
    $banner-width: 100vw;
    $banner-height: 9vh/*80px*;

    $logo-color: #FFD700;
    $logo-size: 40px;

    @mixin displaying() {
        display: flex;
        align-items: center;
    }


    #banner {
        height: $banner-height;
        max-width: 100vw;
        background: $banner-background-color;
        justify-content: space-between;
        overflow: auto;
        @include displaying;
    }

    #logo {
        color: $logo-color;
        font-size: $logo-size;
        margin-left: 20px;
        font-family: "Roboto", system-ui;
        font-weight: 900;
        font-style: normal;
        
        &+div {
            @include displaying;
            gap: 1em;
            margin-right: 20px;
        }
    }

    img {
        height: 40px;
        width: 40px;
    }

    .subscribe {
        color: var(--blue-light);
        font-family: "Roboto", system-ui;
        font-weight: bold;
        font-style: normal;
        font-size: 20px;
    }

    .menu {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 1em;
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
  transform: translateY(-50em);
}

.menu-ic {
    display: none;
  }

@media screen and (max-width: 1280px) {
  .menu-deta {
    display: none;
  }

  .search-icon {
    display: none;
  }

  .menu-ic {
    display: block;
    margin-left: 1em;
  }

  .menu {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        margin-top: 1em;
    }
}*/

$banner-background-color: var(--main-gray);
$banner-width: 100vw;
$banner-height: 9vh;

$logo-color: #FFD700;

// Mixin pour alignement
@mixin displaying {
    display: flex;
    align-items: center;
}

// Bannière principale
#banner {
    height: $banner-height;
    max-width: $banner-width;
    background: $banner-background-color;
    justify-content: space-between;
    overflow: hidden;
    padding: 0 1.5em;
    @include displaying;

    @media screen and (max-width: 1280px) {
        padding: 0 1em;
    }

    @media screen and (max-width: 768px) {
        padding: 0 0.5em;
    }
}

// Logo
#logo {
    color: $logo-color;
    font-size: 2.5em; // Taille par défaut
    margin-left: 1em;
    font-family: "Roboto", system-ui;
    font-weight: 900;

    @media screen and (max-width: 1280px) {
        font-size: 2em;
        margin-left: 0.8em;
    }

    @media screen and (max-width: 768px) {
        font-size: 1.8em;
        margin-left: 0.5em;
    }

    & + div {
        @include displaying;
        gap: 1em;
        margin-right: 1.5em;

        @media screen and (max-width: 1280px) {
            gap: 0.8em;
            margin-right: 1em;
        }

        @media screen and (max-width: 768px) {
            gap: 0.5em;
            margin-right: 0.5em;
        }
    }
}

// Images
img {
    height: 40px;
    width: 40px;

    @media screen and (max-width: 768px) {
        height: 35px;
        width: 35px;
    }
}

// Bouton "Subscribe"
.subscribe {
    color: var(--blue-light);
    font-family: "Roboto", system-ui;
    font-weight: bold;
    font-size: 20px;

    @media screen and (max-width: 1280px) {
        font-size: 1em;
    }

    @media screen and (max-width: 768px) {
        font-size: 0.9em;
    }
}

// Menu
.menu {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 1em;

    @media screen and (max-width: 768px) {
        margin-top: 0.8em;
    }
}

// Transitions pour les animations d'entrée et de sortie
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
    transform: translateY(-50em);
}

// Icône du menu
.menu-ic {
    display: none;

    @media screen and (max-width: 1280px) {
        display: block;
        margin-left: 0.5em;
    }

    @media screen and (max-width: 768px) {
        margin-left: 0.5em;
    }
}

// Menu détaillé
.menu-deta {
    @media screen and (max-width: 1280px) {
        display: none;
    }
}

// Icône de recherche
.search-icon {
    @media screen and (max-width: 1280px) {
        display: none;
    }
}

@media screen and (max-width: 768px) {
    .menu {
        justify-content: flex-start;
    }
}
</style>