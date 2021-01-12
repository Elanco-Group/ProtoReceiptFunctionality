import os
from azure.core.exceptions import ResourceNotFoundError
from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.credentials import AzureKeyCredential


class RecognizeCustomForms(object):

    def recognize_custom_forms(self):
        path_to_sample_forms = os.path.join('receipt.pdf')
        # [START recognize_custom_forms]
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.formrecognizer import FormRecognizerClient

        endpoint = 'https://gsdp-formrecog.cognitiveservices.azure.com/'
        key = '92ef384db39347aab454901071c00685'
        model_id = 'a8428907-2ca6-4e33-8618-1e78d173c4c0'

        form_recognizer_client = FormRecognizerClient(
            endpoint=endpoint, credential=AzureKeyCredential(key)
        )

        # Make sure your form's type is included in the list of form types the custom model can recognize
        with open(path_to_sample_forms, "rb") as f:
            poller = form_recognizer_client.begin_recognize_custom_forms(
                model_id=model_id, form=f
            )
        forms = poller.result()

        for idx, form in enumerate(forms):
            print("--------Recognizing Form #{}--------".format(idx+1))
            # clinicName = receipt.fields.get("clinic name")
            #     if clinicName:
            #     print("The clinic name is: {}" .format(clinicName.value))
            print("Form has type {}".format(form.form_type))
            # print("Form has form type confidence {}".format(form.form_type_confidence))
            # print("Form was analyzed with model with ID {}".format(form.model_id))
            clinic_address = form.fields.get("clinic address")
            if clinic_address:
                print("Clinic address: {}".format(clinic_address.value))
            
            clinicName = form.fields.get("clinic name")
            if clinicName:
                print("Clinic name: {}" .format(clinicName.value))

            items = form.fields.get("item names")
            if items:
                print("\t - Item Name: {}".format(items.value))
            prices = form.fields.get("price")
            if prices:
                print("\t - Price: {}".format(prices.value))
            invoiceDate = form.fields.get("invoice date")
            if invoiceDate:
                print("\t - Invoice Date: {}".format(invoiceDate.value))
                patientName = form.fields.get("patientName")
            if patientName:
                print("\t - Patient Name: {}".format(patientName.value))
                
            microchip = form.fields.get("microchip")
            customerName = form.fields.get("customer name")
            if customerName:
                print("\t - Customer Name: {}".format(customerName.value))
                
                
            transactionNo = form.fields.get("transaction no")
            if transactionNo:
                print("Transaction number: {}".format(transactionNo.value))
            quantity = form.fields.get("quantity")
            if quantity:
                print("quantity: {}".format(quantity.value))
            # for name, field in form.fields.items():
            #     # each field is of type FormField
            #     # label_data is populated if you are using a model trained without labels,
            #     # since the service needs to make predictions for labels if not explicitly given to it.
        


            #     # if items:
            #     #     for idx, item in enumerate(form.fields.get("item names").value):
            #     #         print("\tItem #{}".format(idx+1))
            #     #         item_name = form.fields.get("item names")
            #     #         if item_name:
            #     #             print("\t - Name: {}".format(items.value))
            #     #         item_price = form.fields.get("price")
            #     #         if item_price:
            #     #             print("\t- Price: {}".format(item_price.value))
                




            #     if field.label_data:
            #         print("...Field '{}' has label '{}' with a confidence score of {}".format(
            #             name,
            #             field.label_data.text,
            #             field.confidence
            #         ))

            #     print("...Label '{}' has value '{}' with a confidence score of {}".format(
            #         field.label_data.text if field.label_data else name, field.value, field.confidence
            #     ))

            # print("-----------------------------------")
        # [END recognize_custom_forms]


if __name__ == '__main__':
    sample = RecognizeCustomForms()
    sample.recognize_custom_forms()






# key = '92ef384db39347aab454901071c00685'
# endpoint = 'https://gsdp-formrecog.cognitiveservices.azure.com/'
# model_id = "8bf5a3c1-1ecf-477b-9378-0bc068435edf"

# form_recognizer_client = FormRecognizerClient(endpoint, AzureKeyCredential(key))
# form_training_client = FormTrainingClient(endpoint, AzureKeyCredential(key))
# try:
#     print("Analyzing receipt...")
#     # Get the receipt image file
#     pdf_path = os.path.join('receipt.pdf')

#     # Submit the file data to form recognizer
#     with open(pdf_path, "rb") as f:
#         analyze_receipt = form_recognizer_client.begin_recognize_receipts(receipt=f)
    
#     # Get the results
#     receipt_data = analyze_receipt.result()
#     receipt = receipt_data[0]
#     name = receipt.fields.get("clinic name")
#     for recognized_form in receipt:
#         for name, field in recognized_form.fields.items():
#             print("Field '{}' has label '{}' with value '{}' and a confidence score of {}".format(
#             name,
#             field.label_data.text if field.label_data else name,
#             field.value,
#             field.confidence
#             ))
        




#     #for recognized_form in receipt:
#     clinicName = receipt.fields.get("clinic name")
#     if clinicName:
#         print("The clinic name is: {}" .format(clinicName.value))
#         print("The confidence is: {} \n".format(clinicName.confidence))
#     clinicAddress = receipt.fields.get("clinic address")
#     invoiceDate = receipt.fields.get("invoice date")
#     transactionNo = receipt.fields.get("transaction no")

#     if clinicAddress:
#         print("The address is: {}" .format(clinicAddress.value))
#         print("The confidence is: {} \n".format(clinicAddress.confidence))
#     if invoiceDate:
#         print("The invoice date is: {}" .format(invoiceDate.value))
#         print("The confidence is: {} \n".format(invoiceDate.confidence))
#     if transactionNo:
#         print("The transaction number is: {}" .format(transactionNo.value))
#         print("The confidence is: {} \n".format(transactionNo.confidence))
#     items = receipt.fields.get("item names")
#     if items:
#         for index, item in enumerate(receipt.fields.get("item names").value):
#             print("\n\n Item #{}" .format(index+1))
#             itemName = receipt.value.get("item names")
#             itemQuantity = receipt.value.get("quantity")
#             itemPrice = receipt.value.get("price")
#             if itemName and itemQuantity and itemPrice:
#                 print("Name: {}".format(itemName.value))
#                 print("Quantity: {}".format(itemQuantity.value)) 
#                 print("Price: {}".format(itemPrice.value))
#     total = receipt.fields.get("total")
#     if total:
#         print("The total is: {}" .format(total.value))

# except Exception as ex:
#     print('Error:', ex)