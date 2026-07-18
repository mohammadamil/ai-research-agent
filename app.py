from agent import run_agent


USER_ID="default_user"



print("🚀 AI Research Agent Started")

print("Type exit to stop")




while True:


    user_input=input("\nYou: ")



    if user_input.lower()=="exit":

        print("Goodbye!")

        break



    response=run_agent(

        user_input,

        USER_ID

    )



    print("\nAgent:")

    print(response)