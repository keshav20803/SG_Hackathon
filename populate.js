const { MongoClient } = require('mongodb');
const fs = require('fs')
require('dotenv').config()

async function main() {
  const uri = process.env.MONGO_URI

  const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

  try {
    await client.connect();

    const database = client.db('test'); 
    const collection = database.collection('therapist'); 
    const data = fs.readFileSync('docdata.json');
    const therapists = JSON.parse(data);
    const result = await collection.insertMany(therapists);
    console.log(`${result.insertedCount} documents were inserted`);
  } finally {
    await client.close();
  }
}

main().catch(console.error);
