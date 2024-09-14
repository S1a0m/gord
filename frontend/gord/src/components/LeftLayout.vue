<script setup>
import Button from './Button.vue' 
</script>

<template>
    <aside>
        <slot></slot>
        <div class="menu">
            <Button type="square-v1">
                <img src="./icons/menuv.svg" alt="" class="menu-button">
            </Button>
        </div>
    </aside>
</template>

<style lang="scss" scoped>
aside {
    width: 45vw;
    margin: 1em;
}

.menu {
    position: relative;
    margin-left: 84%;
    margin-top: 35vw;
}

.menu-button {
    height: 40px;
    width: 40px;
    margin: {
        top: 13%;
        left: 13%;
    }
}

</style>