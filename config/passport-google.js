const tokeninput=require('../tokens/tokens');
const loginmailer=require('../mails/login')
const passport=require('passport')
const google=require('passport-google-oauth').OAuth2Strategy;
const crypto=require('crypto')
const passwords_model=require('../models/Passwords')
const account_model=require('../models/account')
passport.use(new google({
    clientID:tokeninput.passgooclientID,
    clientSecret:tokeninput.passgoogclientSecret,
    callbackURL:"http://localhost:3000/login/outh/google/callback"
},function(access, refresh, profile, done){
    account_model.findOne({email:profile.emails[0].value}).exec(function(err,found){   
        if(err){
            console.log(err)
            return;
        }
        if(found){
            loginmailer.login(found)
            return done(null,found)
        }
        else{
            account_model.create({
                account_type:1,
                name_of_account_holder:profile.displayName,
                email:profile.emails[0].value,
            },async function(err,found){
                if(err){
                    console.log(err)
                    return;
                }
                var found2=await passwords_model.create({
                    account_id:found.id,
                    pass:crypto.randomBytes(20).toString('hex')
                })
                return done(null,found);
            })
        }
    })
}
))
passport.serializeUser(function(user, done) {
    done(null, user.id);
  });
  
  passport.deserializeUser(function(id, done) {
    account_model.findById(id, function(err, user) {
      return done(err, user);
    });
  });
module.exports=passport