from fastapi import FastAPI, HTTPException
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

#com: This endpoint allows filtering cars by size and number of doors. If no query parameters are provided, it returns all cars. 
#and also we have typecasted as via HTTP we get all query parameters as strings, so we explicitly cast doors to int

@app.get("/api/cars/filter")
async def filter_cars(size=None,doors:int=None):
    if size is None and doors is None:
        return db
    elif size is None:
        return [car for car in db if car['doors']==doors]
    elif doors is None:
        return [car for car in db if car['size']==size]
    else:
        return [car for car in db if car['size']==size and car['doors']==doors]
    
#com:Path parameter to get car by its ID
@app.get("/api/cars/{id}")
async def get_car_by_id(id:int):
    out=[car for car in db if car['id']==id]
    if not out:
         raise HTTPException(status_code=404, detail="Car not found")
    else:
        return out

#com: This is the welcome endpoint that greets the user by name
@app.get("/")
async def welcome(name):
    return {"message": f" hi {name} Hello !!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
