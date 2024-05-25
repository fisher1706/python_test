import random
from datetime import datetime

"""
Что такое подтверждение/запрос на изменение заказа на поставку EDI 865?
EDI 865 — это электронный документ, отправляемый поставщиком в ответ на заказ на поставку EDI 860 своим торговым 
партнерам. Этот документ используется для информирования покупателя о том, были ли изменения в первоначальном заказе 
приняты или отклонены продавцом. Помимо этого, он также используется для сообщения об изменениях, 
внесенных поставщиком в первоначальный заказ.

Преимущества использования EDI 865
Это позволяет поставщикам эффективно и оперативно информировать клиентов о предстоящих поставках. 
Этот метод обеспечивает точность за счет извлечения данных непосредственно из заказа и других отгрузочных документов. 
ASN помогают поставщикам оптимизировать общение с партнерами и вести электронный учет каждой поставки.

Розничным торговцам EDI 856 помогает отслеживать входящие запасы и облегчает планирование труда на основе ожидаемых 
поставок. Кроме того, это позволяет покупателям автоматизировать процесс получения.


EDI 865 подпадает под категорию наборов транзакций цепочки поставок X12M. Этот документ представляет собой одну из 
транзакций типичного бизнес-процесса купли-продажи, который включает в себя следующие этапы:

 - Покупатель отправляет документ заказа на поставку EDI 850 для размещения заказа.
 - Продавец подтверждает получение заказа на покупку с помощью EDI 855 «Подтверждение заказа на покупку» .
 - Покупатель сообщает о любых изменениях, необходимых в исходном заказе, 
   используя документ запроса заказа на покупку EDI 860 .
 - В свою очередь продавец сообщает о принятии или отклонении запрошенных изменений, 
   используя набор транзакций EDI 865.
   
   
   
What is an EDI 865 Purchase Order Change Acknowledgment/Request?
EDI 865 is an electronic document sent in response to an EDI 860 Purchase Order by the supplier to their trading 
partners. This document is used to inform the buyer whether the changes to the original order have been accepted or 
rejected by the seller. Besides this, it is also used to communicate the changes made to the 
original order by the supplier.

Benefits of Using an EDI 865
It enables vendors to efficiently and promptly update customers regarding upcoming deliveries. This method ensures 
accuracy by extracting data directly from the order and other shipping documents. ASNs assist suppliers in streamlining 
communication with partners and maintaining an electronic record of each shipment.

For retailers, EDI 856 aids in monitoring inbound inventory and facilitates labor planning based on expected deliveries. 
Furthermore, it allows buyers to automate the receiving process.


EDI 865 falls under the category of X12M Supply Chain transaction sets. This document represents one of the 
transactions in a typical buying and selling business process, which includes the following steps:

 - The buyer sends an EDI 850 Purchase Order document to place an order.
 - The seller confirms the receipt of a purchase order with an EDI 855 Purchase Order Acknowledgement.
 - The buyer communicates any changes required to the original order using an EDI 860 Purchase Order Request document.
 - In return, the seller communicates the acceptance or rejection of the changes requested using the 
   EDI 865 transaction set.
"""


class GenerateIDE856:

    @staticmethod
    def generate_data_edi_856_rtf(test_type):
        date = datetime.now().strftime("%y%m%d")
        isa13 = format(int(random.random() * 100)).zfill(9)
        tran_id = int(random.random() * 1000000)
        _order_id = int(random.random() * 1000000)
        amt = int(random.random() * 100)
        ref_number = int(random.random() * 100000)

        data = {
            0: f"ISA*00*          *00*          *01*047583551ANX   *01*116961628      *"
            f"{date}*0457*U*00401*{isa13}*0*P*|",
            1: "GS*SH*047583551ANX*116961628*20211102*0457*13*X*004010",
            2: "ST*856*0024",
            3: f"BSN*00*{tran_id}2021-11-02-04.36.19.72*20211102*0452*0001",
            4: "HL*1**S",
            5: "TD1*CNT*1",
            6: "TD5*B*2*SEE MEMO*D*LUT VAN 3",
            7: f"REF*CN*{tran_id}{format(amt).zfill(3)}/129609",
            8: f"REF*GV*SIQTE-000-{_order_id}-001",
            9: "REF*OQ*67951849",
            10: "DTM*011*20211102",
            11: "N1*BY*LAVAZZA PROFESSIONAL UK LTD*91*072903",
            12: "N1*ST*LAVAZZA PROFESSIONAL UK LTD*91*000",
            13: "N1*SF*EUO - LUTON OEM OPS*91*26A",
            14: "HL*2*1*O",
            15: "PRF*4900001419",
            16: "HL*3*2*I",
            17: "LIN*2*VN*ASADAN1M500944",
            18: f"SN1*2*{amt}*EA",
            19: "REF*GX*SRX185416",
            20: "CTT*3",
            21: "SE*20*0024",
            22: "GE*1*13",
            23: f"IEA*1*{isa13}",
            24: "",
        }

        if test_type == "fail":
            data.update({15: f"PR*{ref_number}"})

        filename = f"ANXEU_STOREROOM_LOGIX_EU_856_OB_19229744_{isa13}.edi"

        return filename, data


if __name__ == "__main__":
    g = GenerateIDE856()
    item = "zapel"

    name, body = g.generate_data_edi_856_rtf(item)

    print(f"name:= {name}")
    for k, v in body.items():
        print(f"{k}: {v}")
