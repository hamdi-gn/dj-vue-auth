<template>
	<div>
		<div class="page-wrapper">
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
                    <h4>Reset Your Password</h4>
                    <div class="form-group">
                      <label class="col-form-label">Enter Your Email Address</label>
                      <div class="row">
                        <div class="col-md-12">
                          <input class="form-control mb-1" v-model="email" type="email">
                        </div>
                        <div class="col-12">
                          <button class="btn btn-primary btn-block m-t-10" @click="sentEmail">Send</button>
                        </div>
                      </div>
                    </div>
                    <div class="text-center mt-4 mb-4"><span class="reset-password-link"><a class="btn-link text-danger" @click="sentEmail" >Resend</a></span></div>
                    <div class="form-group">
                      <label class="col-form-label pt-0">Enter Informations</label>
                      <div class="form-row">
                        <div class="col-md-3 mb-3">
                            <b-form-input type="text"  v-model="uid" required placeholder="Uid"></b-form-input>
                        </div>
                        <div class="col-md-6 mb-3">
                            <b-form-input type="text" v-model="token" required placeholder="Key"></b-form-input>
                        </div>
                      </div>
                    </div>
                    <h6 class="mt-4">Create Your Password</h6>
                    <div class="form-group">
                      <label class="col-form-label">New Password</label>
                      <input class="form-control" type="password" v-model="new_password1" required="" placeholder="*********">
                      <div class="show-hide"><span class="show"></span></div>
                    </div>
                    <div class="form-group">
                      <label class="col-form-label">Retype Password</label>
                      <input class="form-control" type="password" v-model="new_password2" required="" placeholder="*********">
                    </div>
                    <div class="form-group mb-0">
                      <button class="btn btn-primary btn-block" @click="changePassword">Done</button>
                    </div>
                    <p class="mt-4 mb-0">Already have an password?
				            <router-link class="ml-2" tag="a" to="/login" >Login</router-link>  
                  </p>
                </div>
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
  data(){
    return{
      email: '',
      uid: '',
      token: '',
      new_password1: '',
      new_password2: ''
    };
  },
  methods: {
    async sentEmail(){
      await axios
        .post('http://127.0.0.1:8000/dj-rest-auth/password/reset/',
          {
            email: this.email
          },
        ).then(()=>{
          this.$notify.success('E-mail has been sent');
        })
        .catch(()=>{
          this.$notify.error('Error, try again ..');
        });
    },
    async changePassword(){
      await axios
        .post('http://127.0.0.1:8000/dj-rest-auth/password/reset/confirm/',
          {
            uid: this.uid,
            token: this.token,
            new_password1: this.new_password1,
            new_password2: this.new_password2
          },
        ).then(()=>{
          this.$notify.success('Password changed succesfully');
          this.$router.push({name:'login'});

        })
        .catch(()=>{
          this.$notify.error('Error, try again ..');
        });
    }
  }
};
</script>
