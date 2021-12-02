const mongoose = require('mongoose');
const AccountSchema = new mongoose.Schema({
    account_type:{
        type:Number,
        required:true
    },
    name_of_account_holder:{
        type:String,
        required:true
    },
    name_of_organisation:{
        type:String
    },
    email:{
        type:String,
        required:true,
        unique:true
    }
},{
    timestamps:true
})

const Account=mongoose.model('Account',AccountSchema)
module.exports=Account;