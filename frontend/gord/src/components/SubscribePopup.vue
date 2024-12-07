<script setup>
import Button from './Button.vue';  
import { ref } from 'vue';
import apiClient from '../axios'; // Instance Axios configurée

const emit = defineEmits([ 'close-subscribepopup' ])

const closeSubscribepopup = () => {
    emit('close-subscribepopup');
}

const email = ref('');
const message = ref('');

const subscribeToNewsletter = async () => {
  if (!email.value) {
    message.value = 'Veuillez entrer une adresse email.';
    alert(message.value);
    return;
  }

  try {
    const response = await apiClient.post('/newsletter/subscribe/', { email: email.value });
    message.value = response.data.message;
    alert(message.value); // Affiche le message
    email.value = ''; // Réinitialise le champ email
  } catch (error) {
    console.error(error);
    message.value = error.response?.data?.error || 'Une erreur est survenue.';
    alert(message.value); // Affiche l'erreur
  }
};
</script>


<template>
    <div class="subscribe-form">
        <form @submit.prevent="subscribeToNewsletter">
            <!--<label for="email">Enter your mail here</label>-->
            <div>
                <input type="email" name="email" id="email" v-model="email" placeholder="Enter your mail here">
                <Button type="subscribe-button" @click="closeSubscribepopup">
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
    width: 20vw;//389px;
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
    width: 34vw;//37em;
    //height: 11em;
    padding: 3em 0em 4em 2em;
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
    /*margin-left: 2.1em;
    margin-top: 4em;*/
    display: flex;
    justify-content: center;
    align-items: center;

    div {
        margin-top: 0.8em;
        display: flex;
        flex-wrap: wrap;
        gap: 1em;
        padding-right: 2em;
    }
}

@media screen and (max-width: 744px) {
  .subscribe-form {
    width: 70vw;
  }

  #email {
    width: 60vw;
  }
}
</style>
