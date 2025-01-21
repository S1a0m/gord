<script setup>
import { RouterLink } from 'vue-router'
import ArticleBase from '../components/ArticleBase.vue'
import { useRoute } from 'vue-router';
import apiClient from '../axios';
import { ref, onMounted } from 'vue';
import SuccesMessage from '@/components/SuccesMessage.vue';

const route = useRoute();

const unsubscribed_msg = ref();
const error = ref(null);
const successMessage = ref(null);

const fetchUnsubscribed_msg = async () => {
  try {
    const response = await apiClient.get(`/newsletter/subscribe/unsubscribe/?token=${route.params.token}`);
    unsubscribed_msg.value = response.data;
    successMessage.value.show('success');
  } catch(err) {
    unsubscribed_msg.value = error.response?.data?.error || 'Une erreur est survenue.';
    if(route.params.token.length !== 0) {
      successMessage.value.show('error');
    }
  }
};

onMounted(() => {
  fetchUnsubscribed_msg();
})
</script>

<template>
        <ArticleBase active-page="home" section-color="section" section="Dites moi ce à quoi vous pensez et j'en ferai des lignes de code. 🔥">
          <div class="backg-hov">
            <img src="../components/icons/hacker.jpg" alt="" class="avatar">
            <p>
              Développeur Full-Stack et passionné de technologie, je propose mes services pour la conception et le développement de projets web, mobiles et logiciels sur mesure. Mon expertise couvre une large gamme de technologies, dont HTML, CSS, JavaScript, Vue.js, Django, Qt, Rust et Flutter ainsi que l'intégration de bases de données SQL. <br><br>

              Je réalise des sites web modernes et performants, des applications mobiles intuitives et des outils logiciels robustes adaptés aux besoins spécifiques de mes clients. Par ailleurs, ma passion pour la cybersécurité me permet d'offrir des solutions sûres et optimisées. <br><br>

              Que ce soit pour créer une interface utilisateur attractive, développer un système backend puissant ou sécuriser vos projets, je mets tout en œuvre pour répondre à vos attentes avec rigueur et créativité. Mon objectif est de transformer vos idées en solutions concrètes et efficaces. <br><br>
              <span class="link">Voir plus de détails sur <RouterLink to="/about"> cette page</RouterLink>.</span> <br><br>
              Ou allez sur cette page pour consulter <span class="link"><RouterLink to="/projects">mes projets</RouterLink>.</span>
            </p>
          </div>
        </ArticleBase>
        <!-- Succès si le désabonnement est bien effectué -->
        <SuccesMessage ref="successMessage" @success-displayed="handleSuccess">
          {{ unsubscribed_msg }}
        </SuccesMessage>
</template>

<style lang="scss" scoped>
.avatar {
  border-radius: 14px;
  width: 411px;
  height: 450px;

  @media screen and (max-width: 744px) {
    width: 350px;
    height: 410px;
  }

  @media screen and (max-width: 370px) {
    max-width: 310px;
    height: 410px;
  }
}

.backg-hov {
  padding: 1em;
  border-radius: 10px;
}

.backg-hov:hover {
  background: var(--hover-article);
}

p {
  margin-top: 1.5em;
  font-size: 16px;
  color: var(--main-white);
  font: {
    family: "Roboto Mono", monospace;
    optical-sizing: auto;
    style: normal;
  }

  @media screen and (max-width: 1280px) {
        font-size: 1em;
    }

  @media screen and (max-width: 768px) {
      font-size: 0.9em;
  }
}

@media screen and (max-width: 744px) {
  .backg-hov {
        background: var(--hover-article);
    }
}
</style>
