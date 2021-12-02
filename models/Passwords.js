const mongoose = require('mongoose');
const PasswordsSchema = new mongoose.Schema({
    account_id:{
        type: String,
        required: true,
        unique: true
    },
    pass: {
        type: String,
        required: true
    },
},{
    timestamps:true
})

const Passwords=mongoose.model('Passwords',PasswordsSchema)
Passwords.createIndexes({account_id:1})
module.exports=Passwords;