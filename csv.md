'''
    with open(filename, mode='w') as security_details:
        writer = csv.writer(security_details, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(['rule', 'rating', 'details'])

        for rule in settings:
            print('rule_name =', rule)

            for setting in settings[rule]:
                if setting == 'default_risk':
                    risk = settings[rule][setting].split('.')
                    rating = risk[1]
                    print(setting, "=", risk[1])
                    print(rating)

                if setting == 'details':
                    if settings[rule][setting] == '':
                        continue
                    else:
                        detail = settings[rule][setting]
                        print(setting, "=", settings[rule][setting])
                        print(detail)

            print('\n')
            writer.writerow([rule, rating, detail])
