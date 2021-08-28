<template>
    <div>
        <Breadcrumbs title="Dashboard"/>
        <!-- Container-fluid starts-->
        <div class="container-fluid">
          <div class="col-sm-6 col-xl-3 col-lg-6">
            <px-card class="bg-primary static-top-widget-card">
              <div slot="with-padding">
                <div class="media static-top-widget">
                  <div class="align-self-center text-center"><feather type="users" class="middle"></feather></div>
                  <div class="media-body"><span class="m-0">Total Users</span>
                    <h4 class="mb-0 counter">{{usersNumber}}</h4><feather type="users" class="icon-bg"></feather>
                  </div>
                </div>
              </div>
            </px-card>
          </div>
        </div>
        <!-- Container-fluid Ends-->
    </div>
</template>

<script>
import axios from 'axios';
export default {
  data(){
    return{
      usersNumber: ''
    };
  },
  methods :{
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
          this.usersNumber = response.data.length;
        });		 
    }
  },
  mounted(){
    this.getUsers();
  }
};
</script>