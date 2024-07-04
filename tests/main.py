from eazydocs import Updater, generate_docs

from example_methods import set_plot_title

docs = generate_docs(set_plot_title)


updater = Updater("update", "D:/Software/EazyDocs/tests", docs)
