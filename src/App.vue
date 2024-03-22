<template>
  <router-view />
</template>
<script>
import { provide } from "vue";
import * as echarts from "echarts";
import axios from "axios";
import elementPlus from "element-plus";

export default {
  setup() {
    //provide("mingzi","chuandi")
    provide("echarts", echarts);
    provide("axios", axios);
    provide("elementPlus", elementPlus);
  },
  components: {},
};
</script>
<style>
body {
}
* {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}
</style>
