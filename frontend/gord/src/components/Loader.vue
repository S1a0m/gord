<script setup>
</script>

<template>
<div class="loader">
</div>
</template>

<style>
.loader {
    text-indent: 101%;
    overflow: hidden;
    white-space: nowrap;
    width: 5em;
    height: 5em;
    margin: 1em auto;
    border-radius: 50%;
    border: .5em solid transparent;
    border-right-color: var(--blue-dark);
    animation: spin 1s linear infinite;
}

@keyframes spin {
    to {
        transform: rotate(1turn);
    }
}
</style>