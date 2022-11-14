from faker import Faker

faker = Faker()

print(f'name: {faker.name()}')
print(f'address: {faker.address()}')


print(f' random text: {faker.text()}')