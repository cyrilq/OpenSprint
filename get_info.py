import requests
import json

class GetInfo:

    inn = ''

    def __init__(self, inn):

        self.inn = inn
        print(inn)

    def getInfo(self):

        answer = {}
        media_name = ''

        req = requests.get('http://openngo.ru/api/organizations/?inn='+self.inn)
        req = json.loads(req.text)
        print(req)



        if req['count'] == 0:
            answer['wrongINN'] = True
            return answer
        else:
            answer['wrongINN'] = False
            answer['cartNKO'] = 'https://openngo.ru/organization/' + req['results'][0]['ogrn']
            answer['nameNKO'] = req['results'][0]['name']
            answer['INN'] = req['results'][0]['inn']
            answer['OGRN'] = req['results'][0]['ogrn']
            answer['active'] = req['results'][0]['active']
            answer['type'] = req['results'][0]['type']['name']
            answer['region'] = req['results'][0]['region']['name']
            answer['Contract'] = req['results'][0]['money_transfers_sum_by_type']['Contract']
            answer['Grant'] = req['results'][0]['money_transfers_sum_by_type']['Grant']
            answer['Subsidy'] = req['results'][0]['money_transfers_sum_by_type']['Subsidy']



        req_smi = requests.get('http://openmassmedia.ru/api/founders/?inn='+ self.inn)
        req_smi = json.loads(req_smi.text)

        print(req_smi)

        if req_smi['count'] == 0:
            answer['haveMedia'] = False
            return answer
        else:
            answer['haveMedia'] = True
            media_name = req_smi['results'][0]['media'][0]['name']
            answer['mediaName'] = media_name
            req_media = 'https://openmassmedia.ru/api/media/?string_search=' + media_name.lower().replace(' ', '+')

            req_media = requests.get(req_media)
            print(req_media)
            req_media = json.loads(req_media.text)

            answer['territory'] = req_media['results'][0]['territory']
            answer['languages'] = req_media['results'][0]['languages']
            answer['formOutput'] = req_media['results'][0]['type']['name']
            answer['SMIcart'] = 'https://openmassmedia.ru/media/' + req_media['results'][0]['reg_num_id']
            answer['web'] = req_smi['results'][0]['media'][0]['website']
            answer['money_transfers_sum'] = req_media['results'][0]['founders'][0]['money_transfers_sum']

        return answer




if __name__ == '__main__':
    getInfo = GetInfo('7607020804')
    print(getInfo.getInfo())
    del getInfo

    getInfo = GetInfo('123')
    print(getInfo.getInfo())
