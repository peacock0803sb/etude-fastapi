FROM python:3.9-buster as builder

WORKDIR /app
COPY . /app/

RUN pip install -U pip setuptools && pip install .[sam] -c constraints.txt

FROM public.ecr.aws/lambda/python:3.9

WORKDIR /var/task

COPY ./ /var/task/
COPY --from=builder /usr/local/lib/python3.9/site-packages .

CMD ["run.handler"]
