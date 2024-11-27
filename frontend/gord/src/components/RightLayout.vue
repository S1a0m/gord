<script setup>
</script>

<template>
    <aside>
        <slot></slot>
    </aside>
</template>

<style lang="scss" scoped>
aside {
    width: 16vw;
    // margin-top: 2em;
    font-size: 15px;
    padding: 1em;
    font: {
        family: "Roboto Mono", system-ui;
        weight: 300;
        style: normal;
    }
}
</style>