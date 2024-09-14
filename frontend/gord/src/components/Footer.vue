<script setup> 
</script>

<template>
    <div id="footer">
        <div class="main-content">
            <div class="contact">
                <p class="name">
                    AMOUSSOU Précieux Samson <br>Expert informatique
                </p>
                <p class="details">
                    <span class="w-e">Whatsapp:</span><span>+ 229 60 40 60 83</span>
                    <span class="w-e">Email:</span><span>gord@gmail.com</span>
                </p>
            </div>
            <div class="mentions">
                <a href="https://github.com/S1a0m"><img src="./icons/signe-github.png" alt=""></a>
                <br><br>
                <span>
                    Mentions légales et <br>Politiques de confidentialité
                </span>
            </div>
        </div>
        <div>
            © 2024 Gord. Tous droits réservés.
        </div>
    </div>
</template>

<style lang="scss" scoped>
    $footer-background-color: #1C1A1A;
    $footer-width: 100vw;
    $footer-height: 200px;

    @mixin displaying($space, $direction: row) {
        display: flex;
        justify-content: space-$space;
        align-items: center;
        flex-direction: $direction;
    }


    #footer {
        background: $footer-background-color;
        height: $footer-height;
        padding: {
            top: 3em;
            bottom: 1em;
        }
        border: {
            top-style: solid;
            top-color: #00ff00;
            width: 1px;
        }
        @include displaying(between, column);

        .main-content {
            @include displaying(between);
            gap: 691px;

            &+div {
                margin-top: 3em;
                font-size: 16px;
                font-family: "Roboto", system-ui;
                font-weight: 300;
                font-style: normal;
            }
        }
    }

    .contact {
        background: #0A0A0A;
        padding: 1em;
        border: {
            style: solid;
            color: #288F9E;
            radius: 14px;
            width: 1px;
        }
        .name {
            color: #288F9E;
            font-family: "Roboto", system-ui;
            font-weight: 400;
            font-style: normal;
        }

        .details {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4px;
            margin-top: 1em;
        }
    }

    .mentions span {
        color: #AC1D1D;
        font-size: 16px;
        font-family: "Roboto", system-ui;
        font-weight: 300;
        font-style: normal;
    }

    img {
        height: 54px;
        width: 54px;
    }

    .w-e {
        color: #00ff00;
        font-family: "Roboto", system-ui;
        font-weight: 500;
        font-style: normal;
        font-size: 16px;

        &+span {
            color: #288F9E;
            font-family: "Roboto", system-ui;
            font-weight: 300;
            font-style: italic;
        }
    }
</style>