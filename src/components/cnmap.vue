<template>
  <div class="map" id="cnmap">map</div>
</template>

<script>
// 1.引用
import { onMounted, reactive, inject } from "vue";
import bus from "../views/eventBus.js";
// 导入 VisualMap 组件
// 导入地图数据
import mapData from "../assets/china.json";
import { roma } from "../assets/roma.js";
// 示例数据，需要根据您的实际数据进行替换
const data = [
  { name: "广东省", value: "35" },
  { name: "北京市", value: "25" },
  { name: "天津市", value: "25" },
  { name: "上海市", value: "35" },
  { name: "重庆市", value: "35" },
  { name: "江苏省", value: "35" },
  { name: "浙江省", value: "35" },
  { name: "福建省", value: "35" },
  { name: "湖南省", value: "35" },
  { name: "湖北省", value: "35" },
  { name: "广西壮族自治区", value: "35" },
  { name: "云南省", value: "35" },
  { name: "贵州省", value: "35" },
  { name: "四川省", value: "25" },
  { name: "山东省", value: "25" },
  { name: "河南省", value: "25" },
  { name: "安徽省", value: "35" },
  { name: "河北省", value: "25" },
  { name: "江西省", value: "35" },
  { name: "山西省", value: "25" },
  { name: "辽宁省", value: "25" },
  { name: "吉林省", value: "25" },
  { name: "黑龙江省", value: "25" },
  { name: "陕西省", value: "25" },
  { name: "甘肃省", value: "45" },
  { name: "青海省", value: "15" },
  { name: "台湾省", value: "35" },
  { name: "内蒙古自治区", value: "45" },
  { name: "西藏自治区", value: "15" },
  { name: "宁夏回族自治区", value: "45" },
  { name: "新疆维吾尔自治区", value: "45" },
  { name: "香港特别行政区", value: "35" },
  { name: "澳门特别行政区", value: "35" },
  { name: "海南省", value: "55" },
  { name: "南海诸岛", value: "55" },
];

// 假设这是您想要标记的经纬度坐标
const starCoordinate = [116.405285, 39.904989]; // 北京的经纬度

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
      const chart = $echarts.init(document.getElementById("cnmap"), roma);
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
              borderColor: "#FFFFFF",
            },
            emphasis: {
              areaColor: "#FF7A30", // 设置鼠标悬停时的颜色
              borderColor: "#FFFFFF",
            },
          },
        },
        // 使用 VisualMap 组件设置渐变颜色
        visualMap: {
          min: 0,
          max: 100,
          left: 10,
          bottom: 0,
          showLabel: !0,
          // text: ["高", "低"],
          pieces: [
            {
              gt: 50,
              label: "热带季风气候",
              color: "#F7BF27",
            },
            {
              gte: 40,
              lte: 50,
              label: "温带大陆性气候",
              color: "#64FAED",
            },
            {
              gte: 30,
              lte: 40,
              label: "亚热带季风气候",
              color: "#FFF26D",
            },
            {
              gte: 20,
              lte: 30,
              label: "温带季风气候",
              color: "#0CB1E5",
            },
            {
              gte: 10,
              lte: 20,
              label: "高原山地气候",
              color: "#FF9DE6",
            },
          ],
          textStyle: {
            color: "white", // 设置文字颜色为红色
          },
          show: !0,
        },
        series: [
          {
            type: "map",
            map: "china",
            geoIndex: 0,
            aspectScale: 0.75,
            showLegendSymbol: false,
            roam: true,
            // 使用准备好的数据
            data: data,
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
                  color: "#D20062", // 指定星星的颜色
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

  watch: {
    locationvalue: function (newvalue, oldvalue) {
      if (oldvalue !== newvalue) {
        const echarts = require("echarts");
        echarts.registerMap("china", mapData);
        const yChart = echarts.init(document.getElementById("cnmap"), roma);
        starCoordinate[0] = this.locationvalue.LONGITUDE[0];
        starCoordinate[1] = this.locationvalue.LATITUDE[0];
        console.log("haha", starCoordinate);
        yChart.setOption({
          grid: {
            left: "10%",
            bottom: "25%",
          },
          geo: {
            map: "china",
            roam: true, // 开启缩放和平移
            zoom: 3.6, // 初始缩放比例
            center: starCoordinate,
            label: {
              emphasis: {
                show: false,
              },
            },
            itemStyle: {
              // 定制地图的样式
              normal: {
                borderColor: "#FFFFFF",
              },
              emphasis: {
                areaColor: "#FF7A30", // 设置鼠标悬停时的颜色
                borderColor: "#FFFFFF",
              },
            },
          },
          // 使用 VisualMap 组件设置渐变颜色
          visualMap: {
            min: 0,
            max: 100,
            left: 10,
            bottom: 0,
            showLabel: !0,
            // text: ["高", "低"],
            pieces: [
              {
                gt: 50,
                label: "热带季风气候",
                color: "#F7BF27",
              },
              {
                gte: 40,
                lte: 50,
                label: "温带大陆性气候",
                color: "#64FAED",
              },
              {
                gte: 30,
                lte: 40,
                label: "亚热带季风气候",
                color: "#FFF26D",
              },
              {
                gte: 20,
                lte: 30,
                label: "温带季风气候",
                color: "#0CB1E5",
              },
              {
                gte: 10,
                lte: 20,
                label: "高原山地气候",
                color: "#FF9DE6",
              },
            ],
            textStyle: {
              color: "white", // 设置文字颜色为红色
            },
            show: !0,
          },
          series: [
            {
              type: "map",
              map: "china",
              geoIndex: 0,
              aspectScale: 0.75,
              showLegendSymbol: false,
              roam: true,
              // 使用准备好的数据
              data: data,
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
                    color: "#D20062", // 指定星星的颜色
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
      }
    },
  },
};
</script>

<style>
.map {
  padding: 0.3rem;
  margin: 0.3rem;
  height: 6.8rem;
}
</style>
