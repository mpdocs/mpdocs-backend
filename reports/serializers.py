from rest_framework import serializers


class QualificationImprovementSerializer(serializers.Serializer):
    # Форма повышения квалификации
    form = serializers.CharField()
    country = serializers.CharField()
    organization = serializers.CharField()
    course_name = serializers.CharField()

    # № диплома (свидетельства), дата выдачи
    diploma_number = serializers.CharField()
    diploma_date = serializers.DateField()

    hours_count = serializers.IntegerField()


class MethodicalWorkSerializer(serializers.Serializer):
    # наименование
    name = serializers.CharField()
    # фио авторов
    authors = serializers.CharField()  # фио авторов через запятую
    # вид (учебник, пособие, методические указания и т.п.)
    type = serializers.CharField()
    # издательство, isbn
    publisher = serializers.CharField()
    # Объём в п.л. или стр.
    pages_count = (
        serializers.CharField()
    )  # char field, потому что может быть "Электронное издание"


class MonographSerializer(serializers.Serializer):
    # наименование
    name = serializers.CharField()
    # фио авторов
    authors_with_work = (
        serializers.CharField()
    )  # фио авторов через запятую с указанием места работы
    # издательство, isbn
    publisher = serializers.CharField()
    # Объём в п.л. или стр.
    pages_count = (
        serializers.CharField()
    )  # char field, потому что может быть "Электронное издание"


class ArticleSerializer(serializers.Serializer):
    # наименование
    name = serializers.CharField()
    # фио авторов
    authors_with_work = (
        serializers.CharField()
    )  # фио авторов и соавторов через запятую с указанием места работы
    # выходные данные, издательство, isbn
    publisher = serializers.CharField()
    # Объём в п.л. или стр.
    pages_count = (
        serializers.CharField()
    )  # char field, потому что может быть "Электронное издание"


class ConferenceSerializer(serializers.Serializer):
    # наименование
    name = serializers.CharField()
    # дата проведения
    date = serializers.DateField()
    # место проведения
    place = serializers.CharField()
    status = serializers.CharField()
    # вид участия
    participation_type = serializers.CharField()


class ReportSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    patronymic = serializers.CharField()
    work_time_coefficient = serializers.FloatField()  # Например, 1.0 ставки
    # ученая степень
    academic_degree = serializers.CharField()
    # должность
    position = serializers.CharField()

    report_start_date = serializers.DateField()
    report_end_date = serializers.DateField()
    # 1 Информация о повышении квалификации в период 2021-22 уч. год
    qualification_improvement = serializers.ListSerializer(
        child=QualificationImprovementSerializer()
    )
    # 2 Учебно-методическая работа в 2021-22 уч.году
    # 2.1 Перечень изданных учебно-методических пособий и указаний за 2021-22уч.год
    methodical_works = serializers.ListSerializer(child=MethodicalWorkSerializer())

    # 3.Сведения о научной и научно-методической работе
    # 3.1. Сведения об опубликованных монографиях
    monographs = serializers.ListSerializer(child=MonographSerializer())

    # 3.2 Перечень статей в журналах, опубликованных в 2021-22 уч.году
    scopus_articles = serializers.ListSerializer(child=ArticleSerializer())
    web_of_science_articles = serializers.ListSerializer(child=ArticleSerializer())
    vak_articles = serializers.ListSerializer(child=ArticleSerializer())
    rinc_articles = serializers.ListSerializer(child=ArticleSerializer())

    # 3.3 Перечень конференций, в которых принимал участие в 2021-22 уч. году. (в том числе с участием студентов)
    conferences = serializers.ListSerializer(child=ConferenceSerializer())
