<script setup>
const props = defineProps([
    'type'
])
</script>

<template>
    <div :class="props.type">
        <slot>
        
        </slot>
    </div>
</template>

<style lang="scss" scoped>
$square-v1-size: 54px;
$square-v2-size: 42px;
$subscribe-button-width: 145px;

$button-backg: #1C1A1A;
$banner-buttons-backg: #0A0A0A;

@mixin buttonSize($height: none, $width: none, $backg: none, $borderStyle: none) {
    height: $height;
    width: $width;
    background: $backg;
    cursor: pointer;
    border: {
        style: $borderStyle;
        color: #288F9E;
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
    @include buttonSize($square-v1-size, $subscribe-button-width, $banner-buttons-backg, solid);
}

.square-v2 {
    @include buttonSize($square-v2-size, $square-v2-size, $button-backg, solid);
}

div:hover {
    background: #505050;
}
</style>