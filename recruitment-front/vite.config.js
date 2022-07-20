import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  define: {
    'process.env': {
      VUE_APP_BASE_API: '/api'
    }
  },
  server:{
    host: '0.0.0.0',
    port: 3000,
    open: true,
    proxy:{
      '/api':{
        target: 'http://121.4.176.100:8000',
        changeOrigin:true,
        // rewrite:(path) => path.replace(/^\/api/, '')
      }
    }
  }
})
