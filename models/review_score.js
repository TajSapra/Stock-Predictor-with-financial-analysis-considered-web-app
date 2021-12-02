const mongoose = require('mongoose');
const Review_scoresSchema = new mongoose.Schema({
    Company:{
        type: String,
        required: true,
    },
    Current: {
        type: Number,
        required: true
    }
},{
    timestamps:true
})

const Review_scores=mongoose.model('Review_scores',Review_scoresSchema)
module.exports=Review_scores;