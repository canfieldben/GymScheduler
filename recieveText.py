from flask import Flask, request
import twilio.twiml.messaging_response

app = Flask(__name__)
time_list = ['0', '1', '630', '830', '1030', '1230', '1430', '1630', '1830', '2030', '600', '830', '1000', '1200',
             '1400', '1600', '1800', '2000']


@app.route("/sms", methods=['POST'])
def sms():
    final_string = ""
    new_file = ""
    number = request.form['From']
    message_body = (request.form["Body"]).strip()
    user_dict = {"+19786976468": "Ben", "+19785016565": "Jason", "+15857032164": "Riley", "+19086446949": "Evan",
                 "+19545407256": "Deva", "+13108003467": "Zack", "+13472573331": "Alexis"}

    if number in user_dict.keys():
        number = user_dict.get(number)

    for time in time_list:
        if time == message_body:
            if message_body == "1":
                new_message_body = message_body
                resp = twilio.twiml.messaging_response.MessagingResponse()
                resp.message(
                    'Hello {}, you have opted out of the gym.\n\nTo request a slot, submit your time\n\nSalty Inc™'.format(
                        number))
            elif message_body == '0':
                new_message_body = message_body
                resp = twilio.twiml.messaging_response.MessagingResponse()
                resp.message(
                    'Hello {}, you have submitted a testing value.\n\nThis value is for BEN only!\n\nSalty Inc™'.format(
                        number))
            else:
                new_message_body = str(int(message_body) - 600)
                if len(message_body) == 3:
                    message_body = "{}:{}{}".format(message_body[0], message_body[1], message_body[2])
                else:
                    message_body = "{}{}:{}{}".format(message_body[0], message_body[1], message_body[2],
                                                      message_body[3])
                if len(new_message_body) == 3:
                    new_message_body = "0" + new_message_body
                if len(new_message_body) == 2:
                    new_message_body = "00" + new_message_body
                if len(new_message_body) == 0:
                    new_message_body = "0000"

                resp = twilio.twiml.messaging_response.MessagingResponse()
                resp.message(
                    'Hello {}, {} has been submitted as your time.\n\nIf you would like to remove your time, submit "1"\n\nSalty Inc™'.format(
                        number, message_body))

            with open("restricted.txt") as file:
                users = file.readlines()
                for i in users:
                    i.strip()
                    words = i.split(" ")

                    if words[0] == number:
                        words[3] = new_message_body

                        for f in words:
                            final_string += f + " "
                        i = final_string.rstrip() + '\n'
                    new_file += i
            print('{} has changed their time to {}'.format(number, message_body))
            file = open("restricted.txt", "w")
            file.write(new_file)

            return str(resp)

    resp = twilio.twiml.messaging_response.MessagingResponse()
    resp.message('*Action Needed*\n\nYou have not submitted a proper time, try again\n\nSalty Inc™')
    return str(resp)


if __name__ == '__main__':
    app.run()
