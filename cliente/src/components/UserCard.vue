<template>
<div>
  <div class="row" v-if="requisitionSection">
    <div v-for="(requi , index) in requisition" :key="index" class="col-md-12 col-lg-6 " v-if="requisition">
      <div class="card card-block backgroundColor text-center boldText marginCard">
        <div class="card-body">
          <h3 class="card-title whiteText">{{ requi.type}}</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor">{{ requi.subject }}</p>
          </div>
          <h3 class="card-title whiteText">Prioridad</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor" :class="{high: requi.priority == 'Alta', medium: requi.priority == 'Media',
              low: requi.priority == 'Baja'}">{{ requi.priority }}</p>
          </div>
          <h3 class="card-title whiteText">Fecha</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor">{{ requi.date }}</p>
          </div>
          <h3 class="card-title whiteText">Estado</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor">{{ requi.status }}</p>
          </div>
          <button type="button" class="boldText marginButton btn btn-light textColor" v-on:click="editRequisition(requi.id)">EDITAR</button>
          <button type="button" class="boldText marginButton btn btn-danger" v-on:click="deletRequisition(requi.id, index)">ELIMINAR</button>
        </div>
      </div>
    </div>
    <div class="textColor" id="dontExistRequisition" v-if="requisition.length == 0">
      <h1>NO HAY PEDIDOS</h1>
    </div>
  </div>
  <div class="col-12 preload ">
    <moon-loader :loading="loading" :color="color" :size="size"></moon-loader>
  </div>
  <formEdit></formEdit>
</div>
</template>
<script>
import axios from 'axios'
import EventBus from '../bus/eventBus.js'
import formEdit from './FormEdit'
import MoonLoader from 'vue-spinner/src/MoonLoader.vue'
export default {
  components: {
    formEdit,
    MoonLoader
  },
  props: {
    color: {
      type: String,
      default: '#2699FB'
    },
    size: {
      type: String,
      default: '150px'
    }
  },
  data() {
    return {
      requisition: null,
      requisitionSection: true,
      loading: false
    }
  },
  mounted() {
    this.loading = true
    this.load_user_requisitions()
    EventBus.$on('change_section', () => {
      this.requisitionSection = true
    })
  },
  methods: {
    load_user_requisitions() {
      //Devuelve todos los pedidos del usuario
      axios.get('http://127.0.0.1:8000/requisitions/mine/' + sessionStorage.getItem('idUser'))
        .then((response) => {
          this.requisition = response.data
          this.loading = false
        })
        .catch((error) => {
          console.log(error);
        });
    },
    deletRequisition(id, index) {
      this.$swal({
        title: '¿Estas seguro que quieres cancelar este pedido?',
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#2699FB',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, estoy seguro',
        cancelButtonText: 'Volver'
      }).then((result) => {
        if (result.value) {
          this.$swal(
            'Pedido Eliminado',
            this.requisition.splice(index, 1),
            axios.delete('http://127.0.0.1:8000/requisitions/delete/' + id),
          )
        }
      })
    },
    editRequisition(id) {
      var self = this;
      this.requisition.forEach(function(requi) {
        if (requi.id == id) {
          EventBus.$emit('edit_form', requi)
          self.requisitionSection = false;
        }
      })
    },
  }
}
</script>
<style>
.border {
  border-radius: 5px;
}

.marginButton {
  margin-top: 15px;
  margin-right: 25px;
  margin-left: 25px;
  width: 140px;
}

.marginCard {
  margin-top: 10px;
}

#dontExistRequisition {
  margin-top: 20px;
  margin: 0 auto;
}

.high {
  background-color: rgb(255, 0, 0);
  color: white;
  border: 1px solid rgb(255, 0, 0);
  border-radius: 5px;
}

.medium {
  background-color: rgb(255, 255, 0);
  color: black;
  border: 1px solid rgb(255, 255, 0);
  border-radius: 5px;
}

.low {
  background-color: rgb(0, 255, 0);
  color: white;
  border: 1px solid rgb(0, 255, 0);
  border-radius: 5px;
}
</style>
