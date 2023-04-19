import sys, os
def error_message_details(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.fcode.co_filename

    error_message = f"Error occured python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"

    return error_message

class SignException(Exception):
    def __init__(self, error_messgae, error_detail):
        super().__init__(error_messgae)

        self.error_message = error_message_details(
            error_messgae, error_detail=error_detail
        )
    def __str__(self):
        return  self.error_message
