const mongoose = require('mongoose');
const Stock_pricesSchema = new mongoose.Schema({
    Date:{
        type: String,
        required: true
    },
    close: {
        type: Number,
        required: true
    }
},{
    timestamps:true
})

const Stock_prices=mongoose.model('Stock_prices',Stock_pricesSchema)
module.exports=Stock_prices;