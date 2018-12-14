from __future__ import division
import string
import math

tokenize = lambda doc: doc.lower().split(" ")
document_0 = "tab pages places click section firefox second arrow item appear button bar search visible focus set implement doesn't printing small"
document_1 = "ios date column based elements trying : group rest format variable model string read sort specific range value argument bash"
 
document_2 = "button element template size returning docker creating id layout db scala parsing unique css xml container long automatically webpack combine"
document_3 ="doesn't work cannot statement vba activity entity framework memory invalid case 2015 matlab permission dependency submit use outside error times"
document_4 = "unable request post join results http pandas reading aws works condition location displaying instead listview local sending stream modal using" 
document_5 = "filter function click passing undefined cell pass adding video fields reference upload node.js compare exception option collection method always word"
document_6 = "message show spark directory mvc print client asp.net pdf push page folder properly created back load hide classes information installing"
document_7 = "select bootstrap issue install count regex link convert facebook match expression graph getting powershell expected pattern fragment recyclerview hibernate part"
document_8 = "change null background values color mongodb git connection remote binding functions action event plot dictionary log fetch calculate even bind"
document_9 = "laravel loop node found index property website selected could dropdown able thread writing static existing limit rendering single apply vector"
document_10 = "array insert map error: import result value email send replace first can't returns type call instance arrays form console boot"
document_11 = "module response key tables dataframe chrome two download box order typescript need errors binary include file different setup internal know"
document_12 = "angular2 nested react list login item content add items menu wrong loading images grid merge put resource start contains full"
document_13 = "android line showing child csv remove empty authentication command app numbers display copy device file names configure saving generated detect"
document_14 = "angular spring script package ionic parse delete test run strings fails python xamarin sum testing lines jenkins network file? called"
document_15 = " r view controller return save azure parent selenium external position extract space npm want records task label shell cordova frame"
document_16 = " json firebase object div inside component django failed variables dynamically header xcode parameter updating codeigniter height document correctly screen accessing"
document_17 = "angularjs wordpress bar chart syntax execute split url mobile requests changing characters options won't large iframe storage navigation implementation interface"
document_18 = "js columns input rows row table issues auto animation domain don't defined gradle multiple performance program write one events values"
document_19 = "studio output query visual error 10 missing stop character sql route token configuration tab left end trouble types compile linq"
document_20 = "swift google api working excel validation connect attribute last tag core retrieve duplicate setting ui notification sqlite play matrix maps"
 
 

all_documents = [document_0, document_1, document_2, document_3, document_4, document_5, document_6, document_7, document_8, document_9, document_10 ,document_11, document_12, document_13, document_14, document_15, document_16, document_17, document_18, document_19, document_20]

tokenized_documents = [tokenize(d) for d in all_documents] # tokenized docs
all_tokens_set = set([item for sublist in tokenized_documents for item in sublist])

def jaccard_similarity(query, document):
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection)/len(union)

 
print jaccard_similarity(tokenized_documents[0],tokenized_documents[1])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[2])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[3])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[4])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[5])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[6])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[7])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[8])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[9])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[10])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[11])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[12])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[13])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[14])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[15])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[16])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[17])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[18])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[19])
print jaccard_similarity(tokenized_documents[0],tokenized_documents[20])


