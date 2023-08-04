const sequelize = require('./database/sequelize');

const User = sequelize.define('User', {
    id: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true,
    },
    name: {
        type: DataTypes.STRING,
        unique: true,
    },
    favouriteColor: {
        type: DataTypes.STRING,
        defaultValue: 'green'
    },
    age: DataTypes.INTEGER,
    cash: DataTypes.INTEGER,
}, {
    timestamps: false,
});

// Aquí es donde añadimos la funcionalidad para guardar un usuario.
// Para simplificar, solo guardamos un usuario estático.

const saveUser = async () => {
    try {
        const user = await User.create({
            name: "John Doe",
            age: 30,
            cash: 2000
        });

        console.log(`User ${user.name} has been saved.`);
    } catch (error) {
        console.error("Failed to save user:", error);
    }
};

saveUser();
