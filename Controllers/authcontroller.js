const bcrypt=require("bcrypt")
const account_model=require("../models/account")
const passwords_model=require("../models/Passwords")
const saltRounds=10
options=async function(req,res){
    try{
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
        if(req.cookies.method==undefined){
            res.cookie("method", 0)
        }
        console.log(req.cookies)
        if(req.cookies.method==0){
            return res.render('options',{
                title:'Options',
            })
        }
        else{ 
            return res.redirect('/profile')
        }
    }
    catch(err){
        console.log(err);
    }
}
createnewaccount=async function(req,res){
    try{
        if(req.body.pass1!=req.body.pass2){
            return res.redirect('back')
        }
        foundaccount=await account_model.findOne({email:req.body.email})
        if(!foundaccount){
            var created;
            if(req.body.account_type==1){
                created=await account_model.create({
                    account_type:req.body.account_type,
                    name_of_account_holder:name_of_account_holder,
                    email:req.body.email
                })    
            }
            else{
                
                created=await account_model.create({
                    account_type:req.body.account_type,
                    name_of_account_holder:name_of_account_holder,
                    email:req.body.email,
                    name_of_organisation:req.body.name_of_organisation
                })    
            }
            bcrypt.hash(req.body.pass1, saltRounds,async function(err, hash) {
                var created2=await passwords_model.create({
                    account_id:created.id,
                    pass: hash
                })
            });
            
            return res.redirect('/auth/login')
        }
        else{
            return res.redirect('/auth/login')
        }
    }
    catch(err){
        console.log(err);
    }
}
checkaccount=async function(req, res){
    try{
        var foundaccount=await account_model.findOne({email:req.body.email})
        if(foundaccount){
            var found2=await passwords_model.findOne({account_id:foundaccount.id})
            bcrypt.compare(req.body.password, found2.pass, function(err, result) {
                if(result){
                    res.cookie('method', foundaccount.account_type)  
                    let secretkey=foundaccount.id
                    for(var i=0;i<secretkey.length-1;i+=2){
                        let temp
                        temp=secretkey[i]
                        secretkey[i]=secretkey[i+1]
                        secretkey[i+1]=temp
                    }
                    res.cookie('secretkey', secretkey)       
                    return res.redirect('/profile')       
                }
                else{
                    return res.redirect('back')
                }
            });
        }
        else{
            return res.redirect('back')
        }
    }
    catch(err){
        console.log(err)
    }
}
logout=async function(req, res){
    if(req.cookies.secretkey){
        res.clearCookie('method')
        res.clearCookie('secretkey')
        req.session.destroy()    
    }
    return res.redirect('/')
}
module.exports={options,createnewaccount,checkaccount, logout}