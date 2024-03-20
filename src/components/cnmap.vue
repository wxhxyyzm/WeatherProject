<template>
  <div class="map" id="cnmap">map</div>
</template>

<script>
// 1.引用
import { onMounted, reactive, inject } from "vue";
// 导入 VisualMap 组件
import { VisualMapComponent } from "echarts";
// 导入地图数据
import mapData from "../assets/china.json";

export default {
  components: {
    // 注册 VisualMap 组件
    VisualMapComponent,
  },
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
        grid: {
          left: "10%",
          bottom: "25%",
        },
        geo: {
          map: "china",
          roam: true, // 开启缩放和平移
          zoom: 1.6, // 初始缩放比例
          center: [104.195397, 35.86166],
          label: {
            emphasis: {
              show: false,
            },
          },
          itemStyle: {
            // 定制地图的样式
            normal: {
              areaColor: "#FFFFFF",
              borderColor: "#111",
            },
            emphasis: {
              areaColor: "#2a333d",
            },
          },
        },
        // 使用 VisualMap 组件设置渐变颜色
        visualMap: {
          min: 0,
          max: 100,
          inRange: {
            color: ["#e0ffff", "#006edd"],
          },
          textStyle: {
            color: "white",
          },
        },
        series: [
          {
            type: "map",
            map: "china",
            geoIndex: 0,
            aspectScale: 0.75,
            showLegendSymbol: false,
            roam: true,
            data: [
              // 其他区域的数据
            ],
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
  height: 6.5rem;
  border: 2px solid white;
}
</style>
