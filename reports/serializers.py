from rest_framework import serializers


class QualificationImprovementSerializer(serializers.Serializer):
    # Форма повышения квалификации
    qualification_improvement_form = serializers.CharField()
    country = serializers.CharField()
    organization = serializers.CharField()
    course_name = serializers.CharField()

    # № диплома (свидетельства), дата выдачи
    diploma_number = serializers.CharField()
    diploma_date = serializers.DateField()

    hours_count = serializers.IntegerField()


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
