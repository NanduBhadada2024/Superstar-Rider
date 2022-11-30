import frappe

def get_context(context):
    context.secret_message = "Somthing Cool"
    return context