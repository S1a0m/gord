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

<style scoped>

.container {
  display: flex;
}

section {
  margin-left: 1em;
}

h4 {
  color: #00ff00;
  margin-top: 1em;
  margin-bottom: 1em;

  font-family: "Roboto Mono", monospace;
  font-optical-sizing: auto;
  font-style: normal;
  font-size: 20px;
}

.dollar {
    color: #f5f5f5;
}

.section {
    color: #134480;

    font-family: "Roboto Mono", monospace;
    font-optical-sizing: auto;
    font-style: normal;
    font-size: 20px;
}

.article {
    color: #288F9E;
    margin-top: 1em;

    font-family: "Roboto Mono", monospace;
    font-optical-sizing: auto;
    font-style: normal;
    font-size: 20px;
}
</style>
