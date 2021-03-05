import marmotta_export as me
MAX_SIZE = 1000
contexts = me.get_contexts()
print(f"Number of contexts: {len(contexts)}")
for i in contexts:
    if i.size > MAX_SIZE:
        contexts.remove(i)
print(f"Number of contexts: {len(contexts)}")
me.__create_export_folder()
me.export_contexts(contexts, me.save_exported_context)