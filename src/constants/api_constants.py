#All URLs

class APIConstants(object):


    @staticmethod
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    @staticmethod
    def url_put_patch(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
