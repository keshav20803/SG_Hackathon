const mongoose = require('mongoose')

const connectionString = 'mongodb+srv://jainakshat447:node123@taskmanager.xrlpzeb.mongodb.net/?retryWrites=true&w=majority'

const connectDB = (url) =>{
    return mongoose
    .connect(url,{
        useNewUrlParser : true,
        useCreateIndex : true ,
        useFindAndModify : false ,
        useUnifiedTopology : true,
    })
    .then(()=>{
    console.log('Connected to the DB')
    })
    .catch((err)=>{
        console.log('ERROR')
    })
}

module.exports = connectDB
