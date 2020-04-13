suma=1
i=2
puts 'Digite un número'
numero=gets.chomp
n=numero.to_i
while i<n
  if n%i==0
    suma=suma+i
    end
i =i +1
end
if suma==n
  puts 'El numero ' +n.to_s+' es perfecto'
else
  puts 'El numero '+n.to_s+' no es perfecto'
end
