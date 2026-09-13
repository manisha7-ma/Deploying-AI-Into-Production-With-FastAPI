from fastapi import FastAPI
app = FastAPI()
db=[
    {"id":1,"size":"s","fuel":"petrol","doors":4,"transmission":"manual"},
    {"id":2,"size":"m","fuel":"diesel","doors":4,"transmission":"automatic"},
    {"id":3,"size":"l","fuel":"electric","doors":2,"transmission":"automatic"}, 
    {"id":4,"size":"s","fuel":"hybrid","doors":4,"transmission":"manual"},
    {"id":5,"size":"m","fuel":"petrol","doors":4,"transmission":"manual"},
    {"id":6,"size":"l","fuel":"diesel","doors":2,"transmission":"manual"},
    {"id":7,"size":"s","fuel":"electric","doors":2,"transmission":"automatic"},
    {"id":8,"size":"m","fuel":"hybrid","doors":4,"transmission":"automatic"},
    {"id":9,"size":"l","fuel":"petrol","doors":4,"transmission":"automatic"}
]

# Please add an operation called get_cars() That is served at /api/cars and that returns all cars in the database
#com: This is the endpoint to get all cars in the database
@app.get("/api/cars")
async def get_cars():
    return db
#com:This is the endpoint to get based on size
@app.get("/api/cars/size")
async def get_cars_by_size(size):
    return [car for car in db if car['size']==size]
#com : This will check if the size is returned then will give based on the size, otherwise will return an empty list
@app.get("/api/cars/withsize")
async def get_cars(size=None):
    if size is None:
        return db
    else :
        return [car for car in db if car['size']==size]

#

#com: This is the welcome endpoint that greets the user by name
@app.get("/")
async def welcome(name):
    return {"message": f" hi {name} Hello !!"}
