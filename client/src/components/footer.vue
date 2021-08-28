<template>
  <div>
    <footer class="footer">
          <div class="container-fluid">
            <div class="row">
              <div class="col-md-12 footer-copyright text-center">
                <p class="mb-0">Copyright {{ new Date().getFullYear() }} © Hamdi GUENICHI </p>
              </div>
            </div>
          </div>
        </footer>
  </div>
</template>

<script>
import json from '../data/menu';
export default {
  name: 'footerpage',
  data(){
    return{
      data:'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(json)),
    };
  },
};
</script>
