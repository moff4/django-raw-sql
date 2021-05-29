
from typing import List, Tuple
import sqlite3

from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


class ListContact(View):
    """
        Processing requests with RAW SQL queries
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        """
            show user empty form without any users
        """
        rows = []  # type: List[Tuple[int, str, int]]
        return render(
            request=request,
            template_name='list.html',
            context=locals(),
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        """
            send user same form but with data
        """
        # for postgres/mysql/etc can be usefull to get connection and cursor
        # https://stackoverflow.com/questions/52537572/django-postgresql-connection-cannot-use-server-side-cursor
        with sqlite3.connect('db.sqlite3') as connection:
            cursor = connection.cursor()

            params = []  # type: List[str]
            filters = []  # type: List[str]

            # check if age was passed and is not empty
            if request.POST.get('age'):
                filters.append('age == ? ')
                params.append(request.POST['age'])

            # check if name was passed and is not empty
            if request.POST.get('name'):
                filters.append('name == ? ')
                params.append(request.POST['name'])

            # build query with filters
            query = 'select * from firstapp_contact'
            if filters:
                query += ' WHERE ' + ' AND '.join(filters)

            rows = list(cursor.execute(query, params))  # type: List[Tuple[int, str, int]]

            # release resources
            cursor.close()

        return render(
            request=request,
            template_name='list.html',
            context=locals(),
        )
