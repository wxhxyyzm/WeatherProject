<template>

  <router-view/>
</template>
<script>
import { provide } from "vue";
import * as echarts from "echarts";
import axios from 'axios';
export default {
  setup(){
    //provide("mingzi","chuandi")
    provide("echarts",echarts)
    provide("axios",axios)
  },
};
</script>
<style>
body{
  background: url("~@/assets/bg.svg");
  background-size: 100% auto;
}
*{
  margin:0px;
  padding: 0px;
  box-sizing:border-box;
}
</style>
