# Created by Sangameswaran R S #
from urllib.request import urlopen

#check clickjacking Security
def check_clickjack(websiteURL):
    print('-----------Checking for clickjacking vulnerablities in '+str(websiteURL)+' -----------')
    overallFlag = False
    try:
        data = urlopen(websiteURL)
        if 'X-Frame-Options' in data.info():
            print('  [+] Website secured in IE, Mozilla and Other Older Browsers')
            if 'Content-Security-Policy' in data.info():
                print('  [+] Website Secured in Chrome, Safari and Other mordern Browsers that allow CSP Headers')
                overallFlag=True
            else:
                print('  [-] Website Insecure in Chrome, Safari and Other mordern Browsers')
        else:
            print('  [-] Website Insecure to IE, Mozilla, Chrome,Safari-Not Checked')
    
        if overallFlag == True:
            print('-------------------- [OK] Webpage safe towards clickjack attacks--------------------------')
        else:
            print('-------------------- [ERR] Webpage Vulnerable towards clickjack attacks----------------------')
    except Exception as e:
        print('------------------ [FATAL]-----------------')
        print(e)
        print('--------------------------------------------')
    return overallFlag

# Entrypoint
def entry():
    print('------Check Security of a webpage--------')
    websiteURL = input('Enter Webpage URL:  ')
    check_clickjack(websiteURL)
    looper = input('Check for another webpage? [y/n] ')
    if looper == 'y':
        entry()
    else:
        pass

#Entrypoint call
entry()
