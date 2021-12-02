const mongoose = require('mongoose');
const Predicted_stock_pricesSchema = new mongoose.Schema({
    Date:{
        type: String,
        required: true,
        unique: true
    },
    Predicted: {
        type: Number,
        required: true
    }
},{
    timestamps:true
})

const Predicted_stock_prices=mongoose.model('Predicted_stock_prices',Predicted_stock_pricesSchema)
Predicted_stock_prices.createIndexes({Date:1})
module.exports=Predicted_stock_prices;