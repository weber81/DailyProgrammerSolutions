"""Rules:
    Step1-|White|->Step2
    Step1-|Red|->StepBR
    Step2-|White|->StepBR
    Step2-|Orange|->StepGOB
    StepBR-|Red|->Step1
    StepBR-|Black|->StepGOB
    StepGOB-|Orange|->CloseO
    StepGOB-|Green|->CloseG
    StepGOB-|Black|->StepGOB
    CloseO-|Green|->End
    CloseG-|Orange|->End
    CloseO-|Black|->StepGOB
    CloseG-|Black|->StepGOB"""

stages = ["step1", "step2", "stepBR", "stepGOB", "closeO", "closeG", "Boom", "End"]
triggers = ["white", "black", "red", "orange", "green"]

transitions = {"step1":{"white":"step2",
                        "red":"stepBR",
                        "black":"Boom",
                        "orange":"Boom",
                        "green":"Boom"},
               "step2":{"white":"stepBR",
                        "orange":"stepGOB",
                        "red":"Boom",
                        "black":"stepGOB",
                        "green":"Boom"},
               "stepBR":{"black":"stepGOB",
                         "red":"step1",
                         "white":"Boom",
                         "orange":"Boom",
                         "green":"Boom"},
               "stepGOB":{"black":"stepGOB",
                         "red":"Boom",
                         "white":"Boom",
                         "orange":"closeO",
                         "green":"closeG"},
               "closeO":{"black":"stepGOB",
                         "red":"Boom",
                         "white":"Boom",
                         "orange":"Boom",
                         "green":"End"},
               "closeG":{"black":"stepGOB",
                         "red":"Boom",
                         "white":"Boom",
                         "orange":"End",
                         "green":"Boom"},
               "Boom":{"black":"Boom",
                         "red":"Boom",
                         "white":"Boom",
                         "orange":"Boom",
                         "green":"Boom"},
               "End":{"black":"End",
                         "red":"End",
                         "white":"End",
                         "orange":"End",
                         "green":"End"}}

def attemptDefusal():
    state = "step1"
    line = input()
    while line != "":
        state = transitions[state][line]
        line = input()
    if state == "End":
        print("Defused!")
    else:
        print("Boom!")

    
