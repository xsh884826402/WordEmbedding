'''
本函数进行WordEmbedding的训练
最开始调用data_read_csv 进行格式规整
先调用data——load.py 文件，读取法房源ID
再调用dic——build 构建房源ID 与索引的词典
最后使用model_build_bookid进行词向量的训练
'''
import tensorflow as  tf
import collections
import numpy  as np
import batch_generate_bookid
import batch_generate
import pickle

vocabulary_size = 3500000
#超参数配置
batch_size = 129     #这里需要注意，要与你的skipWindows相匹配
embedding_size = 64  # 生成向量维度.
skip_window = 2       # 左右窗口.
num_skips = 2        # 同一个keyword产生label的次数.实际上还要再加一个book-id
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
num_steps = 10000000000
with tf.Session(graph=graph) as session:
    tf.global_variables_initializer().run()
    average_loss = 0
    stop_count = 6
    count = 0
    flag = 0
    for step in range(num_steps):
        # print("STEP",step)
        batch_data,batch_labels = batch_generate_bookid.batch_generate(batch_size,num_skips,skip_window)
        # with open("./data/error.txt","w") as  f:
        #     f.write("batch_data"+str(batch_data)+"\n")
        #     f.write("batch_labels"+str(batch_labels)+"\n")
        # print("batch_data",batch_data[0])
        # print("batch_label",batch_labels[0])
        feed_dict = {train_dataset:batch_data,
                     train_labels:batch_labels}
        _,ave_loss = session.run([optimizer,loss],feed_dict=feed_dict)
        # print("DEbug_2")
        average_loss += ave_loss

        if step % 1000 == 0 and step >0:
            print('Average losss at step %d:%f' % (step,average_loss / 1000))
            print("flag",flag,"count",count)
            if average_loss / 1000 < 0.2:
                if flag == 1:
                    count += 1
                    if count >= stop_count:
                        break
                else:
                    flag = 1
                    count += 1
            else:
                count = 0
                flag = 0
            average_loss = 0
    word2vec = normalized_embeddings.eval()
    with open("./data/word2vec.txt","wb") as f:
        pickle.dump(word2vec,f)

'''
distances = -word2vec[dictionary[u""]].reshape((1,-1)).dot(word2vec.T)
inds = np.argsort(distances.ravel())[1:6]
print(" ".join([reverse_dictionary[i] for i in inds]))
'''