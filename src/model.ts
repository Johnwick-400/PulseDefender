import * as tf from '@tensorflow/tfjs';

let model: tf.LayersModel | null = null;

export async function loadModel() {
  try {
    // Replace '/model/model.json' with the path to your converted model
    model = await tf.loadLayersModel('/model/model.json');
    console.log('Model loaded successfully');
    return true;
  } catch (error) {
    console.error('Error loading model:', error);
    return false;
  }
}

export async function predict(data: number[][]) {
  if (!model) {
    throw new Error('Model not loaded');
  }

  const tensorData = tf.tensor2d(data);
  const predictions = await model.predict(tensorData) as tf.Tensor;
  const results = await predictions.array();
  
  // Clean up tensors
  tensorData.dispose();
  predictions.dispose();

  return results;
}