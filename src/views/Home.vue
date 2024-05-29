<template>
  <div>
    <!-- Header -->

    <!-- Main Banner Section -->
    <section class="w3l-main-banner" id="home">
      <div class="companies20-content">
        <div class="companies-wrapper">
          <div class="item">
            <div class="slider-info banner-view text-center">
              <div class="banner-info container">
                <div class="maintitle">观云图志</div>
                <p class="my-4 mb-5">
                  系统旨在探寻全国气象数据分布与极端天气出现的时空规律，以此对人们的生产生活进行指导
                </p>
                <br />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section></section>
    <!-- Feature Section -->
    <section class="w3l-feature-3" id="features">
      <div class="grid top-bottom">
        <div class="container">
          <!-- <div class="heading text-center mx-auto">
            <h3 class="head text-white">主系统有三个部分</h3>
          </div> -->
          <div class="heading text-center mx-auto">
            <h3 class="head text-white">主系统有三个部分</h3>
            <p class="my-1 head text-white">
              获取全国二百余个城市过去二十年的历史天气数据
            </p>
            <p class="my-1 head text-white">
              使用图表对各城市的气象数据进行可视化处理，并根据极端天气的定义进行统计分析
            </p>
            <p class="my-1 head text-white">
              展示气候指标变化规律与极端天气分布的时空规律，并对未来的气象指标进行一定的预测
            </p>
          </div>
          <div class="middle-section grid-column text-center mt-5 pt-3">
            <div
              class="three-grids-columns"
              v-for="(feature, index) in features"
              :key="index"
            >
              <span :class="feature.icon" style="color: dodgerblue"></span>
              <h4>{{ feature.title }}</h4>
              <p>{{ feature.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials Section -->
    <section class="w3l-testimonials" id="testimonials">
      <div
        class="title"
        style="text-align: center; font-size: 24px; margin-top: 50px"
      >
        点击登录，进入系统
      </div>
      <div class="container py-lg-3">
        <div class="row">
          <div class="col-md-6">
            <router-link to="/loginuser" class="card-link">
              <div class="card">
                <div class="card-header text-center">
                  <img
                    src="../images/user.png"
                    alt="icon"
                    class="icon-center"
                  />
                </div>
                <div
                  class="card-body"
                  style="
                    height: 200px;
                    text-align: center;
                    font-size: 24px;
                    /* margin-top: 20px; */
                  "
                >
                  <p>用户由此登录</p>
                </div>
              </div>
            </router-link>
          </div>
          <div class="col-md-6">
            <router-link to="/loginmanager" class="card-link">
              <div class="card">
                <div class="card-header text-center">
                  <img
                    src="../images/manager.png"
                    alt="icon"
                    class="icon-center"
                  />
                </div>
                <div
                  class="card-body"
                  style="
                    height: 200px;
                    text-align: center;
                    font-size: 24px;
                    /* margin-top: 20px; */
                  "
                >
                  <p>管理员由此登录</p>
                </div>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </section>
    <button @click="topFunction" id="movetop" title="Go to top"></button>
    <!-- Footer Section -->
    <section class="w3l-footer-29-main" id="footer">
      <div class="footer-29 text-center">
        <div class="container">
          <p class="copy-footer-29">
            Copyright &copy; 2024. Company name All rights reserved.
          </p>
        </div>
      </div>
    </section>
  </div>
</template>
  
  <script>
import "../css/style-starter.css";
//import {} from "../js/lightbox-plus-jquery.min.js";
import "../js/popper.min.js";
import "../js/bootstrap.min.js";

export default {
  data() {
    return {
      skills: [
        { name: "Design", width: "50%", value: 50 },
        { name: "Marketing", width: "80%", value: 80 },
        { name: "Photography", width: "60%", value: 60 },
      ],
      features: [
        {
          icon: "fa fa-mixcloud",
          title: "天气简报",
          description:
            "数据来源于美国国家海洋和大气管理局网站上的气象站开源数据，批量下载并处理超过1600万条数据。为每个城市选择一个气象站，获取该城市2000年1月1日至2024年2月29日间的气象数据。气象指标包括日均温、日最高气温、日最低气温、日露点温度、可见度、降雨量和风速等相关信息。",
        },
        {
          icon: "fa fa-expand",
          title: "极端天气",
          description:
            "定义参考中华人民共和国《气象灾害预警信号发布与传播办法》与众多相关论文，结合数据制定了统计标准。例如，寒潮可以根据24小时内降温幅度分为一般、较强、强、特强四个等级。热浪、暴雨、热带气旋的定义也类似。系统默认显示北京市2000年至2023年各类极端天气发生频次的统计。",
        },
        {
          icon: "fa fa-search",
          title: "天气预测",
          description:
            "使用神经网络算法对天气指标进行预测，以指导未来天气情况并预警极端天气。页面展示了日均温、日最高温度、日最低温度、露点温度四种气象指标，使用每个城市2024年1月31日的气象数据指标作为训练集送入LSTM时序模型，使用剩余的气象数据作为测试集验证模型可信度，最终预测2024年3月气象指标。",
        },
      ],
    };
  },
  methods: {
    toggleNav() {
      document.body.classList.toggle("noscroll");
    },
    topFunction() {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    },
  },
};
</script>
  
  <style scoped>
/* Add your CSS styles here */
.maintitle {
  margin: 40px auto 40px auto;
  padding-top: 150px;
  text-align: center;
  font-family: "Microsoft YaHei";
  font-style: normal;
  font-weight: 650;
  font-size: 150px;
  letter-spacing: 1rem;
  line-height: 150px;
  background: linear-gradient(
    269.84deg,
    #9affeb -29.43%,
    #67e0ff 29.95%,
    #7cceff 69.54%,
    #5cb0e1 97.25%
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.icon-center {
  width: 80px; /* 根据需要调整图标大小 */
  height: 80px; /* 根据需要调整图标大小 */
}
#movetop {
  position: fixed;
  right: 20px;
  bottom: 20px;
  z-index: 999;
  width: 40px;
  height: 40px;
  background-color: #6eafe1;
  border: none;
  border-radius: 50%;
  font-size: 20px;
  text-align: center;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
  transition: background-color 0.3s ease;
}

#movetop:before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 12px;
  height: 12px;
  border-top: 2px solid #fff;
  border-left: 2px solid #fff;
  transform: translate(-50%, -20%) rotate(45deg);
}

#movetop:hover {
  background-color: #3599e5;
}
</style>
  