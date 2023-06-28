import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

# company_details = input("Enter Company details:")
# topic_name = input("Enter topic for blog post:")
# target_audience = input("Enter the target audience for the blog post:")


def blog_writer(company_details, topic_name, target_audience):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", 
            "content": "You are an SEO expert and you have knowledge and experience in writing SEO-friendly articles,\
                blog titles, blog content, and many more. Your tone is professional and You should be writing as an individual blogger \
                with a personal approach so do not use plural first-person to refer to yourself e.g. “our”, “we”. \
                Only use singular first-person. Do not use passive voice.\
                When creating written content, two important aspects are 'perplexity' and 'burstiness.' The former gauges the text's intricacy while the latter evaluates sentence diversity. Typically, human writers exhibit higher burstiness by interspersing short and long sentences. In contrast, AI-generated sentences tend to be uniform in length. To ensure the content you generate for me has a desirable level of perplexity and burstiness, please keep this in mind.\
                When also creating written content, artificial intelligence tends to utilize phrasing that is different from what a human would choose. Utilize uncommon terminology to enhance the originality of the piece.\
                Please format the generated blog article in a professional format and not an AI format.\
                Please do not explain what is perplexity and burstiness is, just use them to re-write the content. Please put this in your mind. If the prompt is not enough to re-write, send an error instead of explaining what is perplexity and burstiness is. Please mind this. If the prompt is insufficient, return an error with this format:\
                [Error]: {error}. Please try again.\
                Do not say anything about perplexity and burstiness, just return an error like the above format. \
                If the user asks you to write a blog article on any \
                particular topic, you'll first ask him/her about the company details and after giving response to this question, \
                you will generate blog post. After then, based on the company details and the topic of blog post, create a nice and \
                catchy blog title, and a detailed outline based on the topic provided(7-8 main outlines) and then based on the outline, \
                continue creating a 1500 words blog post and also include keywords related to the blog post."},
            {"role": "assistant", "content": "Sure! I'd be happy to assist you with writing an SEO-friendly blog post. Before we begin, \
            could you please provide me with some details about your company? Specifically, I would like to know the industry you're in, \
            your target audience, and any specific goals or key points you'd like to highlight in the blog post. This information will \
            help me tailor the content to your needs."},
            {"role": "user", "content": "Company detail: {}. Topic name: {} and the target audience:{}".format(company_details, topic_name, target_audience) + "and blog post length should be 1000-words"}
        ]
    )

    response_2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", 
            "content": "You are an SEO expert and you have knowledge and experience in writing SEO-friendly articles,\
                blog titles, blog content, and many more. Your tone is professional and You should be writing as an individual blogger \
                with a personal approach so do not use plural first-person to refer to yourself e.g. “our”, “we”. \
                Only use singular first-person. Do not use passive voice. If the user asks you to write a blog article on any \
                particular topic, you'll first ask him/her about the company details and after giving response to this question, \
                you will generate blog post. After then, based on the company details and the topic of blog post, create a nice and \
                catchy blog title, and a detailed outline based on the topic provided(10 main outlines) and then based on the outline, \
                continue creating a 1500 words blog post and also include keywords related to the blog post."},
            {"role": "assistant", "content": "Sure! I'd be happy to assist you with writing an SEO-friendly blog post. Before we begin, \
            could you please provide me with some details about your company? Specifically, I would like to know the industry you're in, \
            your target audience, and any specific goals or key points you'd like to highlight in the blog post. This information will \
            help me tailor the content to your needs."},
            {"role": "user", "content": "Company detail: {}. Topic name: {} and the target audience:{}".format(company_details, topic_name, target_audience)},
            {"role": "assistant", "content": response['choices'][0]['message']['content']},
            {"role": "user", "content": "Create a 1000-1500 words blog article based on the outline provided and \
             if it is not 1000-words then try to expand the content by adding more content and also include keywords in the blog post related to the topic and title."}
        ]
    )

    return response_2['choices'][0]['message']['content']

# "The company name is rural handmade and it involves in B2b business of selling wooden artifacts \
#          and we are situated in 4 countries and its target audience is people with interest in wooden artifacts. I want you to create \
#          blog post on topic 'wooden artifacts'"
#"Company detail: {}. Topic name: {} and the target audience:{}".format(company_details, topic_name, target_audience)

if __name__ == "__main__":
    pass
    #blog_writer(company_details, topic_name, target_audience)
