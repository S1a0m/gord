<script setup>
import Button from './Button.vue'
import Comment from './Comment.vue'  
</script>

<template>
    <div class="container">
        <div class="comment-form">
            <form action="">
                <div>
                    <!--<label for="comment">Comment</label>-->
                    <textarea name="comment" id="comment" placeholder="Comment"></textarea>
                    <br>
                    <!--<label for="pseudo">Pseudo</label>-->
                    <div class="ps-sub">
                        <input type="text" name="pseudo" id="pseudo" placeholder="Pseudo">
                        <div class="submit-button">
                            <Button type="comment-button">
                                <span class="submit">Submit</span>
                            </Button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
        <div class="comments">
            <Comment name="Toto" date="7/9/2024" likes="07">
                Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium Lorem ipsum dolor sit amet
                Orem ipsum dolor sit amet. Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Sed ut perspiciatis unde
            </Comment>
            <Comment name="Franck" date="20/9/2024" likes="22">
                Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium Lorem ipsum dolor sit amet
                Orem ipsum dolor sit amet. Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Sed ut perspiciatis unde
            </Comment>
            <Comment name="Sandra" date="20/9/2024" likes="01">
                Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium Lorem ipsum dolor sit amet
                Orem ipsum dolor sit amet. Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Sed ut perspiciatis unde
            </Comment>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.container {
    /*border-right-style: solid;
    border-bottom-style: solid;*/
    border-style: solid;
    border-color: #288F9E;
    border-width: 1px;
    background: #0A0A0A;
    width: 38em;
    height: 50vh;
    overflow: auto;
    margin-top: 2em;
    padding: {
        top: 2em;
        bottom: 2em;
    }
}

.submit {
    display: block;
    color: #288F9E;
    font-family: "Roboto", system-ui;
    font-weight: bold;
    font-style: normal;
    font-size: 20px;
}
/*
.submit-button {
    width: 13.5em;
    background-color: red;
}*/

.ps-sub {
    display: flex;
    justify-content: space-between;
    width: 540px;
}

textarea {
    padding: 1em;
    font-size: 20px;
    height: 6em;
    width: 25em;
    border-radius: 14px;
    background: #505050;
    color: #f5f5f5;
    border-style: none;
    outline: none;
    resize: none;
    font-family: "Roboto Mono", system-ui;
    font-optical-sizing: auto;
    font-weight: 400;
    font-style: normal;
}

#pseudo {
    padding-left: 1em;
    padding-right: 1em;
    font-size: 20px;
    height: 54px;
    width: 320px;
    border-radius: 14px;
    background: #505050;
    color: #f5f5f5;
    border-style: none;
    outline: none;
    font-family: "Roboto Mono", system-ui;
    font-optical-sizing: auto;
    font-weight: 400;
    font-style: normal;
}

/*
label {
  font-family: "Roboto", system-ui;
  font-weight: 300;
  font-style: normal;
  font-size: 20px;
}*/

.comment-form {
    margin-left: 2em;
}

form div {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr;
    gap: 1em;
}

.comments {
    margin-top: 5em;
}
</style>
