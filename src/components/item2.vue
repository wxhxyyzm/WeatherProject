<template>
  <!-- 降水信息 -->
  <div id="chartDomy" class="chart"></div>

</template>
  <!-- 折线图 -->
  <script>
import { inject, onMounted } from "vue";
import jsonData from "../assets/beijing.json";
import bus from "./eventBus.js";
import echarts from "echarts";
import {roma} from "../assets/roma.js";
export default {
name: "Bro3",
data() {
  return {
    rainvalue: {
      TREASURE_DATE: [],
      PRCP: [],
    },
  };
},
created() {
  // bus.on 方法注册一个自定义事件，通过事件的处理函数形参接收数据
  bus.on("broSendMsgRain", (val) => {
    this.rainvalue = val;
    console.log(this.rainvalue);
  });
},
setup() {
  // 得到echarts对象
  let $echarts = inject("echarts");
  // 需要获取到element,所以是onMounted 别忘了上面引用
  onMounted(() => {
    // 初始化echarts 别忘了给上面echarts容器添加id
    let myChart = $echarts.init(document.getElementById("chartDomy"),roma);
    // 绘制图表
    //let xdata = ["1", "2", "3", "4", "5", "6", "7"]; //改数据
    //let maxdata = [820, 932, 901, 934, 1290, 1330, 1320];
    //let mindata = [120, 132, 101, 134, 90, 230, 210];
    //let avgdata = [320, 332, 301, 334, 390, 330, 320];
    const xdata = jsonData.map((item) => item.DATE);
    const y2data = jsonData.map((item) => item.DEWP);//露点温度
    const ydata = jsonData.map((item) => item.TEMP);//平均温度
    myChart.setOption({
      title: {
  text: '露点与日均温',
  left: 'center',
},
left: 'center',
grid: {
        left: "10%",
        bottom: "15%",
      },
legend: {
  data: ['日均温','露点温度'],
  left: 10
},
toolbox: {
        feature: {
          restore: {},
          saveAsImage: {
            pixelRatio: 2,
          },
        },
      },
      dataZoom: [
  {
    show: false,
  },
  {
    type: 'inside',
  }
],
tooltip: {
  trigger: 'axis',
  axisPointer: {
    type: 'cross',
    animation: false,
    label: {
      backgroundColor: '#505765'
    }
  }
},
xAxis: {
  data: xdata,
  splitLine: {
    show: false
  }
},
yAxis: {},
series: [
  {
    name: '日均温',
    type: 'bar',
    data: ydata,
    animationDelay: function (idx) {
      return idx * 5;
    }
  },
  {
    name: '露点温度',
    type: 'bar',
    data: y2data,
    animationDelay: function (idx) {
      return idx * 5 + 100;
    }
  }
],
animationEasing: 'elasticOut',
animationDelayUpdate: function (idx) {
  return idx * 5;
}
    });
  });
},
watch: {
  rainvalue: function (newvalue, oldvalue) {
    if (oldvalue !== newvalue) {
      var echarts = require("echarts");
      var yChart = echarts.init(document.getElementById("chartDomy"));
      const xdata = this.rainvalue["TREASURE_DATE"];
      const ydata = this.rainvalue["PRCP"];
      yChart.setOption({
        title: {
          text: "降水",
          x: "center",
        },
        grid: {
          left: "10%",
          bottom: "10%",
        },
        toolbox: {
          feature: {
            saveAsImage: {
              pixelRatio: 2,
            },
          },
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },

        xAxis: {
          data: xdata,
          silent: false,
          splitLine: {
            show: false,
          },
          splitArea: {
            show: false,
          },
        },
        yAxis: {
          splitArea: {
            show: false,
          },
        },
        series: [
          {
            type: "line",
            data: ydata,
            // Set `large` for large data amount
            large: true,
            sort: "ascending",
            markPoint: {
              data: [
                {
                  type: "max",
                  name: "最大值",
                  label: {
                    show: true,
                    formatter: "{b}: {c}",
                  },
                },
                {
                  type: "min",
                  name: "最小值",
                  label: {
                    show: true,
                    formatter: "{b}: {c}",
                  },
                },
              ],
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
#chartDomy {
/* 高度360 */
/* height: 3.9rem; */
/*margin-top: 0.2rem;*/
height: 3.8rem;
padding: 0px;
background-color: transparent;
}
</style>
