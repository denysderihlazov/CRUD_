<template>
    <div class="container">
        <div class="">
            <input type="text" v-model="title" class="card__input form-control mt-2" placeholder="Title">
            <input type="text" v-model="body" class="card__input form-control mt-2" placeholder="Content">
            <button @click="postBlog()" class="save_button"><i class="fa fa-save"></i> Save</button>
        </div>
        <h1 v-show="getWeekDay" class="text-white">{{welcomeText}}</h1>
        <div class="">
            <table class="table">
                <thead>
                <th>Time</th>
                <th>Title</th>
                <th>Body</th>
                <th>Edit</th>
                <th>Delete</th>
                </thead>
                <tbody>
                <tr v-for="blog in blogs" v-bind:key="blog.url">
                    <td>{{blog.time}}</td>
                    <td>{{blog.title}}</td>
                    <td class="td_line">{{blog.body}}</td>
                    <td>
                        <button @click="getOne(blog)" class="secondary_button"><i class="fa fa-edit"></i></button>
                    </td>
                    <td>
                        <button @click="deleteOne(blog.url)" class="secondary_button"><i class="fa fa-trash"></i></button>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Container',
    props: {
    },
    //Here we created all variables
    data(){
        return{
            blogs:null,
            url:'',
            title:'',
            body:'',
            time:'',
            welcomeText:''
        }
    },
    mounted() {
        this.getAll()
        this.getWeekDay()
    },
    methods:{
        //This void is for getting all data from our Django DB
        getAll(){
            axios.get('http://localhost:8000/blogs/')
                .then(response=>{
                    this.blogs=response.data;
                    this.title='';
                    this.body='';
                    this.url='';
                    this.time='';
                })
        },
        //This void is for editing by click on edit-button
        getOne(blog){
            this.url = blog.url;
            this.title = blog.title;
            this.body = blog.body;
        },
        //This void is for deleting by click on delete-button
        deleteOne(url){
            axios.delete(url, {auth:{
                    username:'denys',
                    password:'130299dddd'
                }})
                //getAll helps us make our app more dynamic (by reload data after changes)
                .then(()=>{
                    this.getAll();
                })
        },
        postBlog(){
            //if the url doesn't exist => create it
            if (this.url == ''){
                axios.post('http://localhost:8000/blogs/',
                    {title:this.title,body:this.body},
                    {auth:{username: 'denys', password: '130299dddd'}}
                )
                    .then(()=>{
                        this.getAll();
                    })
            }else { //if the address exists => edit it and SAVE by save-button
                axios.put(this.url,
                    {title:this.title,body:this.body},
                    {auth:{username: 'denys', password: '130299dddd'}}
                )
                    //getAll helps us make our app more dynamic (by reload data after changes)
                    .then(()=>{
                        this.getAll();
                    })
            }
        },
        getWeekDay(){
            let weekday = new Array(7)
            weekday[0] = "Sunday 🖖"
            weekday[1] = "Monday 💪😀"
            weekday[2] = "Tuesday 😜"
            weekday[3] = "Wednesday 😌☕"
            weekday[4] = "Thursday 🤗"
            weekday[5] = "Friday 🍻"
            weekday[6] = "Saturday 😴"

            let randomWordArray = Array(
                "Oh my, it's ",
                "Whoop, it's ",
                "Happy ",
                "Seems it's ",
                "Awesome, it's ",
                "Have a nice ",
                "Happy fabulous ",
                "Enjoy your "
            );

            var randomWord = randomWordArray[Math.floor(Math.random() * randomWordArray.length)];


            const cuttentDayIndex = new Date().getDay()
            this.welcomeText = randomWord + weekday[cuttentDayIndex]
        }
    }
}
</script>

<style scoped>
.container {
    background: linear-gradient(
        to bottom right,
        rgba(255, 255, 255, 0.2),
        rgba(255, 255, 255, 0.05)
    );
    border: 3.5px solid white;
    backdrop-filter: blur(0.7rem);
    padding: 1.5rem;
    border-radius: 1rem;
    max-width: 1200px;
}

.card__input {
    background: none;
    border: none;
    border-bottom: 0.2rem solid rgba(255, 255, 255, 0.15);
    font-size: 1.5rem;
    color: #fff;
    text-shadow: 0 2px 2px rgba(0, 0, 0, 0.3);
}

.card__input::placeholder {
    color: rgba(255, 255, 255, 0.5);
    text-shadow: none;
}

.card__input:focus {
    outline: none;
    border-color: rgba(255, 255, 255, 0.6);
}

.save_button{
    background: none;
    border: none;
    border: 0.2rem solid rgba(255, 255, 255, 0.3);
    border-radius: 10px;
    font-size: 1.5rem;
    color: #fff;
    text-shadow: 0 2px 2px rgba(0, 0, 0, 0.3);
    margin-top: 1rem;
    padding: 10px;

}

.secondary_button{
    background: none;
    border: none;
    border: 0.2rem solid rgba(255, 255, 255, 0.3);
    border-radius: 10px;
    font-size: 1.5rem;
    color: #fff;
    text-shadow: 0 2px 2px rgba(0, 0, 0, 0.3);
    padding: 6px;
}

td { word-wrap:break-word; }
</style>
