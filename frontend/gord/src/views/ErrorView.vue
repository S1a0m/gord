<template>
  <div class="content backg-hov">
    <h1>404 - Error</h1>
    <h2>Vous êtes perdu sur internet??</h2>
    <p>La page à laquelle vous essayez d'accéder n'existe pas.</p>
    <b>Cliquez sur l'un des menus d'en-haut ou l'icone des menus pour continuer.</b>
  </div>
</template>

<style lang="scss" scoped>
h1 {
    color: rgb(146, 14, 14);
}
h2 {
    color: var(--blue-dark);
}
.content {
    margin-left: 1em;
    display: flex;
    gap: 1em;
    flex-direction: column;
    justify-content: center;
    font: {
    family: "Roboto Mono", monospace;
    optical-sizing: auto;
    style: normal;
  }
}

.backg-hov {
  padding: 1em;
  border-radius: 10px;
}

.backg-hov:hover {
  background: var(--hover-article);
}

@media screen and (max-width: 744px) {
  .backg-hov {
        background: var(--hover-article);
    }
}
</style>
