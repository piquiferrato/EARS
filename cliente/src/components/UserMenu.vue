<template>
<div>
  <div class="row backgroundColor">
    <div class="whiteText col-12">
      <a href="#" id="logOut" class="boldText whiteText">LOGOUT</a>
      <p class="boldText text-center">BIENVENIDO "usuario"</p>
    </div>
  </div>
  <div class="row backgroundColor">
    <div class="btn margin mBottom divSize textColor btnNavigationBorder whiteBackground hover col-xs-12 col-md-4" v-on:click="new_requirement">
      <p class="textoNegrita text-center mt-1">NUEVO REQUERIMIENTO</p>
    </div>
    <div class="btn margin mBottom divSize textColor btnNavigationBorder whiteBackground hover col-xs-12 col-md-4">
      <p class="textoNegrita text-center mt-1">INFORMAR ERROR</p>
    </div>
    <div class="btn margin mBottom divSize textColor btnNavigationBorder whiteBackground hover col-xs-12 col-md-4">
      <p class="textoNegrita text-center mt-1">MIS PEDIDOS</p>
    </div>
  </div>
  <div class="row" v-if="requirementSection">
    <form1></form1>
  </div>
</div>
</template>
<script>
import form1 from './Form.vue';
import axios from 'axios';
export default {
  components: {
    form1
  },
  mounted(){
      axios.get('http://127.0.0.1:8000/users', {
        headers: {'Authorization': 'JWT' + sessionStorage.getItem('idToken')},
        // params: {
        //   id: this.id,
        // }
      })
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.log("No salio");
      });
  },
  methods: {
  new_requirement: function(){
    this.requirementSection = !this.requirementSection;
    this.serrorSection = false;
    this.userRequisition = false;
  },
  new_error: function(){
    this.errorSection = !this.errorSection;
    this.requirementSection = false;
    this.userRequisition = false;
  },
  requisition: function(){
    this.userRequisition = !this.userRequisition;
    this.errorSection = false;
    this.requirementSection = false;
  }
},
  data() {
    return {
      requirementSection: false,
      errorSection: false,
      userRequisition: false
    }
  }
}
</script>
<style>
@media (max-width:768px) {
  .margin {
    margin-top: 40px;
    border-radius: 5px;
  }

  .mBottom {
    margin-bottom: 20px;
  }

  .divSize {
    max-width: 70%;
    margin-left: 15%;
    max-height: 60px;
    font-size: 1.3em;
  }
}
</style>
