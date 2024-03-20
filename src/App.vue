<template>
  <navbar />
  <router-view />
</template>
<script>
import { provide } from "vue";
import * as echarts from "echarts";
import axios from "axios";
import elementPlus from "element-plus";
import navbar from "./components/navbar.vue";
export default {
  setup() {
    //provide("mingzi","chuandi")
    provide("echarts", echarts);
    provide("axios", axios);
    provide("elementPlus", elementPlus);
  },
  components: {
    navbar,
  },
};
</script>
<style>
body {
  background: url("~@/assets/bg.svg");
  background-size: 100% auto;
}
* {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}
</style>
