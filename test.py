d = "docker run -p 6379:6379 -d redis:5"
  # {% for message in messages %}
  #       {% for i in message %}
  #           {{i.date}} <br>
  #           {{i.message}}<br>
  #       {% endfor %}
  #   {% endfor %}
 # ses_date = []
    # for ses_dates in Number.objects.filter(number=room_name).values('session', 'date'):
    #     ses_date.append(ses_dates)
    # collection_ses = []
    # collection_ses_ans_date = []
    # for i in ses_date:
    #     key = i.get('session')
    #     if key not in collection_ses:
    #         collection_ses.append(key)
    #         collection_ses_ans_date.append(i)
    # total = []
    # for i in collection_ses_ans_date:
    #     ses = i.get('session')
    #     dt = i.get('date')
    #     # получаем последнее сообщение nm
    #     qset = Number.objects.filter(date=dt, session=ses).values('message', 'session', 'date').order_by('-date')
    #     total.append(qset)
    # to_send = total[-1]
    # for i in to_send:
    #     message_to_send = i.get('message')
    # send_telegram(message_to_send)
