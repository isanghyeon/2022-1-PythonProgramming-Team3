class CustomizeResponse:
    def __init__(self):
        self.Success_returnData = {
            "status": "",
            "message": "Success"
        }
        self.Failed_returnData = {
            "status": "",
            "message": "Failed"
        }

    def return_post_http_status_message(self, Type=bool):
        if Type is True:
            self.Success_returnData["status"] = "201"
            return self.Success_returnData, 201

        if Type is False:
            self.Failed_returnData["status"] = "500"
            return self.Failed_returnData, 500

    def return_patch_http_status_message(self, Type=bool):
        if Type is True:
            self.Success_returnData["status"] = "200"
            return self.Success_returnData, 200

        if Type is False:
            self.Failed_returnData["status"] = "500"
            return self.Failed_returnData, 500
