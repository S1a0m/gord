<script setup>
import Button from './Button.vue';

const emit = defineEmits([ 'close-mp' ])

const closeMpg = () => {
    emit('close-mp');
}
</script>

<template>
    <div class="container">
        <pre>


            <h3>§ Mentions légales</h3>

            Conformément aux dispositions des articles 6-III et 19 de la Loi n°2004-575 du 21 juin 2004 pour la Confiance dans l’économie<br>            numérique, dite L.C.E.N., il est porté à la connaissance des utilisateurs du site <b>PxDev</b> les présentes mentions légales.

            <b>1. Éditeur du site</b>

            Le site <b>PxDev</b> est édité par :
            <b>- Raison sociale :</b> Précieux Samson AMOUSSOU
            <b>- Adresse :</b> Tchinvié - Porto-Novo - Bénin <!--- **Numéro SIRET** : [Numéro SIRET ou équivalent]-->
            <b>- Responsable de la publication :</b> Précieux Samson AMOUSSOU
            <b>- Email :</b> precieuxdev1@gmail.com
            <b>- Téléphone :</b> +229 01 54 14 12 87

            
            <b>2. Hébergement</b>

            Le site est hébergé par :
            <b>- Nom de l’hébergeur :</b> [Nom de l’hébergeur]
            <b>- Adresse :</b> [Adresse de l’hébergeur]
            <b>- Téléphone :</b> [Numéro de téléphone de l’hébergeur]

            <b>3. Propriété intellectuelle</b>

            Tous les contenus présents sur ce site (textes, images, vidéos, logos, etc.) sont protégés par les lois en vigueur sur la propriété intellectuelle. <br>            Toute reproduction, distribution, modification, adaptation, retransmission ou publication de ces éléments est strictement interdite sans l'accord écrit préalable 
            de l’éditeur.

            <b>4. Limitation de responsabilité</b>

            L’éditeur s’efforce de fournir sur le site des informations aussi précises que possible. Toutefois, il ne pourra être tenu responsable des omissions, <br>            des inexactitudes et des carences dans la mise à jour, qu’elles soient de son fait ou du fait des tiers partenaires qui lui fournissent ces informations.

            <b>5. Collecte de données</b>

            Pour plus de détails sur la collecte et l’utilisation des données personnelles, consultez notre <a href="#politique">Politique de confidentialité</a>.


            <h3 id="politique">§ Politique de confidentialité</h3>

            La présente politique de confidentialité a pour but d'informer les utilisateurs du site [Nom du site] de la manière dont leurs données personnelles <br>            sont collectées et traitées conformément aux dispositions du Règlement Général sur la Protection des Données (RGPD) et de la loi Informatique et Libertés.

            <b>1. Responsable du traitement des données</b>

            <b>- Nom de la société ou de l’individu :</b> PxDev
            <b>- Adresse :</b> Tchinvié - Porto-Novo - Bénin
            <b>- Email de contact :</b> precieuxdev1@gmail.com


            <b>2. Types de données collectées</b>

            Nous collectons les types de données suivants lorsque vous utilisez notre site :
            <b>- Données d’identification :</b> adresse email.
            <b>- Données de connexion :</b> nombre de click sur les contenus.


            <b>3. Finalité du traitement des données</b>

            Les données collectées sont utilisées pour :<!--- **Gestion des utilisateurs** : création et gestion des comptes utilisateurs.-->
            <b>- Amélioration du site :</b> statistiques et analyse de la fréquentation.
            <b>- Communications marketing :</b> envoi de newsletters et offres promotionnelles (avec consentement préalable). <!--4. Durée de conservation des données
            Les données personnelles sont conservées pendant une durée maximale de [période] à compter de la dernière interaction avec <br>            l'utilisateur, sauf obligation légale de les conserver plus longtemps.-->


            <b>4. Droits des utilisateurs</b>

            Conformément à la législation en vigueur, vous disposez des droits suivants concernant vos données personnelles :
            <b>- Droit d'accès :</b> vous pouvez demander à accéder aux données que nous détenons à votre sujet.
            <b>- Droit de rectification :</b> vous pouvez demander la correction de vos données si elles sont inexactes.
            <b>- Droit à l'effacement :</b> vous pouvez demander la suppression de vos données personnelles.
            <b>- Droit à la portabilité :</b> vous pouvez demander à recevoir vos données dans un format structuré.
            <b>- Droit d’opposition :</b> vous pouvez vous opposer à l’utilisation de vos données.

            Pour exercer ces droits, veuillez nous contacter à l’adresse email : <a href="mailto:precieuxdev1@gmail.com">precieuxdev1@gmail.com</a>.

        </pre>
        <div class="options-mp">
            <span class="button-mp">
                <Button type="square-v2" @click="closeMpg">
                    <img src="./icons/close_blue.svg" alt="">
                </Button>
            </span>
        </div>
    </div>
</template>

<style lang="scss"  scoped>
.container {
    display: flex;
    position: fixed;
    z-index: 5;
    left: 50%;
    top: 50%;
    height: 80vh;
    width: 70vw;
    transform: translate(-50%, -50%);
    border-style: solid;
    border-width: 1px;
    border-color: var(--green-hack);
    background-color: var(--mp-background);
}

pre {
    overflow: auto;
    color: var(--main-white);
}

.options-mp {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;

    span {
        margin: 8px;
    }
}

h3 {
    color: var(--blue-dark);
    margin-left: 6em;
}

img {
    width: 30px;
    height: 30px;
}
</style>
