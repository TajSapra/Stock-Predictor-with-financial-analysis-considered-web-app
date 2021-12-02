const account_model=require("../models/account")
profile_page=async function(req, res){
    try{
        // if(req.cookies.secretkey){
        //     return res.render('Profile', {
        //         title:'Profile Page'
        //     })
        // }
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
            let oid="";
            for(var i=0;i<req.cookies.secretkey.length-1;i+=2){
                oid+=req.cookies.secretkey[i+1]+req.cookies.secretkey[i];
            }
            console.log(oid)
            var user= await account_model.findById(oid)
            return res.render('Profile', {
                title:'Profile Page',
                user:user
            })
        }
        else{
            return res.redirect('/auth')
        }

    }
    catch(err){
        console.log(err)
    }
}
module.exports={profile_page}