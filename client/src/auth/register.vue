<template>
	<div>
		<div class="container-fluid p-0"> 
      <div class="row">
        <div class="col-12">     
          <div class="login-card">
            <div>
                <div>
                  <a class="logo">
                    <img
                      class="img-fluid for-light"
                      src="../assets/images/logo/login.png"
                      alt="looginpage"
                    />
                    <img
                      class="img-fluid for-dark"
                      src="../assets/images/logo/logo_dark.png"
                      alt="looginpage"
                    />
                  </a>
                </div>
              <div class="login-main login-form-card"> 
                  <h4>Create your account</h4>
                  <p>Enter your personal details to create account</p>
                  <div class="form-group">
                    <label class="col-form-label">Your Username</label>
                    <div class="form-row">
                        <input class="form-control" type="text" v-model="username" required="" placeholder="Username">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-form-label">Email Address</label>
                    <input class="form-control" type="email" v-model="email" required="" placeholder="Test@gmail.com">
                  </div>
                  <div class="form-group">
                    <label class="col-form-label">Password</label>
                    <input class="form-control" type="password" v-model="password1" required="" placeholder="*********">
                  </div>
                  <div class="form-group">
                    <label class="col-form-label">Confirm Password</label>
                    <input class="form-control" type="password" v-model="password2" required="" placeholder="*********">
                  </div>
                  <div class="form-group mb-0">
                    <div class="checkbox p-0">
                      <input id="checkbox1" type="checkbox">
                      <label class="text-muted" for="checkbox1">Agree with<a class="ml-2" href="#">Privacy Policy</a></label>
                    </div>
                    <button class="btn btn-primary btn-block" @click="Register" type="submit">Create Account</button>
                  </div>
                  <h6 class="text-muted mt-4 or">Or signup with</h6>
                  <div class="social mt-4">
                            <div class="btn-showcase">
                              <a class="btn btn-light" >
                                <i class="fa fa-google txt-linkedin"></i>
                                Google
                              </a>
                              <a
                                class="btn btn-light"
                              >
                                <feather
                                  type="twitter"
                                  class="txt-twitter"
                                ></feather
                                >twitter</a
                              >
                              <a
                                class="btn btn-light"
                              >
                                <feather
                                  type="facebook"
                                  class="txt-fb"
                                ></feather
                                >facebook</a
                              >
                            </div>
                          </div>
                      <p class="mt-4 mb-0">Already have an account?
                          <router-link class="ml-2" tag="a" to="/login" >
                            Login
                          </router-link>
                      </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
	</div>
</template>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      username: '',
      email: '',
      password1: '',
      password2: '',
    };
  },
  methods: {
    // regiter
    async Register(){
      await axios
        .post('http://127.0.0.1:8000/dj-rest-auth/registration/',
          {
            username: this.username,
            email: this.email,
            password1: this.password1,
            password2: this.password2
          })
        .then(() => {
          this.$router.push({name: 'login'});
          //this.$notify.success('Registration success');
        }) 
        .catch((error) => { 
          console.log('error message: ', error.response.data.password1);
          this.$notify.error(error.response.headers+' , try again ..');
        });		 
    }
  },
};
</script>