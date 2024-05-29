<template>
  <div class="container">
    <div class="root-page-container">
      <navbar />
      <div class="t-main-page t-account-center">
        <div class="t-layout">
          <!--顶部头像栏-->
          <div class="t-container t-account-center-header">
            <div class="t-avatar t-account-center-header__avatar t-avatar__xxl">
              <img
                src="https://img-static.mihoyo.com/communityweb/upload/c9d11674eac7631d2210a1ba20799958.png"
                class="t-avatar__img"
              />
            </div>
            <div class="t-account-center-user">
              <div class="t-account-center-user__header">
                <div class="t-account-center-user__title">
                  <span class="t-account-center-user__name">wxh</span>
                </div>
                <div class="t-account-center-header__buttons">
                  <div
                    class="t-button t-account-center-header__edit t-button-outlined t-button-md"
                  >
                    <!-- <button class="t-button__button" @click="updateMyInfo">
                      编辑
                    </button> -->
                  </div>
                  <!---->
                </div>
              </div>
              <div class="t-account-center-user__intro">
                <p>
                  <i
                    class="el-icon-tickets"
                    style="
                      color: #ad4e69;
                      margin-top: 50px;
                      margin-right: 10px;
                      font-size: 18px;
                    "
                  ></i
                  >系统原装签名，送给每一位小可爱~
                </p>
              </div>
              <!-- <div class="t-account-center-user__intro">
                <p>
                  <i
                    class="el-icon-location-information"
                    style="color: #00c3ff; margin-right: 10px; font-size: 18px"
                  ></i
                  >IP属地：广东
                </p>
              </div> -->
            </div>
          </div>
        </div>
      </div>
      <div class="t-main-page t-account-center">
        <div class="t-layout" style="width=2000px;">
          <!--顶部头像栏-->
          <div class="t-container t-account-center-header">
            <el-descriptions
              title="个人详细信息"
              direction="vertical"
              :column="3"
              border
              class="t-account-center-descriptions"
            >
              <el-descriptions-item label="年龄">21</el-descriptions-item>
              <el-descriptions-item label="兴趣爱好"
                >唱跳rap蓝桥</el-descriptions-item
              >
              <el-descriptions-item label="电子邮箱"
                >111@qq.com</el-descriptions-item
              >
              <el-descriptions-item label="手机号">
                18100000000
              </el-descriptions-item>
              <el-descriptions-item label="联系地址"
                >江苏省苏州市吴中区吴中大道 1188 号</el-descriptions-item
              >
            </el-descriptions>
          </div>
        </div>
      </div>

      <div class="t-main-page t-account-center" style="margin-top: 40px">
        <div class="t-layout" style="width=2000px">
          <!--顶部头像栏-->
          <div class="t-container t-account-center-header">
            <el-table :data="tableData" style="width: 100%">
              <el-table-column prop="date" label="序号" width="180">
              </el-table-column>
              <el-table-column prop="pic" label="图片" width="280">
                <template v-slot="scope">
                  <img
                    :src="scope.row.pic"
                    alt="图片"
                    style="width: 200px; height: 200px; object-fit: cover"
                  />
                </template>
              </el-table-column>
              <el-table-column label="描述">
                <template v-slot="scope">
                  <el-row :gutter="20">
                    <el-col :span="18">
                      <el-input
                        v-model="scope.row.discription"
                        placeholder="请输入描述"
                      ></el-input>
                    </el-col>
                    <el-col :span="6">
                      <el-button type="primary" @click="submit(scope.row)"
                        >确认</el-button
                      >
                    </el-col>
                  </el-row>
                </template>
              </el-table-column>
            </el-table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from "@/components/navbar.vue";
// console.log("Submitted discription:", row.discription);
// var disp[];
export default {
  components: { navbar },
  data() {
    return {
      tableData: [
        {
          date: "2016-05-02",
          pic: "https://wxhxyyzm.github.io/images/pic.jpg",
          discription: "", //这边应该是服务器读入的一个数据 可能需要写一个列表 因为不同str是不一样的
        },
        {
          date: "2016-05-02",
          pic: "https://wxhxyyzm.github.io/images/pic.jpg",
          discription: "",
        },
      ],
    };
  },
  mounted() {},
  methods: {
    submit(row) {
      console.log("Submitted discription:", row.discription);
      // 这边应该是把改的数据读入服务器
    },
  },
};
</script>

<style scoped>
.container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url("../assets/p4bg.svg") no-repeat center center fixed;
  background-size: cover;
  overflow: auto; /* 允许内容滚动 */
}
.t-main-page {
  padding-top: 30px;
  position: relative;
  height: 200px;
}
.t-layout {
  width: 1000px;
  margin: 0 auto;
  padding-left: 100px;
  padding-right: 100px;
  -webkit-box-sizing: content-box;
  box-sizing: content-box;
}
.t-layout {
  zoom: 1;
}
.t-account-center-header {
  padding: 20px 50px 24px 20px;
  display: flex;
  justify-content: center; /* Center the el-descriptions component */
  margin-bottom: 20px;
}

.t-account-center-descriptions {
  width: 100%; /* Set the width to fill the available space */
}

.t-account-center-descriptions .el-descriptions-item {
  flex-basis: 25%; /* Set the initial width of each item */
  margin-bottom: 20px;
}
.t-container {
  background-color: #fff;
  border-radius: 4px;
}
.t-account-center-header__avatar {
  margin-right: 24px;
  -ms-flex-negative: 0;
  flex-shrink: 0;
}
.t-avatar__xxl {
  width: 120px;
  height: 120px;
}
.t-avatar {
  display: inline-block;
  position: relative;
}
.t-avatar__img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  border: 1px solid #ebebeb;
  vertical-align: top;
}
.t-avatar__img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  border: 1px solid #ebebeb;
  vertical-align: top;
}
img {
  border-style: none;
}
.t-account-center-user {
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  height: 100%;
}
.t-account-center-user__header {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
.t-account-center-user__title {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}
.t-account-center-user__name {
  font-size: 16px;
  line-height: 21px;
  font-weight: 600;
}
.t-account-center-user__level.t-img-icon {
  margin-left: 10px;
  height: 16px;
  -ms-flex-negative: 0;
  flex-shrink: 0;
}
.t-account-center-user__level--self {
  cursor: pointer;
}
.t-img-icon {
  height: 1em;
  fill: currentColor;
  overflow: hidden;
}
.t-account-center-header__buttons {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}
.t-button.t-button-md.t-button-outlined {
  line-height: 32px;
}
.t-button.t-button-md {
  width: 86px;
  height: 34px;
  line-height: 34px;
}
.t-button {
  display: inline-block;
  cursor: pointer;
  -ms-flex-negative: 0;
  flex-shrink: 0;
}
.t-button-outlined .t-button__button {
  background-color: #fff;
  color: #00b2ff;
  border: 1px solid #00c3ff;
  border-radius: 4px;
  -webkit-transition-duration: 0.2s;
  -o-transition-duration: 0.2s;
  transition-duration: 0.2s;
  -webkit-transition-property: border-color, color;
  -o-transition-property: border-color, color;
  transition-property: border-color, color;
}
.t-button__button {
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  cursor: pointer;
  outline: none;
  font-size: inherit;
  color: inherit;
  width: 100%;
  height: 100%;
  background-color: transparent;
  border: none;
  border-radius: 0;
  font-weight: inherit;
  line-height: inherit;
}
input,
button,
textarea {
  color: inherit;
  font: inherit;
}
.t-account-center-user__audit {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}
.t-account-center-user__uid {
  font-size: 12px;
  color: #ccc;
}
a {
  text-decoration: none;
}
.t-account-center-user__certification,
.t-account-center-user__intro {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  margin-top: 12px;
  color: #666;
  line-height: 18px;
}
.t-account-center-user__certification span,
.t-account-center-user__intro span {
  margin-top: 2px;
  -ms-flex-negative: 0;
  flex-shrink: 0;
  line-height: 1;
}
p {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  outline: none;
}
.t-account-center-user__certification,
.t-account-center-user__intro {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  margin-top: 12px;
  color: #666;
  line-height: 18px;
}
.t-account-center-user__certification .ip-icon,
.t-account-center-user__intro .ip-icon {
  color: #76bfe3;
  font-size: 16px;
  margin-right: 8px;
}
.t-icon {
  font-size: inherit;
}
.iconfont {
  font-family: "iconfont" !important;
  font-size: 16px;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.icon-ip:before {
  content: "";
}
.t-account-center-header__data {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  padding-top: 19px;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-item-align: center;
  align-self: center;
  -ms-flex-negative: 0;
  flex-shrink: 0;
  margin-top: 20px;
  border-top: 1px solid #f0f0f0;
}
.t-account-center-header__data-item {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  padding-right: 40px;
}
.t-account-center-header__data-link {
  cursor: pointer;
}
.t-account-center-header__data-num {
  color: #333;
  font-size: 20px;
}
.t-account-center-header__data-label {
  margin-left: 10px;
  color: #ccc;
}
.t-account-center-header__data-item {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  padding-right: 40px;
}
.t-account-center-header__data-link {
  cursor: pointer;
}
.t-account-center-header__data-num {
  color: #333;
  font-size: 20px;
}
.t-account-center-header__data-label {
  margin-left: 10px;
  color: #ccc;
}
.t-account-center-header__data-item {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  padding-right: 40px;
}
.t-account-center-header__data-num {
  color: #333;
  font-size: 20px;
}
.t-account-center-header__data-label {
  margin-left: 10px;
  color: #ccc;
}
</style>