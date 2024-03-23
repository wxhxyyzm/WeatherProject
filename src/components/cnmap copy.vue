<template>
  <div class="map" id="cnmap"></div>
</template>

<script>
import { onMounted, ref } from "vue";
import * as echarts from "echarts/core";
import { MapChart } from "echarts/charts";
import { LegendComponent, TooltipComponent } from "echarts/components";
import { SVGRenderer } from "echarts/renderers";
import mapData from "../assets/china.json";

// 注册 ECharts 需要的组件
echarts.use([MapChart, LegendComponent, TooltipComponent, SVGRenderer]);
const data = [
  { name: "广东省", value: "亚热带季风气候" },
  { name: "北京市", value: "温带季风气候" },
  { name: "上海市", value: "亚热带季风气候" },
  { name: "重庆市", value: "亚热带季风气候" },
  { name: "江苏省", value: "亚热带季风气候" },
  { name: "浙江省", value: "亚热带季风气候" },
  { name: "福建省", value: "亚热带季风气候" },
  { name: "湖南省", value: "亚热带季风气候" },
  { name: "湖北省", value: "亚热带季风气候" },
  { name: "广西壮族自治区", value: "亚热带季风气候" },
  { name: "云南省", value: "亚热带季风气候" },
  { name: "贵州省", value: "亚热带季风气候" },
  { name: "四川省", value: "温带季风气候" },
  { name: "山东省", value: "温带季风气候" },
  { name: "河南省", value: "温带季风气候" },
  { name: "安徽省", value: "亚热带季风气候" },
  { name: "河北省", value: "温带季风气候" },
  { name: "江西省", value: "亚热带季风气候" },
  { name: "山西省", value: "温带季风气候" },
  { name: "辽宁省", value: "温带季风气候" },
  { name: "吉林省", value: "温带季风气候" },
  { name: "黑龙江省", value: "温带季风气候" },
  { name: "陕西省", value: "温带季风气候" },
  { name: "甘肃省", value: "温带大陆性气候" },
  { name: "青海省", value: "高原山地气候" },
  { name: "台湾省", value: "亚热带季风气候" },
  { name: "内蒙古自治区", value: "温带大陆性气候" },
  { name: "西藏自治区", value: "高原山地气候" },
  { name: "宁夏回族自治区", value: "温带大陆性气候" },
  { name: "新疆维吾尔自治区", value: "温带大陆性气候" },
  { name: "香港特别行政区", value: "亚热带季风气候" },
  { name: "澳门特别行政区", value: "亚热带季风气候" },
  { name: "海南省", value: "热带季风气候" },
  { name: "南海诸岛", value: "热带季风气候" },
];
export default {
  setup() {
    const cnmap = ref(null);

    // 数据和颜色映射
    const colorMap = {
      亚热带季风气候: "#ff0000",
      温带季风气候: "#0000ff",
      高原山地气候: "#8B4513",
      温带大陆性气候: "#2E8B57",
      热带季风气候: "#FFD700",
    };

    // 转换数据为 ECharts series 格式
    const convertDataToSeries = () => {
      const climateTypes = Object.keys(colorMap);
      const series = climateTypes.map((climate) => ({
        name: climate,
        type: "map",
        mapType: "china",
        label: {
          show: true,
          formatter: "{b}",
        },
        data: data
          .filter((item) => item.value === climate)
          .map((item) => ({
            name: item.name,
            value: Math.random() * 1000, // 随机数仅为示例，实际应用中可能需要根据具体数据来设置
          })),
        itemStyle: {
          areaColor: colorMap[climate],
        },
      }));

      return series;
    };

    onMounted(() => {
      echarts.registerMap("china", mapData);

      const chart = echarts.init(cnmap.value);
      chart.setOption({
        tooltip: {
          trigger: "item",
          formatter: "{b}: {c}",
        },
        legend: {
          orient: "vertical",
          left: "left",
          data: Object.keys(colorMap),
        },
        series: convertDataToSeries(),
      });
    });

    return {
      cnmap,
    };
  },
};
</script>

<style>
.map {
  padding: 0.3rem;
  margin: 0.3rem;
  height: 500px; /* 调整为实际需要的高度 */
  border: 2px solid white;
}
</style>
