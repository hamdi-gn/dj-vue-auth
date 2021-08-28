<template>
    <div>
        <Breadcrumbs main="Users" title="Edit Profile"/>
        <!-- Container-fluid starts-->
        <div class="container-fluid">
            <div class="edit-profile">
              <div class="row">
                <div class="col-xl-4">
                  <div class="card">
                    <div class="card-header">
                      <h4 class="card-title mb-0">My Profile</h4>
                      <div class="card-options"><a class="card-options-collapse" href="#" data-toggle="card-collapse"><i class="fe fe-chevron-up"></i></a><a class="card-options-remove" href="#" data-toggle="card-remove"><i class="fe fe-x"></i></a></div>
                    </div>
                    <div class="card-body">
                        <div class="row mb-2">
                          <div class="col-auto"><img class="img-70 rounded-circle" alt="" src="../../assets/images/user/7.jpg"></div>
                          <div class="col">
                            <h3 class="mb-1"> {{userdata.first_name}} </h3>
                            <p class="mb-4">{{userdata.last_name}}</p>
                          </div>
                        </div>
                        <div class="form-group">
                          <label class="form-label">Old Password</label>
                          <input class="form-control" type="password" value="password" v-model="userdata.password">
                        </div>
                        <div class="form-group">
                          <label class="form-label">New Password</label>
                          <input class="form-control" type="password" value="password" v-model="userdata.password1">
                        </div>
                        <div class="form-group">
                          <label class="form-label">Confirm New Password</label>
                          <input class="form-control" type="password" value="password" v-model="userdata.password2">
                        </div>
                        <div class="form-footer">
                          <button class="btn btn-primary btn-block">Change Password</button>
                        </div>
                    </div>
                  </div>
                </div>
                <div class="col-xl-8">
                  <div class="card">
                    <div class="card-header">
                      <h4 class="card-title mb-0">Edit Profile</h4>
                      <div class="card-options"><a class="card-options-collapse" href="#" data-toggle="card-collapse"><i class="fe fe-chevron-up"></i></a><a class="card-options-remove" href="#" data-toggle="card-remove"><i class="fe fe-x"></i></a></div>
                    </div>
                    <div class="card-body">
                      <div class="row">
                        <div class="col-sm-6 col-md-6">
                          <div class="form-group">
                            <label class="form-label">First Name</label>
                            <input class="form-control" type="text" placeholder="Last Name" v-model="userdata.first_name">
                          </div>
                        </div>
                        <div class="col-sm-6 col-md-6">
                          <div class="form-group">
                            <label class="form-label">Last Name</label>
                            <input class="form-control" type="text" placeholder="Last Name" v-model="userdata.last_name">
                          </div>
                        </div>
                        <div class="col-md-5">
                          <div class="form-group">
                            <label class="form-label">Phone Number</label>
                            <input class="form-control" type="number" placeholder="Phone Number" v-model="userdata.phone">
                          </div>
                        </div>
                        <div class="col-sm-6 col-md-3">
                          <div class="form-group">
                            <label class="form-label">Username</label>
                            <input class="form-control" type="text" v-model="userdata.username">
                          </div>
                        </div>
                        <div class="col-sm-6 col-md-4">
                          <div class="form-group">
                            <label class="form-label">Email address</label>
                            <input class="form-control" type="email" v-model="userdata.email">
                          </div>
                        </div>
                        <div class="col-md-8">
                          <div class="form-group">
                            <label class="form-label">Address</label>
                            <input class="form-control" type="text" placeholder="Home Address" v-model="userdata.address">
                          </div>
                        </div>
                        <div class="col-sm-6 col-md-4">
                          <div class="form-group">
                            <label class="form-label">Birthday</label>
                            <input class="form-control" type="date"  v-model="userdata.birthday">
                          </div>
                        </div>
                        <div class="col-sm-6 col-md-4">
                          <div class="form-group">
                            <label class="form-label">City</label>
                            <input class="form-control" type="text" placeholder="City" v-model="userdata.city">
                          </div>
                        </div>
                        <div class="col-sm-6 col-md-3">
                          <div class="form-group">
                            <label class="form-label">Postal Code</label>
                            <input class="form-control" type="number" placeholder="ZIP Code" v-model="userdata.postal_code">
                          </div>
                        </div>
                          <div class="mb-2">
                            <div class="col-form-label">Country</div>
                            <multiselect class="form-control" v-model="userdata.country" :options="countries" label="name" :searchable="false" :close-on-select="true" :show-labels="false" placeholder="Pick a value"></multiselect>
                        </div>
                        <div class="col-md-12">
                          <div class="form-group mb-0">
                            <label class="form-label">About Me</label>
                            <textarea class="form-control" rows="5" placeholder="Enter About your description" v-model="userdata.about"></textarea>
                          </div>
                        </div>
                        <div class="col-md-12">
                            <label class="mt-4 form-label">Facebook URL</label>
                            <div class="form-group mb-0">
                                <b-form-input type="url" placeholder="https://facebook.com" v-model="userdata.facebook_link"></b-form-input>
                            </div>
                        </div>
                        <div class="col-md-12">
                            <label class="mt-4 form-label">Twitter URL</label>
                            <div class="form-group mb-0">
                                <b-form-input type="url" placeholder="https://twitter.com" v-model="userdata.twitter_link"></b-form-input>
                            </div>
                        </div>
                        <div class="col-md-12">
                            <label class="mt-4 form-label">Instagram URL</label>
                            <div class="form-group mb-0">
                                <b-form-input type="url" placeholder="https://instagram.com" v-model="userdata.instagram_link"></b-form-input>
                            </div>
                        </div>
                        <div class="col-md-12">
                            <label class="mt-4 form-label">LinkedIn URL</label>
                            <div class="form-group mb-0">
                                <b-form-input type="url" placeholder="https://linkedin.com" v-model="userdata.linkedin_link"></b-form-input>
                            </div>
                        </div>
                      </div>
                    </div>
                    <div class="card-footer text-right">
                      <button class="btn btn-primary" @click="updateUser">Update Profile</button>
                    </div>
                  </div>
                </div> 
              </div>
            </div>
          </div>
        <!-- Container-fluid Ends-->
    </div>
</template>

<script>
import Multiselect from 'vue-multiselect';
import axios from 'axios';

export default {
  components: {
    Multiselect
  },
  data() {
    return {
      userdata: [],
      countries: []
    };
  },
  methods: {
    async getUser(){
      await axios
        .get('/dj-rest-auth/user/',
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
    },
    async getCountries(){
      await axios
        .get('https://restcountries.eu/rest/v2/all',
          {
            headers:{
              'Content-Type': 'application/json',
            }
          })
        .then((response) => {
          this.countries = response.data;
        }) 
        .catch(() => { 
          this.$notify.error('Cannot get countries, try again ..');
        });		 
    },
    async updateUser(){
      await axios
        .put('/dj-rest-auth/user/',
          {
            profile_image: this.userdata.profile_image,
            cover_image: this.userdata.cover_image,
            first_name: this.userdata.first_name,
            last_name: this.userdata.last_name,
            username: this.userdata.username,
            birthday: this.userdata.birthday,
            email: this.userdata.email,
            about: this.userdata.about,
            address: this.userdata.address,
            phone: this.userdata.phone,
            skills: this.userdata.skills,
            facebook_link: this.userdata.facebook_link,
            twitter_link: this.userdata.twitter_link,
            instagram_link: this.userdata.instagram_link,
            linkedin_link: this.userdata.linkedin_link
          },
          {
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            }
          })
        .then(() => {
          this.$notify.success('Profile updated successfully ');
        }) 
        .catch(() => { 
          this.$notify.error('Error, try again ..');
        });	
    }
  },
  mounted(){
    this.getUser();
    this.getCountries();
  }
};
</script>