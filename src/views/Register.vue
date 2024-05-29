<template>
  <div class="login">
    <div class="login-wrap">
      <el-form class="login-container">
        <div class="title">用户注册</div>
        <el-form-item label="" size="medium">
          <el-input
            type="text"
            v-model="username"
            placeholder="注册账号"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="" size="medium">
          <el-input
            type="password"
            v-model="password"
            placeholder="请输入密码"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="" size="medium">
          <el-input
            type="password"
            v-model="confirmPassword"
            placeholder="请再次输入密码"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="" size="medium">
          <el-input
            type="number"
            v-model="age"
            placeholder="年龄"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="" size="medium">
          <el-input
            type="text"
            v-model="hobbies"
            placeholder="兴趣爱好"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="" size="medium">
          <el-input
            type="email"
            v-model="email"
            placeholder="电子邮箱"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="" size="medium">
          <el-input
            type="tel"
            v-model="phoneNumber"
            placeholder="手机号"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="" size="medium">
          <el-input
            type="text"
            v-model="address"
            placeholder="住址"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="" size="medium">
          <el-input
            type="text"
            v-model="signature"
            placeholder="签名"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="" size="medium">
          <el-button type="primary" style="width: 100%" @click="doSubmit()">
            提交
          </el-button>
        </el-form-item>
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
  margin: -80px auto 0;
  width: 350px;
  height: 550px;
  padding: 20px 35px 15px 35px;
  background: #fff;
  border: 1px solid #eaeaea;
  text-align: left;
  box-shadow: 0 0 20px 3px rgba(255, 252, 252, 0.5);
}

.title {
  margin: 5px auto 20px auto;
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
  margin-bottom: 10px; /* 调整表单项之间的垂直间距 */
}

.login-container .el-row {
  margin-top: -10px; /* 调整文本行的上边距 */
}

.login-container .el-button {
  margin-top: 10px; /* 调整提交按钮的上边距 */
}
</style>