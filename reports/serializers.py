from rest_framework import serializers

from reports.models import Report


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


class PatentSerializer(serializers.Serializer):
    # наименование
    name = serializers.CharField()
    # фио авторов (для студентов указать группу)
    authors_fullname = serializers.CharField()
    # номер патента
    number = serializers.IntegerField()
    # страна патентования
    country = serializers.CharField()
    # патентообладатель
    patent_owner = serializers.CharField()


class SoftwareProductSerializer(serializers.Serializer):
    # наименование программного продукта
    name = serializers.CharField()
    # фио авторов (для студентов указать группу)
    authors_fullname = serializers.CharField()
    # место регистрации
    registration_place = serializers.CharField()
    # где используется
    where_used = serializers.CharField()


class ExhibitionSerializer(serializers.Serializer):
    # наименование выставки
    name = serializers.CharField()
    # дата проведения
    date = serializers.DateField()
    # место проведения
    place = serializers.CharField()
    # фио участников (для студентов указать группу)
    participants_fullname = serializers.CharField()
    # cтатус выставки
    exhibition_type = serializers.CharField()
    # наименования экспонатов
    exhibit_names = serializers.CharField()
    # результат участия
    result = serializers.CharField()


class ContestSerializer(serializers.Serializer):
    # наименование конкурса
    name = serializers.CharField()
    # наименование заявки
    application_name = serializers.CharField()
    # фио руководителя
    leader_fullname = serializers.CharField()
    # фио ответственного исполнителя
    responsible_executor_fullname = serializers.CharField()


class ScientificPublicationSerializer(serializers.Serializer):
    # фио авторов (для студентов указать группу)
    authors_fullname = serializers.CharField()
    # наименование публикации, количество печатных листов
    name = serializers.CharField()
    # библиографические данные
    bibliographic_data = serializers.CharField()


class StudentWorkSerializer(serializers.Serializer):
    # название конкурса, статус
    contest = serializers.CharField()
    # организатор конкурса
    organizer = serializers.CharField()
    # наименование работы
    name = serializers.CharField()
    # фио авторов (для студентов указать группу)
    authors_fullname = serializers.CharField()


class OlympiadSerializer(serializers.Serializer):
    # название олимпиады, статус
    name = serializers.CharField()
    # дата проведения
    date = serializers.DateField()
    # место проведения
    place = serializers.CharField()
    # фио участника, номер группы
    participant_fullname = serializers.CharField()
    # результат
    result = serializers.CharField()


class ActivitiesParticipationSerializer(serializers.Serializer):
    # содержание работы
    content = serializers.CharField()
    # степень участия,
    participant_degree = serializers.CharField()
    # результат
    result = serializers.CharField()
    # примечания, рекомендации
    notes = serializers.CharField()


class ReportCreateRequestSerializer(serializers.Serializer):
    template_id = serializers.IntegerField()
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

    # 3 Сведения о научной и научно-методической работе
    # 3.1 Сведения об опубликованных монографиях
    monographs = serializers.ListSerializer(child=MonographSerializer())

    # 3.2 Перечень статей в журналах, опубликованных в 2021-22 уч.году
    scopus_articles = serializers.ListSerializer(child=ArticleSerializer())
    web_of_science_articles = serializers.ListSerializer(child=ArticleSerializer())
    vak_articles = serializers.ListSerializer(child=ArticleSerializer())
    rinc_articles = serializers.ListSerializer(child=ArticleSerializer())

    # 3.3 Перечень конференций, в которых принимал участие в 2021-22 уч. году. (в том числе с участием студентов)
    conferences = serializers.ListSerializer(child=ConferenceSerializer())

    # 3.4 Перечень международных и Российских патентов, полученных в 2021-22 уч. году. (в т. ч. с участием студентов)
    patents = serializers.ListSerializer(child=PatentSerializer())

    # 3.5 Разработанные и зарегистрированные программные продукты. (в том числе с участием студентов)
    software_products = serializers.ListSerializer(child=SoftwareProductSerializer())

    # 3.5 Участие в выставках. (в том числе с участием студентов)
    exhibitions = serializers.ListSerializer(child=ExhibitionSerializer())

    # 3.6 Перечень заявок, поданных на участие в федеральных, региональных и прочих конкурсах НИР
    contests = serializers.ListSerializer(child=ContestSerializer())

    # 4 Сведения о научно-исследовательской работе совместно со студентами в 2021-22 уч. году
    # 4.1 Перечень научных публикаций с участием студентов
    scientific_publications = serializers.ListSerializer(
        child=ScientificPublicationSerializer()
    )

    # 4.2 Перечень студенческих работ, поданных на конкурсы на лучшую НИР
    student_works = serializers.ListSerializer(child=StudentWorkSerializer())

    # 4.3 Руководство студентами, участвующих  в Олимпиадах
    olympiads = serializers.ListSerializer(child=OlympiadSerializer())

    # 5 Сведения об участии в организационной работе кафедры в 2021-22 уч. году.
    organizational_participations = serializers.ListSerializer(
        child=ActivitiesParticipationSerializer()
    )

    # 6 сведения об участии в профориентационной работе
    professional_orientation_participations = serializers.ListSerializer(
        child=ActivitiesParticipationSerializer()
    )

    # 7 Сведения об участии в учебно-воспитательной работе
    educational_participations = serializers.ListSerializer(
        child=ActivitiesParticipationSerializer()
    )


class ReportCreateResponseSerializer(serializers.ModelSerializer[Report]):
    class Meta:
        model = Report
        fields = ["id", "user", "data", "is_reviewed", "created_at", "updated_at"]


class ReportListSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    patronymic = serializers.CharField()

    report_start_date = serializers.DateField()
    report_end_date = serializers.DateField()


class ReportListRequestSerializer(serializers.Serializer):
    pass
