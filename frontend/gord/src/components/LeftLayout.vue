<script setup>
</script>

<template>
    <aside>
        <slot></slot>
        <div class="menu">
            <button class="menu-button" onclick="toggleMenu()">
                <div class="menu-icon"></div>
                <div class="menu-icon"></div>
                <div class="menu-icon"></div>
                <span>Menu</span>
            </button>
        </div>
    </aside>
</template>

<style lang="scss" scoped>
aside {
    width: 14vw;
    margin: 1em;
}

.menu {
    margin-left: 11em;
    margin-top: 35vw;
}

.menu-button {
    background-color: transparent;
    border: 2px solid #00FF00;
    color: #00FF00;
    font-size: 12px;
    padding: 10px 20px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    text-transform: uppercase;
    transition: 0.3s ease-in-out;
}

.menu-button:hover {
    background-color: #00FF00;
    color: black;
}

.menu-button span {
    display: block;
    margin-top: 10px;
}

    .menu-icon {
      width: 30px;
      height: 3px;
      background-color: #00FF00;
      margin: 6px auto;
      transition: all 0.3s;
    }

    .menu-button:hover .menu-icon {
      background-color: black;
    }

    /* Menu icon animation */
    .menu-button.open .menu-icon:nth-child(1) {
      transform: translateY(9px) rotate(45deg);
    }

    .menu-button.open .menu-icon:nth-child(2) {
      opacity: 0;
    }

    .menu-button.open .menu-icon:nth-child(3) {
      transform: translateY(-9px) rotate(-45deg);
    }

</style>