from entities.question import Question
from entities.answer import Answer

def create_database():
    """ This method creates the pool of questions"""
    question_pool = []

    """Ανακυκλώνεται το πλαστικό καλαμάκι;"""
    question_pool.append(
        Question(
            text="Ανακυκλώνεται το πλαστικό καλαμάκι;",
            fact="Ταπλαστικά καλαμάκια δεν ανακυκλώνονται λόγω μεγέθους και ποιότητας. Από τον Ιούλιο του 2021 σταματούν να διατίθενται στην αγορά",
            answers=[
                Answer(text="Nαι", points=0),
                Answer(text="Όχι", points=0, correct=True),
                Answer(text="Μόνο τα μαύρα", points=0)
            ]
        )
    )

    """Ανακυκλώνεται η συσκευασία επιδόρπιων γιαουρτιού;"""
    question_pool.append(
        Question(
            text="Ανακυκλώνεται η συσκευασία επιδόρπιων γιαουρτιού;",
            fact="Ανακυκλώνονται αφού καθαριστούν από υπολείμματα. Το αλουμινένιο σφράγισμα δεν ανακυκλώνεται!",
            answers=[
                Answer(text="Nαι", correct=True, points=0),
                Answer(text="Όχι", points=0)
            ]
        )
    )

    """Ανακυκλώνονται τα μαύρα πλαστικά συσκευασίας;"""
    question_pool.append(
        Question(
            text="Ανακυκλώνονται τα μαύρα πλαστικά συσκευασίας;",
            fact="Δεν αναγνωρίζονται από τους οπτικούς διαχωριστές στις μονάδες ανακύκλωσης. Σε κάποια κέντρα διαλογής μπορεί να γίνει χειρονακτικός διαχωρισμός για ορισμένα από αυτά.",
            answers=[
                Answer(text="Nαι", points=0),
                Answer(text="Όχι", points=0, correct=True),
                Answer(text="Αναλόγως το μέγεθος τους", points=0)
            ]
        )
    )

    """Ανακυκλώνεται η πλαστική οδοντόβουρτσα"""
    question_pool.append(
        Question(
            text="Ανακυκλώνεται η πλαστική οδοντόβουρτσα",
            fact="Λόγω των χρησιμοποιούμενων υλικών δεν ανακυκλώνεται. Πλέον Διατίθενται οδοντόβουρτσες κατασκευασμένες από πιο οικολογικά υλικά.",
            answers=[
                Answer(text="Nαι", points=0),
                Answer(text="Όχι", points=0, correct=True)
            ]
        )
    )

    """Ανακυκλώνεται η πλαστική συσκευασία ψωμιού- τοστ;"""
    question_pool.append(
        Question(
            text="Ανακυκλώνεται η πλαστική συσκευασία ψωμιού - τοστ;",
            fact="Καλύτερη λύση είναι η αγορά φρέσκου ψωμιού ή ακόμη καλύτερα φτιάξε το δικό σου στο σπίτι!",
            answers=[
                Answer(text="Nαι", points=0),
                Answer(text="Όχι", points=0, correct=True),
                Answer(text="Αναλόγως το υλικό τους", points=0)
            ]
        )
    )

    """Ανακυκλώνεται η πλαστική συσκευασία από έτοιμη σαλάτα;"""
    question_pool.append(
        Question(
            text="Ανακυκλώνεται η πλαστική συσκευασία από έτοιμη σαλάτα;",
            fact="Αν είναι φτιαγμένη από πλαστικό PP δεν ανακυκλώνεται, ενώ αν είναι από LDPE ανακυκλώνεται αφού καθαριστεί και δεν σχιστεί σε μικρά κομμάτια.",
            answers=[
                Answer(text="Nαι", points=0),
                Answer(text="Όχι", points=0),
                Answer(text="Αναλόγως το υλικό τους", points=0, correct=True)
            ]
        )
    )

    """Ανακυκλώνεται το σφουγγάρι κουζίνας;"""
    question_pool.append(
        Question(
            text="Ανακυκλώνεται το σφουγγάρι κουζίνας;",
            fact="",
            answers=[
                Answer(text="Nαι", points=0),
                Answer(text="Όχι", points=0, correct=True),
                Answer(text="Μόνο ειδικά απορροφητικά σφουγγάρια", points=0)
            ]
        )
    )

    """Ανακυκλώνονται οι πλαστικές ή μεταλλικές κρεμάστρες;"""
    question_pool.append(
        Question(
            text="Ανακυκλώνονται οι πλαστικές ή μεταλλικές κρεμάστρες;",
            fact="Δεν αποτελούν συσκευασίες επομένως δεν ανακυκλώνονται μέσω του συστήματος των μπλε κάδων.",
            answers=[
                Answer(text="Nαι", points=0),
                Answer(text="Όχι", points=0, correct=True)
            ]
        )
    )

    """Ανακυκλώνεται η πλαστική συσκευασία ξυδιού;"""
    question_pool.append(
        Question(
            text="Ανακυκλώνεται η πλαστική συσκευασία ξυδιού;",
            fact="Θα πρέπει να καθαριστεί από υπολείμματα. Καλύτερη εναλλακτική αποτελεί η αγορά γυάλινης συσκευασίας.",
            answers=[
                Answer(text="Nαι", points=0,correct=True),
                Answer(text="Όχι", points=0)
            ]
        )
    )

    """Ανακυκλώνονται τα καπάκια;"""
    question_pool.append(
        Question(
            text="Ανακυκλώνονται τα καπάκια;",
            fact="Λόγω μεγέθους μπορεί να καταλήξουν στο υπόλειμμα της ανακύκλωσης και άρα στο ΧΥΤΑ. Προτιμότερο να ξεκουμπώνουμε το καπάκι από τα μπουκάλια προτού το πετάξουμε στον κάδο.",
            answers=[
                Answer(text="Nαι", points=0),
                Answer(text="Όχι", points=0,correct=True)
            ]
        )
    )
    return question_pool