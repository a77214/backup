import json

# with open('jobs.json','r',encoding='utf-8') as f:
#     jobs = json.load(f)
#     for job in jobs:
#         job_tag=job['tags']
#         for job_length in job_tag:
#
#             if job_length=='1年以内' and "华为" not in job['company_name']:
#                 print(job['job_name'],job['company_name'],job_length)


with open('jobsJava.json','r',encoding='utf-8') as f:
    jobs = json.load(f)
    for job in jobs:
        job_tag=job['tags']
        for job_length in job_tag:
            if job_length=='1年以内' and "华为" not in job['company_name']:
                print(job['job_name'],job['company_name'],job_length)

