const FabricCAServices = require{'fabric-ca-client'} //fabric sdk
const {Wallets,Gateway} = require{'fabric-network'}

const fs = require('fs')
const path = require('path')

async function main(){
    // Org1 Connection Profile
    const ccpPAth = path.resolve('-----path of connection-org1.json-------')
    const ccp = JSON.parse(fs.readFileSync(cppPAth,'utf8'))
    //console.log(ccp)

    // ORG1 Ca
    const caInfo = ccp.certificateAuthorities['-----name ca---']
    const caTLSCACerts = caInfo.tlsCACerts.pem
    //console.log(caTLSCACerts)
    const ca = new FabricCAServices(caInfo.url,{trustedROOT: caTLSCACerts,verify:false},caInfo.caName)


    //--------------------

    // create Wallet

    const walletPAth = path.join(process.cwd(),'wallet')
    const wallet = await Wallets.newFileSystemWallet(walletPath)
    console.log('Wallet Path:${walletPath}')

    //Get admin identity

    var adminIdentity = await wallet.get('admin')
    const enrollment = await ca.enroll({enrollmentID:'admin',enrollmentSecret:'adminpw'});
    
    const x509Identity ={
        Credentials:{
            certificate: enrollment.certificate,
            privateKey:enrollment.key.toBytes(),
        },
        mspId:'Org1MSP',
        type:'X.509',
    };
    await wallet.put("admin",x509Identity)
    console.log("Admin enrolled and saved into wallet successfully")
    adminIdentity = await wallet.get('admin')


    //Register user for this app

    var userIdentity = await wallet.get("appUser")

    if(userIdentity){
        console.log("User identity exists in wallet...")
    }else{
        const provider = wallet.getProviderRegistry().getProvider(adminIdentity.type);
        const adminUser = await provider.getUserContext(adminIdentity, 'admin');
        
        const secret = await ca.register({
            affiliation: 'org1.department',
            enrollmentID: 'appUser',
            role:'client'            
        },adminUser);
        
        const enrollment = await ca.enroll({
            enrollmentID:'appUser',
            enrollmentSecret: secrect,
        });
        
        const x509Identity ={
            Credentials:{
                certificate: enrollment.certificate,
                privateKey:enrollment.key.toBytes(),
            },
            mspId:'Org1MSP',
            type:'X.509',
        };
    }






}
    

main()


//watch video 25:00