<script setup>
const props = defineProps([
    'activePage',
    'section',
    'sectionColor'
])
</script>

<template>
  <div class="container">
    <div>
      <h4>{{ props.activePage }}@pxdev<span class="dollar">:</span><span :class="props.sectionColor">/{{ props.section }}~</span><span class="dollar">$</span></h4>
        <section>
            <slot></slot>
        </section>
    </div>
  </div>
</template>

<style lang="scss" scoped>

.container {
  display: flex;
}

section {
  margin-left: 1em;
  padding-right: 10em;
  font-size: 16px;
  color: var(--main-white);
  text-wrap: wrap;
  font: {
    family: "Roboto Mono", monospace;
    optical-sizing: auto;
    style: normal;
  }

  @media screen and (max-width: 768px) {
      font-size: 0.9em;
  }
}

h4 {
  color: var(--green-hack);
  margin: {
    top: 1em;
    bottom: 1em;
  }
  font: {
    family: "Roboto Mono", system-ui;
    optical-sizing: auto;
    style: normal;
    size: 20px;
  }
  @media screen and (max-width: 768px) {
      font-size: 0.9em;
  }
}

.dollar {
    color: var(--main-white);
}

.section, .article { /**Agit directement sur le composant appelant */
  font-size: 20px;
  font: {
    family: "Roboto", monospace;
    optical-sizing: auto;
    style: normal;
  }

  @media screen and (max-width: 768px) {
      font-size: 0.9em;
  }
}

.section {
  color: var(--blue-dark);
}

.article {
  color: var(--blue-light);
}
</style>
