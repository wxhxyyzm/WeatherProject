<template>
  <div></div>

  <section class="container">
    <section class="container-top">
      <section class="top-left">
        <item><item1 /></item>
        <item><item2 /></item>
      </section>
      <section class="top-mid">
        <div class="timeselect-container">
          <timeselect></timeselect>
        </div>
        <div class="map-container"><cnmap></cnmap></div>
      </section>
      <section class="top-right">
        <item><item3 /></item>
        <item><item4 /></item>
      </section>
    </section>

    <section class="container-bottom">
      <doubleline></doubleline>
    </section>
  </section>
</template>

<script>
import item from "@/components/item.vue";
import item1 from "@/components/item1.vue";
import item2 from "@/components/item2.vue";
import item3 from "@/components/item3.vue";
import item4 from "@/components/item4.vue";
import cnmap from "@/components/cnmap.vue";
import doubleline from "@/components/doubleline.vue";
import timeselect from "@/components/timeselect.vue";

export default {
  components: {
    item,
    item1,
    item2,
    item3,
    item4,
    cnmap,
    timeselect,
    doubleline,
  },
};
</script>

<style scoped>
.container {
  margin: 0 auto;
  padding: 0.125rem;
  height: calc(100vh - 0.55rem); /* 使用视口高度单位设置页面高度 */
  display: flex;
  flex-direction: column;
}

.top-left,
.top-right {
  flex: 2.5;
  margin: 0;
}

.top-mid {
  flex: 4.2;
}
.top-mid {
  position: relative;
}

.timeselect-container {
  position: absolute;
  top: 0;
  left: 25px;
  transform: translate(-10px, 20px);
  margin-top: -10px; /* 调整上方间距 */
  margin-right: -0px; /* 调整右侧间距 */
}
.map-container {
  margin-top: 50px;
}

.container-top {
  flex: 2;
  display: flex;
  height: 70%;
}

.container-bottom {
  flex: 2;
  height: 20%;
}
</style>
