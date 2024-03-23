<template>
  <div class="p3body">
    <navbar />
    <div class="container">
      <div class="left-top">
        <div class="grid-container">
          <div class="grid-item">
            <img
              src="../assets/kure.jpg"
              alt="Image 1"
              @click="displayText(text1)"
            />
            <div class="overlay-text">01</div>
            <div class="bottom-right-text">热浪</div>
          </div>
          <div class="grid-item">
            <img
              src="../assets/hanchao.jpg"
              alt="Image 2"
              @click="displayText(text2)"
            />
            <div class="overlay-text">02</div>
            <div class="bottom-right-text">寒潮</div>
          </div>
          <div class="grid-item">
            <img
              src="../assets/baoyu.jpg"
              alt="Image 3"
              @click="displayText(text3)"
            />
            <div class="overlay-text">03</div>
            <div class="bottom-right-text">暴雨</div>
          </div>
          <div class="grid-item">
            <img
              src="../assets/jufeng.jpg"
              alt="Image 4"
              @click="displayText(text4)"
            />
            <div class="overlay-text">04</div>
            <div class="bottom-right-text">热带气旋</div>
          </div>
        </div>
      </div>
      <div class="right-top">
        <div id="text-display">{{ displayedText }}</div>
      </div>
      <div class="left-bottom">
        <div class="inline-item">
          <el-cascader
            class="inline-item2"
            size="small"
            :options="options"
            v-model="selectedOptions"
            @change="handleChange"
            placeholder="北京市"
          >
          </el-cascader>

          <el-button class="inline-item" round @click="getData"
            >点击查询</el-button
          ><cnmap />
        </div>
      </div>
      <div class="right-bottom"><lunbo /></div>
    </div>
  </div>
</template>

<script>
import { provinceAndCityData, CodeToText } from "element-china-area-data";
import cnmap from "@/components/cnmap.vue";
import lunbo from "@/components/lunbo.vue";
import navbar from "@/components/navbar.vue";
import axios from "axios";
import bus from "./eventBus.js";
export default {
  components: {
    cnmap,
    lunbo,
    navbar,
  },
  data() {
    return {
      displayedText: "",
      text1:
        "高温热浪是指持续一段时间的异常高温天气过程,目前尚没有统一的判定标准。中国气象局将日最高气温大于等于35 ℃作为判定高温日的阈值,同时规定各省市区可以根据本地天气气候特征规定界限温度值。 中国幅员辽阔,地区间气候条件差异大,在研究高温热浪发生频次、持续时间等特征的区域差异时,若采用同一温度阈值会造成南多北少的结果,因此,相比绝对阈值,利用百分位方法定义阈值能客观对比区域之间高温热浪分布特征的差异。具体方法为将每个站点2000-2023年的逐日最高温度数据进行排序,并取第95%分位数为各站点高温阈值,当某一站点日最高温度超过该站高温阈值时记为一个高温日,然后利用高温日持续时间的长短确定高温热浪等级,高温日持续3d及以上但不足5d时,记为一次弱高温热浪过程;高温日持续5d及以上但不足7d时,记为一次中强高温热浪过程;高温日持续7d及以上,记为一次强高温热浪过程。",
      text2:
        "本项目中，按照（BG/T 21987-2008）定义中国北方寒潮发生的标准，即平均气温24h内降低幅度>=8℃，且日最低气温<=4℃，则可判定为一次寒潮，并结合中华人民共和国（BG/T 21987-2008）寒潮等级标准和《气象灾害预警信号发布与传播办法》中的寒潮预警信号的规定来确定中国北方地区单站寒潮强度等级划分，具体划分为：\n1、一般寒潮：24h降温幅度>=8℃ and 日最低气温<=4℃\n2、较强寒潮：24h降温幅度>=10℃ and 日最低气温<=4℃\n3、强寒潮：24h降温幅度>=12℃ and 日最低气温<=0℃\n4、特强寒潮：24h降温幅度>=16℃ and 日最低气温<=0℃",
      text3:
        "暴雨是指降水强度很大的雨，常在积雨云中形成。中国气象上规定，24小时降水量为50毫米或以上的雨称为“暴雨”。按其降水强度大小又分为三个等级，即24小时降水量为50-99.9毫米称“暴雨”、100-249.9毫米之间为“大暴雨”、250毫米以上称“特大暴雨”。",
      text4:
        "热带气旋生成于热带或副热带洋面上，具有有组织的对流和确定的气旋性环流的非锋面性涡旋的统称，包括热带低压、热带风暴、强热带风暴、台风、强台风和超强台风。本项目根据中华人民共和国国家标准（GB/T 19201—2006）以及蒲福风力等级表，使用最大阵风对风力进行七种划分，分别如下：\n6级： 强风 10.8—13.8 m/s,\n7级： 疾风 13.9—17.1 m/s\n8级： 大风 17.2—20.7 m/s\n9级： 烈风 20.8—24.4 m/s\n10级：狂风 24.5—28.4 m/s\n11级：暴风 28.5—32.6 m/s\n12级：飓风 32.7—36.9 m/s",
      options: provinceAndCityData,
      selectedOptions: [],
    };
  },
  methods: {
    displayText(text) {
      this.displayedText = text;
    },
    getData() {
      // 这是跟后端请求数据的接口
      // 制作向服务器端发送的数据
      const province = CodeToText[this.selectedOptions[0]];
      let city = "";
      if (this.selectedOptions.length > 1) {
        city = CodeToText[this.selectedOptions[1]];
      }
      console.log("省份: ", province, " 城市: ", city); // 打印区域码所对应的属性值即中文地址
      // 这是服务器通信的地址
      const path = "http://127.0.0.1:5000/getMessage3";
      const dataToSend = {
        province: province,
        city: city,
      };
      axios
        .get(path, { params: dataToSend })
        .then((res) => {
          // 这里服务器返回response为一个json对象
          // 通过.data来访返回的数据，然后在通过.变量名进行访问
          // 可以直接通过response.data取得key-value
          const msg = res.data.msg; // 返回的数据

          // 把数据分下去
          // 给第一个图表制作数据
          const figure1 = {
            YearData: msg.YearData,
            General_Coldwave: msg.General_Coldwave,
            Moderate_Coldwave: msg.Moderate_Coldwave,
            Strong_Coldwave: msg.Strong_Coldwave,
            Severe_Coldwave: msg.Severe_Coldwave,
          };
          bus.emit("broSendMsgCold", figure1);

          // 给第二个图表制作数据
          const figure2 = {
            YearData: msg.YearData,
            Heavy_Rainfall: msg.Heavy_Rainfall,
            Severe_Rainfall: msg.Severe_Rainfall,
            Extreme_Rainfall: msg.Extreme_Rainfall,
          };
          bus.emit("broSendMsgRain", figure2);

          // 给第三个图表制作数据
          const figure3 = {
            YearData: msg.YearData,
            High_Threshold: msg.High_Threshold,
            Weak_Heatwave: msg.Weak_Heatwave,
            Moderate_Heatwave: msg.Moderate_Heatwave,
            Strong_Heatwave: msg.Strong_Heatwave,
          };
          bus.emit("broSendMsgHeat", figure3);

          // 给第四个图表制作数据
          const figure4 = {
            YearData: msg.YearData,
            Grade_6_Wind: msg.Grade_6_Wind,
            Grade_7_Wind: msg.Grade_7_Wind,
            Grade_8_Wind: msg.Grade_8_Wind,
            Grade_9_Wind: msg.Grade_9_Wind,
            Grade_10_Wind: msg.Grade_10_Wind,
            Grade_11_Wind: msg.Grade_11_Wind,
            Grade_12_Wind: msg.Grade_12_Wind,
          };
          console.log("haha", figure4);
          bus.emit("broSendMsgWind2", figure4);

          // console.log(msg) // 因为不能直接使用this作为指针，因此在这之前将this赋给了then指针
          // window.alter('Success' + this.serverResponse.status + ',' + this.serverResponse.data + ',' + msg); // 成功后显示提示
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>
.p3body {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url("../assets/p3bg.svg");
  background-size: cover;
}
.container {
  height: auto;
  display: flex;
  flex-wrap: wrap;
  margin: 0.125rem;
}
.container > div {
  box-sizing: border-box;
}
.left-top {
  width: calc(50% - 0.25rem);
  height: 30%;

  box-sizing: border-box;
}

.right-top {
  width: calc(50% - 0.25rem);
  height: 70%;

  box-sizing: border-box;
}

.left-bottom {
  width: calc(50% - 0.25rem);
  height: 60%;

  box-sizing: border-box;
}

.right-bottom {
  width: calc(50% - 0.25rem);
  height: 60%;

  box-sizing: border-box;
}
.grid-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 0.125rem;
}

.grid-item {
  position: relative; /* 确保使用相对定位，便于控制内部元素 */
  overflow: hidden; /* 隐藏超出容器的图片部分 */
  height: 1.6rem;
  margin: 0.1rem;
  margin-left: 0.5rem;
}

.grid-item img {
  width: 90%; /* 设置图片宽度为容器的100%，确保横向铺满 */
  height: 100%; /* 设置图片高度为容器的100%，确保纵向铺满 */
  object-fit: cover; /* 保持图片的宽高比，超出的部分会被裁剪 */
  cursor: pointer; /* 保留点击指针样式 */
  border-radius: 10px;
}

.grid-item .content {
  display: none;
  position: absolute;
  top: 0;
  left: 0;
  width: 20%;
  height: 20%;
  background-color: rgba(0, 0, 0, 0.8);
  color: #fff;
  text-align: center;
  padding: 0.25rem;
  margin: 0.25rem;
}

.grid-item:hover .content {
  display: block;
}

#text-display {
  margin-top: 0.25rem;
  background-color: transparent;
  padding: 0.125rem;
  font-size: 0.225rem;
  font-weight: bold;
  color: white;
  white-space: pre-line;
}
.image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
}

.grid-item .overlay-text,
.grid-item .bottom-right-text {
  position: absolute;
  color: white;
  padding: 10px;
  background-color: transparent;
  /* 设置文字大小为20px */
  font-weight: bold; /* 文字加粗 */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
  font-style: italic;
}

.grid-item .overlay-text {
  font-size: 50px;
  top: -25px;
  left: 0px;
  border-top-left-radius: 10px; /* 文字背景的左上角圆角 */
}

.grid-item .bottom-right-text {
  font-size: 30px;
  bottom: 0;
  right: 50px;
  border-bottom-right-radius: 10px; /* 文字背景的右下角圆角 */
}
.inline-item {
  margin-left: 100px;
  margin-top: 10px;
}

/* */
</style>
