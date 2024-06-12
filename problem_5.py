def main(dist):
  taxa = [0.50, 0.45, 0.35]
  if dist < 200:
    return dist * taxa[0]
  if dist > 400:
    return dist * taxa[2]
  if dist > 200 & dist < 400:
    return dist * taxa[1]

#oi