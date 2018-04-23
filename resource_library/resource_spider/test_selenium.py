
# 导入webdriver
from selenium import webdriver
import time

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS()
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com/')
driver.set_window_size(1366, 768)

# 如果没有在环境变量指定PhantomJS位置
# driver = webdriver.PhantomJS(executable_path = "./phantomjs")

# get方法会一直等到页面加载，然后才会继续程序，通常测试会在这里选择time.sleep(2)

driver.get("http://www.baidu.com/")

#获取页面名为wraper的id标签的文本内容
data = driver.find_element_by_id('wrapper').text

#打印数据内容
print(data)

print(driver.title)

#生成页面快照并保存
driver.save_screenshot("baidu.png")

# id="kw"是百度搜索输入框，输入字符串"长城"
driver.find_element_by_id('kw').send_keys(u'长城')

# id="su"是百度搜索按钮，click()是模拟点击
driver.find_element_by_id('su').click()

#获取新的页面快照
driver.save_screenshot("长城.png")

#打印网页渲染后的源代码
print(driver.page_source)

#获取当前页面Cookie
print(driver.get_cookies())

#ctrl+a全选输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
#ctrl+x剪切输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

#输入框重新输入内容
driver.find_element_by_id('kw').send_keys('itcast')

#模拟Enter回车键
driver.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(5)

#清空输入框内容
driver.find_element_by_id('kw').clear()

#生成新的页面快照
driver.save_screenshot('itcast.png')

#获取当前url
print(driver.current_url)

driver.quit()

'''
定位UI元素(WebElements)
    关于元素的选取，有如下的API单个元素选取
    from selenium.webdriver.common.by import By
    find_element_by_id
    find_element_by_name
    find_element_by_xpath
    find_element_by_link_text
    find_element_by_partial_link_text
    find_eelement_by_tag_name
    find_element_by_class_name
    find_element_by_css_selector
    
    from selenium.webdriver.common.by import By
    1. By ID
    element = driver.find_element_by_id("coolesWidgetEvah")
    element = driver.find_element(by=By.ID, value="coolesWidgetEvah")
    2. By Class Name
    cheese = driver.find_element_by_class_name('cheese')
    cheese = driver.find_elements(By.CLASS_NAME, "cheese")
    3. By Tag Name
    frame = driver.find_element_by_tag_name("iframe")
    frame = driver.find_element(By.TAG_NAME, "iframe")
    4.By Name
    cheese = driver.find_element_by_name("cheese")
    cheese = driver.find_element(By.NAME, "cheese")
    5. By Link Text
    cheese = driver.find_element_by_link_text("cheese")
    cheese = driver.find_element(By.LINK_TEXT, "cheese")
    6.By Partial Link Text
    cheese = driver.find_element_by_partial_link_text("cheese")
    cheese = driver.find_element(By.PARTIAL_LINK_TEXT, "cheese")
    6.By CSS
    cheese = driver.find_element_by_css_selector("#food span.dairy.aged")
    cheese = driver.find_element(By.CSS_SELECTOR, "#food span.dairy.aged")
    7.By XPath
    inputs = driver.find_elements_by_xpath("input")
    inputs = driver.find_elements(By.XPATH, "//input")
'''

'''
鼠标动作链
    #导入ActionChains类
    from selenium.webdrive import ActionChains
    
    #鼠标移动到ac位置
    ac = driver.find_elenemt_by_xpath('element')
    ActionChains(driver).move_to_element(ac).perform()
    
    #在ac位置单击
    ac = driver.find_element_by_xpath('elementA')
    ActionChains(driver).move_to_element(ac).click(ac).perform()
    
    #在ac位置双击
    ac = driver.find_element_by_xpath("elementB")
    ActionChains(driver).move_to_element(ac).double_click(ac).perform()
    
    #在ac位置右击
    ac = driver.find_element_by_xpath('elementC')
    ActionChains(driver).move_to_element(ac).context_click(ac).perform()
    
    #在ac位置左键单击hold住
    ac = driver.find_element_by_xpath('elementF')
    ActionChains(driver).move_to_element(ac).click_and_hold(ac).perform()
    
    #将ac1拖拽到ac2位置
    ac1 = driver.find_element_by_xpath('elementD')
    ac2 = driver.find_element_by_xpath('elementE')
    ActionChains(driver).drag_and_drop(ac1, ac2).perform()
'''

'''
填充表单
我们已经知道了怎样向文本框输入文字，但是有时候我们会碰到<select></select>标签的下拉框。直接点击下拉框中的选项不一定可行。
Selenium专门提供了Select类来处理下拉框。其实WebDriver中提供了一个叫Select的方法，可以帮助我们完成这些事情：
    #导入Select类
    from selenium.webdriver.support.ui import Select
    
    #找到name的选项卡
    select = Select(driver.find_element_by_name('status'))
    
    #s
    select.select_by_index(1)
    select.select_by_value("0")
    select.select_by_visible_text(u'未审核')
    以上是三种选择下拉框的方式，它可以根据索引来选择，可以根据值来选择，可以根据文字来选择。注意：
    
    index索引从0开始
    value是option标签的一个属性值，并不是显示在下拉框中的值
    visible_text实在option标签文本的值，是显示在下拉框的值
    
    全部取消选择怎么办呢？很简单：
    select.deselect_all()
'''

'''
弹窗处理
    alert = driver.switch_to_alert()
'''

'''
页面切换
一个浏览器肯定会有很多窗口，所以我们肯定要有方法来实现窗口的切换，切换窗口的方法如下：
    driver.switch_to_window('this is window name')
也可以使用window_handles方法来获取每个窗口的操作对象。例如：
    for handle in driver.window_handles:
    driver.switch_to_window(handle)
'''

'''
页面的前进和后退
    driver.forward()  #前进
    driver.back()    #后退
'''

'''
Cookies
获取页面每个Cookies值，用法如下：

    for cookie in driver.get_cookies():
        print("%s -> %s"%(cookie['name'], cookie['value']))

删除Cookies,用法如下：

    #By name
    driver.delete_cookie('CookieName')

    #all
    driver.delete_all_cookies()
'''

'''
页面等待
注意：这是非常重要的一部分！
现在的网页原来越多采用了Ajax技术，这样程序变不能确定何时某个元素完全加载出来了。如果实际页面等待事件过长导出某个dom元素还没出来，
但是你的代码直接使用了这个WebElement，那么就会抛出NullPointer的异常。
为了避免这种元素定位困难而且会提高产生ElementNotVisibleException的概率。所以Selenium提供了两种等待方式，一种是隐式等待，一种是显式等待。
隐式等待就是等待特定的时间，显示等待是指定某一条件知道这个条件成立时继续执行。

显式等待
显示等待指定了某个条件，然后设置最长等待事件。如果在这个时间还找到没有元素，那么便会抛出异常。
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    
    #WebDriverWait库，负责循环等待
    from selenium.webdriver.support.ui import WebDriverWait
    #expected_conditions类，负责条件触发
    from selenium.webdriver.support import expected_conditions as EC
    
    driver = webdriver.Chrome()
    
    driver.get("http://www.xxxx.com/loading")
    
    try:
        #页面一直循环，知道id="myDynamicElement"出现
        element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "myDynamicElement"))
            )
    finally:
        driver.quit()    
        
如果不写参数，程序默认会0.5s调用一次来来查看安苏是否已经生成，如果本来元素时存在的，那么会立即返回。

下面是一些内置的等待条件，你可以直接调用这些条件，而不用自己写某些等待条件了。
    title_is
    title_contains
    presence_of_element_located
    visibility_of_element_located
    visibility_of
    presence_of_all_elements_located
    text_to_be_present_in_element
    text_to_be_present_in_element_value
    frame_to_be_available_and_switch_to_it
    invisibility_of_element_located
    element_to_be_clickable - it is Displayed and Enabled
    staleness_of
    element_to_be_selected
    element_located_to_be_selected
    element_selection_state_to_be
    element_located_selection_state_to_be
    aert_is_present
    
隐式等待

隐式等待比较简单，就是简单地设置一个等待时间，单位为秒。
    from selenium import webdriver
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  #seconds
    
    driver.get("http://www.xxxxx.com/loading")
    
    myDynamicElement = driver.find_element_by_id("myDynamicElement")
'''