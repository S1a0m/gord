<script setup>
</script>

<template>
  <div class="container">
    <div class="summary">
      <nav>
        <span class="title">Summary</span>
        <RouterLink to="#"><span>&#9900; Lorem ipsum dolor sit amet, consectetur adipiscing</span></RouterLink>
        <RouterLink to="#"><span>&#9900; Sed ut perspiciatis unde omnis iste natus error sit voluptatem</span></RouterLink>
        <RouterLink to="#"><span>&#9900; Nemo enim ipsam voluptatem quia voluptas sit</span></RouterLink>
        <RouterLink to="#"><span>&#9900; Nemo enim ipsam voluptatem quia voluptas</span></RouterLink>
      </nav>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
    margin: {
        bottom: 2em;
        top: 1em;
    }
}

nav {
  display: flex;
  flex-direction: column;
  gap: 1.5em;
}

.summary {
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--main-gray);
  width: 42em;
  height: 20em;
  /*border-radius: 14px;
  border-color: #288F9E;*/
}

.title {
    font-family: "Roboto Mono", system-ui;
    font-optical-sizing: auto;
    font-weight: 500;
    font-style: normal;
    font-size: 20px;
    display: block;

    &::before {
        content: '';
        display: block;
        height: 5px;
        background: var(--blue-light);
    }
}

a span {
  display: block;
  color: var(--blue-light);
  font-family: "Roboto Mono", system-ui;
  font-optical-sizing: auto;
  font-weight: 300;
  font-style: normal;

  &:hover {
    font-weight: 400;
  }
}
</style>
