<script setup>
import Button from './Button.vue'  
</script>

<template>
    <div class="subscribe-form">
        <form action="">
            <label for="email">Enter your mail here</label>
            <div>
                <input type="email" name="email" id="email">
                <Button type="subscribe-button">
                    <span class="submit">Submit</span>
                </Button>
            </div>
        </form>
    </div>
</template>

<style scoped>
.submit {
    display: block;
    color: #288F9E;
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
    background: #505050;
    border-style: none;
    outline: none;
    color: #f5f5f5;
    font-family: "Roboto Mono", system-ui;
    font-optical-sizing: auto;
    font-weight: 400;
    font-style: normal;
}

label {
  font-family: "Roboto", system-ui;
  font-weight: 300;
  font-style: normal;
  font-size: 24px;
}

.subscribe-form {
    border-style: solid;
    width: 37em;
    height: 14em;
    border-radius: 14px;
    border-color: #288F9E;
}

form {
    margin-left: 2.1em;
    margin-top: 4em;
}

form div {
    margin-top: 0.8em;
    display: flex;
    gap: 1em;
}
</style>
