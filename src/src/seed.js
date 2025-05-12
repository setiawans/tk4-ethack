require('dotenv').config();
const pool = require('./config/db');

const seedDB = async () => {
    try {
        console.log('🌱 Seeding database...');

        await pool.query(`
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            );
        `);

        await pool.query(`
            INSERT INTO users (email, password) VALUES 
            ('kelompok8@ethack.id', '${process.env.ADMIN_PASSWORD}')
            ON CONFLICT (email) DO NOTHING;
        `);

        console.log('✅ Database seeded successfully!');
    } catch (err) {
        console.error('❌ Seeding error:', err);
    }
};

module.exports = seedDB;