import streamlit as st 

def page_config():
    st.set_page_config(page_title='钱海飞的简历',page_icon='📚',layout='wide',initial_sidebar_state='auto')

def side_column():
    with st.sidebar:
        st.logo(image='pic.jpg',link='https://henrychien.streamlit.app/')
        page = st.radio('#### 导航栏',('#### 🧾个人概况','#### 💡作品展示','#### :email:联系方式'))
        st.container(height=320,border=False)
        st.divider()
        st.download_button(label='⏬下载简历',data=open('cv.pdf', 'rb'),file_name='钱海飞的简历.pdf',mime='application/pdf')
        return page

def personal_info():
    left_column, right_column = st.columns([8,2])
    with left_column:
        st.write("#### <center>钱 海 飞</center>",unsafe_allow_html=True)
        mail_text = 'qhf0261120@163.com'
        st.write('<center>本科 | 13776317568 | qhf0261120@163.com </center>',unsafe_allow_html=True)
        st.write('<center>求职意向：运营总监/物流总监/集团总部层面商业分析（数据分析）部门负责人</center>',unsafe_allow_html=True)
        
    with right_column:
        st.image('pic.jpg', width=120,output_format='PNG')
    st.divider()
        
    st.write("##### 🛠️专业技能")
    st.write("""
            - **数据分析与挖掘：** Python、SQL、Power Query、M、NumPy、Pandas、爬虫  
            - **建模与可视化：** Power BI、DAX、Power Pivot、Matplotlib、Seaborn  
            - **统计分析：** 形态分布、离散趋势、集中趋势、假设检验、线性回归、逻辑回归  
            - **数字化搭建与应用开发：** Streamlit、宜搭、Power Apps  
            - **集成自动化：** RPA、Power Automate  
            - **AI大模型(LLM)：** LangChain、Prompt Engineering、Fine Tuning、RAG、Agent、Embedding
             """)
    st.divider()
    
    st.write("##### 💼工作经历")
    columns = st.columns([5,2,3])
    with columns[0]:
        st.write("**江苏弘帆供应链管理有限公司**")    
    with columns[1]:
        st.write("总经理") 
    with columns[2]:
        st.write("2020.08 - ") # 待完善   
    st.write("""
            - **团队管理：** 领导团队完成物流部门的日常工作，包括货物的接收、储存、发运等。制定并执行团队目标，激励团队成员积极工作，提高工作效率和质量。  
            - **战略规划：** 负责公司供应链战略的制定和实施，包括供应商管理、采购、物流、库存管理等方面的规划和优化。  
            - **供应链管理：** 负责公司的供应链管理，协调采购、仓储、运输等部门，确保物流运作顺畅高效。维护与供应商和客户的关系，优化供应链流程，降低成本，提高服务质量。  
            - **成本控制：** 对物流运作的成本进行分析和控制，制定成本控制策略，降低物流成本，提高公司盈利能力。    
            - **安全管理：** 负责物流安全管理工作，制定并执行安全管理制度，加强货物保护和安全防范，确保物流运作的安全可靠。  
            - **供应商管理：** 制定供应商评价体系，确保供应商的履约能力达到公司要求。  
            - **采购管理：** 负责采购流程的优化和改进，确保采购的成本和质量符合公司要求。  
            - **物流管理：** 负责物流流程的优化和改进，确保物流的准时性和成本控制。
             """)
    st.write('')
    columns = st.columns([5,2,3])
    with columns[0]:
        st.write("**苏州工业园区顺丰速运有限公司**")    # 加上获奖情况
    with columns[1]:
        st.write("经营分部负责人") 
    with columns[2]:
        st.write("2015.06 - 2020.07")    
    st.write("""
            - **经营规划：** 结合公司战略及地区业务方向，制定片区的经营策略，并统筹片区经营管理，把握片区经营节奏，合理统筹部署相应资源投入，确保投入产出最大化，推动片区收入、利润、底盘均衡发展。
            - **业务拓展：** 洞察片区市场，掌握客户及客户供应链上下游情况，关注客户需求变化，识别潜在业务机会，联动各组织，利用多元化的产品策略（大件、冷运、医药、国际、仓储、同城等）制定客户解决方案及响应客户需求，做深做大片区业务规模。
            - **精益管理：** 从所辖片区中长期竞争力出发，在充分理解集团各项变革项目前提下，标准SOP落地、以模式变革推动结构成本的弹性化，实现高质量客户体验的稳定交付。
            - **团队建设：** 营造积极向上的团队氛围，识人用人，组建干部团队，清晰充分授权，并灵活运用考核激励辅导等，提升团队绩效，输出经营人才。
            - **风险管控：** 实现经营目标的过程中，将信息、人员、舆论、客户、快件、资金等各类风险进行前置识别及闭环管控，确保风险在预期范围内，避免造成组织利益、品牌等损失。
            - **品牌建设：** 推动地区品牌建设工作，提升品牌影响力。
             """)
    st.write('')
    columns = st.columns([5,2,3])
    with columns[0]:
        st.write("**南通云途贸易有限公司**")
    with columns[1]:
        st.write("线上业务运营负责人") 
    with columns[2]:
        st.write("2012.01 - 2015.05")    
    st.write("""
            - **运营管理：** 负责商品上架、价格调整、库存管理、物流跟进等运营管理工作，保证商品的正常销售和运营。
            - **数据分析：** 负责公司数据的采集、清洗、分析和报告，为决策提供数据支持，提高业务效率和效益。
            - **数据挖掘：** 利用数据挖掘技术，发现数据中的规律和趋势，为业务提供预测和建议，提高决策的准确性和效果。
            - **数据可视化：** 使用数据可视化工具，将数据呈现为图表、报表等形式，直观地展示数据分析结果，为业务决策提供参考。
            - **活动策划：** 负责京东商城各类活动的策划、执行和效果评估，包括双11、618、年中大促等。
            - **用户运营：** 负责用户留存、活跃、转化等运营工作，制定并执行用户运营策略，提高用户满意度和忠诚度。  
            - **团队管理：** 管理运营团队，制定团队目标和和考核标准，培养和激励团队成员，确保团队高效运转。
             """)
    st.write('')
    columns = st.columns([5,2,3])
    with columns[0]:
        st.write("**索尼物流贸易（中国）有限公司**")
    with columns[1]:
        st.write("空运操作主管") 
    with columns[2]:
        st.write("2007.12 - 2011.11")    
    st.write("""
            - **团队管理：** 负责领导和管理团队，指导下属完成日常工作，确保团队高效运转。
            - **运输安排：** 根据客户的要求和货物的特性，选择合适的运输方式，并与物流公司、运输公司等进行协商和安排。
            - **货物跟踪：** 跟踪货物的运输情况，及时解决运输过程中出现的问题，并及时向客户反馈货物的运输情况。
            - **数据分析：** 负责收集、整理公司内部和外部市场数据，进行数据分析并提出相应的解决方案，为公司决策提供支持。
            - **成本控制：** 负责公司运营成本的控制和优化，确保公司运营效益最大化。
            - **沟通协调：** 负责与客户进行沟通，了解客户的需求，并根据情况为客户提供合适的货运方案。
             """)
    st.write('')
    columns = st.columns([5,2,3])
    with columns[0]:
        st.write("**飞利浦照明（上海）有限公司**")
    with columns[1]:
        st.write("供应链专员") 
    with columns[2]:
        st.write("2006.07 - 2007.10")    
    st.write("""
            - **数据分析：** 负责物流数据的统计和分析，及时发现问题并提出解决方案，优化物流流程，提高效率和降低成本。
            - **采购管理：** 负责公司原材料、包装材料的采购工作，与供应商保持良好的合作关系，及时跟进订单进度，确保生产计划的顺利执行。
            - **库存管理：** 负责公司库存的监控和管理，及时更新库存数据，制定合理的库存策略，确保库存水平符合公司的生产和销售计划。
            - **物流管理：** 负责货物的配送和运输安排，与物流公司、运输车队等进行沟通协调，确保货物按时安全到达目的地。
            - **供应商管理：** 负责公司供应商的评估和管理工作，建立供应商档案，定期进行供应商绩效评估，推动供应商的持续改进，提高供应链的稳定性和可靠性。
            - **客户服务：** 与客户沟通协调，解决客户问题和投诉，提高客户满意度。
             """)
    st.divider()
    
    st.write("##### 💻项目经历")
    columns = st.columns([5,2,3])
    with columns[0]:
        st.write("2016.06 - 2024.07")
    with columns[1]:
        st.write("经营驾驶舱") 
    with columns[2]:
        st.write("业务负责人")
    st.write("""
            - **需求收集：** 梳理现有表结构和元数据，理清数据血缘关系，同时进行业务部门调研，收集并总结日常所需的经营数据维度。
            - **数据提取：** 使用Power Query从数据库中提取所需数据，并聚合连接多表形成日常所需的宽表视图，供报表和看板使用。
            - **数据处理：** 基于数据库中的原有字段，结合业务需求增加数据堆度。
            - **看板搭建：** 使用Power BI搭建日常分析所用的数据看板，发布到BI服务，并进行日常的维护。
             """)
    st.write('')
    columns = st.columns([5,2,3])
    with columns[0]:
        st.write("2012.01 - 2015.05")
    with columns[1]:
        st.write("线上商城经营看板") 
    with columns[2]:
        st.write("运营负责人")
    st.write("""
            - **业务诊断：** 针对业务经营的营收、利润、成本、流量进行分析，通过规模、占比、趋势进行维度拆解，形成经营分析矩阵框架。
            - **绩效拆解：** 多维度量化各部门经营目标，可视化展现各部门绩效达标率、对各部门和员工的绩效进行评估和排名，降本增效。
            - **用户分析：** 对用户特征标签进行可视化分析，包括用户年级、地域、教育背景等关键特征，挖掘消费复购潜力，提高UV价值。
            - **渠道分析：** 评估不同渠道带来的用户转化率，关注访问、领券、下单、购买等关键环节专户率，优化用户行为漏斗，提质提效。
             """)    
    st.divider()
    
    st.write("##### 🎓教育背景")
    columns = st.columns([4,3,3])
    with columns[0]:
        st.write("南通大学")    
    with columns[1]:
        st.write("国际经济与贸易") 
    with columns[2]:
        st.write("2002.09 - 2006.06")
    st.write("""
             主修课程：经济学、统计学、运筹学、会计学、物流管理、国际贸易、市场营销、计算机科学与技术等
             """)
    
def introduce_sales():
    st.write("""
                    **一、项目背景**    
                    本报告旨在通过数据可视化工具Power BI，对某企业的销售业务进行全面分析。
                    通过分析销售、利润、订单、客户及产品等多个维度的数据，帮助企业识别业务中的优势和问题，并提出改进建议。  
                        
                    **二、分析思路**  
                    - 销售分析：重点关注月销售额、年累计销售额、月环比及同比变化。  
                    - 利润分析：分析月利润、年累计利润及环比、同比变化，考察利润率。  
                    - 订单分析：评估月订单量、平均订单金额及其变化趋势。   
                    - 客户分析：研究客户数量、客单价、客户的年龄、职业、性别及城市分布。  
                    - 产品分析：根据销售额、利润对产品进行分类，使用ABC分析法识别主要产品。  
                        
                    **三、分析结论**  
                    - 销售情况：9月份销售额为48,833元，同比增加8.27%，但环比减少1.73%。年累计销售额达到454,755元，整体销售趋势稳中有升。  
                    - 利润情况：本月利润为18,079元，环比下降4.51%，但年累计利润为172,333元，同比增长8.48%。整体利润率保持在37%-40%之间。  
                    - 订单量：9月份订单量为284，同比减少24.27%，但平均订单金额增加到171.95元，环比上升29.75%。  
                    - 客户分析：9月份客户数为243，同比减少20.33%，但客单价提高到200.96元。客户主要集中在北京和上海，80后和90后为主要消费群体。  
                    - 产品表现：A类产品（如硬盘、充电宝等）销售额和利润较高，B类和C类产品表现一般，需要优化产品结构。  
                    
                    **四、策略建议**  
                    - 销售策略：针对销售额下降的月份，进行市场调研，了解销售下滑原因，优化销售策略，提升销售额。  
                    - 利润优化：进一步控制成本，提高产品的利润率，特别关注利润率波动较大的产品。  
                    - 订单管理：提升订单处理效率，通过促销活动吸引更多订单，特别是在订单量下降的月份。  
                    - 客户维护：加强与高价值客户的互动，提升客户满意度和忠诚度，开发潜在客户。  
                    - 产品优化：根据ABC分析结果，调整产品线，增加高销售额和高利润产品的比重，淘汰或改进表现不佳的产品。  
                    
                    **五、项目成果**  
                    通过本次数据分析，企业可以更好地了解自身业务状况，发现潜在问题，并通过相应的策略调整，
                    提升整体业务表现。未来可以继续利用Power BI等工具进行数据监控和分析，实现精细化管理。
                     """)

def introduce_hr():
    st.write("""
            **一、项目背景**  
            随着企业规模的不断扩大，人力资源管理变得越来越复杂。为了提高人力资源管理的效率和决策的准确性，本项目利用Power BI对企业的人力资源数据进行了深入分析。
            通过数据可视化展示企业在人力资源方面的关键指标，帮助管理层全面了解员工结构、招聘情况、员工流动、培训效果以及薪酬分布等方面的信息，进而制定科学的管理策略。

            **二、分析思路**  
            - 数据收集: 收集企业的员工基本信息、招聘数据、员工流动数据、培训记录和薪酬数据等。  
            - 数据处理: 对收集到的数据进行清洗、整合和规范化处理，确保数据的准确性和一致性。  
            - 数据分析: 利用Power BI对处理后的数据进行可视化分析，主要分析维度包括员工结构、人才招聘、员工流动、员工培训和薪酬分布。  
            - 结果展示: 通过仪表板的形式展示分析结果，使管理层能够直观地查看和理解人力资源各方面的情况。  
            
            **三、分析结论**  
            - 员工结构: 企业员工主要集中在生产部门，且以40-50岁年龄段为主。本科及以上学历的员工占比较高，已婚员工比例较大，司龄主要集中在15-25年。  
            - 人才招聘: 招聘完成率较低，存在招聘渠道单一、面试通过率低等问题。部分岗位需求量大但招聘完成率低。  
            - 员工流动: 员工流动率较高，尤其是生产部门。主要离职原因包括个人原因、薪资问题和工作与生活平衡问题。  
            - 员工培训: 培训投入较高，但培训效果存在差异。部分部门的培训通过率较低，需要改进培训内容和方式。  
            - 薪酬分布: 各部门薪酬水平差异较大，部分岗位薪酬低于市场平均水平，存在薪酬倒挂现象。  
            
            **四、策略建议**  
            - 优化招聘流程: 拓宽招聘渠道，改进招聘策略，提高面试通过率，特别是针对关键岗位应进行有针对性的招聘。  
            - 完善员工关怀: 提高员工的薪酬福利，特别是生产部门员工，并提供更多的职业发展和晋升机会，减少员工流动率。  
            - 改进培训机制: 根据各部门的具体需求调整培训内容，提高培训的针对性和实用性，同时加强培训后的效果评估。  
            - 薪酬调整: 根据市场薪酬水平和岗位价值，适当调整部分岗位的薪酬标准，避免薪酬倒挂，确保薪酬体系的公平性和竞争力。  
            
            **五、项目成果**  
            - 综合仪表板: 通过Power BI构建的综合仪表板，直观展示了企业在员工结构、招聘、流动、培训和薪酬等方面的关键指标。
            - 数据驱动决策: 提供了数据支持，帮助管理层基于数据做出科学的决策，提升人力资源管理的效率和效果。
            - 发现问题与改进方向: 通过数据分析，发现了当前人力资源管理中的问题，并提出了相应的改进建议，为企业的持续发展提供支持。
             """)

def introduce_finance():
    st.write("""
            **一、项目背景**  
            随着企业规模的不断扩大和业务的多元化发展，财务管理变得愈加复杂和重要。为了提高财务决策的科学性和准确性，本项目利用Power BI对企业的财务数据进行了系统性分析。
            通过数据可视化展示企业在资产负债、利润、现金流量、运营能力和杜邦分析等方面的财务状况，帮助管理层全面了解企业的财务健康状况，优化财务管理策略。  
            
            **二、分析思路**  
            - 数据收集: 收集企业的财务报表数据，包括资产负债表、利润表、现金流量表等。  
            - 数据处理: 对收集到的数据进行清洗、整合和规范化处理，确保数据的准确性和一致性。  
            - 数据分析: 利用Power BI对处理后的数据进行可视化分析，主要分析维度包括资产负债、利润、现金流量、运营能力和杜邦分析。  
            - 结果展示: 通过仪表板的形式展示分析结果，使管理层能够直观地查看和理解企业的财务状况。  
            
            **三、分析结论**  
            ***资产负债:***  
            - 资产负债率: 2023年企业的资产负债率为53.37%，比去年下降了1.31%。  
            - 流动比率: 2023年企业的流动比率为1.23，较年初有所提高，表明企业的短期偿债能力有所增强。  
            - 速动比率: 2023年企业的速动比率为1.20，略有提升，进一步验证了企业的流动性状况良好。  
            
            ***利润:***  
            - 营业收入: 2023年企业的营业收入为25,840,940万元，同比下降了3%。  
            - 净利润: 2023年企业的净利润为791,161万元，净利润率为3.06%，比去年增长了1.17%。  
            - 毛利率: 2023年的毛利率为12.82%，显示企业的盈利能力较为稳定。  
            
            ***现金流量:***  
            - 经营活动产生的现金流量净额: 2023年为2,656,982万元，同比下降18.80%。  
            - 投资活动产生的现金流量净额: 2023年为-1,350,562万元，同比下降11.67%。  
            - 筹资活动产生的现金流量净额: 2023年为-1,299,469万元，同比增加23.66%。  
            
            ***运营能力:***  
            - 应收账款周转天数: 2023年为35天，显示企业的应收账款回收较快。  
            - 存货周转天数: 2023年为4天，表明企业的存货管理较为有效。  
            - 运营周期: 2023年为40天，表明企业的整体运营效率较高。  
            
            ***杜邦分析:***  
            - 净资产收益率: 2023年为7.85%，反映了企业的整体盈利能力。  
            - 总资产周转率: 2023年为117.91%，显示企业资产利用效率较高。  
            - 权益乘数: 2023年为217.46%，反映了企业的财务杠杆水平。  
            
            **四、策略建议**  
            - 提高营收: 通过优化市场营销策略和产品组合，进一步提高企业的营业收入，逆转收入下降的趋势。  
            - 成本控制: 加强成本管理，特别是对销售费用和管理费用的控制，以提升企业的盈利能力。  
            - 优化现金流管理: 提高经营活动现金流入，减少不必要的投资和筹资活动支出，保持健康的现金流状况。  
            - 加强应收账款和存货管理: 进一步缩短应收账款和存货周转天数，提高企业的运营效率。  
            - 合理运用财务杠杆: 在保持财务稳定的前提下，适度利用财务杠杆，提升净资产收益率。  
            
            **五、项目成果**  
            - 全面的财务分析仪表板: 通过Power BI构建的财务分析仪表板，直观展示了企业在资产负债、利润、现金流量、运营能力和杜邦分析等方面的财务状况。  
            - 数据驱动决策: 提供了数据支持，帮助管理层基于数据做出科学的财务决策，提升财务管理的效率和效果。  
            - 发现问题与改进方向: 通过数据分析，发现了当前财务管理中的问题，并提出了相应的改进建议，为企业的持续发展提供支持。  
             """)
    
def works_bi():
    columns = st.columns([2,8])
    with columns[0]:
        bi = st.radio('**查看作品**',['PowerBI销售业务分析报告','PowerBI人力资源分析报告','PowerBI财务报表分析报告'],label_visibility='hidden')
    with columns[1]:
        with st.expander("**项目介绍**"):
            if bi == 'PowerBI销售业务分析报告':
                introduce_sales()
            elif bi == 'PowerBI人力资源分析报告':
                introduce_hr()
            elif bi == 'PowerBI财务报表分析报告':
                introduce_finance()
           
        cols = st.columns((8,2))    
        with cols[0]:
            if bi == 'PowerBI销售业务分析报告':
                st.write('🔗[**交互查看**](https://app.powerbi.com/view?r=eyJrIjoiOWJjYjk4NjEtY2ExZC00NWZkLWFiY2YtYzllMjQ0OGZkOGZiIiwidCI6IjViYjFiNzIxLTRmYjItNDI3MS04ZTcxLTMxMzNlZWMzMWU4NSIsImMiOjEwfQ%3D%3D)')
            elif bi == 'PowerBI人力资源分析报告':
                st.write('🔗[**交互查看**](https://app.powerbi.com/view?r=eyJrIjoiM2VmZGU0ZjUtNjkzNS00OThkLWIwYWQtM2U1M2E3ZDliY2E1IiwidCI6IjViYjFiNzIxLTRmYjItNDI3MS04ZTcxLTMxMzNlZWMzMWU4NSIsImMiOjEwfQ%3D%3D)')
            elif bi == 'PowerBI财务报表分析报告':
                st.write('🔗[**交互查看**](https://app.powerbi.com/view?r=eyJrIjoiYTcwZDVjYjItNmY2Ny00MjQyLThkYzUtM2ExOGY3MjY4M2ZjIiwidCI6IjViYjFiNzIxLTRmYjItNDI3MS04ZTcxLTMxMzNlZWMzMWU4NSIsImMiOjEwfQ%3D%3D)')
        with cols[1]:
            st.write('👇🏼**静态预览**')
        if bi == 'PowerBI销售业务分析报告':
            st.image(['sales_pic/sales01.png',
                        'sales_pic/sales02.png',
                        'sales_pic/sales03.png',
                        'sales_pic/sales04.png',
                        'sales_pic/sales05.png',
                        'sales_pic/sales06.png'])
        elif bi == 'PowerBI人力资源分析报告':
            st.image(['hr_pic/HR01.png',
                        'hr_pic/HR02.png',
                        'hr_pic/HR03.png',
                        'hr_pic/HR04.png',
                        'hr_pic/HR05.png',
                        'hr_pic/HR06.png']
                        )
        elif bi == 'PowerBI财务报表分析报告':
            st.image(['finance_pic/finance1.png',
                        'finance_pic/finance2.png',
                        'finance_pic/finance3.png',
                        'finance_pic/finance4.png',
                        'finance_pic/finance5.png',
                        'finance_pic/finance6.png',
                        'finance_pic/finance7.png'])

def introduce_ai():
    st.write("""
        **一、所用工具**  
        - 编程语言: Python  
        - Web应用框架: Streamlit  
        - LangChain开发框架模块: Prompt Template、Memory、Model、Output Parser、Chain、Retriever、RAG、Agent  
        
        **二、项目描述**  
        本项目旨在开发一组基于大模型和LangChain框架的智能工具集，包括CSV数据分析智能工具、克隆ChatGPT、智能PDF问答工具、视频脚本一键生成器和爆款小红书文案生成器。
        每个工具均使用LangChain框架中的不同模块来实现其特定功能，并通过Streamlit框架提供用户友好的前端界面。  
        
        **三、项目细节**  
        **CSV数据分析智能工具**  
        - ***功能:***  
        上传CSV文件，输入自然语言问题或数据分析请求，生成对应的可视化图表和分析报告。  
        - ***实现细节:***  
        使用Prompt Template生成数据分析的提示。  
        使用Retriever从CSV文件中提取相关数据。  
        使用RAG生成分析报告。  
        - ***界面展示:***  
        用户可以上传CSV文件并输入问题，系统生成对应的可视化图表和分析报告。  
        
        **克隆ChatGPT**    
        - ***功能:***    
        提供类似于ChatGPT的对话体验，能够回答用户提出的各种问题。  
        - ***实现细节:***   
        使用Memory模块记住对话上下文。  
        使用Model模块生成对话响应。  
        使用Agent模块协调不同的功能实现复杂对话。  
        - ***界面展示:***  
        用户可以与克隆ChatGPT进行对话，获取问题答案和建议。  
        
        **智能PDF问答工具**  
        - ***功能:***    
        上传PDF文件，输入问题，系统从PDF内容中提取答案。  
        - ***实现细节:***   
        使用Retriever模块从PDF中检索相关信息。  
        使用Output Parser模块解析答案。  
        - ***界面展示:***  
        用户上传PDF文件并输入问题，系统返回从PDF中提取的答案。  
        
        **视频脚本一键生成器**    
        - ***功能:***    
        输入视频主题和关键词，自动生成视频脚本。  
        - ***实现细节:***   
        使用Prompt Template生成视频脚本的提示。  
        使用Model模块生成脚本内容。  
        - ***界面展示:***  
        用户输入视频主题和关键词，系统生成完整的视频脚本。  
        
        **爆款小红书文案生成器**    
        - ***功能:***    
        输入主题，生成多个吸引人的小红书文案。  
        - ***实现细节:***   
        使用Prompt Template生成文案提示。  
        使用Model模块生成文案内容。  
        - ***界面展示:***  
        用户输入主题，系统生成多个小红书文案供选择。    
        
        **四、项目成果**    
        1. 多功能智能工具集: 提供CSV数据分析、智能对话、PDF问答、视频脚本生成和小红书文案生成等多种功能，满足用户不同的需求。  
        2. 用户友好的界面: 使用Streamlit框架，提供直观的用户界面，用户可以轻松使用各项功能。  
        3. 高效的数据处理与分析: 利用LangChain框架的强大功能模块，实现高效的数据处理与分析，提升用户体验。  
        
        **五、结论**  
        本项目通过整合LangChain和Streamlit框架，成功开发了一组多功能的智能工具集，涵盖数据分析、对话生成、文档问答、脚本生成等多种应用场景。
        这些工具能够有效提高用户的工作效率，满足不同业务场景的需求。未来可以继续扩展功能模块和优化用户界面，以进一步提升应用的实用性和用户体验。 
        """)
                
def works_ai(): 
    columns = st.columns([2,8])
    with columns[0]:
        ai = st.radio('👀**查看作品**',
                        ['视频脚本一键生成器','爆款小红书文案生成器','克隆ChatGPT','智能PDF问答工具','CSV数据分析智能工具'],label_visibility='hidden')
    with columns[1]:
        with st.expander("**项目介绍**"):
            introduce_ai()
        cols = st.columns((8,2))    
        with cols[0]:
            if ai == '视频脚本一键生成器':
                st.link_button(label='**🔗交互查看**',url='https://aiagent01.streamlit.app/%E8%A7%86%E9%A2%91%E8%84%9A%E6%9C%AC%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90%E5%99%A8')
            elif ai == '爆款小红书文案生成器':
                st.link_button(label='**🔗交互查看**',url='https://aiagent01.streamlit.app/%E7%88%86%E6%AC%BE%E5%B0%8F%E7%BA%A2%E4%B9%A6%E6%96%87%E6%A1%88%E7%94%9F%E6%88%90%E5%99%A8')
            elif ai == '克隆ChatGPT':
                st.link_button(label='**🔗交互查看**',url='https://aiagent01.streamlit.app/%E5%85%8B%E9%9A%86ChatGPT')              
            elif ai == '智能PDF问答工具':
                st.link_button(label='**🔗交互查看**',url='https://aiagent01.streamlit.app/%E6%99%BA%E8%83%BDPDF%E9%97%AE%E7%AD%94%E5%B7%A5%E5%85%B7')
            elif ai == 'CSV数据分析智能工具':
                st.link_button(label='**🔗交互查看**',url='https://aiagent01.streamlit.app/')      
        with cols[1]:
            st.write('👇🏼**静态预览**')
        if ai == '视频脚本一键生成器':
            st.image('video_script.png',output_format='PNG')
        elif ai == '爆款小红书文案生成器':
            st.image('xhs.png',output_format='PNG')
        elif ai == '克隆ChatGPT':
            st.image('clone_gpt.png',output_format='PNG')        
        elif ai == '智能PDF问答工具':
            st.image('qa.png',output_format='PNG')
        elif ai == 'CSV数据分析智能工具':
            st.image('csv.png',output_format='PNG')       

def introduce_insurance():
    st.write("""
        **一、所用工具**  
        - 编程语言: Python
        - 数据处理与分析库: pandas, numpy, scikit-learn
        - 可视化库: matplotlib, seaborn
        - Web应用框架: Streamlit
        - 其他库: pickle  
            
        **二、项目描述**  
        本项目旨在开发一个医疗费用预测的Web应用，利用机器学习模型来预测被保险人的医疗费用，为保险公司在定价时提供参考。用户可以通过该应用输入个人信息，如年龄、性别、BMI、吸烟与否等，应用会根据这些信息预测未来的医疗费用。

        **三、项目细节**  
        1. 数据预处理
        - 加载数据: 读取医疗费用数据集。  
        - 数据清洗: 处理缺失值，异常值处理，数据类型转换。  
        - 特征工程: 生成新的特征，处理类别变量，特征缩放。  
        
        2. 数据探索与可视化   
        - 统计分析: 分析各个特征与医疗费用的关系。  
        - 数据可视化: 使用matplotlib和seaborn进行可视化，展示数据分布和特征之间的关系。  
        
        3. 模型生成  
        - 数据拆分: 将数据集拆分为训练集和测试集。  
        - 模型训练: 使用随机森林回归模型训练数据。  
        - 模型评估: 通过均方误差（MSE）、均方根误差（RMSE）等指标评估模型性能。  
        
        4. 模型保存  
        - 模型序列化: 使用pickle将训练好的模型保存为文件，以便在Web应用中加载使用。  
        
        5. Web应用输入格式化  
        - 输入处理: 定义用户输入的格式和类型，并对输入进行处理，以便送入模型进行预测。  
        
        6. Web应用预测功能  
        - 用户界面: 使用Streamlit创建用户界面，用户可以输入个人信息。  
        - 加载模型: 加载预训练的机器学习模型。  
        - 费用预测: 根据用户输入的信息，使用模型预测医疗费用，并展示预测结果。  
        
        
        **四、项目成果**  
        医疗费用预测模型: 通过随机森林回归模型预测医疗费用，具有较高的预测准确度。  
        用户友好的Web应用: 使用Streamlit框架搭建，用户可以方便地输入个人信息并获得医疗费用预测结果。  
        数据可视化与分析报告: 对医疗费用数据进行深入分析，并生成可视化报告，帮助理解数据特征和模型表现。  
            
        **五、结论**  
        本项目通过机器学习和Web应用开发，成功地实现了医疗费用的预测功能，为保险公司的定价策略提供了有效的工具。未来可以通过引入更多的特征和优化模型来进一步提升预测准确度。
            """)
                
def introduce_classifier():
    st.write("""
            **一、所用工具**  
            - 编程语言: Python  
            - 数据处理与分析库: pandas, numpy, scikit-learn  
            - 可视化库: matplotlib, seaborn  
            - Web应用框架: Streamlit  
            - 其他库: pickle  
            
            **二、项目描述**  
            本项目旨在开发一个企鹅种类预测的Web应用，利用机器学习模型来预测企鹅的种类。用户可以通过该应用输入企鹅的各种生物特征，如喙长、喙深、翅长、体重等，应用会根据这些信息预测企鹅的种类。

            **三、项目细节**  
            1. 数据预处理
            - 加载数据: 读取企鹅数据集 penguins-chinese.csv。  
            - 数据清洗: 处理缺失值，异常值处理，数据类型转换。  
            - 特征工程: 生成新的特征，处理类别变量，特征缩放。  
            
            2. 数据探索与可视化   
            - 统计分析: 分析各个特征与企鹅种类的关系。  
            - 数据可视化: 使用matplotlib和seaborn进行可视化，展示数据分布和特征之间的关系。  
            
            3. 模型生成  
            - 数据拆分: 将数据集拆分为训练集和测试集。  
            - 模型训练: 使用随机森林分类模型训练数据。  
            - 模型评估: 通过准确率、混淆矩阵等指标评估模型性能。  
            - 模型保存  
            - 模型序列化: 使用pickle将训练好的模型保存为文件，以便在Web应用中加载使用。  
            
            4. Web应用输入格式化  
            - 输入处理: 定义用户输入的格式和类型，并对输入进行处理，以便送入模型进行预测。  
            
            5. Web应用加载与预测功能  
            - 用户界面: 使用Streamlit创建用户界面，用户可以输入企鹅的生物特征信息。  
            - 加载模型: 加载预训练的机器学习模型。  
            - 种类预测: 根据用户输入的信息，使用模型预测企鹅的种类，并展示预测结果。  
            
            **四、项目成果**  
            1. 企鹅种类预测模型: 通过随机森林分类模型预测企鹅种类，具有较高的预测准确度。  
            2. 用户友好的Web应用: 使用Streamlit框架搭建，用户可以方便地输入企鹅的生物特征并获得种类预测结果。  
            3. 数据可视化与分析报告: 对企鹅数据进行深入分析，并生成可视化报告，帮助理解数据特征和模型表现。  
            
            **五、结论**  
            本项目通过机器学习和Web应用开发，成功地实现了企鹅种类的预测功能，为生物研究和保护提供了有效的工具。未来可以通过引入更多的特征和优化模型来进一步提升预测准确度。
             """)       

def introduce_dashboard():
    st.write("""
            **一、所用工具**  
            - 编程语言: Python  
            - 数据处理与分析库: pandas, numpy  
            - 可视化库: matplotlib, seaborn, plotly  
            - Web应用框架: Streamlit  
            - 其他库: openpyxl（用于处理Excel文件）  
            
            **二、项目描述**  
            本项目旨在开发一个销售数据仪表板Web应用，利用数据可视化技术来展示销售数据的关键指标和趋势。
            用户可以通过该应用选择不同的城市、顾客类型和性别，查看总销售额、平均顾客评分和每单平均销售额等信息，
            并以图表形式直观展示销售数据。

            **三、项目细节**  
            1. 数据加载与预处理
            - 加载数据: 使用pandas加载supermarket_sales.xlsx文件。  
            - 数据清洗: 处理缺失值，数据类型转换，创建必要的衍生变量。  
            
            2. 数据可视化与分析
            - 创建仪表板: 使用Streamlit创建用户界面，用户可以选择城市、顾客类型和性别进行筛选。  
            - 关键指标显示: 计算并显示总销售额、顾客评分的平均值、每单的平均销售额。  
            - 图表展示:  
            - 按小时数划分的销售额: 使用条形图展示不同小时的销售额分布。  
            - 按产品类型划分的销售额: 使用条形图展示不同产品类型的销售额分布。  
            
            3. Web应用部署
            - 用户界面: 使用Streamlit创建交互式用户界面，用户可以通过侧栏选择数据筛选条件。  
            - 动态更新: 根据用户选择的条件，动态更新显示的关键指标和图表。  
            
            **四、项目成果**  
            1. 互动式销售数据仪表板: 用户可以通过选择不同的筛选条件，查看不同城市、顾客类型和性别的销售数据，具有高度互动性。  
            2. 关键指标展示: 仪表板直观展示了总销售额、顾客评分的平均值和每单的平均销售额，为用户提供了清晰的销售概况。  
            3. 数据可视化: 使用多种图表展示销售数据，包括按小时数和按产品类型划分的销售额，帮助用户深入理解销售数据的分布和趋势。  
            
            **五、结论**  
            本项目通过数据处理、分析和可视化技术，成功地实现了一个交互式的销售数据仪表板Web应用。
            该应用为用户提供了方便的工具来查看和分析销售数据，能够有效支持商业决策。
            未来可以通过引入更多的数据维度和高级分析功能来进一步提升应用的实用性和用户体验。
             """)         
            
def works_ml():
    columns = st.columns([2,8])
    with columns[0]:
        ml = st.radio('👀**查看作品**',['用随机森林回归模型预测医疗费用','用随机森林分类算法模型预测企鹅种类','销售数据仪表板'],label_visibility='hidden')
    with columns[1]:
        with st.expander("**项目介绍**"):
            if ml == '用随机森林回归模型预测医疗费用':
                introduce_insurance()
            elif ml == '用随机森林分类算法模型预测企鹅种类':
                introduce_classifier()
            elif ml == '销售数据仪表板':
                introduce_dashboard()
        cols = st.columns((8,2))    
        with cols[0]:
            if ml == '用随机森林分类算法模型预测企鹅种类':
                st.link_button(label='**🔗交互查看**',url='https://randomforestclassifier01.streamlit.app/')
            elif ml == '用随机森林回归模型预测医疗费用':
                st.link_button(label='**🔗交互查看**',url='https://insurancepred.streamlit.app/')
            elif ml == '销售数据仪表板':
                st.link_button(label='**🔗交互查看**',url='https://dashborad.streamlit.app/')
        with cols[1]:
            st.write('👇🏼**静态预览**')
        if ml == '用随机森林分类算法模型预测企鹅种类':
            st.image('penguin01.png',output_format='PNG')
            st.image('penguin02.png',output_format='PNG')
        elif ml == '用随机森林回归模型预测医疗费用':
            st.image('insurance01.png',output_format='PNG')
            st.image('insurance02.png',output_format='PNG')
        elif ml == '销售数据仪表板':
            st.image('dashboard.png',output_format='PNG')

def works_py():
    columns = st.columns([2,8])
    with columns[0]:
        py = st.radio('👀**查看作品**',['用假设检验分析鸢尾花种类差异显著性','可视化探索帕默群岛企鹅数据','用线性回归预测房屋价格','用逻辑回归预测泰坦尼克幸存情况'],label_visibility='hidden')
    with columns[1]:
        cols = st.columns((8,2))    
        with cols[0]:
            if py == '用假设检验分析鸢尾花种类差异显著性':
                st.download_button(label="**下载清晰完整报告⏬**",data=open('用假设检验分析鸢尾花种类差异显著性.pdf', 'rb'),file_name=f'钱海飞_{py}分析报告.pdf')
            elif py == '可视化探索帕默群岛企鹅数据':
                st.download_button(label="**下载清晰完整报告⏬**",data=open('可视化探索帕默群岛企鹅数据分析报告.pdf', 'rb'),file_name=f'钱海飞_{py}分析报告.pdf')
            elif py == '用线性回归预测房屋价格':
                st.download_button(label="**下载清晰完整报告⏬**",data=open('用线性回归预测房价分析报告.pdf', 'rb'),file_name=f'钱海飞_{py}分析报告.pdf')
            elif py == '用逻辑回归预测泰坦尼克幸存情况':
                st.download_button(label="**下载清晰完整报告⏬**",data=open('用逻辑回归预测泰坦尼克号幸存情况.pdf', 'rb'),file_name=f'钱海飞_{py}分析报告.pdf')
        with cols[1]:
            st.write('👇🏼**静态预览**')
        if py == '用假设检验分析鸢尾花种类差异显著性':
            st.image('iris.jpeg',output_format='PNG')
        elif py == '可视化探索帕默群岛企鹅数据':
            st.image('penguin.jpeg',output_format='PNG')
        elif py == '用线性回归预测房屋价格':
            st.image('price_pred.jpeg',output_format='PNG')
        elif py == '用逻辑回归预测泰坦尼克幸存情况':
            st.image('titannic.jpeg',output_format='PNG')
                        
def works_sql():
    pages = [st.Page('sql.py', title="SQL")]
    st.navigation(pages).run()
        
def works_auto():
    st.write("""
                 **【项目介绍】**\n\n
                本项目旨在通过自动化流程实现每日循环切换账号，基于各个账号的凭证批量获取某商城后台数据并存储至本地。
                数据抓取至本地后系统为每个账号创建相应的同名工作表，以高效、准确地存储获取的数据，
                从而为后续的数据分析和可视化展示提供坚实的基础。
                 """)
    st.write("")
    st.write('👇🏼**以下为录制的完整自动化数据抓取过程**')
    st.video("video/自动化批量爬取网页内容.mp4")
        
def page_contact():
    columns=st.columns([2,6,2])
    with columns[1]:
        st.image('Drucker01.png',width=600)
    st.markdown('### 与我联系：')
    st.markdown('#### ☎️：13776317568')
    st.markdown('#### 📧：qhf0261120@163.com')

def main_column(page):
    if page == '#### 🧾个人概况':
        personal_info()    
    elif page == '#### 💡作品展示':
        tabs = st.tabs(('📊**Power BI作品集 |**','🤖**AI作品集 |**','🧠**机器学习作品集 |**','🐍**Python数据分析作品集 |**','🔍**SQL数据分析作品集 |**','🕷**爬虫与自动化 |**'))
        with tabs[0]:
            works_bi()    
        with tabs[1]:
            works_ai()    
        with tabs[2]:
            works_ml()    
        with tabs[3]:
            works_py()    
        with tabs[4]:
            works_sql()    
        with tabs[5]:
            works_auto()    
    else:
        page_contact()
                
def run_app():
    page_config()
    page = side_column()
    main_column(page)
    
if __name__ == '__main__':
    run_app()