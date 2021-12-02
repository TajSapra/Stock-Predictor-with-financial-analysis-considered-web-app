home=async function(req,res){
    if(req.cookies.method==undefined){
        res.cookie("method", 0)
    }
    return res.render('../views/Home.ejs', {
        title: 'Home'
    })
}
module.exports={home}