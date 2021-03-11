import marmotta_export as me
from itertools import filterfalse
MAX_SIZE = 1000
contexts = me.get_contexts()
print(f"Number of contexts: {len(contexts)}")
contexts[:] = filterfalse(lambda t: t.size >= MAX_SIZE, contexts)
print(f"Number of contexts: {len(contexts)}")
me.__create_export_folder()
me.export_contexts(contexts, me.save_exported_context)