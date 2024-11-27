<script setup>
import Button from './Button.vue'  
</script>

<template>
    <div class="subscribe-form">
        <form action="">
            <!--<label for="email">Enter your mail here</label>-->
            <div>
                <input type="email" name="email" id="email" placeholder="Enter your mail here">
                <Button type="subscribe-button">
                    <span class="submit">Submit</span>
                </Button>
            </div>
        </form>
    </div>
</template>

<style lang="scss" scoped>
.submit {
    display: block;
    color: var(--blue-light);
    font-family: "Roboto", system-ui;
    font-weight: bold;
    font-style: normal;
    font-size: 20px;
}

#email {
    padding-left: 1em;
    padding-right: 1em;
    font-size: 20px;
    height: 54px;
    width: 389px;
    border-radius: 14px;
    background: var(--hover-gray);
    border-style: none;
    outline: none;
    color: var(--main-white);
    font-family: "Roboto Mono", system-ui;
    font-optical-sizing: auto;
    font-weight: 400;
    font-style: normal;
}

.subscribe-form {
    border-style: solid;
    width: 37em;
    height: 11em;
    border-radius: 14px;
    border-color: var(--blue-light);
    position: fixed;
    background: var(--main-gray);
    //left: 40em;
    left: 50%;
    top: 12%;
    z-index: 4;
    transform: translate(-50%, -50%);
}

form {
    margin-left: 2.1em;
    margin-top: 4em;

    div {
        margin-top: 0.8em;
        display: flex;
        gap: 1em;
        padding-right: 2em;
    }
}
</style>
