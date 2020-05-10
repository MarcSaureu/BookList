from behave import *
import operator
from functools import reduce
from django.db.models import Q

use_step_matcher("parse")

@when(u'I register List')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('create_list'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Submit').first.click()

@then(u'There are {count:n} lists')
def step_impl(context, count):
    from BookList.models import List
    assert count == List.objects.count()
