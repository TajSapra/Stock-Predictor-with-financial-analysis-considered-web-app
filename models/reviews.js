const mongoose = require('mongoose');
const ReviewsSchema = new mongoose.Schema({
    Review:{
        type: String,
        required: true,
    },
    Type: {
        type: Number,
        required: true
    }
},{
    timestamps:true
})

const Reviews=mongoose.model('Reviews',ReviewsSchema)
module.exports=Reviews;