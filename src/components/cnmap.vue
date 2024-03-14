<template>
    <div class="map" id="cnmap">
      map
    </div>
  </template>
  
  <script>
  // 1.引用
  import { onMounted, reactive, inject } from "vue";
  // 导入地图数据
  import mapData from "../assets/china.json";
  
  export default {
    setup() {
      // 2.得到echarts
      let $echarts = inject("echarts");
      let mapDataReactive = reactive({});
  
      onMounted(() => {
        // 将本地导入的地图数据赋值给响应式对象
        mapDataReactive = mapData;
  
        console.log("map", mapDataReactive);
        // 3.设置地图
        $echarts.registerMap("china", mapDataReactive);
        var chart = $echarts.init(document.getElementById("cnmap"));
        chart.setOption({
          geo: {
            map: "china",
          },
        });
      });
  
      return {
        mapData: mapDataReactive,
      };
    },
  };
  </script>
  
  <style>
  .map {
    width: 600px;
    height: auto;
  }
  </style>