def max_layers(envelopes):
    envelopes.sort(key=lambda envelope: envelope[0] + envelope[1])
    layers = []

    for i, envelope in enumerate(envelopes):
        prev_layers = 0
        for j in range(i):
            if envelopes[j][0] < envelope[0] and envelopes[j][1] < envelope[1]:
                prev_layers = max(prev_layers, layers[j])
        layers.append(prev_layers + 1)

    return max(layers)