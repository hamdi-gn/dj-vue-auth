<template>
  <div>
    <!-- page-wrapper Start-->
    <div class="container-fluid p-0">
      <div class="row m-0">
        <div class="col-12 p-0">
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
              <div class="login-main">
                <b-card no-body>
                  <b-tabs pills vertical>
                      <b-card-text>
                        <form class="theme-form">
                          <h4>Sign in to account</h4>
                          <p>Enter your email & password to login</p>
                          <div class="form-group">
                            <label class="col-form-label">Email Address</label>
                            <input
                              v-model="email"
                              class="form-control"
                              type="email"
                              required=""
                              placeholder="Test@gmail.com"
                              :class="{
                                'is-invalid': !email,
                              }"
                            />
                            <div
                              v-show=" !email"
                              class="invalid-feedback"
                            >
                              Email is required
                            </div>
                          </div>
    
                          <div class="form-group">
                            <label class="col-form-label">Password</label>
                            <input
                              v-model="password"
                              autocomplete=""
                              class="form-control"
                              type="password"
                              required=""
                              placeholder="*********"
                              :class="{
                                'is-invalid':  !email,
                              }"
                            />
                            <div
                              v-show=" !password"
                              class="invalid-feedback"
                            >
                              Email is required
                            </div>
                          </div>
                          <div class="form-group mb-0">
                            <p  class="mt-3 mb-2">
                              <router-link class="md-2" tag="a" to="/resetpassword" >
                              Forgot password
                            </router-link>
                            </p>
                            <button
                              class="btn btn-primary btn-block"
                              type="button"
                              @click="Login"
                            >
                              Login
                            </button>
                          </div>
                          <h6 class="text-muted mt-4 or">Or Sign in with</h6>
                          <div class="social mt-4">
                            <div class="btn-showcase">
                              <a class="btn btn-light">
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
                          <p class="mt-4 mb-0">
                            Don't have account?
                            <router-link class="ml-2" tag="a" to="/register" >
                            Create Account
                          </router-link>
                          </p>
                        </form>
                      </b-card-text>
                  </b-tabs>
                </b-card>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- latest jquery-->
  </div>
</template>

<script>

import axios from 'axios';

export default {

  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    // login
    async Login(){
      await axios
        .post('http://127.0.0.1:8000/dj-rest-auth/login/',
          {
            username: this.email,
            password: this.password
          })
        .then((response) => {
          localStorage.setItem('access_token', response.data.key);
          this.$router.push('/dashboard');
          this.$notify.success('Login success');
        }) 
        .catch((error) => { 
          if (error.response.status == 400) {
            this.$notify.error('Incorrect username or password');
          } else {
            this.$notify.error('Login error, try again ..');
          }
          
        });		 
    }
  },
  mounted(){ 
    if (localStorage.getItem('access_token') !== null) {
      this.$router.push({ path: '/dashboard' });
      this.$notify.warning(' Your\'re already logged in!');

    } else {
      //
    }
  }
};
</script>