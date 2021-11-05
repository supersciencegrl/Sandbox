import pymsteams

webhook = r"https://syngenta.webhook.office.com/webhookb2/c198a158-9e58-4a3d-b9ed-746cb4fadfbd@06219a4a-a835-44d5-afaf-3926343bfb89/IncomingWebhook/2dc314fc05fc4d34bebc1e229991afbb/894ff72d-5ee9-4a9b-82b8-5996a7f82d79"

section1 = pymsteams.cardsection()
section1.title('Introduction')
section1.text('Introductory text')

section2 = pymsteams.cardsection()
section2.title('Development')
section2.activityTitle('Activity title')
section2.activitySubtitle('Activity subtitle')
section2.activityText('Activity text')
section2.addFact('Name', 'Nessa')
section2.addFact('Username', 'S1024501')

message = pymsteams.connectorcard(webhook)
message.text('Test card with activity and facts')
message.color('f731bc')

message.addSection(section1)
message.addSection(section2)
#message.printme()
message.send()
