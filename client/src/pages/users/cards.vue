<template>
  <div>
    <Breadcrumbs main="Users" title="User Cards"/>
    <!-- Container-fluid starts-->
    <div class="container-fluid">
      <div class="row user-cards" >
        <div class="col-md-6 col-lg-6 col-xl-4" v-for="user in users" :key="user.id">
          <div class="card custom-card">
            <div class="card-header"><img class="img-fluid" src="../../assets/images/user-card/1.jpg" alt=""></div>
            <div class="card-profile"><img class="rounded-circle" :src="`${'../../../../server/images/profile_images/',user.profile_image}`" alt=""></div>
            <ul class="card-social">
              <li><a v-bind:href="`${user.first_name}`"><i class="fa fa-facebook"></i></a></li>
              <li><a href="#"><i class="fa fa-google-plus"></i></a></li>
              <li><a href="#"><i class="fa fa-twitter"></i></a></li>
              <li><a href="#"><i class="fa fa-instagram"></i></a></li>
              <li><a href="#"><i class="fa fa-rss"></i></a></li>
            </ul>
            <div class="text-center profile-details"> 
              <h4> {{user.first_name}} {{user.last_name}} </h4>
              <h6> {{user.profession}} </h6>
            </div>
          </div>
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
      users: [],
    };
  },
  methods: {
    async getUsers(){
      await axios
        .get('http://localhost:8080/users/',
          {
            headers:{
              'Content-Type': 'application/json',
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            }
          })
        .then((response) => {
          this.users = response.data;
        }) 
        .catch(() => { 
          this.$notify.error('Error, try again ..');
        });		 
    }
  },
  mounted(){
    this.getUsers();
  }
};
</script>