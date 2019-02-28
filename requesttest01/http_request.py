import requests
#写这个类的目的： 完成接口测试
class HttpRequest:

    def http_request(self,url,request_data,method):

        if method.lower()=='get':
            try:
                response=requests.get(url,request_data)
            except Exception as e:
                print("get报错了:{0}".format(e))
                raise e
        elif method.lower()=='post':
            try:
                response=requests.post(url,request_data)
            except Exception as e:
                print("post报错了： {0}".format(e))
                raise e
        else:
            print("请求方式错误")
        return response.json()

if __name__ == '__main__':
    run = HttpRequest()
    url = 'https://www.ketangpai.com/UserApi/login'
    request_data = {"email":"17718567797","password":"123456","remember":"0"}
    # method = 'post'
    res=run.http_request(url,request_data,'Post')
    print(res)



