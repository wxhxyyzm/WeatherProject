<template>
  <div class="map" id="cnmapp">map</div>
</template>

<script>
// 1.引用
import { onMounted, reactive, inject } from "vue";
import bus from "../views/eventBus.js";
// 导入 VisualMap 组件
// 导入地图数据
import mapData from "../assets/province/zhejiang.json";
//import mapData from "../assets/province/guangdong.json";
import { roma } from "../assets/roma.js";
// 示例数据，需要根据您的实际数据进行替换

// 假设这是您想要标记的经纬度坐标
const starCoordinate = [120.1551, 30.2741]; // 杭州的经纬度
export default {
  data() {
    return {
      locationvalue: {
        LATITUDE: "",
        LONGITUDE: "",
      },
    };
  },
  created() {
    // bus.on 方法注册一个自定义事件，通过事件的处理函数形参接收数据
    bus.on("broSendMsgLocation", (val) => {
      this.locationvalue = val;
      console.log(this.locationvalue);
    });
  },
  setup() {
    // 2.得到echarts
    const $echarts = inject("echarts");
    let mapDataReactive = reactive({});

    onMounted(() => {
      // 将本地导入的地图数据赋值给响应式对象
      mapDataReactive = mapData;

      // console.log('map', mapDataReactive)
      // 3.设置地图
      $echarts.registerMap("china", mapDataReactive);
      const chart = $echarts.init(document.getElementById("cnmapp"), roma);
      chart.setOption({
        grid: {
          left: "10%",
          bottom: "10%",
        },
        geo: {
          map: "china",
          roam: true, // 开启缩放和平移
          zoom: 3.3, // 初始缩放比例
          center: [120.8, 29.2],
          label: {
            show: true,
          },
          label: {
            normal: {
              show: true,
              color: "#fff",
            },
            emphasis: {
              color: "#fff",
            },
          },
          itemStyle: {
            // 定制地图的样式
            //color: "#74913D",
            normal: {
              areaColor: "#67E0FF",
              borderColor: "#FFFFFF",
              borderWidth: 1,
            },
            emphasis: {
              areaColor: "#FFEF47", // 设置鼠标悬停时的颜色
              borderColor: "#AEFF02",
              borderWidth: 1,
            },
          },
        },
        // 使用 VisualMap 组件设置渐变颜色
        series: [
          {
            type: "map",
            map: "china",
            geoIndex: 0,
            aspectScale: 0.75,
            showLegendSymbol: false,
            roam: true,
            // 使用准备好的数据
            data: [],
            label: true,

            // ...省略其他配置,
          },
          {
            name: "星星",
            type: "scatter", // 或者 'effectScatter' 用于涟漪效果
            coordinateSystem: "geo",
            data: [
              {
                name: "选中位置",
                value: [...starCoordinate, 500],
                itemStyle: {
                  color: "#FFB801", // 指定星星的颜色
                }, // 请将 starCoordinate 替换为您想要的经纬度坐标，格式为 [经度, 纬度]
              },
            ],
            symbol: "pin",
            symbolSize: 30, // 星星的大小
            label: {
              show: false,
              formatter: "{b}",
            },
            emphasis: {
              label: {
                show: true,
              },
              textStyle: {
                color: "white", // 设置文字颜色为红色
              },
            },
            visualMap: false, // 禁用此系列的视觉映射
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
  padding: 0rem;
  margin: 0rem;
  height: 8.8rem;
  width: 10rem;
  /* border: 1px solid white; */
  padding: 0.05rem;
  margin-left: -0.8rem;
  margin-right: 0.2rem;
  margin-top: 0.2rem;
}
</style>
