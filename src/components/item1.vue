<template>
  <div id="chartDom" class="chart"></div>
</template>
  <!-- 折线图 -->
  <script>
import { inject, onMounted } from "vue";
import jsonData from "../assets/beijing.json";
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
      const xdata = jsonData.map((item) => item.DATE);
      const ydata = jsonData.map((item) => item.PRCP);//降雨数据
      const y2data = jsonData.map((item) => item.SNDP);//雪深数据
      yChart.setOption({

        textStyle: {
          color: "white", // 设置文字颜色为红色
        },
        title: {
    text: '该地区降雨与降雪数据',
    left: 'center',
    textStyle: {
          color: "white", // 设置文字颜色为红色
        },
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
              type: "jpeg", 
              //backgroundColor: "#000000",
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
    data: ['降雪', '降雨'],
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
  xAxis: [
    {
      type: 'category',
      boundaryGap: false,
      axisLine: { onZero: false },
      // prettier-ignore
      data:xdata
    }
  ],
  yAxis: [
    {
      name: '降雨(单位？)',
      type: 'value'
    },
    {
      name: '降雪(单位？)',
      nameLocation: 'start',
      alignTicks: true,
      type: 'value',
      inverse: true
    }
  ],
  series: [
    {
      name: '降雨',
      type: 'line',
      areaStyle: {},
      lineStyle: {
        width: 1
      },
      emphasis: {
        focus: 'series'
      },
      markArea: {
        silent: true,
        itemStyle: {
          opacity: 0.3
        },
        data: [
          
        ]
      },
      // prettier-ignore
      data: ydata
    },
    {
      name: '降雪',
      type: 'line',
      yAxisIndex: 1,
      areaStyle: {},
      lineStyle: {
        width: 1
      },
      emphasis: {
        focus: 'series'
      },
     
      // prettier-ignore
      data: y2data
    }
  ],
      });
    }
    
    );
    
  },
};
</script>
  <style scope>
#chartDom {
  /* 高度360 */
  /*margin-top: 0.2rem;*/
  height: 3.8rem;
  padding: 0px;
  text-align: center;
}
</style>
  