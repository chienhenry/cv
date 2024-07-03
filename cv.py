import streamlit as st 

st.set_page_config(page_title='钱海飞的简历',page_icon='📚',layout='wide',initial_sidebar_state='auto')

with st.sidebar:
    st.logo(image='pic.jpg',link='https://henrychien.streamlit.app/')
    page = st.radio('#### 导航栏',('#### 🧾个人概况','#### 💡作品展示','#### :email:联系方式'))
    st.container(height=320,border=False)
    st.divider()
    st.download_button(label='⏬下载简历',data=open('用线性回归预测房价分析报告.pdf', 'rb'),file_name='钱海飞的简历.pdf',mime='application/pdf')
if page == '#### 🧾个人概况':
    left_column, right_column = st.columns([8,2])
    with left_column:
        st.write("#### <center>钱 海 飞</center>",unsafe_allow_html=True)
        mail_text = 'qhf0261120@163.com'
        st.write('<center>男 | 13776317568 | qhf0261120@163.com | 本科</center>',unsafe_allow_html=True)
        st.write('<center>求职意向：Python开发工程师</center>',unsafe_allow_html=True)
        
    with right_column:
        st.image('pic.jpg', width=120,output_format='PNG')
        
    st.write("##### 🛠️专业技能")
    st.write("**数据挖掘**：数据获取、数据合并、数据清洗、数据建模、数据可视化")
    st.write("**数据分析**：假设检验、回归分析、业务诊断、异动分析、业务预测")
    st.write("**掌握工具**：Python、SQL、PowerBI、PowerQuery、DAX、M、PowerApps、RPA")
    st.divider()
    
    st.write("##### 💼工作经历")
    columns = st.columns([5,2,3])
    with columns[0]:
        st.write("**江苏弘帆供应链管理有限公司**")    
    with columns[1]:
        st.write("运营总监") 
    with columns[2]:
        st.write("2020.08 - 至今")    
    st.write("""
             - **团队管理：** 负责公司内部的工作流程、团队建设、沟通协调等工作。
             - **项目管理：** 负责公司内部的项目管理、进度控制、资源协调等工作。
             """)
    st.write('')
    columns = st.columns([5,2,3])
    with columns[0]:
        st.write("**苏州工业园区顺丰速运有限公司**")    
    with columns[1]:
        st.write("经营分部负责人") 
    with columns[2]:
        st.write("2015.06 - 2020.07")    
    st.write("""
             - **团队管理：** 负责公司内部的工作流程、团队建设、沟通协调等工作。
             - **项目管理：** 负责公司内部的项目管理、进度控制、资源协调等工作。
             """)
    st.divider()
    
    st.write("##### 📋项目经历")
    st.write('- 熟练掌握Python语言，有良好的编程习惯，能够编写高效、可读性强的代码。')
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

elif page == '#### 💡作品展示':
    tabs = st.tabs(('📊**Power BI作品集 |**','🤖**AI作品集 |**','🧠**机器学习作品集 |**','🐍**Python数据分析作品集 |**','🔍**SQL数据分析作品集 |**'))
    with tabs[0]:
        columns = st.columns([2,8])
        with columns[0]:
            bi = st.radio('👀**查看作品**',['PowerBI销售业务分析报告','PowerBI人力资源分析报告','PowerBI财务报表分析报告'],label_visibility='hidden')
        with columns[1]:
            cols = st.columns((8,2))    
            with cols[0]:
                if bi == 'PowerBI销售业务分析报告':
                    st.write('🔗[**交互查看**](https://www.baidu.com)')
                elif bi == 'PowerBI人力资源分析报告':
                    st.write('🔗[**交互查看**](https://www.baidu.com)')
                elif bi == 'PowerBI财务报表分析报告':
                    st.write('🔗[**交互查看**](https://www.baidu.com)')
            with cols[1]:
                st.write('👇🏼**静态预览**')
            if bi == 'PowerBI销售业务分析报告':
                st.image('QR/baidu.png',output_format='PNG')
            elif bi == 'PowerBI人力资源分析报告':
                st.image('QR/baidu.png',output_format='PNG')
            elif bi == 'PowerBI财务报表分析报告':
                st.image('QR/baidu.png',output_format='PNG')
    with tabs[1]:
        columns = st.columns([2,8])
        with columns[0]:
            ai = st.radio('👀**查看作品**',
                          ['视频脚本一键生成器','爆款小红书文案生成器','克隆ChatGPT','智能PDF问答工具','CSV数据分析智能工具'],label_visibility='hidden')
        with columns[1]:
            cols = st.columns((8,2))    
            with cols[0]:
                if ai == '视频脚本一键生成器':
                    st.link_button(label='**🔗交互查看**',url='https://aiagent01.streamlit.app/%E8%A7%86%E9%A2%91%E8%84%9A%E6%9C%AC%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90%E5%99%A8')
                    # st.write('🔗[**交互查看**](https://aiagent01.streamlit.app/%E8%A7%86%E9%A2%91%E8%84%9A%E6%9C%AC%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90%E5%99%A8)')
                elif ai == '爆款小红书文案生成器':
                    st.link_button(label='**🔗交互查看**',url='https://aiagent01.streamlit.app/%E7%88%86%E6%AC%BE%E5%B0%8F%E7%BA%A2%E4%B9%A6%E6%96%87%E6%A1%88%E7%94%9F%E6%88%90%E5%99%A8')
                    # st.write('🔗[**交互查看**](https://aiagent01.streamlit.app/%E7%88%86%E6%AC%BE%E5%B0%8F%E7%BA%A2%E4%B9%A6%E6%96%87%E6%A1%88%E7%94%9F%E6%88%90%E5%99%A8)')
                elif ai == '克隆ChatGPT':
                    st.link_button(label='**🔗交互查看**',url='https://aiagent01.streamlit.app/%E5%85%8B%E9%9A%86ChatGPT')
                    # st.write('🔗[**交互查看**](https://aiagent01.streamlit.app/%E5%85%8B%E9%9A%86ChatGPT)')              
                elif ai == '智能PDF问答工具':
                    st.link_button(label='**🔗交互查看**',url='https://aiagent01.streamlit.app/%E6%99%BA%E8%83%BDPDF%E9%97%AE%E7%AD%94%E5%B7%A5%E5%85%B7')
                    # st.write('🔗[**交互查看**](https://aiagent01.streamlit.app/%E6%99%BA%E8%83%BDPDF%E9%97%AE%E7%AD%94%E5%B7%A5%E5%85%B7)')
                elif ai == 'CSV数据分析智能工具':
                    st.link_button(label='**🔗交互查看**',url='https://aiagent01.streamlit.app/')
                    # st.write('🔗[**交互查看**](https://aiagent01.streamlit.app/)')       
            with cols[1]:
                st.write('👇🏼**静态预览**')
            if ai == '视频脚本一键生成器':
                st.image('video_script.png',output_format='PNG')
            elif ai == '爆款小红书文案生成器':
                st.image('xhs.png',output_format='PNG')
            elif ai == '克隆ChatGPT':
                st.image('clone_gpt.png',output_format='PNG')        
            elif ai == '智能PDF问答工具':
                st.image('xhs.png',output_format='PNG')
            elif ai == 'CSV数据分析智能工具':
                st.image('csv.png',output_format='PNG')             
    with tabs[2]:
        columns = st.columns([2,8])
        with columns[0]:
            ml = st.radio('👀**查看作品**',['随机森林分类器','随机森林回归器','销售数据仪表板'],label_visibility='hidden')
        with columns[1]:
            cols = st.columns((8,2))    
            with cols[0]:
                if ml == '随机森林分类器':
                    st.link_button(label='**🔗交互查看**',url='https://randomforestclassifier01.streamlit.app/')
                    # st.write('🔗[**交互查看**](https://randomforestclassifier01.streamlit.app/)')
                elif ml == '随机森林回归器':
                    st.link_button(label='**🔗交互查看**',url='https://insurancepred.streamlit.app/')
                    # st.write('🔗[**交互查看**](https://insurancepred.streamlit.app/)')
                elif ml == '销售数据仪表板':
                    st.link_button(label='**🔗交互查看**',url='https://dashborad.streamlit.app/')
                    # st.write('🔗[**交互查看**](https://dashborad.streamlit.app/)')
            with cols[1]:
                st.write('👇🏼**静态预览**')
            if ml == '随机森林分类器':
                st.image('penguin01.png',output_format='PNG')
                st.image('penguin02.png',output_format='PNG')
            elif ml == '随机森林回归器':
                st.image('insurance01.png',output_format='PNG')
                st.image('insurance02.png',output_format='PNG')
            elif ml == '销售数据仪表板':
                st.image('dashboard.png',output_format='PNG')
    with tabs[3]:
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
    with tabs[4]:
        # columns = st.columns([2,8])
        # with columns[0]:
        #     sql = st.radio('👀**查看作品**',['作品D','作品E','作品F'],label_visibility='hidden')
        # with columns[1]:
        #     cols = st.columns((8,2))    
        #     with cols[0]:
        #         if sql == '作品D':
        #             st.download_button(label="**下载完整报告⏬**",data=open('pic.pdf', 'rb'),file_name=f'钱海飞_{sql}.pdf')
        #         elif sql == '作品E':
        #             st.download_button(label="**下载完整报告⏬**",data=open('pic.pdf', 'rb'),file_name=f'钱海飞_{sql}.pdf')
        #         elif sql == '作品F':
        #             st.download_button(label="**下载完整报告⏬**",data=open('pic.pdf', 'rb'),file_name=f'钱海飞_{sql}.pdf')
        #     with cols[1]:
        #         st.write('👇🏼**静态预览**')
        #     if sql == '作品D':
        #         st.image('QR/baidu.png',output_format='PNG')
        #     elif sql == '作品E':
        #         st.image('QR/baidu.png',output_format='PNG')
        #     elif sql == '作品F':
        #         st.image('QR/baidu.png',output_format='PNG')
        # st.page_link(page = 'pages/sql.py',label = '中',icon = '🀄️')
        # pages = [
        #     # "Your account" : [
        #         st.Page("cv.py", title="Create your account"),
        #         st.Page("sql.py", title="Manage your account")
        #     # ]
        #     # "Resources" : [
        #     #     st.Page("cv.py", title="Learn about us"),
        #     #     st.Page("sql.py", title="Try it out")
        #     # ]
        # ]
        # pg = st.navigation(pages)
        # pg.run()
        pages = [st.Page('sql.py', title="SQL")]
        st.navigation(pages).run()
        
else:
    # st.empty().container(height = 150,border = False)
    # with st.container(height = 500,border = False):
    columns=st.columns([2,6,2])
    # with columns[0]:
    #     st.image('Drucker01.png',width=600)
    with columns[1]:
        st.image('Drucker01.png',width=600)
        # st.markdown('### <center>💬唯有知识，让我们免于平庸！</center>',unsafe_allow_html=True)
    st.markdown('### 与我联系：')
    st.markdown('#### ☎️：13776317568')
    st.markdown('#### 📧：qhf0261120@163.com')