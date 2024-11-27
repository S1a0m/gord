<script setup>
const props = defineProps([
    'type'
])
</script>

<template>
    <button :class="props.type">
        <slot>  
        </slot>
    </button>
</template>

<style lang="scss" scoped>
$square-v1-size: 54px;
$square-v2-size: 42px;
$subscribe-button-width: 145px;

$button-backg: var(--main-black);
$banner-buttons-backg: var(--main-black);

@mixin buttonSize($height: none, $width: none, $backg: none, $borderStyle: none) {
    height: $height;
    width: $width;
    background: $backg;
    cursor: pointer;
    border: {
        style: $borderStyle;
        color: var(--blue-light);
        radius: 14px;
        width: 1px;
    }
}

.square-v1 {
    @include buttonSize($square-v1-size, $square-v1-size, $button-backg, solid);
}

.banner-button {
    @include buttonSize($square-v1-size, $square-v1-size, $banner-buttons-backg);
}

.subscribe-button {
    @include buttonSize($square-v1-size, $subscribe-button-width, $banner-buttons-backg);
}

.comment-button {
    @include buttonSize($square-v1-size, $subscribe-button-width, $banner-buttons-backg, solid);
}

.menu-button {
    @include buttonSize($square-v1-size, 190px, $banner-buttons-backg);
}

.inside-button {
    @include buttonSize($square-v2-size, auto, $banner-buttons-backg, solid);
    padding: {
        left: 3em;
        right: 3em;
    }
}

.square-v2 {
    @include buttonSize($square-v2-size, $square-v2-size, $button-backg, solid);
}

button {
    transition: {
        property: all;
        duration: 400ms;
    }
    &:hover {
        background: var(--hover-gray);
    }
}

</style>