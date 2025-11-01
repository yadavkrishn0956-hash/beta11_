const mongoose = require('mongoose');

const patientSchema = new mongoose.Schema({
  patientId: {
    type: String,
    required: true,
    unique: true,
    index: true
  },
  name: {
    type: String,
    required: true
  },
  email: {
    type: String,
    required: true
  },
  age: {
    type: Number,
    required: true
  },
  gender: {
    type: String,
    enum: ['Male', 'Female', 'Other'],
    required: true
  },
  bloodGroup: {
    type: String
  },
  phone: {
    type: String
  },
  address: {
    type: String
  },
  emergencyContact: {
    name: String,
    phone: String,
    relation: String
  },
  medicalHistory: {
    allergies: [String],
    chronicConditions: [String],
    currentMedications: [String]
  },
  blockchainId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Blockchain'
  },
  createdAt: {
    type: Date,
    default: Date.now
  },
  updatedAt: {
    type: Date,
    default: Date.now
  }
});

// Update timestamp on save
patientSchema.pre('save', function(next) {
  this.updatedAt = new Date();
  next();
});

module.exports = mongoose.model('Patient', patientSchema);
