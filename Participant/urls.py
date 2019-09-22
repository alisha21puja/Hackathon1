from django.urls import path

from django.conf import settings

from django.conf.urls.static import static

from Participant import views as ve

urlpatterns = [
    path('', ve.about, name='participantIndex'),
    path('participate', ve.participate, name='participate'),
    path('part_profile', ve.part_profile, name='part_profile'),
    path('part_editProfile', ve.part_editProfile, name='part_editProfile'),
    path('part_updateProfile', ve.part_updateProfile, name='part_updateProfile'),
    path('deleteparticipant', ve.deleteparticipant, name='deleteparticipant'),
    path('event_details', ve.event_details, name='event_details'),
    path('participatein_event/<int:id>',
         ve.participatein_event, name='participatein_event'),
    path('enquire/<int:id>', ve.enquireInfo, name='enquire'),
    path('part_enquire', ve.part_enquire, name='part_enquire'),
    path('enquireInfoMail', ve.enquireInfoMail, name='enquireInfoMail'),
    path('part_shareresources/<int:id>',
         ve.part_shareresources, name='part_shareresources'),
    path('partblog', ve.partblog, name='partblog'),
    path('partWriteBlog', ve.partWriteBlog, name='part-blog_write'),
    path('partblogsDetail', ve.partblogsDetails, name='partblogsDetails'),
    path('req_pdf', ve.req_pdf, name="req_pdf"),
    path('part_feedback', ve.part_feedback, name="part_feedback"),
    path('feedback_load', ve.feedback_load, name='feedback_load'),
    path('feedback', ve.feedback, name="feedback"),
    path('part_for', ve.part_for, name="part_for")


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
