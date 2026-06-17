# The Suspicious Email
# hello this is Libans simple cyber threat game !

image bedroom = im.Scale("bedroom.jpg", 1920, 1080)
image train = im.Scale("train.jpg", 1920, 1080)
image night = im.Scale("night.jpg", 1920, 1080)



label start:

    $ security_score = 0

    scene bedroom

    "The Suspicious Email"

    "You are a university student currently studying for your end-of-year assessments."

    "It is a normal Monday morning and you have just woken up in your accommodation."

    "You decide to make Frosted Cereals as you check your phone before beginning your studies."

    "As you scroll through your notifications, you notice a new email from what appears to be your university's IT department."

    "The email claims that unusual activity has been detected on your student account and that immediate action is required."

    "The message contains a link and warns that failure to act within the next 24 hours may result in your account being suspended."

    "You hesitate for a moment. Your heart begins to pound."

    "The email looks convincing, but something feels unusual about it."

    menu:

        "What should you do?"

        "Click the link immediately and log in.":
            "You click the link and enter your student login details."
            "The website looked real, but you later realise it was a fake login page."
            $ security_score += 0

        "Check the sender's email address and contact university IT.":
            "You inspect the email address carefully and notice it does not look official."
            "You contact the university IT department directly and report the suspicious message."
            $ security_score += 2

        "Ignore the email completely.":
            "You decide not to interact with the email."
            "This prevents you from entering details, but you also miss the chance to report the threat."
            $ security_score += 1

    scene train

    "Later that afternoon, whilst travelling home, your phone vibrates with a text message."

    "The message claims to be from your bank and states that a payment has been blocked due to suspicious activity."

    "The text includes a link and asks you to verify your details immediately."

    "The message creates a sense of urgency."

    "If the message is genuine, ignoring it could cause problems."

    "However, if it is fraudulent, providing personal information could place your account at risk."

    menu:

        "What should you do?"

        "Click the link and enter your banking details.":
            "You click the link and enter your information."
            "The page looked similar to your bank, but it was actually controlled by cyber criminals."
            $ security_score += 0

        "Open your banking app directly and check your account.":
            "You avoid the link and open your banking app directly."
            "There are no warnings or blocked payments, so you realise the text was likely a scam."
            $ security_score += 2

        "Delete the text message immediately.":
            "You delete the message without clicking the link."
            "This protects you from the scam, but you do not investigate whether your bank account is actually affected."
            $ security_score += 1

    scene night

    "That evening, you receive a phone call from an unknown number."

    "The caller claims to work for a cyber security team and explains that your personal information may have been exposed in a recent data breach."

    "They ask several questions and request that you verify your identity to secure your account."

    "The caller sounds professional and confident."

    "They appear to know basic information about you, making the situation seem believable."

    "You must now decide whether you trust the caller or whether additional verification is required."

    menu:

        "What should you do?"

        "Provide the requested information.":
            "You provide personal information to the caller."
            "The caller thanks you and ends the call quickly."
            "Later, you realise the call may have been part of a social engineering attack."
            $ security_score += 0

        "End the call and contact the organisation through its official website.":
            "You end the call and search for the organisation's official contact details."
            "After checking directly, you discover that no cyber security team had contacted you."
            $ security_score += 2

        "Question the caller for more information.":
            "You ask the caller questions and become more suspicious of their answers."
            "Eventually you end the call, but you are still unsure whether it was genuine."
            $ security_score += 1


    "Your decisions throughout the day have now shaped the outcome."

    if security_score >= 5:
        jump secure_ending

    elif security_score >= 3:
        jump neutral_ending

    else:
        jump compromised_ending


label secure_ending:

    scene black

    "Secure Ending"

    "You handled the suspicious messages carefully and avoided giving away sensitive information."

    "By checking official sources, avoiding suspicious links and questioning unusual requests, you protected your accounts."

    "You also reported the phishing attempt, helping prevent other students from becoming victims."

    "Your cyber security awareness helped you stay safe."

    return


label neutral_ending:

    scene black

    "Neutral Ending"

    "You avoided the most dangerous mistakes, but you did not always take the safest action."

    "Some suspicious messages were ignored instead of being properly reported or verified."

    "Your accounts remained safe, but the situation showed that cyber security requires active awareness."

    "Next time, checking official sources and reporting threats would provide stronger protection."

    return


label compromised_ending:

    scene black

    "Compromised Ending"

    "Unfortunately, you trusted the suspicious messages too quickly."

    "By clicking unsafe links or sharing information, you allowed cyber criminals to access sensitive details."

    "You now need to change your passwords, contact your bank and report the incident to the university IT department."

    "This experience shows how phishing and social engineering can manipulate people through fear, urgency and trust."

    return