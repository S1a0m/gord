<script setup>
import Button from './Button.vue' 
</script>

<template>
    <aside>
        <slot></slot>
        <div class="robot">
            <Button type="square-v1">
                <img src="./icons/robot.svg" alt="" class="robot-button">
            </Button>
        </div>
    </aside>
</template>

<style lang="scss" scoped>
aside {
    width: 60vw;
}

.robot {
    margin-top: 28em;
}

.robot-button {
    height: 40px;
    width: 40px;
}
</style>