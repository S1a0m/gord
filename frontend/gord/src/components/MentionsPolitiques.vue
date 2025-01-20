<script setup>
import Button from './Button.vue';

const emit = defineEmits(['close-mp']);

const closeMpg = () => {
    emit('close-mp');
};
</script>

<template>
    <div class="container">
        <div class="content">
            <h3>§ Mentions légales</h3>

            <p>
                Conformément aux dispositions des articles 6-III et 19 de la Loi n°2004-575 du 21 juin 2004 pour la Confiance dans l’économie
                numérique, dite L.C.E.N., il est porté à la connaissance des utilisateurs du site <b>PxDev</b> les présentes mentions légales.
            </p>

            <h4>1. Éditeur du site</h4>
            <p>
                Le site <a href="https://pxdev.amo-iv.tech">pxdev.amo-iv.tech</a> est édité par : Précieux Samson AMOUSSOU<br>
                <b>Adresse :</b> Tchinvié - Porto-Novo - Bénin<br>
                <b>Responsable de la publication :</b> Précieux Samson AMOUSSOU<br>
                <b>Email :</b> precieuxdev1@gmail.com<br>
                <b>Téléphone :</b> +229 01 54 14 12 87
            </p>

            <h4>2. Hébergement</h4>
            <p>
                Le site est hébergé par :<br>
                <b>Nom de l’hébergeur :</b> 001.africa<br>
                <b>Adresse :</b> Cotonou - Bénin<br>
                <b>Téléphone :</b> +229 01 52 68 68 68
            </p>

            <h4>3. Propriété intellectuelle</h4>
            <p>
                Tous les contenus présents sur ce site (textes, images, vidéos, logos, etc.) sont protégés par les lois en vigueur sur la propriété intellectuelle. 
                Toute reproduction, distribution, modification, adaptation, retransmission ou publication de ces éléments est strictement interdite sans l'accord écrit préalable 
                de l’éditeur.
            </p>

            <h4>4. Limitation de responsabilité</h4>
            <p>
                L’éditeur s’efforce de fournir sur le site des informations aussi précises que possible. Toutefois, il ne pourra être tenu responsable des omissions, 
                des inexactitudes et des carences dans la mise à jour, qu’elles soient de son fait ou du fait des tiers partenaires qui lui fournissent ces informations.
            </p>

            <h4>5. Collecte de données</h4>
            <p>
                Pour plus de détails sur la collecte et l’utilisation des données personnelles, consultez notre <a href="#politique">Politique de confidentialité</a>.
            </p>

            <h3 id="politique">§ Politique de confidentialité</h3>

            <h4>1. Responsable du traitement des données</h4>
            <p>
                <b>Nom de la société :</b> PxDev.AMO-IV<br>
                <b>Adresse :</b> Tchinvié - Porto-Novo - Bénin<br>
                <b>Email de contact :</b> precieuxdev1@gmail.com
            </p>

            <h4>2. Types de données collectées</h4>
            <p>
                Nous collectons les types de données suivants lorsque vous utilisez notre site :<br>
                <b>Données d’identification :</b> adresse email.<br>
                <b>Données de connexion :</b> nombre de clics sur les contenus.
            </p>

            <h4>3. Finalité du traitement des données</h4>
            <p>
                Les données collectées sont utilisées pour :<br>
                <b>Amélioration du site :</b> statistiques et analyse de la fréquentation.<br>
                <b>Communications marketing :</b> envoi de newsletters et offres promotionnelles (avec consentement préalable).
            </p>

            <h4>4. Droits des utilisateurs</h4>
            <p>
                Conformément à la législation en vigueur, vous disposez des droits suivants concernant vos données personnelles :<br>
                <b>Droit d'accès :</b> vous pouvez demander à accéder aux données que nous détenons à votre sujet.<br>
                <b>Droit de rectification :</b> vous pouvez demander la correction de vos données si elles sont inexactes.<br>
                <b>Droit à l'effacement :</b> vous pouvez demander la suppression de vos données personnelles.<br>
                <b>Droit à la portabilité :</b> vous pouvez demander à recevoir vos données dans un format structuré.<br>
                <b>Droit d’opposition :</b> vous pouvez vous opposer à l’utilisation de vos données.
            </p>

            <p>
                Pour exercer ces droits, veuillez nous contacter à l’adresse email : 
                <a href="mailto:precieuxdev1@gmail.com">precieuxdev1@gmail.com</a>.
            </p>
        </div>

        <div class="options-mp">
            <span class="button-mp">
                <Button type="square-v2" @click="closeMpg">
                    <img src="./icons/close_blue.svg" alt="">
                </Button>
            </span>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    position: fixed;
    z-index: 5;
    left: 50%;
    top: 50%;
    height: 90vh;
    width: 90vw;
    padding: 20px;
    transform: translate(-50%, -50%);
    border: 2px solid var(--green-hack);
    background-color: var(--mp-background);
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
}

.content {
    overflow-y: auto;
    max-height: 80%;
    width: 100%;
    padding: 10px;
    font-family: "Roboto Mono", monospace;
    font-size: 16px;
    line-height: 1.5;
    color: var(--main-white);
}

.options-mp {
    display: flex;
    justify-content: flex-end;
    width: 100%;
}

.button-mp {
    margin: 10px;
}

h3 {
    font-size: 24px;
    font-weight: bold;
    margin: 20px 0;
    color: var(--blue-dark);
    text-align: center;
    @media screen and (max-width: 768px) {
      font-size: 1em;
    }
}

h4 {
    font-size: 18px;
    font-weight: bold;
    margin: 15px 0 10px;
    @media screen and (max-width: 768px) {
      font-size: 1em;
    }
}

p {
    margin-bottom: 15px;
    @media screen and (max-width: 768px) {
      font-size: 0.8em;
    }
}

img {
    width: 25px;
    height: 25px;
}

a {
    color: var(--blue-light);
    text-decoration: underline;
}
</style>
