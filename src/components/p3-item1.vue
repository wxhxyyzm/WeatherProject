<template>
  <div id="chartDom" class="chart"></div>
</template>
  <!-- 折线图 -->
<script>
import { inject, onMounted } from "vue";
import jsonData from "../assets/unclimate.json";
import bus from "../views/eventBus.js";
import { roma } from "../assets/roma.js";
import echarts from "echarts";
export default {
  // name: 'Bro2',
  data() {
    return {
      coldvalue: {
        YearData: [],
        General_Coldwave: [],
        Moderate_Coldwave: [],
        Strong_Coldwave: [],
        Severe_Coldwave: [],
      },
    };
  },
  created() {
    // bus.on 方法注册一个自定义事件，通过事件的处理函数形参接收数据
    bus.on("broSendMsgCold", (val) => {
      this.coldvalue = val;
      console.log(this.coldvalue);
    });
  },

  setup() {
    // 得到echarts对象
    const $echarts = inject("echarts");
    // 需要获取到element,所以是onMounted 别忘了上面引用
    onMounted(() => {
      // 初始化echarts 别忘了给上面echarts容器添加id
      const yChart = $echarts.init(document.getElementById("chartDom"), roma);
      // 绘制图表
      // DEWP
      const xdata = jsonData.map((item) => item.YearData);
      const ydata = jsonData.map((item) => item.General_Coldwave); // 一般寒潮
      const y2data = jsonData.map((item) => item.Moderate_Coldwave); // 中等寒潮
      const y3data = jsonData.map((item) => item.Strong_Coldwave); // 大寒潮
      const y4data = jsonData.map((item) => item.Severe_Coldwave); // 特强寒潮
      yChart.setOption({
        title: {
          text: "该地区寒潮",
          left: "center",
        },
        grid: {
          left: "10%",
          bottom: "15%",
        },
        toolbox: {
          feature: {
            restore: {},
            saveAsImage: {
              pixelRatio: 2,
            },
          },
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
            animation: false,
            label: {
              backgroundColor: "#505765",
            },
          },
        },
        legend: {
          data: [" 一般寒潮", "较强寒潮", "强寒潮", "特强寒潮"],
          left: "center",
          top: 25,
        },
        dataZoom: [
          {
            show: false,
          },
          {
            type: "inside",
          },
        ],
        tooltip: {
          trigger: "axis",
          axisPointer: {
            // Use axis to trigger tooltip
            type: "shadow", // 'shadow' as default; can also be 'line' or 'shadow'
          },
        },
        xAxis: {
          type: "value",
        },
        yAxis: {
          type: "category",
          data: xdata,
          name: "次数",
        },
        series: [
          {
            name: " 一般寒潮",
            type: "bar",
            stack: "total",
            emphasis: {
              focus: "series",
            },
            data: ydata,
            itemStyle: {
              barBorderRadius: [2, 2, 0, 0], //柱体圆角
              color: new $echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  //代表渐变色从正上方开始
                  offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                  color: "#F7B70B",
                }, //柱图渐变色
                {
                  offset: 1, //指100%处的颜色
                  color: "#FFF26D",
                },
              ]),
            },
          },
          {
            name: "较强寒潮",
            type: "bar",
            stack: "total",
            emphasis: {
              focus: "series",
            },
            data: y2data,
            itemStyle: {
              barBorderRadius: [2, 2, 0, 0], //柱体圆角
              color: new $echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  //代表渐变色从正上方开始
                  offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                  color: "#659400",
                }, //柱图渐变色
                {
                  offset: 1, //指100%处的颜色
                  color: "#AEFF02",
                },
              ]),
            },
          },
          {
            name: "强寒潮",
            type: "bar",
            stack: "total",
            emphasis: {
              focus: "series",
            },
            data: y3data,
            itemStyle: {
              barBorderRadius: [2, 2, 0, 0], //柱体圆角
              color: new $echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  //代表渐变色从正上方开始
                  offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                  color: "#996794",
                }, //柱图渐变色
                {
                  offset: 1, //指100%处的颜色
                  color: "#FFACF7",
                },
              ]),
            },
          },
          {
            name: "特强寒潮",
            type: "bar",
            stack: "total",
            emphasis: {
              focus: "series",
            },
            data: y4data,
            itemStyle: {
              barBorderRadius: [2, 2, 0, 0], //柱体圆角
              color: new $echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  //代表渐变色从正上方开始
                  offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                  color: "#57B2F4",
                }, //柱图渐变色
                {
                  offset: 1, //指100%处的颜色
                  color: "#67E0FF",
                },
              ]),
            },
          },
        ],
      });
    });
  },

  watch: {
    coldvalue: function (newvalue, oldvalue) {
      if (oldvalue !== newvalue) {
        const echarts = require("echarts");
        const yChart = echarts.init(document.getElementById("chartDom"), roma);
        const xdata = this.coldvalue.YearData;
        const ydata = this.coldvalue.General_Coldwave;
        const y2data = this.coldvalue.Moderate_Coldwave;
        const y3data = this.coldvalue.Strong_Coldwave;
        const y4data = this.coldvalue.Severe_Coldwave;

        yChart.setOption({
          title: {
            text: "该地区寒潮",
            left: "center",
          },
          grid: {
            left: "10%",
            bottom: "15%",
          },
          toolbox: {
            feature: {
              restore: {},
              saveAsImage: {
                pixelRatio: 2,
              },
            },
          },
          tooltip: {
            trigger: "axis",
            axisPointer: {
              type: "cross",
              animation: false,
              label: {
                backgroundColor: "#505765",
              },
            },
          },
          legend: {
            data: [" 一般寒潮", "较强寒潮", "强寒潮", "特强寒潮"],
            left: "center",
            top: 25,
          },
          dataZoom: [
            {
              show: false,
            },
            {
              type: "inside",
            },
          ],
          tooltip: {
            trigger: "axis",
            axisPointer: {
              // Use axis to trigger tooltip
              type: "shadow", // 'shadow' as default; can also be 'line' or 'shadow'
            },
          },
          xAxis: {
            type: "value",
          },
          yAxis: {
            type: "category",
            data: xdata,
            name: "次数",
          },
          series: [
            {
              name: " 一般寒潮",
              type: "bar",
              stack: "total",
              emphasis: {
                focus: "series",
              },
              data: ydata,
              itemStyle: {
                barBorderRadius: [2, 2, 0, 0], //柱体圆角
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  {
                    //代表渐变色从正上方开始
                    offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                    color: "#F7B70B",
                  }, //柱图渐变色
                  {
                    offset: 1, //指100%处的颜色
                    color: "#FFF26D",
                  },
                ]),
              },
            },
            {
              name: "较强寒潮",
              type: "bar",
              stack: "total",
              emphasis: {
                focus: "series",
              },
              data: y2data,
              itemStyle: {
                barBorderRadius: [2, 2, 0, 0], //柱体圆角
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  {
                    //代表渐变色从正上方开始
                    offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                    color: "#659400",
                  }, //柱图渐变色
                  {
                    offset: 1, //指100%处的颜色
                    color: "#AEFF02",
                  },
                ]),
              },
            },
            {
              name: "强寒潮",
              type: "bar",
              stack: "total",
              emphasis: {
                focus: "series",
              },
              data: y3data,
              itemStyle: {
                barBorderRadius: [2, 2, 0, 0], //柱体圆角
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  {
                    //代表渐变色从正上方开始
                    offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                    color: "#996794",
                  }, //柱图渐变色
                  {
                    offset: 1, //指100%处的颜色
                    color: "#FFACF7",
                  },
                ]),
              },
            },
            {
              name: "特强寒潮",
              type: "bar",
              stack: "total",
              emphasis: {
                focus: "series",
              },
              data: y4data,
              itemStyle: {
                barBorderRadius: [2, 2, 0, 0], //柱体圆角
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  {
                    //代表渐变色从正上方开始
                    offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                    color: "#57B2F4",
                  }, //柱图渐变色
                  {
                    offset: 1, //指100%处的颜色
                    color: "#67E0FF",
                  },
                ]),
              },
            },
          ],
        });
      }
    },
  },
};
</script>
  <style scope>
#chartDom {
  /* 高度360 */
  /*margin-top: 0.2rem;*/
  height: 7.5rem;
  padding: 0px;
  text-align: center;
}
</style>
