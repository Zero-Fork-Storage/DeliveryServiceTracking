import json
from dst_status import DST_LEVEL, DST_CompleteYN
from dst_main import Get


class Template_Gen:
    def __init__(self, code, dst_code):
        self.json_data = Get.lookup(dst_company_code=code, dst_waybill_number=dst_code)

    def generate(self):
        # print(self.json_data)
        """
        Generate
        ---------

        DST Template Generation :
            1 | DST_Status :
                배송 완료 여부(true or false)

            2 | DST_invoiceNo :
                운송장 번호

            3 | DST_itemName :
                상품 이름

            4 | DST_level :
                진행단계 [level 1: 배송준비중, 2: 집화완료, 3: 배송중, 4: 지점 도착, 5: 배송출발, 6:배송 완료]

            5 | DST_receiverName :
                받는 사람

            6 | DST_receiverAddr :
                받는 사람 주소

            7 | DST_result :
                조회 결과

            8 | DST_trackingDetails :

            9 | DST_estimate :
                배송예정 시간
        """
        try:
            DST_Status = self.json_data['completeYN']
            DST_invoiceNo = self.json_data['invoiceNo']
            DST_itemName = self.json_data['itemName']

            DST_level = self.json_data['level']

            DST_receiverName = self.json_data['receiverName']
            DST_receiverAddr = self.json_data['receiverAddr']

            DST_trackingDetails = self.json_data['trackingDetails']
            DST_estimate = self.json_data['estimate']
            """
            진행단계 [level 1: 배송준비중, 2: 집화완료, 3: 배송중, 4: 지점 도착, 5: 배송출발, 6:배송 완료]
            """
            X = DST_LEVEL(x=DST_level)
            Y = DST_CompleteYN(y=DST_Status)
            # return [DST_Status, DST_invoiceNo, DST_itemName, DST_level, DST_receiverName, DST_receiverAddr, DST_result, DST_trackingDetails, DST_estimate]
            DST_Td = DST_trackingDetails[len(DST_trackingDetails) - 1]
            DST_timeString = DST_Td['timeString']
            DST_telno = DST_Td['telno']
            DST_telno2 = DST_Td['telno2']
            DST_manName = DST_Td['manName']
            DST_where = DST_Td['where']
            # DST_kind = DST_Td['kind']

            return {
                '송장번호': DST_invoiceNo,
                '배송여부': Y,
                '배송상황': X,
                'INFO': {
                    '상품명': DST_itemName,
                    '수령인': DST_receiverName,
                    '주소': DST_receiverAddr,
                    '배송소요시간': DST_estimate,
                    '세부정보': {
                        "진행시간": DST_timeString,
                        "지점전화번호": DST_telno,
                        "배송기사이름": DST_manName,
                        "배송기사전화번호": DST_telno2,
                        "진행위치지점": DST_where
                    }
                }
            }

        except KeyError as e:
            null = e
            return {
                'Error': 'System Error'
            }

# _insted = Template_Gen()
#  print(json.dumps(_insted.generate(), indent=4, ensure_ascii=False))
