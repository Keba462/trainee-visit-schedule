from edc_visit_schedule import FormsCollection, Crf

crf = {}

crfs_initial = FormsCollection (
    Crf(show_order=1, model='trainee_subject.educationalquestionaire'),
    Crf(show_order=2, model='trainee_subject.communityengagement'),
    name= 'initial',
)


crfs_followup = FormsCollection (
    Crf(show_order=1, model='trainee_subject.educationalquestionaire'),
    Crf(show_order=2, model='trainee_subject.communityengagement'),
    Crf(show_order=3, model='trainee_subject.demographic'),
    name= 'followup',
)




crf.update(
    {'initial': crfs_initial,
     'followup': crfs_followup,
    }
)