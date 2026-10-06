def main() -> None:
    print("앱")

    # 작업시작 
    # CHAP6_single-agent / web_agent
    from . import agent
    agent.invoke()

    # CHAP6_single-agent/create_agent
    # from .create_agent import middleware_with_node
