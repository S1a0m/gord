<script setup>
import Button from './Button.vue';
import { ref } from 'vue';
import apiClient from '../axios'; // Instance Axios configurée
import SuccesMessage from './SuccesMessage.vue';

const emit = defineEmits(['close-subscribepopup']);

const closeSubscribepopup = () => {
  emit('close-subscribepopup');
};

const email = ref('');
const message = ref('');
const successMessage = ref(null); // Référence pour le composant SuccesMessage

const subscribeToNewsletter = async () => {
  if (!email.value) {
    message.value = 'Veuillez entrer une adresse email.';
    successMessage.value.show('error'); // Affiche une erreur
    return;
  }

  try {
    const response = await apiClient.post('/newsletter/subscribe/', { email: email.value });
    message.value = response.data.message;
    successMessage.value.show('success'); // Affiche le succès
    email.value = ''; // Réinitialise le champ email
  } catch (error) {
    message.value = error.response?.data?.error || 'Une erreur est survenue.';
    successMessage.value.show('error'); // Affiche une erreur
  }
};

const handleSuccess = () => {
  closeSubscribepopup();
};
</script>

<template>
    <div class="subscribe-form">
      <form @submit.prevent="subscribeToNewsletter">
        <div>
          <input
            type="email"
            name="email"
            id="email"
            v-model="email"
            placeholder="Enter your mail here"
          />
          <Button type="subscribe-button">
            <span class="submit">Submit</span>
          </Button>
        </div>
      </form>
  
      <!-- Composant SuccesMessage -->
      <SuccesMessage ref="successMessage" @success-displayed="handleSuccess">
        {{ message }}
      </SuccesMessage>
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
    @media screen and (max-width: 1280px) {
        font-size: 1em;
    }
}

#email {
    padding-left: 1em;
    padding-right: 1em;
    font-size: 20px;
    height: 54px;
    width: 20vw;//389px;
    // border-radius: 14px;
    background: var(--hover-gray);
    border-style: none;
    outline: none;
    color: var(--main-white);
    font-family: "Roboto Mono", system-ui;
    font-optical-sizing: auto;
    font-weight: 400;
    font-style: normal;
    @media screen and (max-width: 1280px) {
        width: 60vw;
        font-size: 1em;
        height: 50px;
    }

    @media screen and (max-width: 768px) {
        font-size: 0.9em;
        height: 50px;
    }
}

.subscribe-form {
    /*border-style: solid;
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
    transform: translate(-50%, -50%);*/
    padding: 3em 0em 4em 2em;
    display: flex;
    position: fixed;
    z-index: 5;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    border-style: solid;
    border-width: 1px;
    border-radius: 10px;
    border-color: var(--green-hack);
    background-color: var(--mp-background);
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
</style>
