const revscor=require('../models/review_score')
const predstoc=require('../models/predicted_prices')
const stockprices=require('../models/stock_prices')
const reviewsmodel=require('../models/reviews')
const account_model=require('../models/account')
everything=async function(req,res){
    if(req.user){
        var user_email=req.user.email
        var found=await account_model.findOne({email:user_email})
        let secretkey2=found.id
        let secretkey=""
        for(var i=0;i<secretkey2.length;i+=2){
            secretkey+=secretkey2[i+1]+secretkey2[i];
        }
        res.cookie('method', 1)
        res.cookie('secretkey', secretkey)   
    }
    if(req.cookies.secretkey){
        var predsp=await predstoc.find({}).sort({_id:-1}).limit(1)
        var time=await stockprices.find({}).sort({_id:1}).limit(1)
        var revs=await revscor.find({}).sort({_id:-1}).limit(1)
        console.log(revs[0])
        return res.render('everything', {
            title:'All predicted Info Page',
            time:time[0].Date,
            ps:predsp,
            rs:revs            
        })
    }
    else{
        return res.redirect('/auth')
    }
}
prices=async function(req,res){
    if(req.user){
        var user_email=req.user.email
        var found=await account_model.findOne({email:user_email})
        let secretkey2=found.id
        let secretkey=""
        for(var i=0;i<secretkey2.length;i+=2){
            secretkey+=secretkey2[i+1]+secretkey2[i];
        }
        res.cookie('method', 1)
        res.cookie('secretkey', secretkey)   
    }
    if(req.cookies.secretkey){
        var time=await stockprices.find({}).sort({_id:1}).limit(1)
        var predsp=await predstoc.find({}).sort({_id:-1}).limit(1)
        var previous=await stockprices.find({}).sort({_id:-1}).limit(59)
        console.log(predsp)
        return res.render('prices', {
            title:'All predicted Info Page',
            ps:predsp,
            psd:predsp[0].Date,
            time:time[0].Date,
            previous:previous            
        })
    }
    else{
        return res.redirect('/auth')
    }
}
reviews=async function(req,res){
    if(req.user){
        var user_email=req.user.email
        var found=await account_model.findOne({email:user_email})
        let secretkey2=found.id
        let secretkey=""
        for(var i=0;i<secretkey2.length;i+=2){
            secretkey+=secretkey2[i+1]+secretkey2[i];
        }
        res.cookie('method', 1)
        res.cookie('secretkey', secretkey)   
    }
    if(req.cookies.secretkey){
        var revscore=await revscor.find({}).sort({_id:-1}).limit(1)
        var previous=await reviewsmodel.find({})
        return res.render('review', {
            title:'All predicted Info Page',
            reviews:previous,
            rs:revscore           
        })
    }
    else{
        return res.redirect('/auth')
    }
}
module.exports={everything,prices,reviews}