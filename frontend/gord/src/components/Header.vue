<script setup>
import Button from './Button.vue'  
</script>

<template>
    <div id="banner">
        <div id="logo">
            Gord
        </div>
        <div>
            <Button type="banner-button">
                <img src="./icons/search.svg" alt="Search">
            </Button>
            <Button type="subscribe-button">
                <span class="subscribe">Subscribe</span>
            </Button>
            <Button type="banner-button">
                <img src="./icons/dark_mode.svg" alt="Theme">
            </Button>
        </div>
    </div>
</template>

<style lang="scss" scoped>
    $banner-background-color: #1C1A1A;
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
        border-bottom-style: solid;
        border-bottom-color: #00ff00;
        border-width: 1px;
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
        color: #288F9E;
        font-family: "Roboto", system-ui;
        font-weight: bold;
        font-style: normal;
        font-size: 20px;
    }
</style>