<template>
  <div class="container">
    <!-- <router-view></router-view> -->
    <techCard></techCard>
  </div>
</template>

<script>
import techCard from './components/RequisitionSolution.vue'
export default {
  components: {techCard},
  data() {
    return {
    }
  }
}
</script>

<style>
.backgroundColor {
  background-color: #2699FB;
}

.whiteText {
  color: #FFFFFF;

}

.hover:hover {
  background-color: #2699FB;
  color: #FFFFFF;
  border: 1px solid #FFFFFF;
  transition: background-color 0.5s, color 0.5s, border 0.5s;
}

.boldText {
  font-weight: bold;
}

.btnNavigationBorder {
  border: 1px solid #2699FB;
}

.whiteBackground {
  background-color: #FFFFFF;
}

.textColor {
  color: #2699FB;
}

#logOut {
  padding-left: 10px;
}
</style>
