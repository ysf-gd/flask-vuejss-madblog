<--模板部分-->
<template>
    <div class='container'>
        <button type='button' class='btn btn-primary'>{{ msg }}</button>
    </div>
</template>

<--脚本部分-->
<script>
    import axios from 'axios' 
    export default {
        name:'Ping',
        data(){
            return{
                msg:'' 
            }
        },
    methods:{
        getMessage(){
            const path = 'http://localhost:5000/api/ping'
            axios.get(path) 
                .then((res) => {
                    this.msg = res.data;
                })
                .catch((error) => {
                    //eslint-disable-next-line
                    console.error(error);
                })
        }
    },
    created() {
        //组件实例创建完成后触发，此时可以访问data、methods等
        this.getMessage()
    }
}
</script>