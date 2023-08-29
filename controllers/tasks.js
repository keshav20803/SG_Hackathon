const getAllTasks = (req , res)=>{
    res.send('All Items');
}

const createTask = (req , res)=>{
    res.send(req.body);
}

const getTask = (req , res)=>{
    res.send('Create Task');
}

const updateTask = (req , res)=>{
    res.send('Create Task');
}

const deleteTask = (req , res)=>{
    res.send('Create Task');
}

module.exports = {
    getAllTasks,createTask,getTask,updateTask,deleteTask
}