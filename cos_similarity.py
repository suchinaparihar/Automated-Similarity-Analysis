
 
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt') # if necessary...


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')




text0 = "firefox twice appearance using update loading, improve tab tabs multiple broken new checks search bookmarks browsing window query create area"
text1 = "ios date column based elements trying : group rest format variable model string read sort specific range value argument bash"
text2 = "button element template size returning docker creating id layout db scala parsing unique css xml container long automatically webpack combine"
text3 ="doesn't work cannot statement vba activity entity framework memory invalid case 2015 matlab permission dependency submit use outside error times"
text4= "unable request post join results http pandas reading aws works condition location displaying instead listview local sending stream modal using" 
text5 = "filter function click passing undefined cell pass adding video fields reference upload node.js compare exception option collection method always word"
text6 = "message show spark directory mvc print client asp.net pdf push page folder properly created back load hide classes information installing"
text7 = "select bootstrap issue install count regex link convert facebook match expression graph getting powershell expected pattern fragment recyclerview hibernate part"
text8 = "change null background values color mongodb git connection remote binding functions action event plot dictionary log fetch calculate even bind"
text9 = "laravel loop node found index property website selected could dropdown able thread writing static existing limit rendering single apply vector"
text10 = "array insert map error: import result value email send replace first can't returns type call instance arrays form console boot"
text11 = "module response key tables dataframe chrome two download box order typescript need errors binary include file different setup internal know"
text12 = "angular2 nested react list login item content add items menu wrong loading images grid merge put resource start contains full"
text13 = "android line showing child csv remove empty authentication command app numbers display copy device file names configure saving generated detect"
text14 = "angular spring script package ionic parse delete test run strings fails python xamarin sum testing lines jenkins network file? called"
text15 = " r view controller return save azure parent selenium external position extract space npm want records task label shell cordova frame"
text16 = " json firebase object div inside component django failed variables dynamically header xcode parameter updating codeigniter height document correctly screen accessing"
text17 = "angularjs wordpress bar chart syntax execute split url mobile requests changing characters options won't large iframe storage navigation implementation interface"
text18 = "js columns input rows row table issues auto animation domain don't defined gradle multiple performance program write one events values"
text19 = "studio output query visual error 10 missing stop character sql route token configuration tab left end trouble types compile linq"
text20 = "swift google api working excel validation connect attribute last tag core retrieve duplicate setting ui notification sqlite play matrix maps"
 

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

print cosine_sim(text0, text1)
print cosine_sim(text0, text2)
print cosine_sim(text0, text3)
print cosine_sim(text0, text4)
print cosine_sim(text0, text5)
print cosine_sim(text0, text6)
print cosine_sim(text0, text7)
print cosine_sim(text0, text8)
print cosine_sim(text0, text9)
print cosine_sim(text0, text10)
print cosine_sim(text0, text11)
print cosine_sim(text0, text12)
print cosine_sim(text0, text13)
print cosine_sim(text0, text14)
print cosine_sim(text0, text15)
print cosine_sim(text0, text16)
print cosine_sim(text0, text17)
print cosine_sim(text0, text18)
print cosine_sim(text0, text19)
print cosine_sim(text0, text20)

