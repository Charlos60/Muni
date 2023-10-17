from django.urls import path
from . import views
from django.urls import include



app_name = 'task'  

urlpatterns = [
    path('restringida/', views.vista_restringida, name='vista_restringida'),
    path('restringidaAd/', views.vista_restringida_Administrador, name='vista_restringida_Administrador'),
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('registerValdiate/', views.register_view, name='register_view'),
    path('logout/', views.logout_view, name='logout'),
    path('user_table/', views.user_table_view, name='user_table'),
    path('modify_user_view/<int:idusuario>/', views.Modify_user_view, name='modify_user_view'),
    path('modify_user/<int:idusuario>/', views.Modify_user, name='modify_user'),
    path('delete_user/<int:idusuario>/', views.Delete_user, name='delete_user'),
    path('view_fontanero/', views.View_fontanero, name='view_fontanero'),
    path('register_view_fontanero/', views.View_register_fontanero, name='register_view_fontanero'),
    path('register_fontanero/', views.Register_fontanero, name='register_fontanero'),
    path('modify_fontanero_view/<int:idfontanero>/', views.Modify_fontanero_view, name='modify_fontanero_view'),
    path('modify_fontanero/<int:idfontanero>/', views.Modify_fontanero, name='modify_fontanero'),
    path('delete_fontanero/<int:idfontanero>/', views.Delete_fontanero, name='delete_fontanero'),
    path('delete_fontanero/<int:idfontanero>/', views.Delete_fontanero, name='delete_fontanero'),
    path('view_predios/', views.View_predios, name='view_predios'),
    path('register_predios_view/', views.Register_fontanero_view, name='register_predios_view'),
    path('register_predios/', views.Register_predios, name='register_predios'),
    path('modify_predio_view/<int:idpredio>/', views.Modify_predio_view, name='modify_predio_view'),
    path('modify_predio/<int:idpredio>/', views.Modify_predio, name='modify_predio'),
    path('publicar_anuncio/', views.Publicar_anuncio, name='publicar_anuncio'),
    path('sector_view/', views.Sector_view, name='sector_view'),
    path('create_sector/', views.Create_sector, name='create_sector'),
    path('excel_report_usuario/', views.excel_report_usuario, name='excel_report'),
    path('excel_report_fontanero/', views.excel_report_fontanero, name='excel_report_fontanero'),
    path('excel_report_predio/', views.excel_report_predio, name='excel_report_predio'),
    path('excel_report_jornal/', views.excel_report_jornales, name='excel_report_Jornal'),
    path('excel_report_pagosagua/', views.excel_report_pagoagua, name='excel_report_pagosagua'),
    path('excel_report_pagosmulta/', views.excel_report_multas, name='excel_report_pagosmulta'),
    path('search_usuario/', views.search_usuario, name='search_usuario'),
    path('search_fontanero/', views.search_Fontaneros, name='search_fontanero'),
    path('search_jornales/', views.search_Jornal, name='search_jornales'),
    path('search_predios/', views.search_Predios, name='search_predios'),
    path('search_multas_pagos/', views.search_multas_pagos, name='search_multas_pagos'),
    path('search_agua_pagos/', views.search_agua_pagos, name='search_agua_pagos'),
    path('view_user/<int:idusuario>/', views.View_User, name='view_user'),
    path('Create_view_multa/<int:idusuario>/', views.Create_view_multa, name='Create_view_multa'),
    path('create_multa/<int:idusuario>/', views.create_multa, name='create_multa'),
    path('delete_multa/<int:idmulta>/', views.Delete_multa, name='delete_multa'),
    path('pago_realizado/<int:idmulta>/', views.pago_realizado_true, name='pago_realizado'),
    path('view_pagos/', views.pagos_views, name='view_pagos'),
    path('view_pagos_agua/', views.pagos_views_agua, name='view_pagos_agua'),
    path('pago_realizado_agua_true/<int:idpagoagua>/', views.pago_realizado_agua_true, name='pago_realizado_agua_true'),
    path('pendiente_pago_view/', views.pendientes_usuario, name='pendientes_usuario'),
    path('contactanos_view/', views.contactanos_view, name='contactanos_view'),
    path('jornales_view/', views.jornales_view, name='jornales_view'),
    path('crear_jornales_view/', views.crear_jornales_view, name='crear_jornales_view'),
    path('Register_jornal/', views.Register_jornal, name='Register_jornal'),
    path('delete_jornal/<int:idjornal>/', views.Delete_jornal, name='Delete_jornal'),
    path('delete_anuncio/<int:idanuncio>/', views.Delete_anuncio, name='delete_anuncio'),
    path('editar_jornal_view/<int:idjornal>/', views.editar_jornal_view, name='editar_jornal_view'),
    path('editar_jornal/<int:idjornal>/', views.editar_jornal, name='editar_jornal'),
    path('delete_sector/<int:idsector>/', views.Delete_sector, name='delete_sector'),
    path('delete_predio/<int:idpredio>/', views.Delete_predio, name='delete_predio'),
    #path('pago_completado_view/<int:idpagoagua>/', views.pago_completado_view, name='pago_completado_view'),
    path('pago_completado_view/', views.pago_completado_view, name='pago_completado_view'),
    path('pagomulta_completado_view/', views.pagomulta_completado_view, name='pagomulta_completado_view'),
    path('PendienteMultas/', views.pendientes_multas, name='pendientes_multas'),


    


    path('search_users/', views.search_users, name='search_users'),
    path('search_sector/', views.search_sector, name='search_sector'),
    # Otras rutas de URL
]
