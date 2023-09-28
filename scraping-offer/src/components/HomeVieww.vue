<template>
  <div class="big-content w-screen h-screen bg-[#3a647c] overflow-auto flex flex-col space-y-3">
    <div class="flex space-x-4 justify-start px-5 pt-3">
      <div v-for="btn, index in upBtn" :key="index" :class="['w-12 h-12 hover:bg-[#9cb1bd] cursor-pointer rounded-xl flex justify-center items-center active:bg-slate-200', mode === btn.name ? 'bg-[#9cb1bd]' : 'bg-[#618396]']" @click="useMode(btn.name)" :title="btn.name">
        <i :class="[`mdi ${btn.icon} text-2xl font-medium`]"></i>
      </div>
      <div class="w-12 h-12"><i class="mdi mdi-knob text-red-400 text-5xl"></i></div>
    </div>
    <div class="flex-1 flex flex-col space-y-7 justify-center px-16">
      <div v-if="mode === 'link'" class="flex space-x-3">
        <input type="text" class="h-16 w-full text-3xl p-3 rounded-lg shadow-md focus:outline-none" v-model="url">
        <select v-model="limit" class="appearance-none px-5 bg-white rounded-lg shadow-md" title="Limite d'extraction">
          <option value="10">10</option>
          <option value="20">20</option>
          <option value="30">30</option>
          <option value="40">40</option>
          <option value="50">50</option>
        </select>
      </div>
      <div v-else>
        <input type="file" name="" id="">
      </div>
      <button :class="['uppercase text-2xl mx-auto py-3 w-72 rounded-xl shadow-2xl text-white', {'hover:bg-[#618396] active:scale-[95%] transition-all ease-in-out duration-300': url !== '', 'bg-gray-300 cursor-not-allowed': url === ''}]" :disabled="url === ''" @click="submit">Valider</button>
    </div>
  </div>
</template>

<script setup>
  import { ref, inject, watch } from 'vue';
  import { useNotyf } from '../composables/useNotyf';
  import { useNetwork } from '@vueuse/core'
  const axios = inject('axios')
  const url = ref('')
  const limit = ref('10')
  const mode = ref('link')
  const upBtn = ref([
    {icon: 'mdi-link', name: 'link'},
    {icon: 'mdi-file-document', name: 'file'}
  ])

  const notyf = useNotyf()

  const { isOnline } = useNetwork()

  function useMode(value) {
    mode.value = value
  }

  watch(isOnline, (newValue)=> {
    console.log(newValue)
    if (newValue === true) {
      notyf.trigger('Appareil connecté à Internet', 'success', {duration: 10000})
    } else {
      notyf.trigger(`Pas de connexion`, 'error', {duration: 10000})
    }
  })

  async function submit() {
    console.log(`URL for scraping is : ${url.value} and limit of extraction : ${limit.value}`)
    const data = {
      urlSent : url.value,
      limit: limit.value
    }
    try {
      const resp = (await axios.post('/scrap-web/url', JSON.stringify(data))).data.Response
      console.log(`Response of request : ` + resp)
      if (resp.extraction === true) {
        notyf.trigger('Extraction effectuée avec succès', 'success')
      }
    } catch (error) {
      console.log(`Error : ${error}`)
      notyf.trigger('Extraction non réussie', 'error', {duration:5000})
    }
  }
</script>