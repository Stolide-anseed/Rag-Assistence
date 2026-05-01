from src.retriever_tool import retrieve_blog_posts
from src.response.generater import generate_query_or_respond
from  src.graph import make_graph

graph = make_graph()

#======================
# проверка поиска
#======================
def check_retriever_tool():
    retriever_tool = retrieve_blog_posts
    print(retriever_tool.invoke({'query': 'Hill Climbing'}))

#=======================
# Проверка на вывод и генерацию
#=======================
def check_generator_query_or_respond():
    input = {"messages": [{"role": "user", "content": "Hello!"}]}
    return generate_query_or_respond(input)['messages'][-1].pretty_print()


#=======================
# Использование RAG
#=======================
def check_RAG():
    for chunk in graph.stream(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "What is Hill Climbing in The Kaggle Grandmasters Playbook?",
                    }
                ]
            }
    ):
        for node, update in chunk.items():
            print("Update from node", node)
            update["messages"][-1].pretty_print()
            print("\n\n")