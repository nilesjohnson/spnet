
from dbconn import DBConnection
from core import Paper, Person, EmailAddress, Issue, IssueVote, SIG, GplusPersonData, Post, Reply, ArxivPaperData, PubmedPaperData, DoiPaperData, PaperInterest, GplusSubscriptions, Subscription, TopicOptions, Citation
import json
from pymongo.errors import ConnectionFailure

connectDict = {
    Paper:'spnet.paper',
    Person:'spnet.person',
    EmailAddress:'spnet.person',
    Issue:'spnet.issue',
    IssueVote:'spnet.issue',
    SIG:'spnet.sig',
    GplusPersonData:'spnet.person',
    GplusSubscriptions:'spnet.gplus_subs',
    Post:'spnet.paper',
    Reply:'spnet.paper',
    Citation:'spnet.paper',
    ArxivPaperData:'spnet.paper',
    PubmedPaperData:'spnet.paper',
    DoiPaperData:'spnet.paper',
    PaperInterest:'spnet.paper',
    Subscription:'spnet.person',
    TopicOptions:'spnet.person',
    }



def init_connection(spnetUrlBase='https://selectedpapers.net', 
                    dbconfFile='../mongodb/access.json', **kwargs):
    'set klass.coll on each db class to give it db connection'
    try:
        with open(dbconfFile) as ifile:
            dbconfig = json.load(ifile)
        kwargs.update(dbconfig)
        print 'read db connection settings from', dbconfFile
    except IOError:
        pass
    try:
        dbconn = DBConnection(connectDict, **kwargs)
    except ConnectionFailure:
        print '''ERROR: database connection failed with settings: %s
If you are running a test / development platform, 
make sure that your mongod is running
and accepting connections (from localhost, without a password).''' % str(kwargs)
        raise
    for klass in connectDict: # set default URL
        klass._spnet_url_base = spnetUrlBase
    return dbconn
    
