<template>
<div>
  <div class="row backgroundColor">
    <div class="whiteText col-12">
      <a href="#" id="logOut" class="boldText whiteText" v-on:click="logOut">LOGOUT</a>
      <p class="boldText text-center">BIENVENIDO {{ name }}</p>
    </div>
  </div>
  <b-navbar toggleable="md" class="row backgroundColor">
    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
    <b-collapse is-nav id="nav_collapse">
      <b-navbar-nav>
        <b-nav-item class="btn margin mBottom divSize textColor btnNavigationBorder whiteBackground hover col-xs-12 col-md-6 boldText whiteText textoNegrita text-center mt-1" v-on:click="new_requirement" :class="{activeButton: requirementSection}">NUEVO
          PEDIDO</b-nav-item>
        <b-nav-item class="btn margin mBottom divSize textColor btnNavigationBorder whiteBackground hover col-xs-12 col-md-6 boldText textoNegrita text-center mt-1" v-on:click="requisition" :class="{activeButton: userRequisition}">MIS PEDIDOS</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  <div class="row" v-if="requirementSection">
    <formRequisition></formRequisition>
  </div>
  <userCard v-if="userRequisition"></userCard>
  <!-- <div class="row" v-if="formEdit"> -->
  <!-- <formEditRequisition></formEditRequisition> -->
  <!-- </div> -->
</div>
</template>
<script>
import formRequisition from './Form.vue';
import formEditRequisition from './FormEdit.vue';
import userCard from './UserCard.vue';
import axios from 'axios';
import EventBus from '../bus/eventBus.js';
export default {
  components: {
    formRequisition,
    userCard,
    // formEditRequisition
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
    requisition: function() {
      this.userRequisition = !this.userRequisition;
      this.errorSection = false;
      this.requirementSection = false;
    },
    logOut: function() {
      // axios.get('http://127.0.0.1:8000/rest-auth/logout/');
      sessionStorage.clear();
      this.$router.push('/');
    }
  },
  created() {
    EventBus.$on('change_section', () => {
      this.requirementSection = false;
      this.userRequisition = true;
    });
    // EventBus.$on('change_module', () => {
    //   this.userRequisition = false;
    // });

  },
  beforeDestroy() {
    // // EventBus.$off('change_section');
    // EventBus.$off('view_edit_form');

  },
  data() {
    return {
      name: null,
      requirementSection: false,
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

.navbar-light .navbar-nav .nav-link {
  color: inherit;
}



@media (min-width:768px) {
  .navbar-nav {
    margin: 0 auto;
  }

  .navbar-nav li {
    padding-left: 30px;
    padding-right: 60px;
  }
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
