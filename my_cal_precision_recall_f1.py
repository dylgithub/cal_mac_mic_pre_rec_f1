#encoding=utf-8
from sklearn.metrics import classification_report,precision_score,recall_score
from collections import Counter,defaultdict
def cal_precision(true_list,predict_list):
    print("micro_precision",precision_score(true_list,predict_list,average='micro'))
    print("macro_precision",precision_score(true_list,predict_list,average='macro'))
def macro_recall(true_list,predict_list):
    set_label=set(true_list)
    #记录测试集种各个类别的总数目
    sum_count=Counter(true_list)
    num_set_of_label=len(set_label)
    #统计每一类别预测正确的数目
    num_true_dict=defaultdict(int)
    for i,label in enumerate(true_list):
        if predict_list[i]==label:
            num_true_dict[label]+=1
    temp_macro_recall=0.0
    for key in num_true_dict:
        temp_macro_recall+=(num_true_dict[key]/sum_count[key])
    macro_recall=temp_macro_recall/num_set_of_label
    print("my_macro_recall",macro_recall)
def macro_precision(true_list,predict_list):
    set_label = set(true_list)
    num_set_of_label = len(set_label)
    # 记录预测为各个类别的总数目
    sum_count=Counter(predict_list)
    num_true_dict = defaultdict(int)
    for i,label in enumerate(true_list):
        if predict_list[i]==label:
            num_true_dict[label]+=1
    temp_macro_precision = 0.0
    for key in num_true_dict:
        temp_macro_precision += (num_true_dict[key]/sum_count[key])
    macro_precision = temp_macro_precision / num_set_of_label
    print("my_macro_precision",macro_precision)
def micro_recall(true_list,predict_list):
    true_num=0
    for i,label in enumerate(true_list):
        if predict_list[i]==label:
            true_num+=1
    micro_recall=true_num/len(true_list)
    print("my_micro_recall",micro_recall)
def micro_precision(true_list,predict_list):
    true_num=0
    for i,label in enumerate(true_list):
        if predict_list[i]==label:
            true_num+=1
    micro_precision=true_num/len(true_list)
    print("my_micro_precision",micro_precision)
def cal_recall(true_list,predict_list):
    print("micro_recall",recall_score(true_list,predict_list,average='micro'))
    print("macro_recall",recall_score(true_list,predict_list,average='macro'))
if __name__ == '__main__':
    true_list=[1,1,1,1,2,2,2,3,3,3,3,3,4]
    predict_list=[1,3,1,3,2,1,3,2,3,3,2,1,3]
    cal_precision(true_list,predict_list)
    cal_recall(true_list, predict_list)
    macro_precision(true_list, predict_list)
    micro_precision(true_list, predict_list)
    macro_recall(true_list, predict_list)
    micro_recall(true_list, predict_list)