#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:20:38 2021

@author: Azade

Labels -- situational terms

"""

''' Read terms that can associate notes with IPV-positive cases '''
SituationalTerms = ['domestic violence','intimate partner violence','spouse abuse','battered woman','domestic abuse',
                    'intimate partner violence','spousal abuse','intimate partner abuse','battered','violence against women',
                    'domestic assault','domestic dispute','problems with spouse or partner','maltreatment by spouse or partner',
                    'neglect and abandonment by spouse or partner','assault by husband','assault by partner','assault by wife',
                    'assault by spouse','assault by boyfriend','assault by girlfriend','assault by significant other',
                    'referral to partnership against domestic violence','resources or shelter for domestic violence'] # 24


''' Label the visits based on IPV situational terms '''
Labels_SituationalTerms = [0] * len(CSNs)
Labels_SituationalTerms_NoteType = [''] * len(CSNs)
Labels_SituationalTerms_PickedUpTerms = [''] * len(CSNs)


for (ic, c) in enumerate(CSNs):
    ## Chief Complaints
    if (ChiefComplaints_NegationDetected[ic] != ''  and not pd.isnull(ChiefComplaints_NegationDetected[ic])):
        thisNotes = ChiefComplaints_NegationDetected[ic]
        ind_terms = [i for (i,v) in enumerate(SituationalTerms) if re.search(r"\b{}\b".format(v), thisNotes)]
        if len(ind_terms) > 0:    
            Labels_SituationalTerms[ic] = 1   
            Labels_SituationalTerms_NoteType[ic] = Labels_SituationalTerms_NoteType[ic] + 'ChiefComplaint'
            this_terms = [SituationalTerms[iT] for iT in ind_terms]
            for ter in this_terms:
                Labels_SituationalTerms_PickedUpTerms[ic] = Labels_SituationalTerms_PickedUpTerms[ic] + ' ' + ter
    ## Admitting Diagnosis
    if (AdmittingDiagnosis_NegationDetected[ic] != ''  and not pd.isnull(AdmittingDiagnosis_NegationDetected[ic])):
        thisNotes = AdmittingDiagnosis_NegationDetected[ic]
        ind_terms = [i for (i,v) in enumerate(SituationalTerms) if re.search(r"\b{}\b".format(v), thisNotes)]
        if len(ind_terms) > 0:    
            Labels_SituationalTerms[ic] = 1   
            Labels_SituationalTerms_NoteType[ic] = Labels_SituationalTerms_NoteType[ic] + 'AdmittingDiagnosis'
            this_terms = [SituationalTerms[iT] for iT in ind_terms]
            for ter in this_terms:
                Labels_SituationalTerms_PickedUpTerms[ic] = Labels_SituationalTerms_PickedUpTerms[ic] + ' ' + ter
    ## Progress Notes
    if (ProgressNotes_NegationDetected[ic] != ''  and not pd.isnull(ProgressNotes_NegationDetected[ic])):
        thisNotes = ProgressNotes_NegationDetected[ic]
        ind_terms = [i for (i,v) in enumerate(SituationalTerms) if re.search(r"\b{}\b".format(v), thisNotes)]
        if len(ind_terms) > 0:    
            Labels_SituationalTerms[ic] = 1   
            Labels_SituationalTerms_NoteType[ic] = Labels_SituationalTerms_NoteType[ic] + 'ProgressNote'
            this_terms = [SituationalTerms[iT] for iT in ind_terms]
            for ter in this_terms:
                Labels_SituationalTerms_PickedUpTerms[ic] = Labels_SituationalTerms_PickedUpTerms[ic] + ' ' + ter
    ## Consult Notes
    if (ConsultNotes_NegationDetected[ic] != ''  and not pd.isnull(ConsultNotes_NegationDetected[ic])):
        thisNotes = ConsultNotes_NegationDetected[ic]
        ind_terms = [i for (i,v) in enumerate(SituationalTerms) if re.search(r"\b{}\b".format(v), thisNotes)]
        if len(ind_terms) > 0:    
            Labels_SituationalTerms[ic] = 1   
            Labels_SituationalTerms_NoteType[ic] = Labels_SituationalTerms_NoteType[ic] + 'ConsultNote'
            this_terms = [SituationalTerms[iT] for iT in ind_terms]
            for ter in this_terms:
                Labels_SituationalTerms_PickedUpTerms[ic] = Labels_SituationalTerms_PickedUpTerms[ic] + ' ' + ter
    ## Nursing Notes
    if (NursingNotes_NegationDetected[ic] != ''  and not pd.isnull(NursingNotes_NegationDetected[ic])):
        thisNotes = NursingNotes_NegationDetected[ic]
        ind_terms = [i for (i,v) in enumerate(SituationalTerms) if re.search(r"\b{}\b".format(v), thisNotes)]
        if len(ind_terms) > 0:    
            Labels_SituationalTerms[ic] = 1   
            Labels_SituationalTerms_NoteType[ic] = Labels_SituationalTerms_NoteType[ic] + 'Nursing Note'
            this_terms = [SituationalTerms[iT] for iT in ind_terms]
            for ter in this_terms:
                Labels_SituationalTerms_PickedUpTerms[ic] = Labels_SituationalTerms_PickedUpTerms[ic] + ' ' + ter
    ## ED and Triage Notes
    if (EDandTriageNotes_NegationDetected[ic] != ''  and not pd.isnull(EDandTriageNotes_NegationDetected[ic])):
        thisNotes = EDandTriageNotes_NegationDetected[ic]
        ind_terms = [i for (i,v) in enumerate(SituationalTerms) if re.search(r"\b{}\b".format(v), thisNotes)]
        if len(ind_terms) > 0:    
            Labels_SituationalTerms[ic] = 1   
            Labels_SituationalTerms_NoteType[ic] = Labels_SituationalTerms_NoteType[ic] + 'EDandTriageNote'
            this_terms = [SituationalTerms[iT] for iT in ind_terms]
            for ter in this_terms:
                Labels_SituationalTerms_PickedUpTerms[ic] = Labels_SituationalTerms_PickedUpTerms[ic] + ' ' + ter
    ## Social Worker Notes
    if (SocialWorkerNotes_NegationDetected[ic] != ''  and not pd.isnull(SocialWorkerNotes_NegationDetected[ic])):
        thisNotes = SocialWorkerNotes_NegationDetected[ic]
        ind_terms = [i for (i,v) in enumerate(SituationalTerms) if re.search(r"\b{}\b".format(v), thisNotes)]
        if len(ind_terms) > 0:    
            Labels_SituationalTerms[ic] = 1   
            Labels_SituationalTerms_NoteType[ic] = Labels_SituationalTerms_NoteType[ic] + 'SocialWorkerNote'
            this_terms = [SituationalTerms[iT] for iT in ind_terms]
            for ter in this_terms:
                Labels_SituationalTerms_PickedUpTerms[ic] = Labels_SituationalTerms_PickedUpTerms[ic] + ' ' + ter
    ## HP Notes
    if (HPNotes_NegationDetected[ic] != ''  and not pd.isnull(HPNotes_NegationDetected[ic])):
        thisNotes = HPNotes_NegationDetected[ic]
        ind_terms = [i for (i,v) in enumerate(SituationalTerms) if re.search(r"\b{}\b".format(v), thisNotes)]
        if len(ind_terms) > 0:    
            Labels_SituationalTerms[ic] = 1   
            Labels_SituationalTerms_NoteType[ic] = Labels_SituationalTerms_NoteType[ic] + 'H&PNote'
            this_terms = [SituationalTerms[iT] for iT in ind_terms]
            for ter in this_terms:
                Labels_SituationalTerms_PickedUpTerms[ic] = Labels_SituationalTerms_PickedUpTerms[ic] + ' ' + ter
    ## Miscellaneous Notes
    if (MiscellaneousNotes_NegationDetected[ic] != ''  and not pd.isnull(MiscellaneousNotes_NegationDetected[ic])):
        thisNotes = MiscellaneousNotes_NegationDetected[ic]
        ind_terms = [i for (i,v) in enumerate(SituationalTerms) if re.search(r"\b{}\b".format(v), thisNotes)]
        if len(ind_terms) > 0:    
            Labels_SituationalTerms[ic] = 1   
            Labels_SituationalTerms_NoteType[ic] = Labels_SituationalTerms_NoteType[ic] + 'MiscellaneousNotes'
            this_terms = [SituationalTerms[iT] for iT in ind_terms]
            for ter in this_terms:
                Labels_SituationalTerms_PickedUpTerms[ic] = Labels_SituationalTerms_PickedUpTerms[ic] + ' ' + ter
                
                
