import tensorflow as  tf
import collections
import numpy  as np

#----
import batch_generate

vocabulary_size = 200000
#超参数配置
batch_size = 128
embedding_size = 128  # 生成向量维度.
skip_window = 2       # 左右窗口.
num_skips = 2        # 同一个keyword产生label的次数.
num_sampled = 64      # 负样本抽样数.

graph = tf.Graph()
with graph.as_default():
    train_dataset = tf.placeholder(tf.int32,shape=[batch_size])
    train_labels = tf.placeholder(tf.int32,shape=[batch_size,1])

    embeddings = tf.Variable(tf.random_uniform([vocabulary_size,embedding_size],minval=-1.0,maxval=1.0,))
    softmax_weights = tf.Variable(
        tf.truncated_normal([vocabulary_size,embedding_size],stddev=1.0/np.sqrt(embedding_size))
    )
    softmax_biases = tf.Variable( tf.zeros([vocabulary_size]))

    embed = tf.nn.embedding_lookup(embeddings,train_dataset)
    loss = tf.reduce_mean(
        tf.nn.sampled_softmax_loss(weights=softmax_weights,biases=softmax_biases,inputs=embed,
                                   labels=train_labels,num_sampled=num_sampled,num_classes=vocabulary_size)
    )

    optimizer = tf.train.AdagradOptimizer(1.0).minimize(loss)

    norm = tf.sqrt(tf.reduce_sum(tf.square(embeddings),1,keep_dims=True))
    normalized_embeddings = embeddings / norm


#模型训练
num_steps = 500001
with tf.Session(graph=graph) as session:
    tf.global_variables_initializer().run()
    average_loss = 0
    for step in range(num_steps):
        print("STEP",step)
        batch_data,batch_labels = batch_generate.batch_generate(batch_size,num_skips,skip_window)
        print("batch_data",batch_data[0])
        print("batch_label",batch_labels[0])
        feed_dict = {train_dataset:batch_data,
                     train_labels:batch_labels}
        _,ave_loss = session.run([optimizer,loss],feed_dict=feed_dict)
        print("DEbug_2")
        average_loss += ave_loss

        if step % 100 == 0 and step >0:
            print('Average losss at step %d:%f' % (step,average_loss / 100))
            average_loss = 0
    word2vec = normalized_embeddings.eval()

'''
distances = -word2vec[dictionary[u""]].reshape((1,-1)).dot(word2vec.T)
inds = np.argsort(distances.ravel())[1:6]
print(" ".join([reverse_dictionary[i] for i in inds]))
'''