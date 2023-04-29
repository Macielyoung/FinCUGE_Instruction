'''
Author: Macielyoung
Date: 2023-04-26
'''
import json
import random
import pandas as pd


def process_finfe(finfe_path):
    '''
    description: 处理论坛情绪分析FinFE数据集
    return: finfe_lines(List)
    '''
    instruction_list = ["识别以下句子的情感。",
                        "判断以下句子的情感属性。",
                        "以下句子包含哪种情感极性。",
                        "分析以下句子的情感。",
                        "请分析这段文本的情感是积极、消极还是中性的。",
                        "这段文字表达的情感是什么。",
                        "请对这段文本的情感进行分析并给出评价。",
                        "这个文本的情感倾向是积极、消极还是中性的。",
                        "请评估以下内容的整体情感倾向，包含积极、消极和中性。"
                        "分析以下内容的情感偏向。"]
    output_list = ["{}。",
                   "该文本情感是{}的。",
                   "以上文本情感极性属于{}。",
                   "情感倾向是{}。",
                   "所属情感是{}。"]
    label_dict = {0: "消极", 1: "中性", 2: "积极"}
    with open(finfe_path, 'r') as f:
        finfe_list = json.load(f)
    
    finfe_lines = []
    for finfe_pair in finfe_list:
        instruction = random.choice(instruction_list)
        text, label = finfe_pair
        label = label_dict[label]
        output = random.choice(output_list)
        output = output.format(label)
        item = {'task': 'FINFE',
                'desc': '论坛情绪分析任务',
                'instruction': instruction,
                'input': text,
                'output': output}
        finfe_lines.append(item)
    return finfe_lines


def process_finqa(finqa_path):
    '''
    description: 处理事件抽取FinQA数据集
    return: finqa_lines(List)
    '''
    output_list = ['以上内容暂无说明。', 
                   '从以上文本中我们暂无发现。', 
                   '我们不能发现具体信息。',
                   '暂不清楚，需要更多信息说明。',
                   '我们无法得知，可能需要更多内容说明。',
                   '暂无明确信息说明。']
    
    with open(finqa_path, 'r') as f:
        finqa_list = json.load(f)
    
    finqa_lines = []
    for finqa_pair in finqa_list:
        input, output = finqa_pair
        if output == "无相应参数":
            output = random.choice(output_list)
        item = {'task': 'FINQA',
                'desc': '事件抽取任务',
                'instruction': input,
                'input': "",
                'output': output}
        finqa_lines.append(item)
    return finqa_lines


def process_fincqa(fincqa_path):
    '''
    description: 处理因果事件抽取FinCQA数据集
    return fincqa_lines(List)
    '''
    output_list = ['以上内容暂无说明。', 
                   '从以上文本中我们暂无发现。', 
                   '我们不能发现具体信息。',
                   '暂不清楚，需要更多信息说明。',
                   '我们无法得知，可能需要更多内容说明。']
    
    with open(fincqa_path, 'r') as f:
        fincqa_list = json.load(f)
    
    fincqa_lines = []
    for fincqa_pair in fincqa_list:
        input, output = fincqa_pair
        if output == "无参数":
            output = random.choice(output_list)
        item = {'task': 'FINCQA',
                'desc': '因果事件抽取任务',
                'instruction': input,
                'input': "",
                'output': output}
        fincqa_lines.append(item)
    return fincqa_lines


def process_finna(finna_path):
    '''
    description: 处理新闻文本摘要FinNA数据集
    return: finna_lines(List)
    '''
    instruction_list = ["针对以下新闻生成摘要。",
                        "根据以下新闻生成摘要。",
                        "对下面新闻生成标题。",
                        "总结下面这篇新闻的内容。",
                        "简述以下新闻。",
                        "摘要以下新闻内容。"]
    with open(finna_path, 'r') as f:
        finna_list = json.load(f)
    
    finna_lines = []
    for finna_pair in finna_list:
        instruction = random.choice(instruction_list)
        output, input = finna_pair
        item = {'task': 'FINNA',
                'desc': '新闻文本摘要任务',
                'instruction': instruction,
                'input': input,
                'output': output}
        finna_lines.append(item)
    return finna_lines


def process_finre(finre_path):
    '''
    description: 处理事件关系抽取FinRE数据集
    return: finre_lines(List)
    '''
    instruction_list = ['分析以下两个实体{}和{}之间的关系。',
                        '根据以下文本，描述以下两个实体{}和{}之间的关系。',
                        '请说明这两个实体{}和{}间的关系。',
                        '根据数据，可以得出这两个实体{}和{}之间的关系。',
                        '这两个实体{}、{}之间有什么关联。',
                        '从以下内容中，分析实体{}、{}之间的联系。']
    output_list = ["以上内容无法得知两者之间的关系。",
                   "我们暂时无法发现两者的关系。",
                   "对于这两者之间的关系，文中没有明确提及，可能需要更多信息说明。",
                   "上文没有明确说明两个实体之间的关联。"]
    
    with open(finre_path, 'r') as f:
        finre_list = json.load(f)
    
    finre_lines = []
    for finre_tuple in finre_list:
        instruction = random.choice(instruction_list)
        head_entity, tail_entity, relation, news = finre_tuple
        instruction = instruction.format(head_entity, tail_entity)
        if relation == "unknown":
            relation = random.choice(output_list)
        item = {'task': 'FINRE',
                'desc': '事件关系抽取任务',
                'instruction': instruction,
                'input': news,
                'output': relation}
        finre_lines.append(item)
    return finre_lines


def process_finnsp(finnsp_path):
    '''
    description: 处理负面消息识别及主体判定FinNSP数据集
    return: finnsp_lines(List)
    '''
    instruction_list = ["识别以下内容中的负面金融实体信息。",
                        "以下文本中包含哪些负面主体。",
                        "分析以下文本，从中筛选出负面金融实体。",
                        "选择下面文本中的负面金融主体信息。",
                        "判断该文本是否包含金融实体的负面信息，如果存在则输出负面实体名称。",
                        "输出以下内容中负面金融主体信息。"]
    without_output_list = ["上文中没有负面主体。",
                           "以上文本不存在负面主体。",
                           "该文本中不包含负面金融实体。",
                           "该内容中没有负面金融实体。",
                           "分析上述文本，发现没有负面金融实体。"]
    with_output_list = ["负面金融主体：{}",
                        "负面金融主体包含以下几个：{}",
                        "负面主体有：{}",
                        "文中包含的负面主体：{}",
                        "负面金融实体有以下几个：{}",
                        "负面金融实体有：{}"]
    with open(finnsp_path, 'r') as f:
        finnsp_list = json.load(f)
    
    finnsp_lines = []
    for finnsp_tuple in finnsp_list:
        _, _, news, _, _, negative_subject = finnsp_tuple
        instruction = random.choice(instruction_list)
        if len(negative_subject) > 0:
            output = random.choice(with_output_list)
            output = output.format(negative_subject)
        else:
            output = random.choice(without_output_list)
        item = {'task': 'FINNA',
                'desc': '负面消息识别及主体判定任务',
                'instruction': instruction,
                'input': news,
                'output': output}
        finnsp_lines.append(item)
    return finnsp_lines


def process_finnl(finnl_path):
    '''
    description: 处理新闻分类FinNL数据集
    return: finnl_lines(List)
    '''
    instruction_list = ["针对以下新闻进行分类，包含公司（个股）、行业（板块）、大盘、中国、国际、经济、政策、期货、债券、房地产、外汇、虚拟货币、新冠、能源、政治等15个类别。",
                        "把金融新闻分类为一个或多个与其描述内容相关的类别，包含公司（个股）、行业（板块）、大盘、中国、国际、经济、政策、期货、债券、房地产、外汇、虚拟货币、新冠、能源、政治等15个类别。",
                        "识别以下新闻的分类，包含公司（个股）、行业（板块）、大盘、中国、国际、经济、政策、期货、债券、房地产、外汇、虚拟货币、新冠、能源、政治等15个类别。",
                        "对以下新闻进行文本分类，包含公司（个股）、行业（板块）、大盘、中国、国际、经济、政策、期货、债券、房地产、外汇、虚拟货币、新冠、能源、政治等15个类别。",
                        "对下面新闻进行分类，类别包含公司（个股）、行业（板块）、大盘、中国、国际、经济、政策、期货、债券、房地产、外汇、虚拟货币、新冠、能源、政治。"]
    output_list = ["该新闻属于{}类别。",
                   "以上新闻类别是{}。",
                   "新闻的类别可能是{}。",
                   "分析以上新闻，我们认为它属于{}类别。",
                   "我们把以上新闻归属于{}类别。"]
    with open(finnl_path, 'r') as f:
        finnl_list = json.load(f)
    
    finnl_lines = []
    for finnl_pair in finnl_list:
        instruction = random.choice(instruction_list)
        news, label = finnl_pair
        label = label.split(" ")[-1]
        output = random.choice(output_list)
        output = output.format(label)
        item = {'task': 'FINNL',
                'desc': '新闻分类任务',
                'instruction': instruction,
                'input': news,
                'output': output}
        finnl_lines.append(item)
    return finnl_lines


def process_finese(finese_path):
    '''
    description: 处理事件主体抽取FinESE数据集
    return: finese_lines(List)
    '''
    instruction_list = ["分析以下新闻，抽取{}事件相关的主体信息。",
                        "以下新闻中，{}事件相关的金融主体是什么。",
                        "分析下面的新闻，属于{}事件的金融主体是什么。",
                        "下面新闻中属于{}事件的主体是什么。",
                        "以下关于{}事件的主体是什么。",
                        "抽取以下新闻中{}事件的主体信息。"]
    output_list = ["{}事件的主体是：{}。",
                   "上述新闻中{}事件的相关主体是{}。",
                   "和{}事件相关的主体是{}。",
                   "所属{}事件的金融主体是{}。",
                   "{}事件描述的金融主体是{}。"]
    with open(finese_path, 'r') as f:
        finese_list = json.load(f)
    
    finese_lines = []
    for finese_tuple in finese_list:
        _, news, event, subject = finese_tuple
        instruction = random.choice(instruction_list)
        instruction = instruction.format(event)
        if event == "其他":
            continue
        output = random.choice(output_list)
        output = output.format(event, subject)
        item = {'task': 'FINESE',
                'desc': '事件主体抽取任务',
                'instruction': instruction,
                'input': news,
                'output': output}
        finese_lines.append(item)
    return finese_lines
    
        
if __name__ == "__main__":
    tag = "eval"
    
    # 论坛情绪分析数据集
    finfe_path = "../FinCUGE_Publish/finfe/{}_list.json".format(tag)
    finfe_list = process_finfe(finfe_path)
    print(finfe_list[:3])
    
    # 事件抽取数据集
    finqa_path = "../FinCUGE_Publish/finqa/{}_list.json".format(tag)
    finqa_list = process_finqa(finqa_path)
    print(finqa_list[:3])
    
    # 因果事件抽取数据集
    fincqa_path = "../FinCUGE_Publish/fincqa/{}_list.json".format(tag)
    fincqa_list = process_fincqa(fincqa_path)
    print(fincqa_list[:3])
    
    # 新闻文本摘要数据集
    finna_path = "../FinCUGE_Publish/finna/{}_list.json".format(tag)
    finna_list = process_finna(finna_path)
    print(finna_list[:3])
    
    # 事件关系抽取数据集
    finre_path = "../FinCUGE_Publish/finre/{}_list.json".format(tag)
    finre_list = process_finre(finre_path)
    print(finre_list[:3])
    
    # 负面消息识别及主体判定数据集
    finnsp_path = "../FinCUGE_Publish/finnsp/{}_list.json".format(tag)
    finnsp_list = process_finnsp(finnsp_path)
    print(finnsp_list[:3])
    
    # 新闻分类数据集
    finnl_path = "../FinCUGE_Publish/finnl/{}_list.json".format(tag)
    finnl_list = process_finnl(finnl_path)
    print(finnl_list[:3])
    
    # 事件主体抽取数据集
    finese_path = "../FinCUGE_Publish/finese/{}_list.json".format(tag)
    finese_list = process_finese(finese_path)
    print(finese_list[:3])
    
    fin_list = finfe_list + finqa_list + fincqa_list + finna_list + finre_list + finnsp_list + finnl_list + finese_list
    print(len(fin_list))
    
    finance_df = pd.DataFrame(fin_list)
    fin_file = "{}_finance.csv".format(tag)
    finance_df.to_csv(fin_file)