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
      <h4>{{ props.activePage }}@gord<span class="dollar">:</span><span :class="props.sectionColor">/{{ props.section }}~</span><span class="dollar">$</span></h4>
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
}

h4 {
  color: #00ff00;
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
}

.dollar {
    color: #f5f5f5;
}

.section { /**Agit directement sur le composant appelant */
  color: #134480;
  font-size: 20px;
  font: {
    family: "Roboto", monospace;
    optical-sizing: auto;
    style: normal;
  }
}
</style>
