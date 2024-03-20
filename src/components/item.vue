<template>
  <div class="item">
    <slot></slot>
  </div>
</template>

<script>
export default {};
</script>

<style scope>
.item {
  height: 3.8rem;
  margin: 0.1rem;
  /* border: 1px solid rgb(0, 255, 132); */
  align-items: center;
  background-color: rgba(240, 231, 231, 0.1);
  border-radius: 0.2rem;
}
</style>