from flask import request

class Parser(object):

  sep = ';'

  # ...

  def filter_query(self, query):
    model_class = self._get_model_class(query) # returns the query's Model
    raw_filters = request.args.getlist('filter')
    for raw in raw_filters:
      try:
        key, op, value = raw.split(self.sep, 3)
      except ValueError:
        raise Exception(400, 'Invalid filter: %s' % raw)
      column = getattr(model_class, key, None)
      if not column:
        raise Exception(400, 'Invalid filter column: %s' % key)
      if op == 'in':
        filt = column.in_(value.split(','))
      else:
        try:
          attr = filter(
            lambda e: hasattr(column, e % op),
            ['%s', '%s_', '__%s__']
          )[0] % op
        except IndexError:
          raise Exception(400, 'Invalid filter operator: %s' % op)
        if value == 'null':
          value = None
        filt = getattr(column, attr)(value)
      query = query.filter(filt)
    return query