<template>
    <div>
        <Breadcrumbs main="Users" title="User Profile"/>
        <!-- Container-fluid starts-->
        <div class="container-fluid">
            <div class="user-profile">
              <div class="row">
                <!-- user profile first-style start-->
                <div class="col-sm-12">
                  <div class="card hovercard text-center">
                    <div class="cardheader"></div>
                    <div class="user-image">
                      <div class="avatar"><img alt="" :src="`${'../../../../server/images/profile_images/',userdata.profile_image}`"></div>
                    </div>
                    <div class="info">
                      <div class="row">
                        <div class="col-sm-6 col-lg-4 order-sm-1 order-xl-0">
                          <div class="row">
                            <div class="col-md-6">
                              <div class="ttl-info text-left">
                                <h6><i class="fa fa-envelope mr-2"></i>Email</h6><span>{{userdata.email}}</span>
                              </div>
                            </div>
                            <div class="col-md-6">
                              <div class="ttl-info text-left">
                                <h6><i class="fa fa-calendar mr-2"></i>BOD</h6><span>{{userdata.birthday}}</span>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="col-sm-12 col-lg-4 order-sm-0 order-xl-1">
                          <div class="user-designation">
                            <div class="title"><a target="_blank" href=""> {{userdata.first_name}} {{userdata.last_name}}  </a></div>
                            <div class="desc mt-2"> {{userdata.profession}} </div>
                          </div>
                        </div>
                        <div class="col-sm-6 col-lg-4 order-sm-2 order-xl-2">
                          <div class="row">
                            <div class="col-md-6">
                              <div class="ttl-info text-left">
                                <h6><i class="fa fa-phone mr-2"></i>Contact Us</h6><span> {{userdata.phone}} </span>
                              </div>
                            </div>
                            <div class="col-md-6">
                              <div class="ttl-info text-left">
                                <h6><i class="fa fa-location-arrow mr-2"></i>Location</h6><span>{{userdata.address}}</span>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <hr>
                      <div class="social-media">
                        <ul class="list-inline">
                          <li class="list-inline-item"><a  target="_blank" v-bind:href="`${userdata.facebook_link}`"><i class="fa fa-facebook"></i></a></li>
                          <li class="list-inline-item"><a  target="_blank" v-bind:href="`${userdata.twitter_link}`"><i class="fa fa-twitter"></i></a></li>
                          <li class="list-inline-item"><a  target="_blank" v-bind:href="`${userdata.instagram_link}`"><i class="fa fa-instagram"></i></a></li>
                          <li class="list-inline-item"><a  target="_blank" v-bind:href="`${userdata.linkedin_link}`"><i class="fa fa-linkedin"></i></a></li>
                        </ul>
                      </div>
                      <div class="follow">
                        <div class="row">
                          <div class="col-6 text-md-right border-right">
                            <div class="follow-num counter">25869</div><span>Follower</span>
                          </div>
                          <div class="col-6 text-md-left">
                            <div class="follow-num counter">659887</div><span>Following</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- user profile first-style end-->
              </div>
            </div>
          </div>
        <!-- Container-fluid Ends-->
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userdata: [],
    };
  },
  methods: {
    async getUser(){
      await axios
        .get('https://dj-vue-js.herokuapp.com/dj-rest-auth/user/',
          {
            headers:{
              'Content-Type': 'application/json',
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            }
          })
        .then((response) => {
          this.userdata = response.data;
        }) 
        .catch(() => { 
          this.$notify.error('Error, try again ..');
        });		 
    }
  },
  mounted(){
    this.getUser();
  }
};
</script>