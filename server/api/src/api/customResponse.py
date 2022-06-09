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

    def return_get_http_status_message(self, Type=bool, data=None):
        if Type is True:
            self.Success_returnData["status"] = "200"
            self.Success_returnData["message"] = data
            return self.Success_returnData, 200

    def return_post_http_status_message(self, Type=bool):
        if Type is True:
            self.Success_returnData["status"] = "201"
            return self.Success_returnData, 201

        if Type is False:
            self.Failed_returnData["status"] = "500"
            return self.Failed_returnData, 404

    def return_patch_http_status_message(self, Type=bool):
        if Type is True:
            self.Success_returnData["status"] = "200"
            return self.Success_returnData, 200

        if Type is False:
            self.Failed_returnData["status"] = "500"
            return self.Failed_returnData, 404

    def return_delete_http_status_message(self, Type=bool):
        if Type is True:
            self.Success_returnData["status"] = "200"
            return self.Success_returnData, 200

        if Type is False:
            self.Failed_returnData["status"] = "404"
            return self.Failed_returnData, 404
