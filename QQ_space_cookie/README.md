qq空间cookie登陆的两种方式

    1、requests.get(url,headers) 其中cookie在headers头文件中，每次请求都要带上headers
    2、s=request.session() s.cookies[‘xxxxx’] = “cookie的值”，每次请求不用再带上headers,直接get就好
