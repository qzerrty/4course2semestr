from prototypes import *

frame_types = {
  'Файл': [
    {
      'type': 'text',
      'name': 'Тип файла',
      'property_name': 'file_type',
    },
    {
      'type': 'text',
      'name': 'Название',
      'property_name': 'name',
    },
    {
      'type': 'text',
      'name': 'Дата создания',
      'property_name': 'creation_date',
    },
    {
      'type': 'text',
      'name': 'Дата последнего изменения',
      'property_name': 'last_change_date',
    },
    {
      'type': 'text',
      'name': 'Размер',
      'property_name': 'size',
    },
    {
      'type': 'frame',
      'name': 'Расположение',
      'property_name': 'location',
      'filter': lambda frame: isinstance(frame, (Directory, Disk))
    },
  ],
  'Директория': [
    {
      'type': 'text',
      'name': 'Название',
      'property_name': 'name',
    },
    {
      'type': 'text',
      'name': 'Дата создания',
      'property_name': 'creation_date',
    },
    {
      'type': 'frame',
      'name': 'Расположение',
      'property_name': 'location',
      'filter': lambda frame: isinstance(frame, (Directory, Disk))
    },
  ],
  'Диск': [
    {
      'type': 'text',
      'name': 'Название',
      'property_name': 'name',
    },
    {
      'type': 'text',
      'name': 'Размер',
      'property_name': 'max_size',
    },
  ],
  'Содержит': [
    {
      'type': 'frame',
      'name': 'Ребенок',
      'property_name': 'children',
      'filter': lambda frame: isinstance(frame, (Directory, File))
    },
    {
      'type': 'frame',
      'name': 'Родитель',
      'property_name': 'parent',
      'filter': lambda frame: isinstance(frame, (Directory, Disk))
    },
  ],
}

frame_types_classes = {
  'Файл': File,
  'Директория': Directory,
  'Диск': Disk,
  'Содержит': Contains,
}

frame_types_classes_en = {
  'File': File,
  'Directory': Directory,
  'Disk': Disk,
  'Contains': Contains,
}