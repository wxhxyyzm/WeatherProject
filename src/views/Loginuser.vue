<template>
  <div class="login">
    <div class="login-wrap">
      <el-form class="login-container">
        <div class="title">用户登录</div>
        <el-form-item label="" size="medium">
          <el-input
            type="text"
            v-model="username"
            placeholder="登录账号"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="" size="medium">
          <el-input
            type="password"
            v-model="password"
            placeholder="登录密码"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="" size="medium">
          <el-button type="primary" style="width: 100%" @click="doSubmit()"
            >提交</el-button
          >
        </el-form-item>
        <el-row style="text-align: center; margin-top: -10px">
          <el-link type="primary" @click="showContactAdminDialog"
            >忘记密码</el-link
          >&nbsp;

          <el-link type="primary" @click="gotoRegister()">用户注册</el-link>
        </el-row>
      </el-form>
    </div>
  </div>
</template>
   
  <script>
export default {
  methods: {
    doSubmit() {
      this.$router.push("/p2");
    },
    gotoRegister() {
      this.$router.push("/register");
    },
    showContactAdminDialog() {
      this.$confirm("请联系管理员处理忘记密码问题", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          // 用户点击确定按钮时的处理逻辑
          // 这里可以添加相应的操作，比如发送请求或跳转页面
        })
        .catch(() => {
          // 用户点击取消按钮时的处理逻辑
          // 可以不做任何处理，或者添加相应的提示信息
        });
    },
  },
  name: "Login",
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
      username: "",
      password: "",
    };
  },
};
</script>
   
  <style scoped>
.login {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url("../assets/p1bg.svg");
  background-size: 100% auto;
  overflow: hidden;
}
.login-wrap {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  padding: 10%;
  background-repeat: no-repeat;
  background-position: center right;
  background-size: 100%;
}
.login-container {
  border-radius: 10px;
  margin: 0px auto;
  width: 350px;
  height: 300px;
  padding: 30px 35px 15px 35px;
  background: #fff;
  border: 1px solid #eaeaea;
  text-align: left;
  box-shadow: 0 0 20px 3px rgba(255, 252, 252, 0.5);
}

.title {
  margin: 0px auto 40px auto;
  text-align: center;
  font-family: "Microsoft YaHei";
  font-style: normal;
  font-weight: 700;
  font-size: 35px;
  line-height: 50px;
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
.login-container .el-form-item {
  margin-bottom: 20px; /* 调整表单项之间的垂直间距 */
}

.login-container .el-row {
  margin-top: -10px; /* 调整文本行的上边距 */
}

.login-container .el-button {
  margin-top: 10px; /* 调整提交按钮的上边距 */
}
</style>