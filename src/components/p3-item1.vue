<template>
  <div id="chartDom" class="chart"></div>
</template>
  <!-- 折线图 -->
  <script>
import { inject, onMounted } from "vue";
import jsonData from "../assets/unclimate.json";
import bus from "./eventBus.js";
import {roma} from "../assets/roma.js";
export default {
  name: "Bro2",
  data() {
    return {
      newvalue: {
        TREASURE_DATE: [],
        DEWP: [],
      },
    };
  },
  created() {
    // bus.on 方法注册一个自定义事件，通过事件的处理函数形参接收数据
    bus.on("broSendMsg", (val) => {
      this.newvalue = val;
      console.log(this.newvalue);
    });
  },

  setup() {
    // 得到echarts对象
    let $echarts = inject("echarts");
    // 需要获取到element,所以是onMounted 别忘了上面引用
    onMounted(() => {
      // 初始化echarts 别忘了给上面echarts容器添加id
      let yChart = $echarts.init(document.getElementById("chartDom"),roma);
      // 绘制图表
      //let xdata = ["1", "2", "3", "4", "5", "6", "7"];
      //let ydata = [820, 932, 901, 934, 1290, 1330, 1320];
      //DEWP
      const xdata = jsonData.map((item) => item.YearData);
      const ydata = jsonData.map((item) => item.General_Coldwave);//降雨数据
      const y2data = jsonData.map((item) => item.Moderate_Coldwave);//雪深数据
      const y3data = jsonData.map((item) => item.Strong_Coldwave);//雪深数据
      const y4data = jsonData.map((item) => item.Severe_Coldwave);//雪深数据
      yChart.setOption({
        title: {
    text: '该地区寒潮',
    left: 'center',
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
    trigger: 'axis',
    axisPointer: {
      type: 'cross',
      animation: false,
      label: {
        backgroundColor: '#505765'
      }
    }
  },
  legend: {
    data: ['小寒潮', '中寒潮','强寒潮','严重寒潮'],
    left: 10
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
      // Use axis to trigger tooltip
      type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
    }
  },
  xAxis: {
    type: 'value'
  },
  yAxis: {
    type: 'category',
    data: xdata
  },
  series: [
    {
      name: '小寒潮',
      type: 'bar',
      stack: 'total',
      label: {
        show: true
      },
      emphasis: {
        focus: 'series'
      },
      data: ydata
    },
    {
      name: '中寒潮',
      type: 'bar',
      stack: 'total',
      label: {
        show: true
      },
      emphasis: {
        focus: 'series'
      },
      data: y2data
    },
    {
      name: '强寒潮',
      type: 'bar',
      stack: 'total',
      label: {
        show: true
      },
      emphasis: {
        focus: 'series'
      },
      data: y3data
    },
    {
      name: '严重寒潮',
      type: 'bar',
      stack: 'total',
      label: {
        show: true
      },
      emphasis: {
        focus: 'series'
      },
      data: y4data
    }
  ]
 
      });
    });
  },
};
</script>
  <style scope>
#chartDom {
  /* 高度360 */
  /*margin-top: 0.2rem;*/
  height: 6rem;
  padding: 0px;
  text-align: center;
}
</style>
  