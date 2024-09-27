<script setup>
import Button from './Button.vue';

const emit = defineEmits([ 'close-mp' ])

const closeMpg = () => {
    emit('close-mp');
}
</script>

<template>
    <div class="">
        <pre>


            **Mentions légales**

            Conformément aux dispositions des articles 6-III et 19 de la Loi n°2004-575 du 21 juin 2004 pour la Confiance dans l’économie<br>            numérique, dite L.C.E.N., il est porté à la connaissance des utilisateurs du site[Nom du site] les présentes mentions légales.

            #### **1. Éditeur du site**
            Le site [Nom du site] est édité par :
            - **Raison sociale** : [Nom de la société ou de l’individu]
            - **Adresse** : [Adresse postale complète]
            - **Numéro SIRET** : [Numéro SIRET ou équivalent]
            - **Responsable de la publication** : [Nom du responsable]
            - **Email** : [Adresse email de contact]
            - **Téléphone** : [Numéro de téléphone]

            #### **2. Hébergement**
            Le site est hébergé par :
            - **Nom de l’hébergeur** : [Nom de l’hébergeur]
            - **Adresse** : [Adresse de l’hébergeur]
            - **Téléphone** : [Numéro de téléphone de l’hébergeur]

            #### **3. Propriété intellectuelle**
            Tous les contenus présents sur ce site (textes, images, vidéos, logos, etc.) sont protégés par les lois en vigueur sur la propriété intellectuelle. <br>            Toute reproduction, distribution, modification, adaptation, retransmission ou publication de ces éléments est strictement interdite sans l'accord écrit préalable de l’éditeur.

            #### **4. Limitation de responsabilité**
            L’éditeur s’efforce de fournir sur le site des informations aussi précises que possible. Toutefois, il ne pourra être tenu responsable des omissions, <br>            des inexactitudes et des carences dans la mise à jour, qu’elles soient de son fait ou du fait des tiers partenaires qui lui fournissent ces informations.

            #### **5. Collecte de données**
            Pour plus de détails sur la collecte et l’utilisation des données personnelles, consultez notre [Politique de confidentialité].


            ---


            **Politique de confidentialité**

            La présente politique de confidentialité a pour but d'informer les utilisateurs du site [Nom du site] de la manière dont leurs données personnelles <br>            sont collectées et traitées conformément aux dispositions du Règlement Général sur la Protection des Données (RGPD) et de la loi Informatique et Libertés.

            #### **1. Responsable du traitement des données**
            - **Nom de la société ou de l’individu** : [Nom de la société]
            - **Adresse** : [Adresse postale complète]
            - **Email de contact** : [Adresse email de contact]

            #### **2. Types de données collectées**
            Nous collectons les types de données suivants lorsque vous utilisez notre site :
            - **Données d’identification** : nom, prénom, adresse email, etc.
            - **Données de connexion** : adresse IP, cookies, logs de connexion.

            #### **3. Finalité du traitement des données**
            Les données collectées sont utilisées pour :
            - **Gestion des utilisateurs** : création et gestion des comptes utilisateurs.
            - **Amélioration du site** : statistiques et analyse de la fréquentation.
            - **Communications marketing** : envoi de newsletters et offres promotionnelles (avec consentement préalable).

            #### **4. Durée de conservation des données**
            Les données personnelles sont conservées pendant une durée maximale de [période] à compter de la dernière interaction avec <br>            l'utilisateur, sauf obligation légale de les conserver plus longtemps.

            #### **5. Droits des utilisateurs**
            Conformément à la législation en vigueur, vous disposez des droits suivants concernant vos données personnelles :
            - **Droit d'accès** : vous pouvez demander à accéder aux données que nous détenons à votre sujet.
            - **Droit de rectification** : vous pouvez demander la correction de vos données si elles sont inexactes.
            - **Droit à l'effacement** : vous pouvez demander la suppression de vos données personnelles.
            - **Droit à la portabilité** : vous pouvez demander à recevoir vos données dans un format structuré.
            - **Droit d’opposition** : vous pouvez vous opposer à l’utilisation de vos données.

            Pour exercer ces droits, veuillez nous contacter à l’adresse email : [adresse email].

            #### **6. Cookies**
            Nous utilisons des cookies pour améliorer votre expérience sur le site. Vous pouvez configurer vos préférences de cookies à tout <br>            moment via votre navigateur. Pour plus d'informations, consultez notre [Politique de cookies].

            #### **7. Sécurité des données**
            Nous mettons en place des mesures de sécurité adaptées pour protéger vos données personnelles contre tout accès non autorisé, <br>            modification ou divulgation.

            #### **8. Modifications de la politique de confidentialité**
            Nous nous réservons le droit de modifier cette politique de confidentialité à tout moment. Les modifications seront publiées <br>            sur cette page et seront effectives dès leur mise en ligne.


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
div {
    position: fixed;
    z-index: 4;
    top: 6em;
    left: 17em;
    height: 80vh;
    overflow: auto;
    color: #00ff00;
    border-style: solid;
    border-width: 1px;
    /*background: rgba($color: #050505, $alpha: 1.0);*/
    background-color: rgba(0, 0, 0, .8);
}

/*
.close-mp {
    font-weight: bold;
    font-size: 32px;
    color: #00ff00;
}*/

.options-mp {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    width: 4em;

    span {
        margin: 8px;
    }
}

img {
    width: 30px;
    height: 30px;
}
</style>
