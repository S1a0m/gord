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

/*label {
  font-family: "Roboto", system-ui;
  font-weight: 300;
  font-style: normal;
  font-size: 20px;
}*/

.subscribe-form {
    border-style: solid;
    width: 37em;
    height: 11em;
    border-radius: 14px;
    border-color: #288F9E;
    position: absolute;
    background: #1C1A1A;
    left: 40em;
    top: 20px;
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
