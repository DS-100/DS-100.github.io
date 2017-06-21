import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
import math


###################################################################
# Some functions for visualizing images and filters in the MNIST
# dataset.  (As usual, visualization code is long and intricate.)
# You don't need to read this file.
###################################################################

_image_size = 28

def example_to_image(example):
    '''Takes in a length-784 training example and returns a (28, 28) image.'''
    return example.reshape((_image_size, _image_size))

def show_flat_images(images, ncols=2, image_titles=None, **kwargs):
    """
    Shows one or more images, represented as flat length-784 arrays.
    
    images: Image or list of images, each a 1D array of length 784.
      The images can also be (title, array) pairs.
    """
    if isinstance(images, np.ndarray) and len(images.shape) == 2:
        images = list(images)
    elif not (isinstance(images, list) or isinstance(images, tuple)):
        images = [images]
    
    if len(images) > 0 and isinstance(images[0], tuple):
        image_titles = [i[0] for i in images]
        images = [i[1] for i in images]
    
    unflattened_images = [example_to_image(i) for i in images]
    show_images(unflattened_images, ncols=ncols, image_titles=image_titles, **kwargs)

def show_images(images, ncols=2, title=None, image_titles=None, **kwargs):
    """
    Shows one or more images.
    
    images: Image or list of images.
    """
    def show_image(image, norm=None):
        plt.imshow(image, norm=norm, cmap=plt.get_cmap('RdGy'))
    
    def draw_border(axis):
        from matplotlib.patches import Rectangle
        rec = Rectangle((0, 0), 1, 1,
            fill=False, lw=2, transform=axis.transAxes)
        rec = axis.add_patch(rec)
        rec.set_clip_on(False)
    
    if not (isinstance(images, list) or isinstance(images, tuple)):
        images = [images]
    
    from matplotlib.colors import Normalize
    class NormalizePiecewise(Normalize):
        def __init__(self):
            vmin = min(-1e-10, np.min([np.min(i) for i in images]))
            vmax = max(1e-10, np.max([np.max(i) for i in images]))
            Normalize.__init__(self, vmin, vmax)

        def __call__(self, value, clip=None):
            x, y = [self.vmin, 0, self.vmax], [0, 0.5, 1]
            return np.interp(value, x, y)
    
    nrows = math.ceil(len(images) / ncols)
    ncols = min(len(images), ncols)
    
    height = 2.8*nrows + 1
    width = 2*ncols
    fig = plt.figure(figsize=(width, height))
    if title is not None: fig.suptitle(title, fontsize=24)
    for i, image in enumerate(images):
        axis = plt.subplot2grid(
            (nrows, ncols),
            (i // ncols,  i % ncols),
        )
        axis.tick_params(labelleft='off', labelbottom='off')
        axis.grid(False)
        show_image(image, norm=NormalizePiecewise())
        draw_border(axis)
        if image_titles is not None and len(image_titles) == len(images):
            axis.set_title(image_titles[i])
    
    plt.tight_layout(h_pad=-8)

def display_all_filters(filters_by_label):
    """A utility function; ignore this."""
    show_flat_images(
        [(label, f) for label, filters_for_label in enumerate(filters_by_label) for f in filters_for_label],
        5,
        title = "All filters")
        
def display_mistakes(
        mnist,
        tf_session,
        x_tf,
        y__tf,
        filters_tf,
        actual_classifications_tf,
        true_classes_tf,
        is_correct_tf,
        num_labels=10,
        examples_to_show=5):
    actual_classifications, true_classes, is_correct = tf_session.run(
        [actual_classifications_tf, true_classes_tf, is_correct_tf],
        feed_dict={x_tf: mnist.validation.images, y__tf: mnist.validation.labels})
    filters = tf_session.run(
        filters_tf,
        feed_dict={x_tf: mnist.validation.images, y__tf: mnist.validation.labels}).reshape([784, num_labels, -1])
    num_filters_per_label = filters.shape[2]
    filters_by_label = [[filters[:,j,i] for i in range(num_filters_per_label)] for j in range(num_labels)]
    
    incorrect_indices = np.where(~is_correct)[0][:examples_to_show]
    incorrect_images = mnist.validation.images[incorrect_indices]
    classifications_for_incorrects = actual_classifications[incorrect_indices]
    true_classes_for_incorrects = true_classes[incorrect_indices]
    
    display_all_filters(filters_by_label)
    
    def filter_products_and_titles(i, for_actual_label):
        image = incorrect_images[i]
        if for_actual_label:
            label = classifications_for_incorrects[i]
        else:
            label = true_classes_for_incorrects[i]
        filters = filters_by_label[label]
        return [(
                  "Elementwise product\nof image and filter\n{:d}/{:d} for label {:d}".format(
                      i+1,
                      len(filters),
                      label),
                  image*f)
                for i, f in enumerate(filters)]
    
    filter_products_for_actual_classifications = [filter_products_and_titles(i, True) for i in range(examples_to_show)]
    filter_products_for_true_classes = [filter_products_and_titles(i, False) for i in range(examples_to_show)]
    
    def filters_and_titles(i, for_actual_label):
        image = incorrect_images[i]
        if for_actual_label:
            label = classifications_for_incorrects[i]
        else:
            label = true_classes_for_incorrects[i]
        filters = filters_by_label[label]
        return [(
                  "Filter {:d}/{:d} for\nlabel {:d} ({})".format(
                      i+1,
                      len(filters),
                      label,
                      "predicted" if for_actual_label else "true"),
                  f)
                for i, f in enumerate(filters)]
        
    filters_for_actual_classifications = [filters_and_titles(i, True) for i in range(examples_to_show)]
    filters_for_true_classes = [filters_and_titles(i, False) for i in range(examples_to_show)]
    
    def flatten(l):
        return [elt for sublist in l for elt in sublist]
    def interlace(list0, list1):
        return [e for t in zip(list0, list1) for e in t]
    def nested_interlace(list_of_lists0, list_of_lists1):
        return [interlace(l0, l1) for l0, l1 in zip(list_of_lists0, list_of_lists1)]
    def nested_concatenate(list_of_lists0, list_of_lists1):
        return [l0 + l1 for l0, l1 in zip(list_of_lists0, list_of_lists1)]
    
    filter_pictures_actual = nested_interlace(filters_for_actual_classifications, filter_products_for_actual_classifications)
    filter_pictures_truth = nested_interlace(filters_for_true_classes, filter_products_for_true_classes)
    alternating_filters_and_products = nested_concatenate(filter_pictures_actual, filter_pictures_truth)
    images_with_titles = [("An image that was\nincorrectly classified", im) for im in incorrect_images]
    pictures_to_show = flatten([[im] + fs for im, fs in zip(images_with_titles, alternating_filters_and_products)])
    
    show_flat_images(
        pictures_to_show,
        1 + 4*num_filters_per_label,
        title="Some incorrectly-classified pictures, corresponding filters, and activations")

def train_and_display(mnist, x_tf, y__tf, filters, output, train_step, num_labels=10, num_iterations=10000, batch_size=100):
    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()

    for _ in range(num_iterations):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        sess.run(train_step, feed_dict={x_tf: batch_xs, y__tf: batch_ys})
    
    model_classifications = tf.argmax(output, 1)
    true_classes = tf.argmax(y__tf, 1)
    correct_prediction = tf.equal(model_classifications, true_classes)
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print("Accuracy on the validation set: {:f}".format(
            sess.run(accuracy, feed_dict={x_tf: mnist.validation.images, y__tf: mnist.validation.labels})))
    
    display_mistakes(mnist, sess, x_tf, y__tf, filters, model_classifications, true_classes, correct_prediction, num_labels=num_labels)
    return sess

def display_confusion_matrix(compute_confusion_matrix, mnist, sess, x_tf, y__tf, output_tf, num_classes):
    """Plot the confusion matrix for a pipeline with the given
    output tensor.  The confusion proportions are computed on
    the validation set.
    
    The given function is used to compute the confusion matrix."""
    classifications_tf = tf.argmax(output_tf, 1)
    true_classes_tf = tf.argmax(y__tf, 1)
    classifications, true_classes = sess.run(
        [classifications_tf, true_classes_tf],
        feed_dict={x_tf: mnist.validation.images, y__tf: mnist.validation.labels}
    )
    mat = compute_confusion_matrix(classifications, true_classes, num_classes)
    
    ax = plt.gca()
    plt.imshow(mat, interpolation='none', cmap=plt.cm.Reds)
    plt.colorbar()
    classes = np.arange(num_classes)
    
    # Axis ticks
    ax.set_xticks(classes)
    ax.set_yticks(classes)
    ax.set_xticklabels(classes)
    ax.set_yticklabels(classes)
    ax.grid(False)

    # Gridlines based on minor ticks
    ax.set_xticks(np.arange(-.5, 10, 1), minor=True);
    ax.set_yticks(np.arange(-.5, 10, 1), minor=True);
    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
    
    plt.xlabel("Model's classification")
    plt.ylabel("True class")
    plt.title("Confusion matrix for your classifier\n(on the validation set)")
    plt.tight_layout()
