<template>
<div>
  <div class="row backgroundColor">
    <div class="whiteText col-12">
      <a href="#" id="logOut" class="boldText whiteText">LOGOUT</a>
      <p class="boldText text-center">BIENVENIDO {{ name }}</p>
    </div>
  </div>
  <div class="row backgroundColor">
    <div class="btn margin mBottom divSize textColor btnNavigationBorder whiteBackground hover col-xs-12 col-md-4 boldText" v-on:click="new_requirement" :class="{activeButton: requirementSection}">
      <p class="textoNegrita text-center mt-1">NUEVO REQUERIMIENTO</p>
    </div>
    <div class="btn margin mBottom divSize textColor btnNavigationBorder whiteBackground hover col-xs-12 col-md-4 boldText" v-on:click="new_error" :class="{activeButton: errorSection}">
      <p class="textoNegrita text-center mt-1">INFORMAR ERROR</p>
    </div>
    <div class="btn margin mBottom divSize textColor btnNavigationBorder whiteBackground hover col-xs-12 col-md-4 boldText" v-on:click="requisition" :class="{activeButton: userRequisition}">
      <p class="textoNegrita text-center mt-1">MIS PEDIDOS</p>
    </div>
  </div>
  <div class="row" v-if="requirementSection">
    <form1></form1>
  </div>
  <requisition v-if="userRequisition"></requisition>
</div>
</template>
<script>
import form1 from './Form.vue';
import requisition from './Requisition.vue';
import axios from 'axios';
export default {
  components: {
    form1,
    requisition
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/users/' + sessionStorage.getItem('idUser'), {
        //  params: {
        //   id: sessionStorage.getItem('idUser')
        // },
        headers: {
          'Authorization': 'JWT' + sessionStorage.getItem('idToken')
        }
      })
      .then((response) => {
        this.name = response.data.username;
      })
      .catch((error) => {
        console.log("No salio");
      });
  },
  methods: {
    new_requirement: function() {
      this.requirementSection = !this.requirementSection;
      this.errorSection = false;
      this.userRequisition = false;
    },
    new_error: function() {
      this.errorSection = !this.errorSection;
      this.requirementSection = false;
      this.userRequisition = false;
    },
    requisition: function() {
      this.userRequisition = !this.userRequisition;
      this.errorSection = false;
      this.requirementSection = false;
    }
  },
  data() {
    return {
      name: null,
      requirementSection: false,
      errorSection: false,
      userRequisition: true,

    }
  }
}
</script>
<style>
.activeButton {
  background: #2699FB;
  color: #FFFFFF;
  border: 1px solid #FFFFFF;
}

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
