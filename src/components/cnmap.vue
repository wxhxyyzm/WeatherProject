<template>
  <div class="map" id="cnmap">map</div>
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
        //backgroundColor: "#404a59", // 设置背景色
        geo: {
          map: "china",
          roam: true, // 开启缩放和平移
          zoom: 1.2, // 初始缩放比例
          label: {
            emphasis: {
              show: false,
            },
          },
          itemStyle: {
            // 定制地图的样式
            normal: {
              areaColor: "#323c48",
              borderColor: "#111",
            },
            emphasis: {
              areaColor: "#2a333d",
            },
          },
        },
        series: [
          {
            type: "map",
            map: "china",
            geoIndex: 0,
            aspectScale: 0.75, // 长宽比
            showLegendSymbol: false, // 去除地图指示小红点
            roam: true,
            itemStyle: {
              normal: {
                areaColor: "#031525",
                borderColor: "#3B5077",
              },
              emphasis: {
                areaColor: "#2B91B7",
              },
            },
            data: [
              // 数据项
            ],
          },
        ],
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
  padding: 0.3rem;
  margin: 0.3rem;
  border: 1px solid black;
  height: 6.5rem;
}
</style>