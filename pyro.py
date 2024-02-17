!pip install pyro-ppl

import pyro

n = int(input("Enter the number of sample: "))
concentration = 1.0
rate = 0.7
#sample = []
for _ in range(n):
    x = pyro.sample("my_sample", pyro.distributions.Gamma(concentration, rate))
    print(x)
    #sample.append(x)
#print(sample)

import pyro.distributions as dist
def Lung_Cancer():
    Lcancer = pyro.sample('Lcancer', dist.Exponential(1.0))
    Lcancer = 'Lcancer' if Lcancer.item() > 0.60 else 'no_Lcancer'
    mean_ALLERGY = {'Lcancer': 7.0, 'no_Lcancer': 6.0}[Lcancer]
    scale_ALLERGY = {'Lcancer': 8.0, 'no_Lcancer': 3.0}[Lcancer]
    ALLERGY  = pyro.sample('ph', dist.Laplace(mean_ALLERGY , scale_ALLERGY ))
    mean_CHEST_PAIN = {'Lcancer': 100.0, 'no_Lcancer': 150.0}[Lcancer]
    scale_CHEST_PAIN = {'Lcancer': 50.0, 'no_Lcancer': 75.0}[Lcancer]
    CHEST_PAIN = pyro.sample('hardness', dist.Laplace(mean_CHEST_PAIN, scale_CHEST_PAIN))
    mean_ANXIETY = {'Lcancer': 10000.0, 'no_Lcancer': 15000.0}[Lcancer]
    scale_ANXIETY = {'Lcancer': 50.0, 'no_Lcancer': 75.0}[Lcancer]
    ANXIETY = pyro.sample('solid', dist.Laplace(mean_ANXIETY, scale_ANXIETY))
    return Lcancer, ALLERGY.item(), CHEST_PAIN.item(), ANXIETY.item()
n = int(input("Enter the number of samples: "))
print("Class\t\t\tALLERGY\t\t\tCHEST_PAIN\t\tANXIETY")
for _ in range(n):
    #print(water_portability())
    a, b, c,d = Lung_Cancer()
    print(a,"\t",b,"\t",c,"\t",d)



