
scientists = ['Marie Curie', 'Albert Einstein', 'Niels Bohr', 'Isaak Newton', 'Dmitri Mendeleev', 'Antoine Lavoisier',
              'Carl Linnaeus', 'Alfred Wegener', 'Charles Darwin']
sorted(scientists, key=lambda name: name.split()[-1])

if __name__ == '__main__':
    print(sorted(scientists, key=lambda name: name.split()[-1]))
