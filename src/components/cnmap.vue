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
import {roma} from "../assets/roma.js";
// 示例数据，需要根据您的实际数据进行替换
const data = [
  { name: '广东省', value: Math.random() * 100 },
  { name: '北京市', value: Math.random() * 100 },
  { name: '上海市', value: Math.random() * 100 },
  { name: '重庆市', value: Math.random() * 100 },
  { name: '江苏省', value: Math.random() * 100 },
  { name: '浙江省', value: Math.random() * 100 },
  { name: '福建省', value: Math.random() * 100 },
  { name: '湖南省', value: Math.random() * 100 },
  { name: '湖北省', value: Math.random() * 100 },
  { name: '广西壮族自治区', value: Math.random() * 100 },
  { name: '云南省', value: Math.random() * 100 },
  { name: '贵州省', value: Math.random() * 100 },
  { name: '四川省', value: Math.random() * 100 },
  { name: '山东省', value: Math.random() * 100 },
  { name: '河南省', value: Math.random() * 100 },
  { name: '安徽省', value: Math.random() * 100 },
  { name: '河北省', value: Math.random() * 100 },
  { name: '江西省', value: Math.random() * 100 },
  { name: '山西省', value: Math.random() * 100 },
  { name: '辽宁省', value: Math.random() * 100 },
  { name: '吉林省', value: Math.random() * 100 },
  { name: '黑龙江省', value: Math.random() * 100 },
  { name: '陕西省', value: Math.random() * 100 },
  { name: '甘肃省', value: Math.random() * 100 },
  { name: '青海省', value: Math.random() * 100 },
  { name: '台湾省', value: Math.random() * 100 },
  { name: '内蒙古自治区', value: Math.random() * 100 },
  { name: '西藏自治区', value: Math.random() * 100 },
  { name: '宁夏回族自治区', value: Math.random() * 100 },
  { name: '新疆维吾尔自治区', value: Math.random() * 100 },
  { name: '香港特别行政区', value: Math.random() * 100 },
  { name: '澳门特别行政区', value: Math.random() * 100 },
  // 根据您的地图数据情况，可能需要将“海南省”添加到数据中，如果地图包括
  { name: '海南省', value: Math.random() * 100 },
  // 台湾省可能在某些地图数据集中不被包含
  // 如果您的地图数据集包含南海诸岛，也可以添加
  { name: '南海诸岛', value: Math.random() * 100 }, // 这个名称可能因不同数据源而异
];

// 假设这是您想要标记的经纬度坐标
var starCoordinate = [116.405285, 39.904989]; // 北京的经纬度


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
      var chart = $echarts.init(document.getElementById("cnmap"),roma);
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
    type: 'map',
    map: 'china',
    geoIndex: 0,
    aspectScale: 0.75,
    showLegendSymbol: false,
    roam: true,
    // 使用准备好的数据
    data: data,
    // ...省略其他配置
  },
  {
  name: '星星',
  type: 'scatter', // 或者 'effectScatter' 用于涟漪效果
  coordinateSystem: 'geo',
  data: [{
    name: '选中位置',
    value: [...starCoordinate, 500] ,
    itemStyle: {
    color: '#F7B70B', // 指定星星的颜色
  },// 请将 starCoordinate 替换为您想要的经纬度坐标，格式为 [经度, 纬度]
  }],
  symbol: 'pin', symbolSize: 30, // 星星的大小
  label: {
    show: false,
    formatter: '{b}'
  },

  emphasis: {
    label: {
      show: true
    }
  },
  visualMap: false // 禁用此系列的视觉映射
}


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
