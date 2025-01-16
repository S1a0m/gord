<script setup>
import { ref } from 'vue';
import MentionsPolitiques from './MentionsPolitiques.vue';

const showMp = ref(false);

const showMpg = () => {
  showMp.value = true;
}

const closeMpg = () => {
  showMp.value = false;
}
</script>

<template>
    <div id="footer">
        <div class="content">
            <div class="main-content">
                <div class="contact">
                    <p class="name">
                        AMOUSSOU Précieux Samson <br>Expert informatique
                    </p>
                    <p class="details">
                        <span class="w-e">Whatsapp:</span><span>+229 01 54 14 12 87</span>
                        <span class="w-e">Email:</span><span>precieuxdev1@gmail.com</span>
                    </p>
                </div>
                <div class="git-mentions">
                    <div class="coords">
                        <a href="https://github.com/S1a0m"><img src="./icons/signe-github.png" alt=""></a>
                        <a href="https://www.linkedin.com/in/amoussou-pr%C3%A9cieux-samson-040303244/"><img src="./icons/linkdin.png" alt=""></a>
                    </div>
                    <br>
                    <span class="m-p" @click="showMpg">
                        Mentions légales & <br>Politiques de confidentialité
                    </span>
                </div>
            </div>
        </div>
        <div class="copyright">
            © 2025 PxDev. Tous droits réservés.
        </div>
        <MentionsPolitiques v-if="showMp" @close-mp="closeMpg" class="fade-mp"/>
    </div>
</template>

<style lang="scss" scoped>
   /* $footer-background-color: var(--main-gray);
    $footer-width: 100vw;
    $footer-height: 20vh/*200px*;

    @mixin displaying($direction: row) {
        display: flex;
        justify-content: space-between;
        flex-direction: $direction;
    }


    #footer {
        margin-top: 4em;
        background: $footer-background-color;
        height: $footer-height;
        // align-items: center;
        //width: $footer-width;
        padding: {
            top: 3em;
            bottom: 1em;
        }
        @include displaying(column);

        .content {
            display: flex;
            justify-content: center;
            width: 100%;
            height: 100%;
            align-items: center;
        }
    }

    .main-content {
                /// @include displaying(row);
                display: flex;
                justify-content: space-around;
                align-items: center;
                gap: 2em;
                width: 100vw;
                flex-wrap: wrap;
                

                &+div {
                    margin-top: 3em;
                    font-size: 16px;
                    font-family: "Roboto Mono", system-ui;
                    font-weight: 300;
                    font-style: normal;
                    color: #f5f5f5;
                }
            }

    .copyright {
        text-align: center;
        font-family: "Roboto Mono", system-ui;
    }

    .contact {
        .name {
            color: var(--blue-light);
            font-family: "Roboto Mono", system-ui;
            font-weight: 400;
            font-style: normal;
        }

        .details {
            max-width: 20em;
            display: grid;
            grid-template-columns: 1fr 1fr;
            //gap: 1px;
            margin-top: 1em;
        }
    }

    .m-p {
        color: var(--main-red);
        font-size: 16px;
        font-family: "Roboto Mono", system-ui;
        font-weight: 300;
        font-style: normal;
        cursor: pointer;

        &:hover {
            text-decoration: underline;
        }
    }

    img {
        height: 54px;
        width: 54px;
        background: var(--blue-light);
        border-radius: 14px;
        transition: all 500ms ease-in-out;

        &:hover {
            background: var(--hover-gray);
        }
    }

    .coords {
        display: flex;
        gap: 1em;
    }

    .w-e {
        color: var(--hover-gray);
        font-family: "Roboto Mono", system-ui;
        font-weight: 500;
        font-style: normal;
        font-size: 16px;

        &+span {
            color: var(--blue-light);
            font-family: "Roboto Mono", system-ui;
            font-weight: 300;
            font-style: italic;
        }
    }*/
$footer-background-color: var(--main-gray);
$footer-width: 100vw;
$footer-height: 20vh;

@mixin displaying($direction: row) {
    display: flex;
    justify-content: space-between;
    flex-direction: $direction;
}

#footer {
    margin-top: 4em;
    background: $footer-background-color;
    height: $footer-height;
    padding: {
        top: 3em;
        bottom: 1em;
    }
    @include displaying(column);

    .content {
        display: flex;
        justify-content: center;
        width: 100%;
        height: 100%;
        align-items: center;
    }
}

.main-content {
    display: flex;
    justify-content: space-around;
    align-items: center;
    gap: 2em;
    width: 100vw;
    flex-wrap: wrap;

    & + div {
        margin-top: 3em;
        font-size: 1rem;
        font-family: "Roboto Mono", system-ui;
        font-weight: 300;
        color: #f5f5f5;

        @media screen and (max-width: 1280px) {
            font-size: 0.9rem;
        }

        @media screen and (max-width: 768px) {
            font-size: 0.8rem;
        }
    }
}

.copyright {
    text-align: center;
    font-family: "Roboto Mono", system-ui;
    font-size: 0.9rem;

    @media screen and (max-width: 768px) {
        font-size: 0.8rem;
    }
}

.contact {
    .name {
        color: var(--blue-light);
        font-family: "Roboto Mono", system-ui;
        font-weight: 400;
        font-size: 1.2rem;

        @media screen and (max-width: 1280px) {
            font-size: 1rem;
        }

        @media screen and (max-width: 768px) {
            font-size: 0.9rem;
        }
    }

    .details {
        max-width: 20em;
        display: grid;
        grid-template-columns: 1fr 1fr;
        margin-top: 1em;
        font-size: 0.9rem;

        @media screen and (max-width: 768px) {
            font-size: 0.8rem;
        }
    }
}

.m-p {
    color: var(--main-red);
    font-size: 1rem;
    font-family: "Roboto Mono", system-ui;
    font-weight: 300;
    cursor: pointer;

    &:hover {
        text-decoration: underline;
    }

    @media screen and (max-width: 1280px) {
        font-size: 0.9rem;
    }

    @media screen and (max-width: 768px) {
        font-size: 0.8rem;
    }
}

img {
    height: 54px;
    width: 54px;
    background: var(--blue-light);
    border-radius: 14px;
    transition: all 500ms ease-in-out;

    &:hover {
        background: var(--hover-gray);
    }

    @media screen and (max-width: 1280px) {
        height: 45px;
        width: 45px;
    }

    @media screen and (max-width: 768px) {
        height: 40px;
        width: 40px;
    }
}

.coords {
    display: flex;
    gap: 1em;

    @media screen and (max-width: 768px) {
        gap: 0.8em;
    }
}

.w-e {
    color: var(--hover-gray);
    font-family: "Roboto Mono", system-ui;
    font-weight: 500;
    font-size: 1rem;

    & + span {
        color: var(--blue-light);
        font-family: "Roboto Mono", system-ui;
        font-weight: 300;
        font-style: italic;
    }

    @media screen and (max-width: 1280px) {
        font-size: 0.9rem;
    }

    @media screen and (max-width: 768px) {
        font-size: 0.8rem;
    }
}
</style>